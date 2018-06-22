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


#from collections import defaultdict
from raven import Client
from cached_property import cached_property
import sqlite3
import glob
import shutil
from time import gmtime, strftime
import coloredlogs


from zas_rep_tools.src.utils.logger import Logger
from zas_rep_tools.src.utils.sql_helper import *
from zas_rep_tools.src.utils.db_helper import *
from zas_rep_tools.src.utils.debugger import p
from zas_rep_tools.src.utils.sql_qearies import * 
from zas_rep_tools.src.utils.helpers import path_to_zas_rep_tools
from zas_rep_tools.src.utils.error_tracking import initialisation



class DB(object):

    default_attributs = {"corpus":attributs_names_corpus, "stats":attributs_names_stats}

    def __init__(self,  folder_for_log_files=False,  use_logger=True,
                logger_level=logging.INFO, error_tracking=True, developingMode = False):

        ## Developing Mode: Part 1
        self._developingMode = developingMode
        self._logger_level = logger_level 
        if self._developingMode:
            self._logger_level = logging.DEBUG


        ## Logger Initialisation 
        logger = Logger()
        self._folder_for_log_files = folder_for_log_files
        self._use_logger = use_logger
        self.logger = logger.myLogger("DatenBank", self._folder_for_log_files, use_logger=self._use_logger, level=self._logger_level)
        self.logger.debug('Beginn of creating an instance of DB()')


        ## Developing Mode: Part 2:
        if self._developingMode:
            self.logger.info("DEVELOPING_MODE: was started")


        #Input: Incaplusation:
        self._error_tracking = error_tracking

        #p(inpdata)

        #InstanceAttributes: Initialization
        self.db = False
        self._attachedDBs = []

        ## Error-Tracking:Initialization #1
        if self._error_tracking:
            self.client = initialisation()
            self.client.context.merge({'InstanceAttributes': self.__dict__})


        self.logger.debug('Intern InstanceAttributes was initialized')




        self.logger.debug('An instance of DB() was created ')


        ############################################################







        ############################################################
        ####################__init__end#############################
        ############################################################




    def __del__(self):
        #self.db.close()
        if self.db:
            self.db.close()
            self.logger.info("Connection with DB was closed")
        self.logger.debug("DB-Instance was destructed")


    def fname(self):
        if self.db:
            cur = self.db.cursor()
            cur.execute("PRAGMA database_list")
            rows = cur.fetchall()
            return os.path.basename(rows[0][2])

        else:
            self.error("Cannot get file_name because Database wasn't initialized or wasn't given.")
            sys.exit()


    def path(self):
        if self.db:
            cur = self.db.cursor()
            cur.execute("PRAGMA database_list")
            rows = cur.fetchall()
            return rows[0][2]

        else:
            self.error("Cannot get path_to_db because Database wasn't initialized or wasn't given.")
            sys.exit()


    def pathAttachedDBs(self):
        if self.db:

            cur = self.db.cursor()
            cur.execute("PRAGMA database_list")
            rows = cur.fetchall()

            return [row[2] for row in rows if row[1]!= "main"]

        else:
            self.error("Cannot get any file_names of attached DBs because Database wasn't initialized or wasn't given.")
            sys.exit()



    def fnameAttachedDBs(self):
        if self.db:

            cur = self.db.cursor()
            cur.execute("PRAGMA database_list")
            rows = cur.fetchall()

            return [ os.path.basename(row[2]) for row in rows if row[1]!= "main"]

        else:
            self.error("Cannot get any file_names of attached DBs because Database wasn't initialized or wasn't given.")
            sys.exit()


    def attachedDBs(self):
        if self.db:
            cur = self.db.cursor()
            cur.execute("PRAGMA database_list")
            rows = cur.fetchall()
            return [ row[1] for row in rows if row[1]!= "main"]
            # for row in rows:
            #     print row[0], row[1], row[2]

        else:
            self.error("Cannot get names of attached DBs because Database wasn't initialized or wasn't given.")
            sys.exit()


    def dbsName(self):
        if self.db:
            cur = self.db.cursor()
            cur.execute("PRAGMA database_list")
            rows = cur.fetchall()
            return [ row[1] for row in rows]
            # for row in rows:
            #     print row[0], row[1], row[2]

        else:
            self.error("Cannot get names of attached DBs because Database wasn't initialized or wasn't given.")
            sys.exit()


    def tableColumns(self, tableName):
        if self.db:

            if not filter(lambda x: unicode(tableName) == unicode(x), self.tables()):
                self.logger.error("Given Table is not exist: ('{}').".format(tableName))
                return None

            query = "PRAGMA table_info('{table_name}'); ".format(table_name=tableName)
            cursor = self.db.cursor()
            cursor.execute(query)
            #tables_exist = cursor.fetchone()
            columns = cursor.fetchall()
            return [column[1] for column in columns]

        else:
            self.error("Cannot get any tables because Database wasn't initialized or wasn't given.")
            return None


    def tableColumnsTypes(self, tableName):
        if self.db:
            if not filter(lambda x: unicode(tableName) == unicode(x), self.tables()):
                self.logger.error("Given Table is not exist: ('{}').".format(tableName))
                return None

            query = "PRAGMA table_info('{table_name}'); ".format(table_name=tableName)
            cursor = self.db.cursor()
            cursor.execute(query)
            #tables_exist = cursor.fetchone()
            columns = cursor.fetchall()

            return [(column[1],column[2]) for column in columns]

        else:
            self.error("Cannot get any tables because Database wasn't initialized or wasn't given.")
            return None


    def tables(self):
        if self.db:
            cursor = self.db.cursor()
            cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
            #tables_exist = cursor.fetchone()
            tables_exist = cursor.fetchall()
            return [table_name[0] for table_name in tables_exist]

        else:
            self.error("Cannot get any tables because Database wasn't initialized or wasn't given.")
            return None


    def rowsNumber(self, tableName):
        if self.db:
            if not filter(lambda x: unicode(tableName) == unicode(x), self.tables()):
                self.logger.error("Given Table is not exist: ('{}').".format(tableName))
                return None

            query = "select count(*) from {table_name}; ".format(table_name=tableName)
            cursor = self.db.cursor()
            cursor.execute(query)
            #tables_exist = cursor.fetchone()
            number = cursor.fetchone()
            return number[0]
            #return [(column[1],column[2]) for column in columns]

        else:
            self.error("Cannot get any tables because Database wasn't initialized or wasn't given.")
            return None



    def add_attributs(self,attributs_names, values):

        # Check if attributes and values have the same length
        if len(attributs_names) != len(values):
            self.logger.error("Length of given attributs_names and values is not equal.")
            sys.exit()


        attributName_as_str = attributs_to_str(attributs_names)
        values_as_str = values_list_to_str(values)
        #p(attributName_as_str, c="m")
        #p(values_as_str, c="m")
        ### Add Attributes
        if self.db:
            if filter(lambda x: u"info" == unicode(x), self.tables()):
                qeary = 'INSERT INTO info ({columns}) \nVALUES ({values});'.format(columns=attributName_as_str,values=values_as_str)
                cursor = self.db.cursor()
                #p(qeary)
                cursor.execute(qeary)
                self.db.commit()
                return True
            else:
                self.logger.error("Info-Table is wasn't found or not exist. Please initialize the Info Table, bevor you may add any attributes.")
                return False
        else:
            self.critical("Cannot add any attributes because Database wasn't initialized or wasn't given.")
            return False


    def update_attribut(self,attribut_name, value):
        ### Exception Handling
        # Check if attributes and values have the same length
        if not isinstance(attribut_name, (str, unicode)):
            self.logger.error("Given AttributName should be an string or unicode object.")
            return None

        # if given attribute exist in the Info_Table
        if not filter(lambda x: unicode(attribut_name) == unicode(x), self.tableColumns("info")):
            self.logger.error("Given Attribute ('{}') is not exist in this DataBase.".format(attribut_name))
            return None

        ### Update Attribute
        if self.db:
            if filter(lambda x: u"info" == unicode(x), self.tables()):
                qeary = 'UPDATE info  \nSET {}="{}";'.format(attribut_name,value)
                cursor = self.db.cursor()
                p(qeary)
                cursor.execute(qeary)
                self.db.commit()
                return True
            else:
                self.logger.error("Info-Table is wasn't found or not exist. Please initialize the Info Table, bevor you may add any attributes.")
                return False
        else:
            self.critical("Cannot add any attributes because Database wasn't initialized or wasn't given.")
            return False


    def get_attribut(self,attributName):
        if not isinstance(attributName, (str, unicode)):
            self.logger.error("Given AttributName should be an string or unicode object.")
            return None

        # p(repr(self.tableColumns("info")))
        # p(repr(unicode(attributName)))
        
        # if given attribute exist in the Info_Table
        if not filter(lambda x: unicode(attributName) == unicode(x), self.tableColumns("info")):
            self.logger.error("Given Attribute ('{}') is not exist in this DatebBank.".format(attributName))
            return None


        if self.db:
            if u"info" in unicode(self.tables()):
                qeary = 'SELECT {} FROM  info;'.format(attributName)
                cursor = self.db.cursor()
                cursor.execute(qeary)
                attribut = cursor.fetchall()
                return attribut[0][0]
            else:
                self.logger.error("Info-Table is wasn't found or not exist. Please initialize the Info Table, bevor you may add any attributes.")
                return None
        else:
            self.critical("Cannot add any attributes because Database wasn't initialized or wasn't given.")
            return None


    def get_all_attributs(self):
        if self.db:
            if u"info" in unicode(self.tables()):
                qeary = 'SELECT * FROM  info;'
                cursor = self.db.cursor()
                cursor.execute(qeary)
                attribut = cursor.fetchall()[0]
                if self.rowsNumber("info") ==1:
                    columns = self.tableColumns("info")
                    return dict(zip(columns, list(attribut)))
                elif self.rowsNumber("info") ==0:
                    self.logger.error("Table 'info' is empty. Please set attributes bevor!")
                    return None
                else:
                    self.logger.error("Table 'info' has more as 1 row. It's not correct. Please delete not needed rows.")
                    return None

            else:
                self.logger.error("Info-Table is wasn't found or not exist. Please initialize the Info Table, bevor you may add any attributes.")
                return None
        else:
            self.critical("Cannot add any attributes because Database wasn't initialized or wasn't given.")
            return None




    def initialise_corpus(self, prjFolder, DBname,  language, platform_name,
                            visibility, fileName=False, source="NULL", license="NULL",
                            template_name="NULL", version="NULL"):
        ### Preprocessing: Create File_Name
        typ= "corpus"
        fileName,path_to_db = get_file_name(prjFolder,DBname, language,visibility, typ,fileName)

        
        ### Initialisation of DB
        if  not self.db:
            if os.path.isdir(prjFolder):
                self.db = sqlite3.connect(path_to_db)
                #cursor = self.db.cursor()
                corpus_id= create_id(DBname,language, typ, visibility)
                created_at = strftime("%Y-%m-%d %H:%M:%S", gmtime())
                attributs_list = DB.default_attributs[typ]
                values = [corpus_id, DBname, platform_name, template_name, version, language, created_at, source,license,visibility,typ]


                self._initialize_info_table(attributs_list)
                self.add_attributs(attributs_list,values)
                self.db.commit()
                self.logger.info("DB ({}) was initialized and connected.".format(fileName))
            else:
                self.logger.error("Given Project Folder is not exist: '{}'. ".format(prjFolder))
                sys.exit()

        else:
            self.logger.warning("DB was already initialized or connected. You can't initialize second DB if one DB already activ.")
            sys.exit()



    def initialise_stats(self,  prjFolder, corpus_id, DBname,  
                         visibility,language, fileName=False, version="NULL"):
        ### Preprocessing: Create File_Name
        typ= "stats"
        fileName,path_to_db = get_file_name(prjFolder,DBname, language,visibility, typ,fileName)


        ### Initialisation of DB
        if  not self.db:
            if os.path.isdir(prjFolder):
                self.db = sqlite3.connect(path_to_db)
                #cursor = self.db.cursor()
                stats_id= create_id(DBname,language, typ, visibility,corpus_id=corpus_id)
                created_at = strftime("%Y-%m-%d %H:%M:%S", gmtime())
                attributs_list = DB.default_attributs[typ]
                values = [stats_id,corpus_id, DBname, version,  created_at, visibility,typ]


                self._initialize_info_table(attributs_list)
                self.add_attributs(attributs_list,values)
                self.db.commit()
                self.logger.info("DB ({}) was initialized and connected.".format(fileName))
            else:
                self.logger.error("Given Project Folder is not exist: '{}'. ".format(prjFolder))
                sys.exit()

        else:
            self.logger.warning("DB was already initialized or connected. You can't initialize second DB if one DB already activ.")
            sys.exit()




    # def connect_corpus(self, path_to_db):
    #     if not os.path.isfile(path_to_db):
    #         self.logger.error("CorpusDB-File wasn't found: ('{}').".format(path_to_db))
    #         #os._exit(1)
    #         sys.exit()

    #     if not self.db: 
    #         self.db = sqlite3.connect(path_to_db)
    #         self.logger.info("CorpusDB was connected")

    #     else:
    #         self.logger.warning("DB was already initialized or connected. You can't initialize second DB if one DB already activ.")
    #         sys.exit()



    # def connect_stats(self,path_to_db):
    #     if not os.path.isfile(path_to_db):
    #         self.logger.error("StatsDB-File wasn't found: ('{}').".format(path_to_db))
    #         #os._exit(1)
    #         sys.exit()

    #     if not self.db: 
    #         self.db = sqlite3.connect(path_to_db)
    #         self.logger.info("StatsDB was connected")

    #     else:
    #         self.logger.warning("DB was already initialized or connected. You can't initialize second DB if one DB already activ.")
    #         sys.exit()


    def connect(self,path_to_db):
        self._check_file_existens(path_to_db)


        dbName = os.path.splitext(os.path.basename(path_to_db))[0]
        if not self.db: 
            self.db = sqlite3.connect(path_to_db)
            try:
                self.tables()
            except:
                self.logger.error("DatabaseError: file is not a database")
                sys.exit()

            self.logger.info("DB ('{}') was connected".format(dbName))

        else:
            self.logger.warning("DB was already initialized or connected. You can't initialize second DB if one DB already activ.")
            sys.exit()


    def attach(self,path_to_db):
        self._check_file_existens(path_to_db)


        ### Check, if it is right DB and get name
        tempdb = DB(logger_level=logging.ERROR)
        tempdb.connect(path_to_db)
        del tempdb
        self._change_logger_level_back()


        dbName = os.path.splitext(os.path.basename(path_to_db))[0]
        if self.db: 
            qeary = "ATTACH DATABASE '{path_to_db}' AS {dbName};".format(path_to_db=path_to_db, dbName=dbName)
            cursor = self.db.cursor()
            cursor.execute(qeary)
            #output = cursor.fetchall()
            self._attachedDBs.append((path_to_db, dbName))
            self.logger.info("DB ('{}') was attached".format(dbName))

        else:
            self.logger.warning("No active DB was found. If you want to attach an DB you need to connect mainDB first.")
            sys.exit()






####################################################################################
####################################################################################
####################################################################################
######################################INTERN########################################
####################################################################################
####################################################################################

    def _change_logger_level_back(self):
        coloredlogs.install(level=self._logger_level)

    def _check_file_existens(self, path_to_file):
        if not os.path.isfile(path_to_file):
            self.logger.error("DB-File wasn't found: ('{}').".format(path_to_db))
            #os._exit(1)
            sys.exit()



    def _addTable(self, table_name, attributs_names_with_types_as_str, constrains=False):
        if self.db:
            if unicode(table_name) not in unicode(self.tables()):
                if constrains:
                    qeary = 'CREATE TABLE {} ({}\n{});'.format(table_name,attributs_names_with_types_as_str, constrains)
                else:
                    qeary = 'CREATE TABLE {} ({});'.format(table_name,attributs_names_with_types_as_str)
                
                cursor = self.db.cursor()
                cursor.execute(qeary)
                self.db.commit()
                return True

            else:
                self.logger.error("Info-Table is already exist in the given DB. You can not initialize it one more time!")
                sys.exit()

        else:
            self.critical("Cannot add any attributes because Database wasn't initialized or wasn't given.")
            return False


    def _initialize_info_table(self, attributs_names):
        #p(attributs_names)

        str_attributs_names = attributs_and_types_to_str(attributs_names)
        if not str_attributs_names:
            self.logger.error("Something was wrong by Converting attributes into string. Program was stoped!")
            sys.exit()

        self._addTable("info", str_attributs_names)

        self.logger.debug("Info-Table was initialized")



















####################################################################################
####################################################################################
####################################################################################
######################################Extern########################################
####################################################################################
####################################################################################


