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
#Info:
# SQLite will easily do 50,000 or more INSERT statements per second on an average desktop computer. 
# But it will only do a few dozen transactions per second. 
# avoid cursore.executescript() becuase it makes commit first 
# By default, the sqlite3 module opens transactions implicitly before a Data Modification Language (DML) statement (i.e. INSERT/UPDATE/DELETE/REPLACE), and commits transactions implicitly before a non-DML, non-query statement (i. e. anything other than SELECT or the aforementioned).



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
    __metaclass__ = DBErrorCatcher
    DBErrorCatcher = False

    default_attributs = {
                        "corpus":attributs_names_corpus,
                        "stats":attributs_names_stats
                        }

    templates = {
            "twitter":extended_columns_and_types_for_corpus_documents_twitter,
            "blogger":extended_columns_and_types_for_corpus_documents_blogger
            }


    def __init__(self,  folder_for_log_files=False,
                use_logger=True, logger_level=logging.INFO, error_tracking=True,
                developingMode = False, lazyness_border=50000):

        #p(Metaclass.__dict__)
        ## Developing Mode: Part 1
        self._developingMode = developingMode
        self._logger_level = logger_level 
        if self._developingMode:
            self._logger_level = logging.DEBUG


        # Logger Initialisation 
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
        self._db = False
        self._encryption_key = False



        self._attachedDBs = []
        self._tables_dict = {}
        self._DBsNames = [] 


        self._lazy_writer_all_inserts_counter = 0
        self._lazy_writer_number_inserts_after_last_commit = 0
        self._lazyness_border = lazyness_border
        self._successful_commits_with_lazy_writer = 0

        self.all_inserts_counter = 0
        self.number_of_new_inserts_after_last_commit = 0
        self.inserts_was_committed = 0

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
        #self._db.close()
        if self._db:
            #self.commit()
            self._db.close()
            if self.number_of_new_inserts_after_last_commit:
                self.logger.info("Connection with DB was closed without commits. {} new inserts wasn't committed/saved_on_the_disk. (Notice: All not-committed changes in the DB wasn't saved on the disk!!!  Please use 'db.close()' to commit all changes into DB and save them on the disk before exit the script.".format(self.number_of_new_inserts_after_last_commit))
            else:
                self.logger.info("Connection with DB was closed without commits. ({} insertion was waiting for commit)".format(self.number_of_new_inserts_after_last_commit))

        self.logger.debug("DB-Instance was destructed")






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



###########################DB-Initialization#############################


    def init(self, typ, prjFolder, DBname, language, visibility,
            platform_name=False, encryption_key=False, fileName=False,
            source=False, license=False, template_name=False, version=False,
            additional_columns_with_types_for_documents=False):

        supported_typs = ["stats", "corpus"]

        if typ == "corpus":
            if not platform_name:
                self.logger.error("'Platform_name' wasn't given. 'Corpus' initialization need 'platform_name'.")
                sys.exit()

            self.init_corpus(prjFolder, DBname, language,  visibility, platform_name,
                    encryption_key=encryption_key,fileName=fileName, source=source, license=license,
                    template_name=template_name, version=version,
                    additional_columns_with_types_for_documents=additional_columns_with_types_for_documents)


        elif typ == "stats":
            if not corpus_id:
                self.logger.error("'Corpus_id' wasn't given. 'Stats' initialization need Corpus_id.")
                sys.exit()
                
            self.init_stats(prjFolder, DBname, language, visibility, corpus_id,
                    encryption_key=encryption_key,fileName=fileName, version=version)


        else:
            self.logger.error("Given DB-Typ is not supported! Please one of the following  types: '{}'.".format(typ, supported_typs))
            sys.exit()


    def init_corpus(self, prjFolder, DBname, language,  visibility, platform_name,
                    encryption_key=False,fileName=False, source=False, license=False,
                    template_name=False, version=False, additional_columns_with_types_for_documents=False):
        ### Preprocessing: Create File_Name
        
        self._encryption_key = encryption_key
        source="NULL" if not source else source
        license = "NULL" if not license else license
        version = "NULL" if not "NULL" else version
        template_name = "NULL" if not template_name else template_name
        typ= "corpus"

        fileName,path_to_db = get_file_name(prjFolder,DBname, language,visibility, typ,fileName)

        
        ### Initialisation of DB
        self._check_db_should_not_exist()

        if os.path.isdir(prjFolder):

            if self._encryption_key:
                self._db = sqlite3.connect(path_to_db)
                c = self._db.cursor()
                c.execute("PRAGMA key='{}'".format(self._encryption_key))
                self._commit()

            else:

                self._db = sqlite3.connect(path_to_db)
            #cursor = self._db.cursor()
            corpus_id= create_id(DBname,language, typ, visibility)
            created_at = strftime("%Y-%m-%d %H:%M:%S", gmtime())
            attributs_list = DB.default_attributs[typ]
            values = [corpus_id, DBname, platform_name, template_name, version, language, created_at, source,license,visibility,typ]


            self._init_info_table(attributs_list)
            self.add_attributs(attributs_list,values)
            #p(template_name)
            self._init_default_tables("corpus", template=template_name, additional_columns_with_types=additional_columns_with_types_for_documents)
            #self._init_documents_table_in_corpus()
            self._commit()
            self._DBsNames.append("main")
            self.logger.info("DB ({}) was initialized and saved on the disk: '{}'. ".format(fileName, path_to_db))
            self.logger.info("DB ({}) was connected.".format(fileName))
        else:
            self.logger.error("Given Project Folder is not exist: '{}'. ".format(prjFolder))
            sys.exit()




    def init_stats(self, prjFolder, DBname, language, visibility, corpus_id,
                    encryption_key=False,fileName=False, version=False):

        self._encryption_key = encryption_key

        ### Preprocessing: Create File_Name
        version = "NULL" if not version else version
        typ= "stats"
        fileName,path_to_db = get_file_name(prjFolder,DBname, language,visibility, typ,fileName)


        ### Initialisation of DB
        self._check_db_should_not_exist()

        if os.path.isdir(prjFolder):
            if self._encryption_key:
                self._db = sqlite3.connect(path_to_db)
                c = self._db.cursor()
                c.execute("PRAGMA key='{}'".format(self._encryption_key))
                self._commit()

            else:
                self._db = sqlite3.connect(path_to_db)
            #cursor = self._db.cursor()
            stats_id= create_id(DBname,language, typ, visibility,corpus_id=corpus_id)
            created_at = strftime("%Y-%m-%d %H:%M:%S", gmtime())
            attributs_list = DB.default_attributs[typ]
            values = [stats_id,corpus_id, DBname, version,  created_at, visibility,typ]


            self._init_info_table(attributs_list)
            self.add_attributs(attributs_list,values)
            self._init_default_tables("stats")
            self._commit()
            self._DBsNames.append("main")
            self.logger.info("DB ({}) was initialized and saved on the disk: '{}'. ".format(fileName, path_to_db))
            self.logger.info("DB ({}) was connected.".format(fileName))
        else:
            self.logger.error("Given Project Folder is not exist: '{}'. ".format(prjFolder))
            sys.exit()




















##########################DB-Connection#############################

    def connect(self,path_to_db, encryption_key=False):
        self._check_file_existens(path_to_db)
        self._check_db_should_not_exist()

        self._encryption_key = encryption_key

        dbName = os.path.splitext(os.path.basename(path_to_db))[0]

        if self._encryption_key:
            self._db = sqlite3.connect(path_to_db)
            c = self._db.cursor()
            c.execute("PRAGMA key='{}'".format(self._encryption_key))
            self._commit()

        else:

            self._db = sqlite3.connect(path_to_db)

        try:
            self.tables()
        except sqlite3.DatabaseError, e:
            self.logger.error("DatabaseError: {}".format(e))
            sys.exit()
        # except Exception, e:
        #     self.logger.error("Something goes wrong: ('{}')".format(e))
        #     sys.exit()
        self._DBsNames.append("main")
        self.logger.info("DB ('{}') was connected".format(dbName))



    def attach(self,path_to_db, encryption_key_for_attachedDB=False):

        self._check_file_existens(path_to_db)
        self._check_db_should_exist()


        ### Check, if it is right DB and get name
        tempdb = DB(logger_level=logging.ERROR)
        tempdb.connect(path_to_db, encryption_key=encryption_key_for_attachedDB)
        del tempdb
        self._reinitialize_logger()

        dbName = os.path.splitext(os.path.basename(path_to_db))[0]
        
        if encryption_key_for_attachedDB:
            qeary = "ATTACH DATABASE '{path_to_db}' AS {dbName} KEY '{key}';".format(path_to_db=path_to_db, dbName=dbName, key=encryption_key_for_attachedDB)

        else:
            qeary = "ATTACH DATABASE '{path_to_db}' AS {dbName};".format(path_to_db=path_to_db, dbName=dbName)


        cursor = self._db.cursor()
        cursor.execute(qeary)
        #output = cursor.fetchall()
        self._attachedDBs.append((path_to_db, dbName))
        self._DBsNames.append(dbName)
        self._update_temp_tablesList_in_instance()
        self.logger.info("DB ('{}') was attached".format(dbName))
        #p("ghjkghjk")














##########################DB-Attributes#####################



    def add_attributs(self,attributs_names, values, dbname=False):
        self._check_db_should_exist()
        self._commit_if_inserts_was_did()

        if self.insertCV("info", [attr[0] for attr in attributs_names], values, dbname=dbname):
            return True
        else:
            self.logger.error("Attributes wasn't added into InfoTable (dbName:{})".format(dbname))
        #p(attributName_as_str, c="m")
        #p(values_as_str, c="m")
        ### Add Attributes



    def update_attribut(self,attribut_name, value, dbname=False):
        ### Exception Handling

        self._check_db_should_exist()
        self._commit_if_inserts_was_did()
        # Check if attributes and values have the same length
        if not isinstance(attribut_name, (str, unicode)):
            self.logger.error("Given AttributName should be an string or unicode object.")
            return None

        # if given attribute exist in the Info_Table
        if not filter(lambda x: unicode(attribut_name) == unicode(x), self.tableColumns("info")):
            self.logger.error("Given Attribute ('{}') is not exist in this DataBase.".format(attribut_name))
            return None


        if dbname:
            if dbname  in self.dbsNames():
                qeary = 'UPDATE {}.info  \nSET {}="{}";'.format(dbname,attribut_name,value)
            else:
                self.logger.error("Given dbName ('{}') is not exist in the current DB-Structure".format(dbname))
                return None
        else:
            qeary = 'UPDATE info  \nSET {}="{}";'.format(attribut_name,value)


        ### Update Attribute
        if "info" in self.tables():
            cursor = self._db.cursor()
            cursor.execute(qeary)
            self._commit()
            return True
        else:
            self.logger.error("Info-Table is wasn't found or not exist. Please initialize the Info Table, bevor you may add any attributes.")
            return False




    def get_attribut(self,attributName, dbname=False):
        self._check_db_should_exist()
        self._commit_if_inserts_was_did()

        if not isinstance(attributName, (str, unicode)):
            self.logger.error("Given AttributName should be an string or unicode object.")
            return None

        # p(repr(self.tableColumns("info")))
        # p(repr(unicode(attributName)))
        
        # if given attribute exist in the Info_Table
        if not filter(lambda x: unicode(attributName) == unicode(x), self.tableColumns("info")):
            self.logger.error("Given Attribute ('{}') is not exist in this DatebBank.".format(attributName))
            return None
  

        if dbname:
            if dbname  in self.dbsNames():
                qeary = 'SELECT {} FROM  {}.info;'.format(attributName, dbname)
            else:
                self.logger.error("Given dbName ('{}') is not exist in the current DB-Structure".format(dbname))
                return None
        else:
            qeary = 'SELECT {} FROM  info;'.format(attributName)



        if u"info" in unicode(self.tables()):
            cursor = self._db.cursor()
            cursor.execute(qeary)
            attribut = cursor.fetchall()
            return attribut[0][0]
        else:
            self.logger.error("Info-Table is wasn't found or not exist. Please initialize the Info Table, bevor you may add any attributes.")
            return None





    def get_all_attributs(self):
        self._check_db_should_exist()
        self._commit_if_inserts_was_did()
        if u"info" in unicode(self.tables()):
            qeary = 'SELECT * FROM  info;'
            cursor = self._db.cursor()
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



























##########################DB-Info######################


    def tables(self,dbname=False):
        self._check_db_should_exist()

        if dbname:
            if dbname in self._DBsNames:
                self.logger.debug("Table names was returned (dbname: '{}')".format(dbname))

                if len(self._tables_dict)>0:
                    return self._tables_dict[dbname]
                else:
                    return {}

            else:
                self.logger.error("Given dbName ('{}') is not exist in the current DB-Structure".format(dbname))
                return {}

        else:
            self.logger.debug("Table names was returned for 'main' DB. (from temp list)")
            if len(self._tables_dict)>0:
                return self._tables_dict["main"]
            else:
                return {}


    def fname(self,dbname=False):
        self._check_db_should_exist()
        self._commit_if_inserts_was_did()
        cur = self._db.cursor()
        cur.execute("PRAGMA database_list")
        rows = cur.fetchall()

        if dbname:
            if dbname  in self.dbsNames():
                for row in rows:
                    if row[1] == dbname:
                        return os.path.basename(row[2])
            else:
                self.logger.error("Given dbName ('{}') is not exist in the current DB-Structure".format(dbname))
                return None
        else:
            return os.path.basename(rows[0][2])



    def path(self, dbname=False):
        self._check_db_should_exist()
        self._commit_if_inserts_was_did()
        cur = self._db.cursor()
        cur.execute("PRAGMA database_list")
        rows = cur.fetchall()
        ## check existents of the dbName
        if dbname:
            if dbname  in self.dbsNames():
                for row in rows:
                    if row[1] == dbname:
                        return row[2]
            else:
                self.logger.error("Given dbName ('{}') is not exist in the current DB-Structure".format(dbname))
                return None
        else:
            return rows[0][2]


    def dirname(self, dbname=False):
        self._check_db_should_exist()
        self._commit_if_inserts_was_did()
        cur = self._db.cursor()
        cur.execute("PRAGMA database_list")
        rows = cur.fetchall()
        ## check existents of the dbName
        if dbname:
            if dbname  in self.dbsNames():
                for row in rows:
                    if row[1] == dbname:
                        return os.path.dirname(row[2])
            else:
                self.logger.error("Given dbName ('{}') is not exist in the current DB-Structure".format(dbname))
                return None
        else:
            return os.path.dirname(rows[0][2])





    def pathAttachedDBs(self):
        self._check_db_should_exist()
        self._commit_if_inserts_was_did()
        cur = self._db.cursor()
        cur.execute("PRAGMA database_list")
        rows = cur.fetchall()

        return [row[2] for row in rows if row[1]!= "main"]


    def fnameAttachedDBs(self):
        self._check_db_should_exist()
        self._commit_if_inserts_was_did()
        cur = self._db.cursor()
        cur.execute("PRAGMA database_list")
        rows = cur.fetchall()

        return [ os.path.basename(row[2]) for row in rows if row[1]!= "main"]



    def attachedDBs(self):
        self._check_db_should_exist()
        self._commit_if_inserts_was_did()
        cur = self._db.cursor()
        cur.execute("PRAGMA database_list")
        rows = cur.fetchall()
        return [ row[1] for row in rows if row[1]!= "main"]




    def dbsNames(self):
        cur = self._db.cursor()
        self._commit_if_inserts_was_did()
        cur.execute("PRAGMA database_list")
        rows = cur.fetchall()
        return [ row[1] for row in rows]
        # for row in rows:
        #     print row[0], row[1], row[2]



    def tableColumns(self, tableName,dbname=False):
        self._check_db_should_exist()
        self._commit_if_inserts_was_did()

        if not filter(lambda x: unicode(tableName) == unicode(x), self.tables(dbname=dbname)):
            self.logger.error("Given Table is not exist: ('{}').".format(tableName))
            return None

        ## check existents of the dbName
        if dbname:
            if dbname  in self.dbsNames():
                query = "PRAGMA {dbname}.table_info('{table_name}'); ".format(table_name=tableName, dbname=dbname)
            else:
                self.logger.error("Given dbName ('{}') is not exist in the current DB-Structure".format(dbname))
                return None
        else:
            query = "PRAGMA table_info('{table_name}'); ".format(table_name=tableName)


        cursor = self._db.cursor()
        cursor.execute(query)
        #tables_exist = cursor.fetchone()
        columns = cursor.fetchall()
        self.logger.debug("Columns for Table '{}'  was returned (dbName:'{}')".format(tableName,dbname))
        return [column[1] for column in columns]



    def tableColumnsTypes(self, tableName,dbname=False):
        self._check_db_should_exist()
        self._commit_if_inserts_was_did()

        if not filter(lambda x: unicode(tableName) == unicode(x), self.tables(dbname=dbname)):
            self.logger.error("Given Table is not exist: ('{}').".format(tableName))
            return None

        ## check existents of the dbName
        if dbname:
            if dbname  in self.dbsNames():
                query = "PRAGMA {dbname}.table_info('{table_name}'); ".format(table_name=tableName, dbname=dbname)
            else:
                self.logger.error("Given dbName ('{}') is not exist in the current DB-Structure".format(dbname))
                return None
        else:
            query = "PRAGMA table_info('{table_name}'); ".format(table_name=tableName)


        cursor = self._db.cursor()
        cursor.execute(query)
        #tables_exist = cursor.fetchone()
        columns = cursor.fetchall()
        self.logger.debug("Columns with types for Table '{}'  was returned (dbName:'{}')".format(tableName,dbname))
        return [(column[1],column[2]) for column in columns]





    def rowsNumber(self, tableName,dbname=False):
        self._check_db_should_exist()
        self._commit_if_inserts_was_did()
        ## check existents of the tableName
        if not filter(lambda x: unicode(tableName) == unicode(x), self.tables()):
            self.logger.error("Given Table is not exist: ('{}').".format(tableName))
            return None

        ## check existents of the dbName
        if dbname:
            if dbname  in self.dbsNames():
                query = "select count(*) from {dbname}.{table_name}; ".format(table_name=tableName, dbname=dbname)
            else:
                self.logger.error("Given dbName ('{}') is not exist in the current DB-Structure".format(dbname))
                return None
        else:
            query = "select count(*) from {table_name}; ".format(table_name=tableName)


        cursor = self._db.cursor()
        cursor.execute(query)
        #tables_exist = cursor.fetchone()
        number = cursor.fetchone()
        self.logger.debug("rowsNumber was returned")
        return number[0]
        #return [(column[1],column[2]) for column in columns]














##########################DB--Getters######################



    def lazy_getter(self, tableName, columns=False,  dbname=False, size_to_get=1000):
        self._check_db_should_exist()
        self._check_if_table_exist(tableName, dbname=dbname)
        self._commit_if_inserts_was_did()


        if columns:
            self._check_if_given_columns_exist(tableName, columns, dbname=dbname)
            columns_str = columns_list_to_str(columns)
            if not  columns_str:
                self.logger.error("TypeError: Given Columns should be given as a list. '{}' was given. ".format(type(columns)))
                sys.exit()
        else:
            columns_str = '*'



        if dbname:
            if dbname  in self.dbsNames():
                qeary = 'SELECT {} FROM  {}.{};'.format(columns_str, dbname, tableName)
            else:
                self.logger.error("Given dbName ('{}') is not exist in the current DB-Structure".format(dbname))
                sys.exit()
        else:
            qeary = 'SELECT {} FROM  {};'.format(columns_str, tableName)

        cursor = self._db.cursor()
        cursor.execute(qeary)
        #i=0
        while True:
            # i +=1
            # p(i)
            results = cursor.fetchmany(size_to_get)
            if not results:
                break
            for row in results:
                yield row




    def getall(self, tableName, columns=False,  dbname=False):
        self._check_db_should_exist()
        self._check_if_table_exist(tableName, dbname=dbname)
        self._commit_if_inserts_was_did()

        if columns:
            self._check_if_given_columns_exist(tableName, columns, dbname=dbname)
            columns_str = columns_list_to_str(columns)
            if not  columns_str:
                self.logger.error("TypeError: Given Columns should be given as a list. '{}' was given. ".format(type(columns)))
                sys.exit()
        else:
            columns_str = '*'

        if dbname:
            if dbname  in self.dbsNames():
                qeary = 'SELECT {} FROM  {}.{};'.format(columns_str, dbname, tableName)
            else:
                self.logger.error("Given dbName ('{}') is not exist in the current DB-Structure".format(dbname))
                sys.exit()
        else:
            qeary = 'SELECT {} FROM  {};'.format(columns_str, tableName)

        cursor = self._db.cursor()
        cursor.execute(qeary)
        results = cursor.fetchall()
        return results




    def getone(self, tableName, columns=False,  dbname=False):
        self._check_db_should_exist()
        self._check_if_table_exist(tableName, dbname=dbname)
        self._commit_if_inserts_was_did()

        if columns:
            self._check_if_given_columns_exist(tableName, columns, dbname=dbname)
            columns_str = columns_list_to_str(columns)
            if not  columns_str:
                self.logger.error("TypeError: Given Columns should be given as a list. '{}' was given. ".format(type(columns)))
                sys.exit()
        else:
            columns_str = '*'


        if dbname:
            if dbname  in self.dbsNames():
                qeary = 'SELECT {} FROM  {}.{};'.format(columns_str, dbname, tableName)
            else:
                self.logger.error("Given dbName ('{}') is not exist in the current DB-Structure".format(dbname))
                sys.exit()
        else:
            qeary = 'SELECT {} FROM  {};'.format(columns_str, tableName)

        cursor = self._db.cursor()
        cursor.execute(qeary)
        while True:
            results = cursor.fetchone()
            if not results:
                break

            yield results
  


    def getlimit(self, limit, tableName, columns=False,  dbname=False):
        self._check_db_should_exist()
        self._check_if_table_exist(tableName, dbname=dbname)
        self._commit_if_inserts_was_did()

        if columns:
            self._check_if_given_columns_exist(tableName, columns, dbname=dbname)
            columns_str = columns_list_to_str(columns)
            if not  columns_str:
                self.logger.error("TypeError: Given Columns should be given as a list. '{}' was given. ".format(type(columns)))
                sys.exit()
        else:
            columns_str = '*'


        if dbname:
            if dbname  in self.dbsNames():
                qeary = 'SELECT {} FROM  {}.{} LIMIT {};'.format(columns_str, dbname, tableName, limit)
            else:
                self.logger.error("Given dbName ('{}') is not exist in the current DB-Structure".format(dbname))
                sys.exit()
        else:
            qeary = 'SELECT {} FROM  {} LIMIT {};'.format(columns_str, tableName, limit)

        cursor = self._db.cursor()
        cursor.execute(qeary)
        results = cursor.fetchall()
        return results
  















##########################DB-Setters##################




    def lazy_writer(self, table_name, typ, columns_names=False,values=False, dbname=False):
        self._lazy_writer_number_inserts_after_last_commit +=1
        # self.writer_counter
        # self._lazyness_border

        if self._lazy_writer_number_inserts_after_last_commit <  self._lazyness_border:
            if typ.lower() == "cv":
                if columns_names and values:
                    self.insertCV(table_name,columns_names, values, dbname)
                else:
                    self.logger.error("LazyWriterError: Columns_names or Values wasn't given.")
                    sys.exit()

            elif typ.lower() == "v":
                if values:
                    self.insertV(table_name, values, dbname)
                else:
                    self.logger.error("LazyWriterError: Values wasn't given.")
                    sys.exit()

            elif typ.lower() == "csvs":
                if columns_names and values:
                    self.insertCsVs(table_name,columns_names, values, dbname)
                else:
                    self.logger.error("LazyWriterError: Columns_names or Values wasn't given.")
                    sys.exit()

            else:
                self.logger.error("Not Supported type of lazy_writer. This type was given: '{}'. Please use one of the supported types: ['cv','v', 'csvs'].".format(typ))
                sys.exit()
        else:
            self._commit()
            self._successful_commits_with_lazy_writer += 1
            self._lazy_writer_all_inserts_counter +=  self._lazy_writer_number_inserts_after_last_commit
            self._lazy_writer_number_inserts_after_last_commit = 0

            self.logger.debug("LazyWriter: Last {} inserts was committed in the DB. ".format(self._lazyness_border))




    def insertCV(self,table_name,columns_names,values, dbname=False):
        # INSERT INTO users (email, user_name, create_date)
        # VALUES ("foo@bar.com", "foobar", "2009-12-16");

        if table_name != "info":
            self.all_inserts_counter +=1
            self.number_of_new_inserts_after_last_commit += 1

        self._check_db_should_exist()
        # Check if attributes and values have the same length
        if len(columns_names) != len(values):
            self.logger.error("Length of given columns_names and values is not equal.")
            sys.exit()


        columnsName_as_str = columns_list_to_str(columns_names)
        values_as_str = values_list_to_str(values)
        #p(columnsName_as_str, c="m")
        #p(values_as_str, c="m")
        ### Add Attributes

        if dbname:
            if dbname  in self.dbsNames():
                qeary = 'INSERT INTO {dbname}.{tableName} ({columns}) \nVALUES ({values});'.format(columns=columnsName_as_str,values=values_as_str, tableName=table_name, dbname=dbname)
            else:
                self.logger.error("Given dbName ('{}') is not exist in the current DB-Structure".format(dbname))
                return None
        else:
            qeary = 'INSERT INTO {tableName} ({columns}) \nVALUES ({values});'.format(columns=columnsName_as_str,values=values_as_str, tableName=table_name)


        if table_name in self.tables():
            cursor = self._db.cursor()
            #p(qeary)
            cursor.execute(qeary)
            #self._commit()
            if dbname:
                self.logger.debug("Insertion: One row was inserted into '{}.{}'-Table. ".format(table_name, dbname))
            else:
                self.logger.debug("Insertion: One row was inserted into '{}'-Table. ".format(table_name))
            return True
        else:
            self.logger.error("Table ('{}') wasn't found or not exist. Please initialize the Info Table, before you may add any attributes.".format(table_name))
            return False





    def insertV(self,table_name,values, dbname=False):
        # INSERT INTO users VALUES (
        # NULL,
        # "johndoe",
        # "john@doe.com",
        # "2009.12.14"
        # );
        self._check_db_should_exist()
        # Check if attributes and values have the same length
        if table_name != "info":
            self.all_inserts_counter +=1
            self.number_of_new_inserts_after_last_commit += 1
        values_as_str = values_list_to_str(values)
        #p(columnsName_as_str, c="m")
        #p(values_as_str, c="m")
        ### Add Attributes

        if dbname:
            if dbname  in self.dbsNames():
                qeary = 'INSERT INTO {dbname}.{tableName}  \nVALUES ({values});'.format(values=values_as_str, tableName=table_name, dbname=dbname)
            else:
                self.logger.error("Given dbName ('{}') is not exist in the current DB-Structure".format(dbname))
                return None
        else:
            qeary = 'INSERT INTO {tableName}  \nVALUES ({values});'.format(values=values_as_str, tableName=table_name)

        #p(qeary, c="m")
        if table_name in self.tables():
            cursor = self._db.cursor()
            #p(qeary)
            cursor.execute(qeary)
            if dbname:
                self.logger.debug("Insertion: One row was inserted into '{}.{}'-Table. ".format(table_name, dbname))
            else:
                self.logger.debug("Insertion: One row was inserted into '{}'-Table. ".format(table_name))

            return True
        else:
            self.logger.error("Table ('{}') wasn't found or not exist. Please initialize the Info Table, before you may add any attributes.".format(table_name))
            return False



    def insertCsVs(self,table_name,columns_names,values, dbname=False):
        
        # INSERT INTO table1 (
        #  column1,
        #  column2 ,..)
        # VALUES
        #  (
        #  value1,
        #  value2 ,...),
        #  (
        #  value1,
        #  value2 ,...),
        #         ...
        #  (
        #  value1,
        #  value2 ,...);
        self.logger.warning("ImplementationError: 'insertCsVs' wasn't implemented. Please use other Inserter")#
        sys.exit()

        if table_name != "info":
            self.all_inserts_counter +=1
            #!!!!!self.number_of_new_inserts_after_last_commit + = "" insert number of insertion















##########################DB-Other Functions###############





    def get_db(self):
        return self._db


    def drop_table(self, table_name, dbname=False):
        self._check_db_should_exist()
        self._commit_if_inserts_was_did()
        if dbname:
            if dbname  in self.dbsNames():
                query = "DROP TABLE {}.{}".format(dbname,table_name)
            else:
                self.logger.error("Given dbName ('{}') is not exist in the current DB-Structure".format(dbname))
                return None
        else:
            query = "DROP TABLE {}".format(table_name)

        cursor = self._db.cursor()
        cursor.execute(query)
        #tables_exist = cursor.fetchone()
        tables_exist = cursor.fetchall()
        self._commit()
        self.logger.debug("Table names was deleted (dbname: '{}')".format(dbname))
        return [table_name[0] for table_name in tables_exist]



    def update(self,table_name,columns_names,values,condition, dbname=False):
        # UPDATE COMPANY SET ADDRESS = 'Texas' WHERE ID = 6;

        self._check_db_should_exist()
        self._commit_if_inserts_was_did()
        # Check if attributes and values have the same length
        if len(columns_names) != len(values):
            self.logger.error("Length of given columns_names and values is not equal.")
            sys.exit()


        columns_and_values_as_str = columns_and_values_to_str(columns_names,values)
        #p(columnsName_as_str, c="m")
        #p(values_as_str, c="m")
        ### Add Attributes

        if dbname:
            if dbname  in self.dbsNames():
                qeary = 'UPDATE {dbname}.{tableName}  \nSET {col_and_val} WHERE {condition};'.format(col_and_val=columns_and_values_as_str, dbname=dbname, tableName=table_name, condition=condition)
            else:
                self.logger.error("Given dbName ('{}') is not exist in the current DB-Structure".format(dbname))
                return None
        else:
            qeary = 'UPDATE {tableName}  \nSET {col_and_val} WHERE {condition};'.format(col_and_val=columns_and_values_as_str, tableName=table_name, condition=condition)


        if table_name in self.tables():
            cursor = self._db.cursor()
            #p(qeary)
            cursor.execute(qeary)
            self._commit()
            return True
        else:
            self.logger.error("Table ('{}') wasn't found or not exist. Please initialize the Info Table, before you may add any attributes.".format(table_name))
            return False




    def commit(self):
        self._check_db_should_exist()

        #self._lazy_writer_counter = 0
        self._db.commit()
        if self.number_of_new_inserts_after_last_commit>0:
            self.logger.debug("ExternCommitter: DB was committed ({} last inserts was wrote on the disk)".format(self.number_of_new_inserts_after_last_commit))
        else:
            self.logger.debug("ExternCommitter: DB was committed (some changes was wrote on the disk)".format(self.number_of_new_inserts_after_last_commit))
        self.inserts_was_committed += self.number_of_new_inserts_after_last_commit
        self.number_of_new_inserts_after_last_commit = 0

    def _commit(self):
        self._check_db_should_exist()

        self._db.commit()
        if self.number_of_new_inserts_after_last_commit>0:
            self.logger.debug("InternCommitter: DB was committed ({} last insert(s) was wrote on the disk)".format(self.number_of_new_inserts_after_last_commit))
        else:
            self.logger.debug("InternCommitter: DB was committed (some changes was wrote on the disk)".format(self.number_of_new_inserts_after_last_commit))
        self.inserts_was_committed += self.number_of_new_inserts_after_last_commit
        self.number_of_new_inserts_after_last_commit = 0


    def close(self):
        self.commit()
        self._db.close()
        self._db = False
        self.logger.info("DBExit: DB was committed and closed. (all changes was saved on the disk)")

    def _close(self):
        self.commit()
        self._db.close()
        self._db = False
        self.logger.debug("DBExit: DB was committed and closed. (all changes was saved on the disk)")



    def rollback(self):
        '''
        -> rollback to roll back any change to the database since the last call to commit.
        -> Please remember to always call commit to save the changes. If you close the connection using close or the connection to the file is lost (maybe the program finishes unexpectedly), not committed changes will be lost
        '''
        self._check_db_should_exist()
        self._db.rollback()
        self.logger.info("DB was rolled back.")




    def addTable(self, table_name, attributs_names_with_types_as_str,dbname=False, constrains=False) :
        self._check_db_should_exist()
        self._commit_if_inserts_was_did()

        if table_name not in self.tables():
            if constrains:
                if dbname:
                    if dbname  in self.dbsNames():
                        qeary = 'CREATE TABLE {}.{} ({}\n{});'.format(dbname,table_name,attributs_names_with_types_as_str, constrains)
                    else:
                        self.logger.error("Given dbName ('{}') is not exist in the current DB-Structure".format(dbname))
                        return None
                else:
                    qeary = 'CREATE TABLE {} ({}\n{});'.format(table_name,attributs_names_with_types_as_str, constrains)
            else:
                if dbname:
                    if dbname  in self.dbsNames():
                        qeary = 'CREATE TABLE {}.{} ({});'.format(dbname,table_name,attributs_names_with_types_as_str)
                    else:
                        self.logger.error("Given dbName ('{}') is not exist in the current DB-Structure".format(dbname))
                        return None
                else:
                    qeary = 'CREATE TABLE {} ({});'.format(table_name,attributs_names_with_types_as_str)
            
            try:
                cursor = self._db.cursor()
                cursor.execute(qeary)
                self._commit()
                dbname = "main" if not dbname else dbname
                self.logger.debug("'{}'-Table was added into '{}'-DB. ".format(table_name,dbname))
                self._update_temp_tablesList_in_instance()
                return True
            except sqlite3.OperationalError, e:
                self.logger.error("OperationalError while addTable ('{}'): {}".format(table_name,e))
                sys.exit()

        else:
            self.logger.error("'{}'-Table is already exist in the given DB. You can not initialize it one more time!".format(table_name))
            sys.exit()


    def change_key(self, new_key_to_enryption):
        self._check_db_should_exist()
        self._check_should_be_str_or_unicode(new_key_to_enryption)
        cursor = self._db.cursor()
        cursor.execute("PRAGMA rekey = '{}';".format(new_key_to_enryption))
        self._commit()


    def encrypte(self, key_to_encryption):
        '''
        set key
        '''
        self._check_db_should_exist()
        self._check_should_be_str_or_unicode(key_to_encryption)
        path_to_temp_db = os.path.join(self.dirname(), "temp_encrypted.db")
        path_to_current_db = self.path()
        fname_of_the_current_db = self.fname()
        cursor = self._db.cursor()
        cursor.execute("ATTACH DATABASE '{}' AS temp_encrypted KEY '{}';".format(path_to_temp_db, key_to_encryption))
        cursor.execute("SELECT sqlcipher_export('temp_encrypted');")
        cursor.execute("DETACH DATABASE temp_encrypted;")
        if os.path.isfile(path_to_temp_db):
            self.close()
            os.remove(path_to_current_db)
            os.rename(path_to_temp_db, path_to_current_db)
            if os.path.isfile(path_to_current_db):
                self.connect(path_to_current_db, encryption_key=key_to_encryption)
            else:
                self.logger.error("Renamed CurrentDB wasn't found. Encryption is fail!")
                sys.exit()

        else:
            self.logger.error("TempDB wasn't found. Encryption is fail!")
            sys.exit()

        # 
        


        # ATTACH DATABASE 'plaintext.db' AS plaintext KEY '';  -- empty key will disable encryption
        # SELECT sqlcipher_export('plaintext');
        # DETACH DATABASE plaintext;
        # p(self.fname())
        # p(self.path())


    def decrypte(self):
        '''
        delete key
        '''
        self._check_db_should_exist()
        path_to_temp_db = os.path.join(self.dirname(), "temp_decrypted.db")
        path_to_current_db = self.path()
        fname_of_the_current_db = self.fname()
        cursor = self._db.cursor()
        cursor.execute("ATTACH DATABASE '{}' AS temp_decrypted KEY '';".format(path_to_temp_db))
        cursor.execute("SELECT sqlcipher_export('temp_decrypted');")
        cursor.execute("DETACH DATABASE temp_decrypted;")
        if os.path.isfile(path_to_temp_db):
            self.close()
            os.remove(path_to_current_db)
            os.rename(path_to_temp_db, path_to_current_db)
            if os.path.isfile(path_to_current_db):
                self.connect(path_to_current_db)
            else:
                self.logger.error("Renamed CurrentDB wasn't found. Encryption is fail!")
                sys.exit()

        else:
            self.logger.error("TempDB wasn't found. Encryption is fail!")
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




###########################DB-Checker#########################

    def _check_should_be_str_or_unicode(self, giv_obj):
        if not isinstance(giv_obj, (str, unicode)):
            self.logger.error("Given Object is not from frollowing type: (str, unicode).")
            sys.exit()


    def _check_if_given_columns_exist(tableName,columns, dbname=False):
        for column in columns:
            if column not in  self.tableColumns(tableName):
                self.logger.error("Given Column '{}' is not exist in the following Table '{}' (dbname='{}') ".format(column,tableName,dbname))
                sys.exit()

    def _check_if_table_exist(self,tableName, dbname=False):
        if tableName not in self.tables(dbname=False):
            self.logger.error("Given Table '{}' is not exist (dbname='{}')) ".format(tableName,dbname))
            sys.exit()

    def _check_db_should_exist(self):
        if not self._db: 
            self.logger.warning("No active DB was found. You need to connect or initialize a DB first, before you can make some operation on the DB.")
            sys.exit()


    def _check_db_should_not_exist(self):
        if self._db: 
            self.logger.warning("An active DB was found. You need to initialize new empty Instance of DB before you can do this operation.")
            sys.exit()


    def _db_should_be_a_corpus(self):
        self._check_db_should_exist()
        db_typ = self.get_attribut(attributName="typ")
        if db_typ != "corpus":
            self.logger.error("Active DB is from typ '{}'. But it should be from typ 'corpus'. ".format(db_typ))
            sys.exit()


    def _db_should_be_stats(self):
        self._check_db_should_exist()
        db_typ = self.get_attribut(attributName="typ")
        if db_typ != "stats":
            self.logger.error("Active DB is from typ '{}'. But it should be from typ 'stats'. ".format(db_typ))
            sys.exit()





    def _check_file_existens(self, path_to_file):
        if not os.path.isfile(path_to_file):
            self.logger.error("DB-File wasn't found: ('{}').".format(path_to_db))
            #os._exit(1)
            sys.exit()










###########################DB-Evaluation###########################





    def evaluate_DBfile(self, path_to_db):
        pass





    def _evaluate_corpusDB(self):
        pass

    def _evaluate_statsDB(self):
        pass


































###########################DB-OtherHelpers################





    def _reinitialize_logger(self):
        #level=logging.INFO
        #p(self._logger_level, c="r")
        #coloredlogs.install(level=self._logger_level)
        #coloredlogs.install(level=self._logger_level)
        #self.logger.setLevel(self._logger_level)
        self.logger = Logger().myLogger("DatenBank", self._folder_for_log_files, use_logger=self._use_logger, level=self._logger_level)
        #self.logger.debug('Beginn of creating an instance of DB()')
        self.logger.debug("Logger was reinitialized.")



    def _init_default_tables(self,typ, template=False, additional_columns_with_types=False):
        if template and template!="NULL":
            if template in DB.templates:
                if additional_columns_with_types:
                    additional_columns_with_types += DB.templates[template]
                else:
                    additional_columns_with_types = DB.templates[template]
            else:
                self.logger.error("Given Template ('{}') is not exist".format(template))


        if typ == "corpus":
            self._init_default_table("corpus", "documents",
                    default_columns_and_types_for_corpus_documents, 
                    additional_collumns_with_types=additional_columns_with_types,
                    constrains=default_constraints_for_corpus_documents)
        
        elif typ == "stats":
            self._init_default_table("stats", "baseline",
                    default_columns_and_types_for_stats_baseline, 
                    additional_collumns_with_types=additional_columns_with_types)
 
            self._init_default_table("stats", "replications",
                    default_columns_and_types_for_stats_replications, 
                    additional_collumns_with_types=additional_columns_with_types,
                    constrains=default_constrains_for_stats_replications)
 
            self._init_default_table("stats", "reduplications",
                default_columns_and_types_for_stats_reduplications, 
                additional_collumns_with_types=additional_columns_with_types,
                constrains=default_constrains_for_stats_reduplications)
 

        else:
            self.logger.error("Given typ of DB ('{}') is not exist.".format(typ))
            sys.exit()


    def _init_default_table(self, typ, tableName , default_collumns_with_types, additional_collumns_with_types=False, constrains=False):
        if typ=="corpus":
            self._db_should_be_a_corpus()
        elif typ=="stats":
            self._db_should_be_stats()
        else:
            self.logger.error("Not supported typ ('{}')".format(typ))


        if additional_collumns_with_types:
            columns_and_types = default_collumns_with_types + additional_collumns_with_types
        else:
            columns_and_types = default_collumns_with_types
        constrains_in_str = constrains_list_to_str(constrains)
        attributs_names_with_types_as_str = columns_and_types_in_tuples_to_str(columns_and_types)
        self.addTable( tableName, attributs_names_with_types_as_str,constrains=constrains_in_str)
        self.logger.debug("{}-Table in {} was initialized".format(tableName, typ))



    def _commit_if_inserts_was_did(self):
        if self.number_of_new_inserts_after_last_commit >0:
            self._commit()



    def _init_info_table(self, attributs_names):
        #p(attributs_names)

        str_attributs_names = columns_and_types_in_tuples_to_str(attributs_names)
        if not str_attributs_names:
            self.logger.error("Something was wrong by Converting attributes into string. Program was stoped!")
            sys.exit()

        self.addTable("info", str_attributs_names)

        self.logger.debug("Info-Table was initialized")



    def _get_tables_from_db(self,dbname=False):
        self._check_db_should_exist()
        self._commit_if_inserts_was_did()
        if dbname:
            if dbname  in self.dbsNames():
                query = "SELECT name FROM {}.sqlite_master WHERE type='table';".format(dbname)
            else:
                self.logger.error("Given dbName ('{}') is not exist in the current DB-Structure".format(dbname))
                return None
        else:
            query = "SELECT name FROM sqlite_master WHERE type='table';"

        cursor = self._db.cursor()
        cursor.execute(query)
        #tables_exist = cursor.fetchone()
        tables_exist = cursor.fetchall()
        if dbname:
            self.logger.debug("TableNames was get directly from DB.  (dbname: '{}')".format(dbname))
        else:
            self.logger.debug("TableNames was get directly from DB.  (dbname: 'main')")
        
        return [table_name[0] for table_name in tables_exist]



    def _update_temp_tablesList_in_instance(self):
        self._check_db_should_exist()
        #p(self._DBsNames, c="r")
        self._tables_dict = {}
        if self._DBsNames:
            for DBName in self._DBsNames:
                self._tables_dict[DBName] = self._get_tables_from_db(dbname=DBName)
        else:
            self._tables_dict['main'] = self._get_tables_from_db(dbname='main')
        
        self.logger.debug("Temporary TableList in the DB-Instance was updated!")









