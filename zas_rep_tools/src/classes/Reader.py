#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# : XXX{Information about this code}XXX
# Author:
# c(Developer) ->     {'Egor Savin'}
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

###Programm Info######
#
#
#
#
#



import os
import copy
import sys
import regex
import logging
import codecs
import json
import csv
import unicodecsv as unicodecsv
from lxml import etree as ET


#from collections import defaultdict
from raven import Client
from cached_property import cached_property
from encodings.aliases import aliases


from zas_rep_tools.src.utils.logger import Logger
from zas_rep_tools.src.utils.debugger import p
from zas_rep_tools.src.utils.error_tracking import initialisation
from zas_rep_tools.src.utils.helpers import get_file_list



class Reader(object):
    #supported_encodings_types = ["utf-8"]
    supported_encodings_types = set(aliases.values())
    supported_file_types = ["txt", "json", "xml", "csv"]

    regex_templates = {
                "blogger":r"(?P<blogger_id>[\d]*)\.(?P<gender>[\w]*)\.(?P<age>\d*)\.(?P<working_area>.*)\.(?P<star_constellation>[\w]*)",
                }

    def __init__(self, inp_path, file_format, columns_source=False, regex_template=False, regex_for_fname=False,
                 folder_for_log_files=False,  use_logger=True, logger_level=logging.INFO, error_tracking=True):



        ## Logger Initialisation 
        logger = Logger()
        self._folder_for_log_files = folder_for_log_files
        self._use_logger = use_logger
        self.logger = logger.myLogger("Reader", self._folder_for_log_files, use_logger=self._use_logger, level=logger_level)

        self.logger.debug('Beginn of creating an instance of Reader()')



        #Input: Incaplusation:
        self._inp_path = inp_path
        self._file_format = file_format
        self._columns_source = columns_source
        self._regex_template = regex_template
        self._regex_for_fname = regex_for_fname 

        self.xmlroottag = False
        self.xmlchildetag = False


        self._error_tracking = error_tracking

        #p(inpdata)

        #InstanceAttributes: Initialization
        #self._



        ## Error-Tracking:Initialization #1
        if self._error_tracking:
            self.client = initialisation()
            self.client.context.merge({'tags': self.__dict__})


        self.logger.debug('Intern InstanceAttributes was initialized')



        ## Validation 
        if not self._validate_given_file_format():
            sys.exit()

        if not self._validation_given_path():
            sys.exit()

        if not self._validation_regex_treatment():
            sys.exit()


        ## 
        self.files_to_read = self._extract_all_files_according_given_file_format()





        self.logger.debug('An instance of Reader() was created ')




        ############################################################
        ####################__init__end#############################
        ############################################################







####################################################################################
####################################################################################
####################################################################################
####################################################################################
####################################################################################
####################################################################################
######################################Extern########################################
####################################################################################
####################################################################################
####################################################################################
####################################################################################
####################################################################################



###########################+++++++++############################
    
    



    def getlazy(self, colnames=False, encoding="utf-8", csvdelimiter=','):
        #p(self.files_to_read)
        for path_to_file in self.files_to_read:
            if self._file_format == "txt":
                #p(self._readTXT(path_to_file, encoding=encoding, columns_extract_from_fname=True))
                row =  self._readTXT(path_to_file, encoding=encoding, columns_extract_from_fname=True, colnames=colnames)
                yield row
            elif self._file_format == "json":
                for row in self._readJSON(path_to_file, encoding=encoding, colnames=colnames):
                    yield row
            elif self._file_format == "xml":
                for row in self._readXML(path_to_file, encoding=encoding, colnames=colnames):
                    yield row
            elif self._file_format == "csv":
                for row in self._readCSV(path_to_file, encoding=encoding, colnames=colnames, delimiter=csvdelimiter):
                    yield row
            else:
                self.logger.error("'{}'-Format not supported.".format(self._file_format))
                yield False
                return 





    # def getlazy1(self, colnames=False, encoding="utf_8", logger_level=logging.INFO):
    #     p(self.files_to_read)
    #     for path_to_file in self.files_to_read:
    #         if self._file_format == "txt":
    #             yield PlainTextCorpusReader(path_to_file, encoding=encoding, logger_level=logger_level).getdata()
    #         elif self._file_format == "json":
    #             yield JSONCorpusReader(path_to_file, encoding=encoding, logger_level=logger_level)
    #         elif self._file_format == "xml":
    #             yield XMLCorpusReader(path_to_file, encoding=encoding, logger_level=logger_level)
    #         elif self._file_format == "csv":
    #             yield CSVCorpusReader(path_to_file, encoding=encoding, logger_level=logger_level)
    #         else:
    #             self.logger.error("'{}'-Format not supported.".format(self._file_format))
    #             yield False
    #             return 





####################################################################################
####################################################################################
####################################################################################
####################################################################################
####################################################################################
####################################################################################
######################################INTERN########################################
####################################################################################
####################################################################################
####################################################################################
####################################################################################
####################################################################################


    def _get_col_and_values_from_fname(self, fname, compiled_regex_for_fname):
        try:
            col_and_values_dicts = {}
            try:
                for m in compiled_regex_for_fname.finditer(fname):
                    for k,v in m.groupdict().iteritems():
                        if v.isdigit():
                            col_and_values_dicts[unicode(k)]= int(v)
                        elif isinstance(v, (int, float)):
                            col_and_values_dicts[unicode(k)]= v
                        else:
                            col_and_values_dicts[unicode(k)]= unicode(v)

                #p(col_and_values_dicts)
                #col_and_values_dicts = [{unicode(k): unicode(v) for k,v in m.groupdict().iteritems()} for m in compiled_regex_for_fname.finditer(fname)]
            except Exception, e:
                self.logger.error("RegexError: RegexDictExtractor throw following Error: '{}'. ".format(e))
                return False
            #col_and_values_dicts = [m.groupdict() for m in compiled_regex_for_fname.finditer(fname)]
            #p(col_and_values_dicts)
            if  len(col_and_values_dicts)==0:
                self.logger.critical("ColumnsExctractionFromFileNameError: Some of the columns in the given Fname '{}' wasn't detected. Following RegEx-Expression was used: '{}'. ".format(fname,self._regex_for_fname))
                return False

            return col_and_values_dicts
        except Exception as  exception:
            self.logger.critical("ColumnsExctractionFromFileNameError: Following Error was raised: '{}'. ".format(repr(exception)))
            return False


    def _validation_regex_treatment(self):
        if self._regex_template and self._regex_for_fname:
            self.logger.error("InputValidationError: Template for Regex and Regex_for_Fname was given parallel. Please give just one of them.")
            return False

        if self._file_format == "txt":
            if not self._regex_template and not self._regex_for_fname:
                self.logger.error("InputValidationError: Template_for_Regex or Regex_for_Fname wasn't given. Please give one of them.")
                return False

            if self._regex_template and ( self._regex_template.lower() not in Reader.regex_templates):
                self.logger.error("InputValidationError: Given RegexTemplateName '{}' is not supporting! ".format(self._regex_template.lower()))
                return False

            if self._regex_for_fname and  not isinstance(self._regex_for_fname, (str, unicode)):
                self.logger.error("InputValidationError: RegexForFname should be an str or unicode object. Given: '{}'.".format(self._regex_for_fname))
                return False

            if self._regex_template and not self._regex_for_fname:
                try:
                    self._regex_for_fname = Reader.regex_templates[self._regex_template]
                    self._compiled_regex_for_fname = regex.compile(self._regex_for_fname, regex.UNICODE)

                except Exception, e:
                    self.logger.error("InputValidationError: Given RegEx-Template '{}' is not exist or it wasn't possible to compile it. Check this Exception: '{}'. ".format(self._regex_template, e))
                    return False

            elif not self._regex_template and self._regex_for_fname:
                try:
                    self._compiled_regex_for_fname = regex.compile(self._regex_for_fname, regex.UNICODE)

                except Exception, e:
                    self.logger.error("InputValidationError: Given RegEx-Template '{}' is not exist or it wasn't possible to compile it.  Check this Exception: '{}'.".format(self._regex_template, e))
                    return False



        return True





    # def _extract_colnames_from_regex(self, regex_for_fname):
    #     p(repr(regex_for_fname), c="m")
    #     columns_name = regex.findall(regex_for_fname, fname.strip())

    #     p(columns_name, c="r")
    #     if not isinstance(columns_name, list) or len(columns_name)==0 or len(columns_name[0])<5:
    #         self.logger.critical("ColumnsExctractionFromFileNameError: Some of the columns in the given Fname '{}' wasn't detected. Following RegEx-Expression was used: '{}'. ".format(fname,regex_for_fname))
    #         return False


    #     return columns_name


    def _get_data_from_dic_for_given_keys(self, colnames_to_extract, given_row_data ):
        if  isinstance(colnames_to_extract, list):
            outputdict = {}
            for col in  colnames_to_extract:
                if col in given_row_data:
                    outputdict[col] =given_row_data[col]
                else:
                    self.logger.critical("ColumnsGetter: '{}'-Column wasn't found in the given Structure and was ignored.".format(col))
            
            return outputdict
        else:
            self.logger.error("ColumnsGetterError: Given 'colnames_to_extract' are not from type 'list' ")
            return {}




    def _readTXT(self, path_to_file,encoding="utf-8", columns_extract_from_fname=True, colnames=False):
        if os.path.isfile(path_to_file):
            try:
                if columns_extract_from_fname:
                    #file = open(path_to_file, "r")
                    file = codecs.open(path_to_file, "r", encoding=encoding)
                    fname = os.path.splitext(os.path.basename(path_to_file))
                    output_data = self._get_col_and_values_from_fname(fname[0],self._compiled_regex_for_fname)
                    #p(output_data)
                    if not output_data or not isinstance(output_data, dict):
                        self.logger.critical("ReadTXTError: '{}' wasn't readed.".format(fname))
                        return {}
                    file_data = file.read()


                    output_data.update({"text":file_data})
                    if colnames:
                        return self._get_data_from_dic_for_given_keys(colnames, output_data)
                    else:
                        return output_data
                else:
                    self.logger.error("ReadTXTError: Other sources of Columns as from FName are not implemented!")
                    return False 

            except Exception, e:
                self.logger.error("TXTReaderError: Following Exception was throw: '{}'. ".format(e))
                return False
                #return

        else:
            self.logger.error("TXTFileNotExistError: Following File wasn't found: '{}'. ".format(path_to_file))
            return False


    def _readCSV(self, path_to_file,encoding="utf_8", delimiter=',', colnames=False):
        if os.path.isfile(path_to_file):
            try:
                csvfile = open(path_to_file, "r")

                readCSV = unicodecsv.DictReader(csvfile, delimiter=delimiter, encoding=encoding)
                headers = readCSV.fieldnames

                for row in readCSV:
                    if colnames:
                        yield self._get_data_from_dic_for_given_keys(colnames, row)
                    else:
                        yield row

            except Exception, e:
                self.logger.error("CSVReaderError: Following Exception was throw: '{}'. ".format(e))
                yield False
                return

        else:
            self.logger.error("CSVFileNotExistError: Following File wasn't found: '{}'. ".format(path_to_file))
            yield False
            return


    def _readXML(self, path_to_file,encoding="utf_8", colnames=False):
        if os.path.isfile(path_to_file):
            tree = ET.parse(path_to_file)
            root = tree.getroot()
            self.xmlroottag = root.tag
            #root.attrib
            for child in root:
                row_dict = {}
                if not self.xmlchildetag:
                    self.xmlchildetag = child.tag

                if self.xmlchildetag != child.tag:
                    self.logger.critical("XMLReaderError: Child Tags in the the XML-root are different and was ignored. ('{}'!='{}')".format(self.xmlchildetag, child.tag))
                    break
                
                # collect all columns into dict from the current child
                for column in child:
                        row_dict[column.tag] = column.text

                if colnames:
                    yield self._get_data_from_dic_for_given_keys(colnames, row_dict)
                else:
                    yield row_dict

        else:
            self.logger.error("XMLFileNotExistError: Following File wasn't found: '{}'. ".format(path_to_file))
            yield False
            return



    def _readJSON(self, path_to_file,encoding="utf_8", colnames=False):
        if os.path.isfile(path_to_file):
            try:
                #p(path_to_file)
                f = open(path_to_file)
                data = json.load(f)
                #p(data)

                # if colnames:
                #     yield self._get_data_from_dic_for_given_keys(colnames, row_dict)
                # else:
                #     yield row_dict
            except ValueError, e:
                if "Expecting , delimiter" in str(e) or "No JSON object could be decoded" in str(e):
                    self.logger.error("JSONReaderError: Current File is not valid JSON: Path to File: '{}'. Following Exception was throw: '{}'. ".format(path_to_file, e))
                else:
                    self.logger.error("JSONReaderError: ValueError in the current File '{}' following Exception was throw: '{}'. ".format(path_to_file, e))
            except Exception, e:
                self.logger.error("JSONReaderError: For current File '{}' following Exception was throw: '{}'. ".format(path_to_file, e))

        else:
            self.logger.error("JSONFileNotExistError: Following File wasn't found: '{}'. ".format(path_to_file))
            yield False
            return





    def _validation_given_path(self):
        if not os.path.isdir(self._inp_path):
            self.logger.error("ValidationError: Given PathToCorpus is not exist: '{}'. ".format(self._inp_path))
            return False

        return True


    def _validate_given_file_format(self):
        if self._file_format.lower() not in Reader.supported_file_types:
            self.logger.error("ValidationError: Given FileFormat '{}' is not supported by this Reader.".format(self._file_format.lower()))
            return False

        return True



    def _extract_all_files_according_given_file_format(self):
        output_path_to_file = []
        for root, dirs, files in os.walk(self._inp_path, topdown=False):
           for name in files:
              if self._file_format in name:
                output_path_to_file.append(os.path.join(root, name))

        if len(output_path_to_file)==0:
            self.logger.error("FilesExtractionProblem: No '{}'-Files was found. (check given FileFormat).".format(self._file_format))
            return output_path_to_file

        self.logger.info("FilesExtraction: '{}' files was found in the given folder Structure.".format(len(output_path_to_file)))
        return output_path_to_file














####################################################################################
####################################################################################
####################################################################################
####################################################################################
####################################################################################
####################################################################################
###################################Other Classes#####################################
####################################################################################
####################################################################################
####################################################################################
####################################################################################
####################################################################################




# class PlainTextCorpusReader(Reader):
#     def __init__(self, path_to_file, encoding="utf_8",
#                  folder_for_log_files=False,  use_logger=True, logger_level=logging.INFO, error_tracking=True):


#         ## Logger Initialisation 
#         logger = Logger()
#         self._folder_for_log_files = folder_for_log_files
#         self._use_logger = use_logger
#         self.logger = logger.myLogger("PlainTextCorpusReader", self._folder_for_log_files, use_logger=self._use_logger, level=logger_level)

#         self.logger.debug('Beginn of creating an instance of PlainTextCorpusReader()')


#         ## Error-Tracking:Initialization #1
#         if error_tracking:
#             self.client = initialisation()
#             self.client.context.merge({'tags': self.__dict__})




#         #Input: Encapsulation:
#         self._path_to_file = path_to_file
#         self._encoding = encoding
#         self._error_tracking = error_tracking

#         #p(path_to_file)

#         self.logger.debug('Input was encapsulated')


#         #InstanceAttributes: Initialization
#         self._paths_list = get_file_list(path_to_file, ".txt")
#         self._readed_data = self._read_data()
#         #p( self._readed_data )


#         self.logger.debug('Intern InstanceAttributes was initialized')

#         ### Error Tracking #2
#         if self._error_tracking:
#             self.client.context.merge({'tags': self.__dict__})


#         self.logger.debug('An instance of PlainTextCorpusReader() was created ')


#     def getdata(self):
#         pass





# class CSVCorpusReader(Reader):
#     def __init__(self, inpdata, 
#                  folder_for_log_files=False,  use_logger=True, logger_level=logging.INFO, error_tracking=True):



#         ## Logger Initialisation 
#         logger = Logger()
#         self._folder_for_log_files = folder_for_log_files
#         self._use_logger = use_logger
#         self.logger = logger.myLogger("CSVCorpusReader", self._folder_for_log_files, use_logger=self._use_logger, level=logger_level)

#         self.logger.debug('Beginn of creating an instance of CSVCorpusReader()')



#         #Input: Incaplusation:
#         self._inpdata = inpdata

#         self._error_tracking = error_tracking

#         #p(inpdata)

#         #InstanceAttributes: Initialization



#         ## Error-Tracking:Initialization #1
#         if self._error_tracking:
#             self.client = initialisation()
#             self.client.context.merge({'tags': self.__dict__})


#         self.logger.debug('Intern InstanceAttributes was initialized')



#         ### Error Tracking #2
#         if self._error_tracking:
#             self.client.context.merge({'tags': self.__dict__})


#         ### Error Tracking #3
#         if self._error_tracking:
#             self.client.context.merge({'tags': self.__dict__})




#         self.logger.debug('An instance of CSVCorpusReader() was created ')




# class JSONCorpusReader(Reader):
#     def __init__(self, inpdata, 
#                  folder_for_log_files=False,  use_logger=True, logger_level=logging.INFO, error_tracking=True):



#         ## Logger Initialisation 
#         logger = Logger()
#         self._folder_for_log_files = folder_for_log_files
#         self._use_logger = use_logger
#         self.logger = logger.myLogger("JSONCorpusReader", self._folder_for_log_files, use_logger=self._use_logger, level=logger_level)

#         self.logger.debug('Beginn of creating an instance of JSONCorpusReader()')



#         #Input: Incaplusation:
#         self._inpdata = inpdata

#         self._error_tracking = error_tracking

#         #p(inpdata)

#         #InstanceAttributes: Initialization



#         ## Error-Tracking:Initialization #1
#         if self._error_tracking:
#             self.client = initialisation()
#             self.client.context.merge({'tags': self.__dict__})


#         self.logger.debug('Intern InstanceAttributes was initialized')



#         ### Error Tracking #2
#         if self._error_tracking:
#             self.client.context.merge({'tags': self.__dict__})


#         ### Error Tracking #3
#         if self._error_tracking:
#             self.client.context.merge({'tags': self.__dict__})




#         self.logger.debug('An instance of JSONCorpusReader() was created ')







# class XMLCorpusReader(Reader):
#     def __init__(self, inpdata, 
#                  folder_for_log_files=False,  use_logger=True, logger_level=logging.INFO, error_tracking=True):



#         ## Logger Initialisation 
#         logger = Logger()
#         self._folder_for_log_files = folder_for_log_files
#         self._use_logger = use_logger
#         self.logger = logger.myLogger("XMLCorpusReader", self._folder_for_log_files, use_logger=self._use_logger, level=logger_level)

#         self.logger.debug('Beginn of creating an instance of XMLCorpusReader()')



#         #Input: Incaplusation:
#         self._inpdata = inpdata

#         self._error_tracking = error_tracking

#         #p(inpdata)

#         #InstanceAttributes: Initialization



#         ## Error-Tracking:Initialization #1
#         if self._error_tracking:
#             self.client = initialisation()
#             self.client.context.merge({'tags': self.__dict__})


#         self.logger.debug('Intern InstanceAttributes was initialized')



#         ### Error Tracking #2
#         if self._error_tracking:
#             self.client.context.merge({'tags': self.__dict__})


#         ### Error Tracking #3
#         if self._error_tracking:
#             self.client.context.merge({'tags': self.__dict__})




#         self.logger.debug('An instance of XMLCorpusReader() was created ')




