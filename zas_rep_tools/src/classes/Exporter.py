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
#import collections
import types
import csv
#import unicodecsv as csv
import codecs
from lxml import etree as ET
import json


from collections import defaultdict
from raven import Client
from cached_property import cached_property

from zas_rep_tools.src.classes.DBHandler import DBHandler
from zas_rep_tools.src.utils.logger import Logger
from zas_rep_tools.src.utils.debugger import p
from zas_rep_tools.src.utils.error_tracking import initialisation



class Exporter(object):

    supported_file_formats = ["csv", "json", "csv", "txt", "xml"]

    def __init__(self, inpdata,
                 folder_for_log_files=False,  use_logger=True, logger_level=logging.INFO, error_tracking=True):



        ## Logger Initialisation 
        logger = Logger()
        self._folder_for_log_files = folder_for_log_files
        self._use_logger = use_logger
        self._logger_level = logger_level
        self.logger = logger.myLogger("Exporter", self._folder_for_log_files, use_logger=self._use_logger, level=self._logger_level)

        self.logger.debug('Beginn of creating an instance of Exporter()')



        #Input: Incaplusation:
        self._inpdata = inpdata
        self._numbers_of_alredy_created_files = defaultdict(lambda: defaultdict(int))
        self._number_of_inserts_in_the_current_file = 0
        #self._fieldnames = fieldnames
        self.sqlite_db = False

        self._error_tracking = error_tracking

        #p(inpdata)

        #InstanceAttributes: Initialization




        ## Error-Tracking:Initialization #1
        if self._error_tracking:
            self.client = initialisation()
            self.client.context.merge({'InstanceAttributes': self.__dict__})


        self.logger.debug('Intern InstanceAttributes was initialized')


        if not self._eval_input_data():
            sys.exit()


        self.logger.debug('An instance of Exporter() was created ')

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





    def tocsv(self, path_to_export_dir , fname, fieldnames,  rows_limit_in_file=50000, encoding="utf-8"):
        self.current_csvfile = False
        rows_was_exported = 0
        for row in self._inpdata:
            try:
                self._write_to_csv_files(row, fieldnames, path_to_export_dir, fname, rows_limit_in_file=rows_limit_in_file, encoding=encoding)
                rows_was_exported += 1
            except Exception, e:
               self.logger.error("CSVWriterError: Not possible to Export into CSV. Following Exception was throw: '{}'.".format(e))
               return False
        self.logger.info("CSVWriter: '{}' rows  was exported into CSV File(s) in '{}'.".format(rows_was_exported,path_to_export_dir))






    def toxml(self, path_to_export_dir , fname, rows_limit_in_file=50000, encoding="utf-8", root_elem_name="Docs", row_elem_name="Doc"):
        self.current_xmlfile = False
        rows_was_exported = 0
        for row in self._inpdata:
            try:
                self._write_to_xml_files(row,  path_to_export_dir, fname, rows_limit_in_file=rows_limit_in_file, encoding=encoding, root_elem_name=root_elem_name, row_elem_name=row_elem_name)
                rows_was_exported += 1
            except Exception, e:
               self.logger.error("XMLWriterError: Not possible to Export into XML. Following Exception was throw: '{}'.".format(e))
               return False
        #to save all last data
        self._save_output_into_current_xml_file()
        self.logger.info("XMLWriter: '{}' rows  was exported into XML File(s) in '{}'.".format(rows_was_exported,path_to_export_dir))





    def tojson(self, path_to_export_dir , fname, rows_limit_in_file=50000, encoding="utf-8", unicode_encode=True):
        self.current_jsonfile = False
        rows_was_exported = 0
        for row in self._inpdata:
            #p(row)
            try:
            #p((row,  path_to_export_dir, fname))
                self._write_to_json_files(row,  path_to_export_dir, fname, rows_limit_in_file=rows_limit_in_file, encoding=encoding, unicode_encode=unicode_encode)
                rows_was_exported += 1

            except Exception, e:
               self.logger.error("JSONWriterError: Not possible to Export into JSON. Following Exception was throw: '{}'.".format(e))
               return False

        self.current_jsonfile.seek(-1, os.SEEK_END)
        #self.current_jsonfile.truncate()
        #self.current_jsonfile.write("test")
        self.current_jsonfile.write("\n\n ]")
        self.current_jsonfile.close()
        #self._save_output_into_current_xml_file()
        self.logger.info("JSONWriter: '{}' rows  was exported into JSONS File(s) in '{}'.".format(rows_was_exported,path_to_export_dir))




    def tosqlite(self, path_to_export_dir, dbname, fieldnames,  encoding="utf-8", encryption_key=False, table_name= "Documents", attributs_names_with_types_as_str=False):
        self.current_jsonfile = False
        rows_was_exported = 0

        if not  attributs_names_with_types_as_str:
            attributs_names_with_types_as_str = self._create_list_with_colms_and_types_for_sqlite(fieldnames)


        if not self.sqlite_db: 
            self.sqlite_db = DBHandler(logger_level=self._logger_level) 
            self.sqlite_db.init_emptyDB(path_to_export_dir, dbname, encryption_key=encryption_key)
            self.sqlite_db.addtable(table_name, attributs_names_with_types_as_str)

        for row in self._inpdata:
            #p(row)
            #try:
            self._write_to_sqliteDB(row,  path_to_export_dir, table_name,  encoding=encoding)
            rows_was_exported += 1

            # except Exception, e:
            #    self.logger.error("SQLITEWriterError: Not possible to Export into SQLITE-DB. Following Exception was throw: '{}'.".format(e))
            #    return False

        try:
            self.sqlite_db.close()
        except Exception, e:
            self.logger.error("SQLITEWriterError: Following Exception was throw: '{}'. ".format(e))

        self.logger.info("SQLITEWriter: '{}' rows  was exported into SQLITE-DB in '{}'.".format(rows_was_exported,path_to_export_dir))







    def totxt(self):
        self.logger.error("TXTReader is not implemented!")
        sys.exit()



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

    def _get_new_file(self, path_to_dir, fname, file_extention, delete_file_if_exist=True, encoding="utf-8", file_flag="w", open_file_with_codecs=False):
        
        if file_extention not in Exporter.supported_file_formats:
            self.logger.error("NewFileGetterError: Given file_format '{}' is not supported. Please use one of the following file formats: '{}'. ".format(file_extention,Exporter.supported_file_formats ))
            sys.exit()

        count_of_existing_files = self._numbers_of_alredy_created_files[path_to_dir][fname]
        new_fname_without_extention = fname+ "_{}".format(count_of_existing_files)
        new_fname_with_extention =new_fname_without_extention+ "." + file_extention
        path_to_file = os.path.join(path_to_dir, new_fname_with_extention)
        if os.path.isfile(path_to_file):
            if delete_file_if_exist:
                os.remove(path_to_file)
                self.logger.critical("NewFileGetterProblem: '{}' File is already exist and  was removed from '{}'.  \nBefore we can create new file, old files with the same names should be deleted from the current directory.".format(new_fname_with_extention, path_to_file))
            else:
                self.logger.critical("NewFileGetterError: '{}' File is already exist in '{}'.  Please delete it before you can start extraction.".format(new_fname_with_extention, path_to_file))
                sys.exit()

        #else:
        #p(path_to_file, c="r")
        if open_file_with_codecs:
            current_csvfile = codecs.open(path_to_file, 'w', encoding)
        else:
            current_csvfile = open(path_to_file, file_flag)
        #p(current_csvfile,  c="r")
        self._numbers_of_alredy_created_files[path_to_dir][fname] += 1
        self.logger.debug("NewFileGetter: New File  '{}' was created in '{}'.".format(new_fname_with_extention, path_to_dir))
        return current_csvfile




    
    def _write_to_csv_files(self, row_as_dict, fieldnames, path_to_dir , fname,  rows_limit_in_file=50000, encoding="utf-8"):
        # check if current file has not more row as given rows limits
        
        if self.current_csvfile:
            if self._number_of_inserts_in_the_current_file >= rows_limit_in_file:
                self.current_csvfile.close()
                self._number_of_inserts_in_the_current_file = 0
                self.current_csvfile = self._get_new_file(path_to_dir , fname, "csv", encoding=encoding)
                #p((self.current_csvfile, fieldnames))
                #self.current_csv_writer = csv.DictWriter(self.current_csvfile, fieldnames=fieldnames, encoding=encoding)
                self.current_csv_writer = csv.DictWriter(self.current_csvfile, fieldnames=fieldnames)
                self.current_csv_writer.writeheader()
        else:
            self.current_csvfile = self._get_new_file(path_to_dir , fname, "csv", encoding=encoding)
            #self.current_csv_writer = csv.DictWriter(self.current_csvfile, fieldnames=fieldnames, encoding=encoding)
            self.current_csv_writer = csv.DictWriter(self.current_csvfile, fieldnames=fieldnames)
            self.current_csv_writer.writeheader()

        #p(str(row_as_dict)[55])
        #p(row_as_dict)
        encoded_into_str = {k.encode(encoding): v.encode(encoding) for k,v in row_as_dict.iteritems()}
        #p(encoded_into_str)
        self.current_csv_writer.writerow(encoded_into_str)
        #self.current_csv_writer.writerow(row_as_dict)
        self._number_of_inserts_in_the_current_file += 1


    def _write_to_json_files(self,row_as_dict, path_to_dir, fname, rows_limit_in_file=50000, encoding="utf-8",unicode_encode=True):
        # check if current file has not more row as given rows limits
        

        if self.current_jsonfile:
            if self._number_of_inserts_in_the_current_file >= rows_limit_in_file:
                self.current_jsonfile.seek(-1, os.SEEK_END)
                self.current_jsonfile.write("\n\n ]")
                self.current_jsonfile.close()
                self._number_of_inserts_in_the_current_file = 0
                self.current_jsonfile = self._get_new_file(path_to_dir , fname, "json", encoding=encoding, file_flag="a+", open_file_with_codecs=unicode_encode)
                self.current_jsonfile.write("[ \n\n")
        
        else:
            self.current_jsonfile = self._get_new_file(path_to_dir , fname, "json", encoding=encoding, file_flag="a+", open_file_with_codecs=unicode_encode)
            self.current_jsonfile.write("[ \n\n")


        #json.dump(row_as_dict, self.current_jsonfile,indent=4)
        json.dump(row_as_dict, self.current_jsonfile,indent=4, ensure_ascii=False)
        self.current_jsonfile.write(",")
        self._number_of_inserts_in_the_current_file += 1


    def _write_row_to_xml(self,root_elem, row_as_dict, row_elem_name="Doc"):
        try:
            row_element = ET.SubElement(root_elem, row_elem_name)
            for col_name, value in row_as_dict.iteritems():
                tag = ET.SubElement(row_element, col_name)
                tag.text = value
        except Exception, e:
            self.logger.error("WriterRowIntoXMLError: Following Exception was throw: '{}'. ".format(e))
            return False


    def _save_output_into_current_xml_file(self):
        if self.current_xmlfile:
            tree = ET.ElementTree(self.current_xml_root_elem)
            output_xml = ET.tostring(tree, pretty_print=True, xml_declaration=True,  encoding="utf-8")
            #p(output_xml)
            self.current_xmlfile.write(output_xml)
            self.current_xmlfile.close()
            self.current_xmlfile = False
        else:
            self.logger.error("SaveOutputIntoXMLError: There is not activ XML-Files")
            return False


    def _write_to_xml_files(self,row_as_dict, path_to_dir, fname, rows_limit_in_file=50000, encoding="utf-8", root_elem_name="Docs", row_elem_name="Doc"):
        # check if current file has not more row as given rows limits
        if self.current_xmlfile:
            if self._number_of_inserts_in_the_current_file >= rows_limit_in_file:
                self._save_output_into_current_xml_file()
                self._number_of_inserts_in_the_current_file = 0
                self.current_xmlfile = self._get_new_file(path_to_dir , fname, "xml", encoding=encoding)

        
                self.current_xml_root_elem = ET.Element(root_elem_name)

        else:
            self.current_xmlfile = self._get_new_file(path_to_dir , fname, "xml", encoding=encoding)
            self.current_xml_root_elem = ET.Element(root_elem_name)

        self._write_row_to_xml(self.current_xml_root_elem, row_as_dict,row_elem_name=row_elem_name)
        #self.current_xml_root_elem.writerow(row_as_dict)
        self._number_of_inserts_in_the_current_file += 1




    def _write_to_sqliteDB(self,row_as_dict, path_to_export_dir, tablename,  encoding="utf-8"):
        if not self.sqlite_db:
            self.logger.error("SQLITEWriterError: No Active DB to write in exist! Please Initialize first an Empty DB.")
            sys.exit()

        col=[]
        val=[]

        for k, v in row_as_dict.iteritems():
            col.append(k)
            val.append(v)

        self.sqlite_db.insertlazy(tablename, "cv", columns_names=col, values=val)



    def _create_list_with_colms_and_types_for_sqlite(self, fieldnames):
        outputlist = []
        if isinstance(fieldnames, list):
            for colname in fieldnames:
                outputlist.append((colname,"TEXT"))
            return outputlist
        else:
            self.logger.error("SQLITECreaterError: Given Fieldnames are not from List Type.")
            return False




    def _eval_input_data(self):
        #p((isinstance(self._inpdata, list), isinstance(self._inpdata, types.GeneratorType)))

        check = (isinstance(self._inpdata, list), isinstance(self._inpdata, types.GeneratorType))

        if True not in check:
            self.logger.error("InputValidationError: Given 'inpdata' is not iterable. ")
            return False


        return True







