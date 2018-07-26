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
from __future__ import division
from __future__ import absolute_import


import os
#import copy
import sys
import regex
import logging
import codecs
import json
import csv
import unicodecsv as unicodecsv
from lxml import etree as ET
import psutil


#from collections import defaultdict
from raven import Client
#from cached_property import cached_property
from encodings.aliases import aliases
from decimal import Decimal, ROUND_HALF_UP, ROUND_UP, ROUND_HALF_DOWN, ROUND_DOWN

#from zas_rep_tools.src.utils.db_helper import *
#from zas_rep_tools.src.classes.configer import Configer
from zas_rep_tools.src.utils.helpers import set_class_mode, print_mode_name, LenGen, path_to_zas_rep_tools, get_number_of_streams_adjust_cpu
from zas_rep_tools.src.utils.logger import *
from zas_rep_tools.src.utils.debugger import p
from zas_rep_tools.src.utils.error_tracking import initialisation
from zas_rep_tools.src.utils.helpers import get_file_list
from zas_rep_tools.src.utils.traceback_helpers import print_exc_plus


import platform
if platform.uname()[0].lower() !="windows":
    import colored_traceback
    colored_traceback.add_hook()
else:
    import colorama


class Reader(object):
    #supported_encodings_types = ["utf-8"]
    supported_encodings_types = set(aliases.values())
    supported_file_types = ["txt", "json", "xml", "csv"]

    regex_templates = {
                "blogger":r"(?P<id>[\d]*)\.(?P<gender>[\w]*)\.(?P<age>\d*)\.(?P<working_area>.*)\.(?P<star_constellation>[\w]*)",
                }

    reader_supported_formatter = ["twitter"]

    def __init__(self, inp_path, file_format, columns_source=False, regex_template=False, regex_for_fname=False,
                formatter_name=False, text_field_name = "text", id_field_name="id", ignore_retweets=True,
                logger_folder_to_save=False,  logger_usage=True, logger_level=logging.INFO,
                logger_save_logs=True, logger_num_buffered=5, error_tracking=True,
                ext_tb=False, logger_traceback=False, mode="prod"):

        
        ## Set Mode: Part 1
        self._mode = mode
        if mode != "free":
            _logger_level, _logger_traceback, _logger_save_logs = set_class_mode(self._mode)
            logger_level = _logger_level if _logger_level!=None else logger_level
            logger_traceback = _logger_traceback if _logger_traceback!=None else logger_traceback
            logger_save_logs = _logger_save_logs if _logger_save_logs!=None else logger_save_logs

    
    
        ## Logger Initialisation
        self._logger_level = logger_level
        self._logger_traceback =logger_traceback
        self._logger_folder_to_save = logger_folder_to_save
        self._logger_usage = logger_usage
        self._logger_save_logs = logger_save_logs
        self.logger = main_logger(self.__class__.__name__, level=self._logger_level, folder_for_log=self._logger_folder_to_save, use_logger=self._logger_usage, save_logs=self._logger_save_logs)

        ## Set Mode: Part 2:
        print_mode_name(self._mode, self.logger)


        self.logger.debug('Beginn of creating an instance of {}()'.format(self.__class__.__name__))





        #Input: Incaplusation:
        self._inp_path = inp_path
        self._file_format = file_format
        self._columns_source = columns_source
        self._regex_template = regex_template
        self._regex_for_fname = regex_for_fname 
        self._formatter_name = formatter_name
        self._text_field_name = text_field_name
        self._id_field_name = id_field_name
        self._ignore_retweets = ignore_retweets
        self.retweet_counter = 0

        self.xmlroottag = False
        self.xmlchildetag = False


        self._error_tracking = error_tracking
        self._ext_tb = ext_tb

        #p(inpdata)

        #InstanceAttributes: Initialization
        self._ignored_retweets_counter = 0



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
    # def __del__(self):
    #     self.logger.newline(1)






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
    
    



    # def getlazy(self, colnames=False, encoding="utf-8", csvdelimiter=',', input_path_list=False):
    #     #p(self.files_to_read)
    #     if input_path_list:
    #         path_to_files = input_path_list
    #     else:
    #         path_to_files = self.files_to_read

    #     for path_to_file in path_to_files:
    #         if self._file_format == "txt":
    #             #p(self._readTXT(path_to_file, encoding=encoding, columns_extract_from_fname=True))
    #             row =  self._readTXT(path_to_file, encoding=encoding, columns_extract_from_fname=True, colnames=colnames)
    #             yield row
    #         elif self._file_format == "json":
    #             for row in self._readJSON(path_to_file, encoding=encoding, colnames=colnames):
    #                 yield row
    #         elif self._file_format == "xml":
    #             for row in self._readXML(path_to_file, encoding=encoding, colnames=colnames):
    #                 yield row
    #         elif self._file_format == "csv":
    #             for row in self._readCSV(path_to_file, encoding=encoding, colnames=colnames, delimiter=csvdelimiter):
    #                 yield row
    #         else:
    #             self.logger.error("'{}'-Format not supported.".format(self._file_format), exc_info=self._logger_traceback)
    #             yield False
    #             return 


    def getgenerator(self, colnames=False, encoding="utf-8", csvdelimiter=',', input_path_list=False):
        if input_path_list:
            path_to_files = input_path_list
        else:
            path_to_files = self.files_to_read

        for path_to_file in path_to_files:
            if self._file_format == "txt":
                #p(self._readTXT(path_to_file, encoding=encoding, columns_extract_from_fname=True))
                row =  self._readTXT(path_to_file, encoding=encoding, columns_extract_from_fname=True, colnames=colnames)
                yield row
            elif self._file_format == "json":
                for row in self._readJSON(path_to_file, encoding=encoding, colnames=colnames,):
                    yield row
            elif self._file_format == "xml":
                for row in self._readXML(path_to_file, encoding=encoding, colnames=colnames):
                    yield row
            elif self._file_format == "csv":
                for row in self._readCSV(path_to_file, encoding=encoding, colnames=colnames, delimiter=csvdelimiter):
                    yield row
            else:
                self.logger.error("'{}'-Format not supported.".format(self._file_format), exc_info=self._logger_traceback)
                yield False
                return 

        if self.retweet_counter > 0:
            self.logger.warning("'{}'-retweets was ignored.".format(self.retweet_counter))

    def getlazy(self,colnames=False, encoding="utf-8", csvdelimiter=',', input_path_list=False,stream_number=1, adjust_to_cpu=True, min_files_pro_stream=1000):
        if not input_path_list:
            input_path_list = self.files_to_read

        wish_stream_number = stream_number
        if stream_number <1:
            stream_number = 10000
            adjust_to_cpu = True
            self.logger.debug("StreamNumber is less as 1. Automatic computing of strem number according cpu was enabled.")
        #p(stream_number, "stream_number")
        if adjust_to_cpu:
            stream_number= get_number_of_streams_adjust_cpu( min_files_pro_stream, len(self.files_to_read), stream_number)
            if stream_number is None:
                self.logger.error("Number of input files is 0. Not generators could be returned.")
                return []
        #p(stream_number, "stream_number")
        #p(stream_number, "stream_number")
        if stream_number > len(self.files_to_read):
            self.logger.error("StreamNumber is higher as number of the files to read. This is not allowed.")
            return False

        list_with_generators = []
        #number_of_files_per_stream = 
        number_of_files_per_stream = int(Decimal(float(len(self.files_to_read)/stream_number)).quantize(Decimal('1.'), rounding=ROUND_DOWN))
        #p(number_of_files_per_stream)
        current_index = 0
        #p(range(stream_number), "range(stream_number)")
        for i in range(stream_number):
            #p(i, "i")
            if i < (stream_number-1): # for gens in between 
                new_index = current_index+number_of_files_per_stream
                #p((current_index,new_index))
                temp_list_with_paths  = self.files_to_read[current_index:new_index]
                #list_with_generators.append()
                current_index = new_index
            else: # for the last generator
                temp_list_with_paths  = self.files_to_read[current_index:]
                # list_with_generators.append(self.getlazy(input_path_list=temp_list_with_paths, colnames= colnames, encoding=encoding, csvdelimiter=csvdelimiter,))
            
            gen = self._getlazy_single(input_path_list=temp_list_with_paths, colnames= colnames, encoding=encoding, csvdelimiter=csvdelimiter)
            
            if stream_number == 1:
                if wish_stream_number > 1:

                    return [gen]
                else:
                    return gen
            #else:
            list_with_generators.append(gen)

        self.logger.debug(" '{}'-streams was created.".format(stream_number))
        return list_with_generators




    def _getlazy_single(self,colnames=False, encoding="utf-8", csvdelimiter=',', input_path_list=False):
        if not input_path_list:
            input_path_list = self.files_to_read
        
        length = len(input_path_list)
        gen = self.getgenerator(colnames=colnames, encoding=encoding, csvdelimiter=csvdelimiter, input_path_list=input_path_list)
        #p(type(gen))
        return LenGen(gen, length)


# #number_of_files_per_thread = len(self.files_to_read)/threads_to_create
#         return threads_to_create,  int(Decimal(float(number_of_files_per_thread)).quantize(Decimal('1.'), rounding=ROUND_DOWN))



    # def getparallel(self, thread_number=False, colnames=False, encoding="utf-8", csvdelimiter=',', min_files_pro_thread=100):
    #     list_with_generators = []
    #     threads_to_create= self._get_number_of_streams_adjust_cpu( min_files_pro_thread, thread_number=thread_number)
    #     current_index = 0
    #     if threads_to_create >1:
    #         for i in range(threads_to_create):
    #             #if i < threads_to_create-1:
    #             if i < (threads_to_create-1):
    #                 new_index = current_index+number_of_files_per_thread
    #                 #p((current_index,new_index), "reader", c="r")
    #                 temp_list_with_paths  = self.files_to_read[current_index:new_index]
    #                 #p(temp_list_with_paths, "reader",c="r")
    #                 list_with_generators.append(self._getlazy_single(input_path_list=temp_list_with_paths, colnames= colnames, encoding=encoding, csvdelimiter=csvdelimiter,))
    #                 #p(len(list(list_with_generators[-1])), "reader",c="r")
    #                 current_index = new_index
    #             else:
    #                 #p((current_index), "reader",c="m")
    #                 temp_list_with_paths  = self.files_to_read[current_index:]
    #                 #p(temp_list_with_paths, "reader",c="m")
    #                 #p(len(list(list_with_generators[-1])))
    #                 list_with_generators.append(self._getlazy_single(input_path_list=temp_list_with_paths, colnames= colnames, encoding=encoding, csvdelimiter=csvdelimiter,))
    #                 #p(len(list(list_with_generators[-1])), "reader",c="m")
    #     else:
    #         list_with_generators.append(self._getlazy_single(input_path_list=self.files_to_read, colnames= colnames, encoding=encoding, csvdelimiter=csvdelimiter,))
        
    #     self.logger.debug("GetParallel: '{}'-generators was created.".format(len(list_with_generators)))
    #     return list_with_generators

##################################################################################
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
                print_exc_plus() if self._ext_tb else ""
                self.logger.error("RegexError: RegexDictExtractor throw following Error: '{}'. ".format(e), exc_info=self._logger_traceback)
                return False
            #col_and_values_dicts = [m.groupdict() for m in compiled_regex_for_fname.finditer(fname)]
            #p(col_and_values_dicts)
            if  len(col_and_values_dicts)==0:
                self.logger.critical("ColumnsExctractionFromFileNameError: Some of the columns in the given Fname '{}' wasn't detected. Following RegEx-Expression was used: '{}'. ".format(fname,self._regex_for_fname))
                return False

            return col_and_values_dicts
        except Exception as  exception:
            print_exc_plus() if self._ext_tb else ""
            self.logger.critical("ColumnsExctractionFromFileNameError: Following Error was raised: '{}'. ".format(repr(exception)))
            return False


    def _validation_regex_treatment(self):
        if self._regex_template and self._regex_for_fname:
            self.logger.error("InputValidationError: Template for Regex and Regex_for_Fname was given parallel. Please give just one of them.", exc_info=self._logger_traceback)
            return False

        if self._file_format == "txt":
            if not self._regex_template and not self._regex_for_fname:
                self.logger.error("InputValidationError: Template_for_Regex or Regex_for_Fname wasn't given. Please give one of them.", exc_info=self._logger_traceback)
                return False

            if self._regex_template and ( self._regex_template.lower() not in Reader.regex_templates):
                self.logger.error("InputValidationError: Given RegexTemplateName '{}' is not supporting! ".format(self._regex_template.lower()), exc_info=self._logger_traceback)
                return False

            if self._regex_for_fname and  not isinstance(self._regex_for_fname, (str, unicode)):
                self.logger.error("InputValidationError: RegexForFname should be an str or unicode object. Given: '{}'.".format(self._regex_for_fname), exc_info=self._logger_traceback)
                return False

            if self._regex_template and not self._regex_for_fname:
                try:
                    self._regex_for_fname = Reader.regex_templates[self._regex_template]
                    ### set given id_field_name
                    self._regex_for_fname = self._regex_for_fname.replace("id", self._id_field_name)
                    self._compiled_regex_for_fname = regex.compile(self._regex_for_fname, regex.UNICODE)

                except Exception, e:
                    print_exc_plus() if self._ext_tb else ""
                    self.logger.error("InputValidationError: Given RegEx-Template '{}' is not exist or it wasn't possible to compile it. Check this Exception: '{}'. ".format(self._regex_template, e), exc_info=self._logger_traceback)
                    return False

            elif not self._regex_template and self._regex_for_fname:
                try:
                    self._compiled_regex_for_fname = regex.compile(self._regex_for_fname, regex.UNICODE)

                except Exception, e:
                    print_exc_plus() if self._ext_tb else ""
                    self.logger.error("InputValidationError: Given RegEx-Template '{}' is not exist or it wasn't possible to compile it.  Check this Exception: '{}'.".format(self._regex_template, e), exc_info=self._logger_traceback)
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
            if given_row_data:
                for col in  colnames_to_extract:
                    if col in given_row_data:
                        outputdict[col] =given_row_data[col]
                        #p(outputdict)
                    else:
                        self.logger.critical("ColumnsGetter: '{}'-Column wasn't found in the given Structure and was ignored.".format(col))
                
                return outputdict
        else:
            self.logger.error("ColumnsGetterError: Given 'colnames_to_extract' are not from type 'list' ", exc_info=self._logger_traceback)
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


                    output_data.update({self._text_field_name:file_data})
                    if colnames:
                        return self._get_data_from_dic_for_given_keys(colnames, output_data)
                    else:
                        return output_data
                else:
                    self.logger.error("ReadTXTError: Other sources of Columns as from FName are not implemented!", exc_info=self._logger_traceback)
                    return False 

            except Exception, e:
                print_exc_plus() if self._ext_tb else ""
                self.logger.error("TXTReaderError: Following Exception was throw: '{}'. ".format(e), exc_info=self._logger_traceback)
                return False
                #return

        else:
            self.logger.error("TXTFileNotExistError: Following File wasn't found: '{}'. ".format(path_to_file), exc_info=self._logger_traceback)
            return False


    def _readCSV(self, path_to_file,encoding="utf_8", delimiter=',', colnames=False):
        csv.field_size_limit(sys.maxsize)
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
                print_exc_plus() if self._ext_tb else ""
                self.logger.error("CSVReaderError: Following Exception was throw: '{}'. ".format(e), exc_info=self._logger_traceback)
                yield False
                return

        else:
            self.logger.error("CSVFileNotExistError: Following File wasn't found: '{}'. ".format(path_to_file), exc_info=self._logger_traceback)
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
            self.logger.error("XMLFileNotExistError: Following File wasn't found: '{}'. ".format(path_to_file), exc_info=self._logger_traceback)
            yield False
            return



    def _json_tweets_preprocessing(self, data):
        if isinstance(data, dict):
            data = [data]
        output_json_list = []
        if isinstance(data, (list, tuple)):
            for json in data:
                output_json_list.append(self._clean_json_tweet(json))
            return output_json_list
        else:
            self.logger.critical("JsonTweetsPreparationError: Given '{}'-JSON-Type is from not right type.".format(type(data)))
            return {}
            #return 


    def _clean_json_tweet(self, json_tweet):
        #self.logger.info(repr(json_tweet))
        #p(json_tweet)
        #sys.exit()

        ### Step 1:  Variables Initialization
        is_extended = False
        is_retweet = False
        is_answer = False
        t_id = json_tweet["id"]
        t_created_at = json_tweet["created_at"]
        t_language = json_tweet["lang"]
        t_used_client = json_tweet["source"]
        t_text = json_tweet["text"]
        u_created_at = json_tweet["user"]["created_at"]
        u_description = json_tweet["user"]["description"]
        u_favourites = json_tweet["user"]["favourites_count"]
        u_followers = json_tweet["user"]["followers_count"]
        u_friends = json_tweet["user"]["friends_count"]
        u_id = json_tweet["user"]["id"]
        u_lang = json_tweet["user"]["lang"]
        u_given_name = json_tweet["user"]["name"]
        u_username = json_tweet["user"]["screen_name"]
        u_verified = json_tweet["user"]["verified"]
        u_location = json_tweet["user"]["location"]


        ### Initialization fron new Tweet-Dict
        new_structure = {}

        # Step 2: Extraction of the additional Information
        # "extended_tweet"."full_text" ( 280>len(text)>140)
        if "extended_tweet" in json_tweet:
            t_text = json_tweet["extended_tweet"]["full_text"]
            #p(json_tweet["extended_tweet"])
            is_extended = True

        if "retweeted_status" in json_tweet:
            #p(json_tweet)
            #p(json_tweet["retweeted_status"])
            is_retweet = True
            if self._ignore_retweets:
                self.retweet_counter += 1
                self.logger.warning("RetweenIgnoring: Current RETweet with ID='{}' was ignored. (for allowing retweets please use 'ignore_retweets' option.)".format(json_tweet["id"]))
                return {}


        if "quoted_status" in json_tweet:
            #p(json_tweet)
            #p(json_tweet["quoted_status"])
            is_answer = True


        # Step 3: Write into new Object
        
        ## main paarameters
        new_structure[self._id_field_name] = t_id
        new_structure["t_created_at"] = t_created_at
        new_structure["t_language"] = t_language
        new_structure["t_used_client"] = t_used_client
        new_structure[self._text_field_name] = t_text
        new_structure["u_created_at"] = u_created_at
        new_structure["u_description"] = u_description
        new_structure["u_favourites"] = u_favourites
        new_structure["u_followers"] = u_followers
        new_structure["u_friends"] = u_friends
        new_structure["u_id"] = u_id
        new_structure["u_lang"] = u_lang 
        new_structure["u_given_name"] = u_given_name
        new_structure["u_username"] = u_username
        new_structure["u_verified"] = u_verified 
        new_structure["u_location"] = u_location 

        # additional parameters
        new_structure["is_extended"] = is_extended
        new_structure["is_retweet"] = is_retweet
        new_structure["is_answer"] = is_answer



        #p(new_structure, c="r")


        return new_structure




    def _readJSON(self, path_to_file,encoding="utf_8", colnames=False):
        if os.path.isfile(path_to_file):
            try:
                #p(path_to_file)
                f = open(path_to_file)
                data = json.load(f)

                if len(data) == 0:
                    self.logger.debug("Given JSON '{}' is empty.".format(path_to_file))
                    yield {}

                if self._formatter_name:
                    if self._formatter_name.lower() in Reader.reader_supported_formatter:
                        try:
                            data = self._json_tweets_preprocessing(data)

                            if len(data) == 0:
                                self.logger.debug("TweetsPreprocessing out-sorted current file: '{}' .".format(path_to_file))
                                yield {}
                        except Exception, e:
                            self.logger.error("JSONReader: Exception encountered during cleaning Twitter-JSON. This File was ignoren. Exception: '{}'.".format(e))
                            yield {}
                            return 
                    else:
                        self.logger.critical("JSONReaderError: Given '{}'-FormatterName is not supported. Please choice one of the following: '{}'. Execution of the Program was stopped- ".format(self._formatter_name, Reader.reader_supported_formatter))
                        sys.exit()

                if isinstance(data, dict):
                    data = [data]

                for row_dict in data:
                    if colnames: 
                        yield self._get_data_from_dic_for_given_keys(colnames, row_dict)
                    else:
                        yield row_dict 
            except ValueError, e:
                print_exc_plus() if self._ext_tb else ""
                if "Expecting , delimiter" in str(e) or "No JSON object could be decoded" in str(e):
                    self.logger.error("JSONReaderError: Current File is not valid JSON: Path to File: '{}'. Following Exception was throw: '{}'. ".format(path_to_file, e), exc_info=self._logger_traceback)
                else:
                    self.logger.error("JSONReaderError: ValueError in the current File '{}' following Exception was throw: '{}'. ".format(path_to_file, e), exc_info=self._logger_traceback)
            except Exception, e:
                print_exc_plus() if self._ext_tb else ""
                self.logger.error("JSONReaderError: For current File '{}' following Exception was throw: '{}'. ".format(path_to_file, e), exc_info=self._logger_traceback)

        else:
            self.logger.error("JSONFileNotExistError: Following File wasn't found: '{}'. This File was ignored.".format(path_to_file), exc_info=self._logger_traceback)
            yield {}
            #return





    def _validation_given_path(self):
        if not os.path.isdir(self._inp_path):
            self.logger.error("ValidationError: Given PathToCorpus is not exist: '{}'. ".format(self._inp_path), exc_info=self._logger_traceback)
            return False

        return True


    def _validate_given_file_format(self):
        if self._file_format.lower() not in Reader.supported_file_types:
            self.logger.error("ValidationError: Given FileFormat '{}' is not supported by this Reader.".format(self._file_format.lower()), exc_info=self._logger_traceback)
            return False

        return True



    def _extract_all_files_according_given_file_format(self):
        output_path_to_file = []
        for root, dirs, files in os.walk(self._inp_path, topdown=False):
           for name in files:
              if self._file_format in name:
                output_path_to_file.append(os.path.join(root, name))

        if len(output_path_to_file)==0:
            #p((self._inp_path))
            self.logger.error("FilesExtractionProblem: No '{}'-Files was found. (check given FileFormat).".format(self._file_format), exc_info=self._logger_traceback)
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



