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
# By default, the sqlite module opens transactions implicitly before a Data Modification Language (DML) statement (i.e. INSERT/UPDATE/DELETE/REPLACE), and commits transactions implicitly before a non-DML, non-query statement (i. e. anything other than SELECT or the aforementioned).
from __future__ import absolute_import


import os
import copy
import sys
#import regex
import logging
import json
import traceback


from collections import defaultdict#, OrderedDict
from raven import Client
#from cached_property import cached_property
#import sqlite3 as sqlite
#import pysqlcipher
from pysqlcipher import dbapi2 as sqlite
#import glob
#import shutil
from time import gmtime, strftime
#import coloredlogs
import random

#from zas_rep_tools.src.classes.configer import Configer  
from zas_rep_tools.src.utils.logger import *       
import  zas_rep_tools.src.utils.db_helper as db_helper
from zas_rep_tools.src.utils.helpers import set_class_mode, print_mode_name, path_to_zas_rep_tools
from zas_rep_tools.src.utils.debugger import p

from zas_rep_tools.src.utils.error_tracking import initialisation
from zas_rep_tools.src.utils.traceback_helpers import print_exc_plus

import platform
if platform.uname()[0].lower() !="windows":
    import colored_traceback
    colored_traceback.add_hook()
else:
    import colorama



class DBHandler(object):
    __metaclass__ = db_helper.DBErrorCatcher
    #DBErrorCatcher = True


    templates = {
            "twitter":db_helper.default_tables["corpus"]["documents"]["twitter"],
            "blogger":db_helper.default_tables["corpus"]["documents"]["blogger"]
            }

    supported_db_typs = ["stats", "corpus"]
    path_to_json1 = os.path.join(path_to_zas_rep_tools, "src/extensions/json1/json1")
    def __init__(self,  lazyness_border=50000, rewrite= False, stop_if_db_already_exist=False,
                logger_folder_to_save=False,  logger_usage=True, logger_level=logging.INFO,
                logger_save_logs=True, logger_num_buffered=5, error_tracking=True,
                ext_tb=False, logger_traceback=False, mode="free"):

        
        ## Set Mode: Part 1
        self._mode = mode
        #p(self._mode, c="r")
        if mode != "free":
            _logger_level, _logger_traceback, _logger_save_logs = set_class_mode(self._mode)
            logger_level = _logger_level if _logger_level!=None else logger_level
            logger_traceback = _logger_traceback if _logger_traceback!=None else logger_traceback
            logger_save_logs = _logger_save_logs if _logger_save_logs!=None else logger_save_logs
        #p((logging.INFO, logging.DEBUG, logging.ERROR)) #-> (20, 10, 40)
        #p((logger_level, logger_traceback, logger_save_logs))
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
        self._error_tracking = error_tracking
        self._ext_tb = ext_tb
        self._rewrite = rewrite
        self._stop_if_db_already_exist = stop_if_db_already_exist

        #InstanceAttributes: Initialization
        self._db = False
        self._encryption_key = False
        self.is_encrypted = False
        self.compile_options = False



        self._attachedDBs_config = []
        self._attachedDBs_config_from_the_last_session = [] 
        self._tables_dict = {}
        self._indexes_dict = {}
        self._attributs_dict = {}
        self.dbnames = [] 


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
        # self.logger.newline(1)






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
            platform_name=False,  encryption_key=False, fileName=False,
            source=False, license=False, template_name=False, version=False,
            additional_columns_with_types_for_documents=False, corpus_id=False,stats_id=False):

        additional_columns_with_types_for_documents = copy.deepcopy(additional_columns_with_types_for_documents)
        supported_typs = DBHandler.supported_db_typs
        typ = typ.lower()
        if typ == "corpus":
            if not platform_name:
                self.logger.error("'Platform_name' wasn't given. 'Corpus' initialization need 'platform_name'.", exc_info=self._logger_traceback)
                return False

            if not self.init_corpus(prjFolder, DBname, language,  visibility, platform_name, encryption_key=encryption_key,fileName=fileName, source=source, license=license, template_name=template_name, version=version, corpus_id=corpus_id, additional_columns_with_types_for_documents=additional_columns_with_types_for_documents):
                return False
            
            return True

        elif typ == "stats":
            if not corpus_id:
                self.logger.error("'Corpus_id' wasn't given. 'Stats' initialization need Corpus_id.", exc_info=self._logger_traceback)
                return False
                
            if not self.init_stats(prjFolder, DBname, language, visibility, corpus_id, encryption_key=encryption_key,fileName=fileName, version=version, stats_id=stats_id):
                return False
            
            return True

        else:
            self.logger.error("Given DB-Typ is not supported! Please one of the following  types: '{}'.".format(typ, supported_typs), exc_info=self._logger_traceback)
            return False





    def init_corpus(self, prjFolder, DBname, language,  visibility, platform_name,
                    encryption_key=False,fileName=False, source=False, license=False,
                    template_name=False, version=False,
                    additional_columns_with_types_for_documents=False, corpus_id=False):
        ### Preprocessing: Create File_Name
        additional_columns_with_types_for_documents =copy.deepcopy(additional_columns_with_types_for_documents)
        self._encryption_key = encryption_key
        source="NULL" if not source else source
        license = "NULL" if not license else license
        version = "NULL" if not "NULL" else version
        template_name = "NULL" if not template_name else template_name
        typ= "corpus"

        
        
        if not corpus_id:
            corpus_id= db_helper.create_id(DBname,language, typ, visibility)
        #p((self._rewrite, self._stop_if_db_already_exist))
        fileName,path_to_db = db_helper.get_file_name(prjFolder,corpus_id,DBname,
                            language,visibility, typ,fileName, platform_name,
                            encrypted= True if encryption_key else False,
                            rewrite=self._rewrite,
                            stop_if_db_already_exist=self._stop_if_db_already_exist)
        
        if path_to_db is None:
            self.logger.info("InitCorpusDBProblem: DB with the same Name '{}' is already exist. InitProcess was stopped.".format(fileName))
            return False 

        
        ### Initialisation of DB
        if not self._check_db_should_not_exist():
            return False

        if os.path.isdir(prjFolder):

            if self._encryption_key:
                self._db = sqlite.connect(path_to_db, check_same_thread=False)
                self._check_db_compilation_options(self._db)
                try:
                    c = self._db.cursor()
                    c.execute("PRAGMA key='{}'".format(self._encryption_key))
                    self._commit()
                    self.is_encrypted = True
                except Exception as  exception:
                    print_exc_plus() if self._ext_tb else ""
                    self.logger.error("Something happens while initialization of Corpus '{}'".format( exception), exc_info=self._logger_traceback)
                    return False

            else:
                self._db = sqlite.connect(path_to_db, check_same_thread=False)
                self._check_db_compilation_options(self._db)

            self._update_temp_list_with_dbnames_in_instance()



            created_at = strftime("%Y-%m-%d %H:%M:%S", gmtime())
            attributs_list = db_helper.default_tables[typ]["info"]
            values = [corpus_id, DBname, platform_name, template_name, version, language, created_at, source,license,visibility,typ]
            
            if not self._init_info_table(attributs_list):
                self.logger.error("CorpusInitialisatioError: Corpus wasn't initialized because  info Table wasn't initialized. ", exc_info=self._logger_traceback)
                self._close()
                os.remove(path_to_db)
                return False
            #p(dict(zip([attr[0] for attr in attributs_list],values)))
            if not self.add_attributs(dict(zip([attr[0] for attr in attributs_list],values))):
                self.logger.error("CorpusInitialisatioError: Corpus wasn't initialized because attributes wasn't added into   info Table. ", exc_info=self._logger_traceback)
                self._close()
                os.remove(path_to_db)

                return False
            #p(template_name)
            if not self._init_default_tables("corpus", template=template_name, additional_columns_with_types=additional_columns_with_types_for_documents):
                self.logger.error("CorpusInitialisatioError: Corpus wasn't initialized because  default Tables wasn't initialized. ", exc_info=self._logger_traceback)
                self._close()
                os.remove(path_to_db)
                return False
            #self._init_documents_table_in_corpus()
            self._commit()
            
            self._update_temp_indexesList_in_instance()

            self.logger.info("Corpus-DB ({}) was initialized and saved on the disk: '{}'. ".format(fileName, path_to_db))
            self.logger.info("Corpus-DB ({}) was connected.".format(fileName))
            return True
        else:
            self.logger.error("Given Project Folder is not exist: '{}'. ".format(prjFolder), exc_info=self._logger_traceback)
            return False





    def init_stats(self, prjFolder, DBname, language, visibility, corpus_id,
                    encryption_key=False,fileName=False, version=False, stats_id=False):

        self._encryption_key = encryption_key

        ### Preprocessing: Create File_Name
        version = "NULL" if not version else version
        typ= "stats"

        if not stats_id:
            stats_id= db_helper.create_id(DBname,language, typ, visibility)

        
        if not stats_id:
            self.logger.error("Id wasn't created. Stats-ID was given without Corpus-ID. This is an illegal input.", exc_info=self._logger_traceback)
            return False


        fileName,path_to_db = db_helper.get_file_name(prjFolder,corpus_id,DBname,
                        language,visibility, typ, fileName, second_id=stats_id,
                        encrypted= True if encryption_key else False,
                        rewrite=self._rewrite, stop_if_db_already_exist=self._stop_if_db_already_exist)
        
        if path_to_db is None:
            self.logger.info("InitStatsDBProblem: DB with the same Name '{}' is already exist. InitProcess was stopped.".format(fileName))
            return False 

        ### Initialisation of DB
        if not self._check_db_should_not_exist():
            return False

        if os.path.isdir(prjFolder):
            if self._encryption_key:
                self._db = sqlite.connect(path_to_db, check_same_thread=False)
                self._check_db_compilation_options(self._db)
                try:
                    c = self._db.cursor()
                    c.execute("PRAGMA key='{}'".format(self._encryption_key))
                    self._commit()
                    self.is_encrypted = True
                except Exception as  exception:
                    print_exc_plus() if self._ext_tb else ""
                    self.logger.error("Something happens while initialization of Stats '{}'".format( exception), exc_info=self._logger_traceback)
                    return False

            else:
                self._db = sqlite.connect(path_to_db, check_same_thread=False)
                self._check_db_compilation_options(self._db)

            self._update_temp_list_with_dbnames_in_instance()
            if not stats_id:
                stats_id= db_helper.create_id(DBname,language, typ, visibility,corpus_id=corpus_id)
            created_at = strftime("%Y-%m-%d %H:%M:%S", gmtime())
            attributs_list = db_helper.default_tables[typ]["info"]
            values = [stats_id,corpus_id, DBname, version,  created_at, visibility,typ]


            if not self._init_info_table(attributs_list):
                self.logger.error("StatsInitialisatioError: Stats wasn't initialized because  info Table wasn't initialized. ", exc_info=self._logger_traceback)
                self._close()
                os.remove(path_to_db)
                return False

            if not self.add_attributs(dict(zip([attr[0] for attr in attributs_list],values))):
                self.logger.error("StatsInitialisatioError: Stats wasn't initialized because attributes wasn't added into   info Table. ", exc_info=self._logger_traceback)
                self._close()
                os.remove(path_to_db)
                return False

            if not self._init_default_tables("stats"):
                self.logger.error("StatsInitialisatioError: Corpus wasn't initialized because  default Tables wasn't initialized. ", exc_info=self._logger_traceback)
                self._close()
                os.remove(path_to_db)
                return False
            
            self._commit()
            #self.dbnames.append("main")

            self._update_temp_indexesList_in_instance()
            
            self.logger.info("Stats-DB ({}) was initialized and saved on the disk: '{}'. ".format(fileName, path_to_db))
            self.logger.info("Stats-DB ({}) was connected.".format(fileName))
            return True
        else:
            self.logger.error("Given Project Folder is not exist: '{}'. ".format(prjFolder), exc_info=self._logger_traceback)
            return False



    def initempty(self, prjFolder, DBname, encryption_key=False):
        ### Preprocessing: Create File_Name
        self._encryption_key = encryption_key
        fileName,path_to_db = db_helper.get_file_name_for_empty_DB(prjFolder,DBname,
                    encrypted= True if encryption_key else False,
                    rewrite=self._rewrite, stop_if_db_already_exist=self._stop_if_db_already_exist)
        
        if path_to_db is None:
            self.logger.info("InitEmptyDBProblem: DB with the same Name '{}' is already exist. InitProcess was stopped.".format(fileName))
            return False 

        if os.path.isdir(prjFolder):

            if self._encryption_key:
                self._db = sqlite.connect(path_to_db, check_same_thread=False)
                self._check_db_compilation_options(self._db)
                try:
                    c = self._db.cursor()
                    c.execute("PRAGMA key='{}'".format(self._encryption_key))
                    self._commit()
                    self.is_encrypted = True
                except Exception as  exception:
                    print_exc_plus() if self._ext_tb else ""
                    self.logger.error("Something happens while initialization of Corpus '{}'".format( exception), exc_info=self._logger_traceback)
                    return False

            else:
                self._db = sqlite.connect(path_to_db, check_same_thread=False)
                self._check_db_compilation_options(self._db)

            self._update_temp_list_with_dbnames_in_instance()
            self._update_temp_indexesList_in_instance()
            
            #p(self._db)

            self.logger.info("Empty-DB ({}) was initialized and saved on the disk: '{}'. ".format(fileName, path_to_db))
            self.logger.info("Empty-DB ({}) was connected.".format(fileName))
            return True
        else:
            self.logger.error("Given Project Folder is not exist: '{}'. ".format(prjFolder), exc_info=self._logger_traceback)
            return False




    def init_default_indexes(self):
        if not self._check_db_should_exist():
            return False
        try:
            for table_name, index_query_list in db_helper.default_indexes[self.typ()].iteritems():  
                for index_query in index_query_list:
                    #p(index_query)
                    c = self._db.cursor()
                    c.execute(index_query)
                    self.logger.debug("Index for '{}'-DB, '{}'-Table was initialized.".format(self.typ(), table_name))
            self._update_temp_indexesList_in_instance()
        except Exception, e:
            print_exc_plus() if self._ext_tb else ""
            self.logger.error("IndexesInitError: Following Exception was throw: '{}'".format(e), exc_info=self._logger_traceback)
            return False



# ##########################DB-Connection#############################

    def connect(self,path_to_db, encryption_key=False, reconnection=False, logger_debug=False):
        #p(logger_debug, "logger_debug")
        if not self._check_file_existens(path_to_db):
            return False
            # if path_to_db != ":memory:":
            #     return False
            # else:
            #     self.logger.info("DBConnection: Temporary DB will be created in the Working Memory. Please don't forget to save you DB on the disc after that.")

        if not self._check_db_should_not_exist():
            return False
        self._encryption_key = encryption_key

        dbName = os.path.splitext(os.path.basename(path_to_db))[0]

        if not self._validation_DBfile( path_to_db, encryption_key=encryption_key):
            self.logger.error("ValidationError: DB cannot be connected!", exc_info=self._logger_traceback)
            return False


        if self._encryption_key:
            try:
                self._db = sqlite.connect(path_to_db, check_same_thread=False)
                self._check_db_compilation_options(self._db)
                c = self._db.cursor()
                c.execute("PRAGMA key='{}'".format(self._encryption_key))
                self._commit()
                self.is_encrypted = True
            except Exception as  exception:
                print_exc_plus() if self._ext_tb else ""
                self.logger.error("Something happens while DB-Connection '{}'. PathToDB: '{}'. ".format( repr(exception), path_to_db), exc_info=self._logger_traceback)
                return False

        else:
            self._db = sqlite.connect(path_to_db, check_same_thread=False)
            self._check_db_compilation_options(self._db)

        try:
            self._update_temp_list_with_dbnames_in_instance()
            self._update_temp_tablesList_in_instance()
        except sqlite.DatabaseError, e:
            print_exc_plus() if self._ext_tb else ""
            self.logger.error("DatabaseError: {}".format(e), exc_info=self._logger_traceback)
            return False

        
        self._update_temp_attributsList_in_instance()
        # except Exception, e:
        #     self.logger.error("Something goes wrong: ('{}')".format(e), exc_info=self._logger_traceback)
        #     return False
        if reconnection:
            msg= "DB ('{}') was RE-connected".format(dbName)
        else:
            msg= "DB ('{}') was connected.".format(dbName)

        if logger_debug:
            self.logger.debug(msg)
        else:
            self.logger.info(msg)

        return True



    def attach(self,path_to_db, encryption_key=False, reattaching=False):
        #p((path_to_db, encryption_key), c="m")
        if not self._check_file_existens(path_to_db):
            return False

        if not self._check_db_should_exist():
            return False

        if not self._validation_DBfile( path_to_db, encryption_key=encryption_key):
            self.logger.error("ValidationError: DB cannot be attached!", exc_info=self._logger_traceback)
            return False

        ### Check, if it is right DB and get name
        tempdb = DBHandler(logger_level=logging.ERROR, mode=self._mode)
        tempdb.connect(path_to_db, encryption_key=encryption_key)
        #dbName = "{}_{}".format(tempdb.typ(), tempdb.name())
        del tempdb
        self._reinitialize_logger()

        dbName = "_" + os.path.splitext(os.path.basename(path_to_db))[0]
        
        if self._encryption_key:
            if encryption_key:
                query = "ATTACH DATABASE '{path_to_db}' AS {dbName} KEY '{key}';".format(path_to_db=path_to_db, dbName=dbName, key=encryption_key)

            else:
                query = "ATTACH DATABASE '{path_to_db}' AS {dbName} KEY '';".format(path_to_db=path_to_db, dbName=dbName)

        else:
            if encryption_key:
                query = "ATTACH DATABASE '{path_to_db}' AS {dbName} KEY '{key}';".format(path_to_db=path_to_db, dbName=dbName, key=encryption_key)

            else:
                query = "ATTACH DATABASE '{path_to_db}' AS {dbName};".format(path_to_db=path_to_db, dbName=dbName)

        #p(query)
        if dbName not in self.dbnames:
            try:
                cursor = self._db.cursor()
                cursor.execute(query)
            except Exception as  exception:
                print_exc_plus() if self._ext_tb else ""
                if "unrecognized token" in str(exception):
                    self.logger.error("DBAttachError:  While attaching of the '{}'-DB attacher get an following error: '{}'. Probably you used not allowed characters in the db or file name. (e.g. '.' not allowed).".format(dbName, repr(exception) ), exc_info=self._logger_traceback)
                else:    
                    self.logger.error("DBAttachError: Something happens while attaching of '{}'-DB: '{}'".format(dbName, repr(exception) ), exc_info=self._logger_traceback)
                return False

            self._attachedDBs_config.append((path_to_db, dbName, encryption_key))
            #p(self._attachedDBs_config, c="r")
            self._update_temp_list_with_dbnames_in_instance()
            self._update_temp_tablesList_in_instance()
            self._update_temp_attributsList_in_instance()
            if reattaching:
                self.logger.info("DB ('{}') was Reattached".format(dbName))
            else:
                self.logger.info("DB ('{}') was attached".format(dbName))
            return True
        else:
            self.logger.error("DB '{}' is already attached. You can not attached same DB more as 1 time!".format(dbName), exc_info=self._logger_traceback)
            return False




    def reattach(self, dbname=False):
        if not self._check_db_should_exist():
            return False
        self._commit_if_inserts_was_did()

        list_to_reattach =[]
        if dbname:
            list_to_reattach.append(dbname)
        else:
            list_to_reattach = [attacheddb[1] for attacheddb in self._attachedDBs_config]


        for attached_db_name in list_to_reattach:
            if attached_db_name  in self.dbnames:
                configs_list_of_detached_dbs =self.detach(attached_db_name)
                #p(configs_list_of_detached_dbs )
                if configs_list_of_detached_dbs:
                    path_to_db = configs_list_of_detached_dbs[0][0]
                    encryption_key = configs_list_of_detached_dbs[0][2]
                    dbname_to_retach = configs_list_of_detached_dbs[0][1]
                    if not self.attach(path_to_db, encryption_key=encryption_key):
                        self.logger.error("'{}' DB wasn't re-attached".format(dbname_to_retach), exc_info=self._logger_traceback)

                else:
                    self.logger.error("'{}' DB wasn't detached.".format(attached_db_name), exc_info=self._logger_traceback)
                #self.attach()
                # else:
                #     self.logger.error("Given Attached DB wasn't detached! DBName: '{}'. ".format(attached_db_name), exc_info=self._logger_traceback)
                #     return False
            else:
                self.logger.error("Given dbName ('{}') is not exist in the current DB-Structure.".format(attached_db_name), exc_info=self._logger_traceback)
                return False


        # self._update_temp_list_with_dbnames_in_instance()
        # self._update_temp_tablesList_in_instance()
        # self._update_temp_attributsList_in_instance()
        return True



    def detach(self, dbname=False):

        if not self._check_db_should_exist():
            return False
        self._commit_if_inserts_was_did()

        list_to_detach =[]
        detached_dbs = []
        if dbname:
            list_to_detach.append(dbname)
        else:
            list_to_detach = [attacheddb[1] for attacheddb in self._attachedDBs_config]

        #p(list_to_detach, c="r")
        for attached_db_name in list_to_detach:
            if attached_db_name  in self.dbnames:
                configs = self._get_configs_from_attached_DBList(attached_db_name)
                if configs:
                    #p(configs, c="m")
                    self._del_attached_db_from_a_config_list(attached_db_name)
                    query = "DETACH DATABASE '{}';".format( attached_db_name)
                    
                    try:
                        cursor = self._db.cursor()
                        cursor.execute(query)
                        self.logger.debug("'{}'-DB was detached.".format(attached_db_name))

                        detached_dbs.append( configs[0])
                    except Exception as  exception:
                        print_exc_plus() if self._ext_tb else ""
                        self.logger.error("Something happens while detaching of '{}'-DB: '{}'".format(attached_db_name, repr(exception) ), exc_info=self._logger_traceback)
                else:
                    self.logger.error("Given Attached DB '{}' is not in the Config-List of AttachedDBs. ".format(attached_db_name), exc_info=self._logger_traceback)
                    return False
            else:
                self.logger.error("Given dbName ('{}') is not exist in the current DB-Structure".format(attached_db_name), exc_info=self._logger_traceback)
                return False


        self._update_temp_list_with_dbnames_in_instance()
        self._update_temp_tablesList_in_instance()
        self._update_temp_attributsList_in_instance()
        return detached_dbs






##########################DB-Attributes#####################



    def add_attributs(self,inp_dict, dbname=False):
        if not self._check_db_should_exist():
            return False
        self._commit_if_inserts_was_did()

        if self.insertdict("info", inp_dict, dbname=dbname):
            self._update_temp_attributsList_in_instance()
            return True
        else:
            self.logger.error("Attributes wasn't added into InfoTable (dbName:{})".format(dbname), exc_info=self._logger_traceback)
            return False




    def update_attr(self,attribut_name, value, dbname=False):
        ### Exception Handling
        dbname = dbname if dbname else "main"
        if not self._check_db_should_exist():
            return False
        self._commit_if_inserts_was_did()
        # Check if attributes and values have the same length
        if not isinstance(attribut_name, (str, unicode)):
            self.logger.error("Given AttributName should be an string or unicode object.", exc_info=self._logger_traceback)
            return None

        # if given attribute exist in the Info_Table
        if not filter(lambda x: unicode(attribut_name) == unicode(x), self.col("info")):
            self.logger.error("Given Attribute ('{}') is not exist in this DataBase.".format(attribut_name), exc_info=self._logger_traceback)
            return None


        if dbname  in self.dbnames:
            query = 'UPDATE {}.info  \nSET {}="{}";'.format(dbname,attribut_name,value)
        else:
            self.logger.error("Given dbName ('{}') is not exist in the current DB-Structure".format(dbname), exc_info=self._logger_traceback)
            return None
        
        ### Update Attribute
        if "info" in self.tables(dbname=dbname):
            try:
                cursor = self._db.cursor()
                cursor.execute(query)
                self._commit()
                self._update_temp_attributsList_in_instance()
                return True
            except Exception as  exception:
                print_exc_plus() if self._ext_tb else ""
                self.logger.error("Something happens while detaching of '{}'-DB: '{}'".format(attached_db_name, repr(exception) ), exc_info=self._logger_traceback)
                return False
        else:
            self.logger.error("Info-Table is wasn't found or not exist. Please initialize the Info Table, bevor you may add any attributes.", exc_info=self._logger_traceback)
            return False



    def update_attrs(self, inp_dict_, dbname=False):
        ### Exception Handling
        dbname = dbname if dbname else "main"
        if not self._check_db_should_exist():
            return False
        self._commit_if_inserts_was_did()
        # Check if attributes and values have the same length
        # Check if attributes and values have the same length
        if not isinstance(inp_dict_, dict):
            self.logger.error("UpdateAttributes: InputDict is not an 'dict'.", exc_info=self._logger_traceback)
            return False
        inp_dict = copy.deepcopy(inp_dict_)

        # if given attribute exist in the Info_Table
        col_in_info_table = self.col("info")
        if not all(elem in col_in_info_table for elem in inp_dict_.keys()):
            average = list(set(inp_dict_.keys())-set(col_in_info_table))
            self.logger.error("Some of the given  Attributes ('{}') is not exist in this DataBase. ".format(average ), exc_info=self._logger_traceback)
            return None

        attrib_to_str = ",".join(["{}='{}'".format(k,v)  for k,v in inp_dict_.iteritems()])

        if dbname  in self.dbnames:
            query = 'UPDATE {}.info  \nSET {};'.format(dbname,attrib_to_str)
        else:
            self.logger.error("Given dbName ('{}') is not exist in the current DB-Structure".format(dbname), exc_info=self._logger_traceback)
            return None
        
        ### Update Attribute
        if "info" in self.tables(dbname=dbname):
            try:
                cursor = self._db.cursor()
                cursor.execute(query)
                self._commit()
                self._update_temp_attributsList_in_instance()
                return True
            except Exception as  exception:
                print_exc_plus() if self._ext_tb else ""
                self.logger.error("Something happens while detaching of '{}'-DB: '{}'".format(attached_db_name, repr(exception) ), exc_info=self._logger_traceback)
                return False
        else:
            self.logger.error("Info-Table is wasn't found or not exist. Please initialize the Info Table, bevor you may add any attributes.", exc_info=self._logger_traceback)
            return False





    def get_attr(self,attributName, dbname=False):
        if not self._check_db_should_exist():
            return False
        if not isinstance(attributName, (str, unicode)):
            self.logger.error("Given AttributName should be an string or unicode object.", exc_info=self._logger_traceback)
            return None

        dbname = dbname if dbname else "main" 

        if not self._attributs_dict:
            self.logger.warning("Temporary AttributesList is empty")
            return None

        # if given attribute exist in the Info_Table
        if attributName not in self._attributs_dict[dbname]:
            self.logger.error("Given Attribute ('{}') is not exist in this '{}'-DB.".format(attributName,dbname), exc_info=self._logger_traceback)
            return None


        if dbname:
            if dbname  in self.dbnames:
                return self._attributs_dict[dbname][attributName]
            else:
                self.logger.error("Given dbName ('{}') is not exist in the current DB-Structure".format(dbname), exc_info=self._logger_traceback)
                return None
        else:
            #p(self._attributs_dict)
            return self._attributs_dict['main'][attributName]




    def get_all_attr(self, dbname=False):
        if not self._check_db_should_exist():
            return False

        if u"info" in self.tables(dbname=dbname):
            if dbname:
                if dbname  in self.dbnames:
                    return self._attributs_dict[dbname]
                else:
                    self.logger.error("Given dbName ('{}') is not exist in the current DB-Structure".format(dbname), exc_info=self._logger_traceback)
                    return None
            else:
                return self._attributs_dict["main"]

        else:
            self.logger.error("Info-Table wasn't found or not exist. Please initialize the Info Table, bevor you may add any attributes.", exc_info=self._logger_traceback)
            return None

















##########################DB-Execute Commands#####################



    def execute(self, query):
        if not self._check_db_should_exist():
            return False
        self._commit_if_inserts_was_did()
        #p(query)
        try:
            cur = self._db.cursor()
            cur.execute(query)
            self._update_temp_tablesList_in_instance()
            self._update_temp_indexesList_in_instance()
            return cur

        except Exception as  exception:
            print_exc_plus() if self._ext_tb else ""
            self.logger.error("Something happens while execution of the following query: '{}'. See following Exception: '{}'. ".format(query,str(exception)), exc_info=self._logger_traceback)
            return False

        
    def executescript(self, query):
        if not self._check_db_should_exist():
            return False
        self._commit_if_inserts_was_did()
        try:
            cur = self._db.cursor()
            cur.execute(query)
            self._update_temp_tablesList_in_instance()
            self._update_temp_indexesList_in_instance()
            return cur
        except Exception as  exception:
            print_exc_plus() if self._ext_tb else ""
            self.logger.error("Something happens while execution of the following query: '{}'. See following Exception: '{}'. ".format(query,str(exception)), exc_info=self._logger_traceback)
            return False


    def executemany(self, query, argument):
        if not self._check_db_should_exist():
            return False
        self._commit_if_inserts_was_did()
        try:
            cur = self._db.cursor()
            cur.executemany(query, argument)
            self._update_temp_tablesList_in_instance()
            self._update_temp_indexesList_in_instance()
            return cur
        except Exception as  exception:
            print_exc_plus() if self._ext_tb else ""
            self.logger.error("Something happens while execution of the following query: '{}'. See following Exception: '{}'. ".format(query,str(exception)), exc_info=self._logger_traceback)
            return False
#executemany










##########################DB-Info######################

    def exist(self):
        return True if self._db else False

    def typ(self, dbname=False):
        return self.get_attr("typ", dbname=False)

    def name(self, dbname=False):
        return self.get_attr("name", dbname=False)


    def visibility(self, dbname=False):
        return self.get_attr("visibility", dbname=False)

    def version(self, dbname=False):
        return self.get_attr("version", dbname=False)

    def id(self, dbname=False):
        return self.get_attr("id", dbname=False)


    def encryption(self):
        if self.is_encrypted:
            return "encrypted"
        else:
            return "plaintext"

    def status(self):
        if self._db:
            if self._attachedDBs_config:
                return "manyDB"
            else:
                return "oneDB"
        else:
            return "noDB"

    def tables(self,dbname=False):
        if not self._check_db_should_exist():
            return False
        if dbname:
            if dbname in self.dbnames:
                self.logger.debug("Table names was returned (dbname: '{}')".format(dbname))

                if len(self._tables_dict)>0:
                    return self._tables_dict[dbname]
                else:
                    self.logger.critical("Temporary TableList is empty!")
                    return []

            else:
                self.logger.error("Given dbName ('{}') is not exist in the current DB-Structure".format(dbname), exc_info=self._logger_traceback)
                return []

        else:
            self.logger.debug("Table names was returned for 'main' DB. (from temp list)")
            if len(self._tables_dict)>0:
                return self._tables_dict["main"]
            else:
                return []


    def indexes(self,dbname=False):
        if not self._check_db_should_exist():
            return False
        if dbname:
            if dbname in self.dbnames:
                self.logger.debug("Indexes names was returned (dbname: '{}')".format(dbname))

                if len(self._indexes_dict)>0:
                    return self._indexes_dict[dbname]
                else:
                    self.logger.critical("Temporary IndexList is empty!")
                    return []

            else:
                self.logger.error("Given dbName ('{}') is not exist in the current DB-Structure".format(dbname), exc_info=self._logger_traceback)
                return []

        else:
            self.logger.debug("Indexes names was returned for 'main' DB. (from temp list)")
            if len(self._indexes_dict)>0:
                return self._indexes_dict["main"]
            else:
                return []




        

    def fname(self,dbname=False):
        if not self._check_db_should_exist():
            return False
        self._commit_if_inserts_was_did()
        try:
            cur = self._db.cursor()
            cur.execute("PRAGMA database_list")
            rows = cur.fetchall()
        except Exception as  exception:
            print_exc_plus() if self._ext_tb else ""
            self.logger.error("Something happens while getting DB-FileName:  '{}'.".format( repr(exception) ), exc_info=self._logger_traceback)
            return False

        if dbname:
            if dbname  in self.dbnames:
                for row in rows:
                    if row[1] == dbname:
                        return os.path.basename(row[2])
            else:
                self.logger.error("Given dbName ('{}') is not exist in the current DB-Structure".format(dbname), exc_info=self._logger_traceback)
                return None
        else:
            return os.path.basename(rows[0][2])



    def path(self, dbname=False):
        if not self._check_db_should_exist():
            return False
        self._commit_if_inserts_was_did()
        try:
            cur = self._db.cursor()
            cur.execute("PRAGMA database_list")
            rows = cur.fetchall()
        except Exception as  exception:
            print_exc_plus() if self._ext_tb else ""
            self.logger.error("Something happens while getting DB-Path:  '{}'.".format( repr(exception) ), exc_info=self._logger_traceback)
            return False
        ## check existents of the dbName
        if dbname:
            if dbname  in self.dbnames:
                for row in rows:
                    if row[1] == dbname:
                        return row[2]
            else:
                self.logger.error("Given dbName ('{}') is not exist in the current DB-Structure".format(dbname), exc_info=self._logger_traceback)
                return None
        else:
            return rows[0][2]


    def dirname(self, dbname=False):
        if not self._check_db_should_exist():
            return False
        self._commit_if_inserts_was_did()
        try: 
            cur = self._db.cursor()
            cur.execute("PRAGMA database_list")
            rows = cur.fetchall()
        except Exception as  exception:
            print_exc_plus() if self._ext_tb else ""
            self.logger.error("Something happens while getting DB-DirName:  '{}'.".format( repr(exception) ), exc_info=self._logger_traceback)
            return False

        ## check existents of the dbName
        if dbname:
            if dbname  in self.dbnames:
                for row in rows:
                    if row[1] == dbname:
                        return os.path.dirname(row[2])
            else:
                self.logger.error("Given dbName ('{}') is not exist in the current DB-Structure".format(dbname), exc_info=self._logger_traceback)
                return None
        else:
            return os.path.dirname(rows[0][2])


    def pathAttachedDBs(self):
        if not self._check_db_should_exist():
            return False
        self._commit_if_inserts_was_did()
        try:
            cur = self._db.cursor()
            cur.execute("PRAGMA database_list")
            rows = cur.fetchall()
        except Exception as  exception:
            print_exc_plus() if self._ext_tb else ""
            self.logger.error("Something happens while getting Paths of AttachedDBs:  '{}'.".format( repr(exception) ), exc_info=self._logger_traceback)
            return False

        return [row[2] for row in rows if row[1]!= "main"]


    def fnameAttachedDBs(self):
        if not self._check_db_should_exist():
            return False

        self._commit_if_inserts_was_did()

        try:
            cur = self._db.cursor()
            cur.execute("PRAGMA database_list")
            rows = cur.fetchall()
        except Exception as  exception:
            print_exc_plus() if self._ext_tb else ""
            self.logger.error("Something happens while getting FileName of AttachedDBs:  '{}'.".format( repr(exception) ), exc_info=self._logger_traceback)
            return False

        return [ os.path.basename(row[2]) for row in rows if row[1]!= "main"]



    def attached(self):
        if not self._check_db_should_exist():
            return False
        self._commit_if_inserts_was_did()

        try:
            cur = self._db.cursor()
            cur.execute("PRAGMA database_list")
            rows = cur.fetchall()
        except Exception as  exception:
            print_exc_plus() if self._ext_tb else ""
            self.logger.error("Something happens while getting of AttachedDBs:  '{}'.".format( repr(exception) ), exc_info=self._logger_traceback)
            return False

        return [ row[1] for row in rows if row[1]!= "main"]





    def col(self, tableName,dbname=False):
        if not self._check_db_should_exist():
            return False
        self._commit_if_inserts_was_did()

        if not filter(lambda x: unicode(tableName) == unicode(x), self.tables(dbname=dbname)):
            self.logger.error("Given Table is not exist: ('{}').".format(tableName), exc_info=self._logger_traceback)
            return None

        ## check existents of the dbName
        if dbname:
            if dbname  in self.dbnames:
                query = "PRAGMA {dbname}.table_info('{table_name}'); ".format(table_name=tableName, dbname=dbname)
            else:
                self.logger.error("Given dbName ('{}') is not exist in the current DB-Structure".format(dbname), exc_info=self._logger_traceback)
                return None
        else:
            query = "PRAGMA table_info('{table_name}'); ".format(table_name=tableName)

        try:
            cursor = self._db.cursor()
            cursor.execute(query)
            columns = cursor.fetchall()
        except Exception as  exception:
            print_exc_plus() if self._ext_tb else ""
            self.logger.error("Something happens while getting of TableColumns for '{}'-Table:  '{}'.".format(tableName, repr(exception) ), exc_info=self._logger_traceback)
            return False

        self.logger.debug("Columns for Table '{}'  was returned (dbName:'{}')".format(tableName,dbname))
        return [column[1] for column in columns]



    def colt(self, tableName,dbname=False):
        if not self._check_db_should_exist():
            return False
        self._commit_if_inserts_was_did()

        if not filter(lambda x: unicode(tableName) == unicode(x), self.tables(dbname=dbname)):
            self.logger.error("Given Table is not exist: ('{}').".format(tableName), exc_info=self._logger_traceback)
            return None

        ## check existents of the dbName
        if dbname:
            if dbname  in self.dbnames:
                query = "PRAGMA {dbname}.table_info('{table_name}'); ".format(table_name=tableName, dbname=dbname)
            else:
                self.logger.error("Given dbName ('{}') is not exist in the current DB-Structure".format(dbname), exc_info=self._logger_traceback)
                return None
        else:
            query = "PRAGMA table_info('{table_name}'); ".format(table_name=tableName)

        try:
            cursor = self._db.cursor()
            cursor.execute(query)
            columns = cursor.fetchall()
        except Exception as  exception:
            print_exc_plus() if self._ext_tb else ""
            self.logger.error("Something happens while getting of Types of TableColumns for '{}'-Table:  '{}'.".format(tableName, repr(exception) ), exc_info=self._logger_traceback)
            return False

        self.logger.debug("Columns with types for Table '{}'  was returned (dbName:'{}')".format(tableName,dbname))
        return [(column[1],column[2]) for column in columns]



    def rownum(self, tableName,dbname=False):
        if not self._check_db_should_exist():
            return False
        self._commit_if_inserts_was_did()
        ## check existents of the tableName
        if not filter(lambda x: unicode(tableName) == unicode(x), self.tables(dbname=dbname)):
            self.logger.error("Given Table is not exist: ('{}').".format(tableName), exc_info=self._logger_traceback)
            return None

        ## check existents of the dbName
        if dbname:
            if dbname  in self.dbnames:
                query = "select count(*) from {dbname}.{table_name}; ".format(table_name=tableName, dbname=dbname)
            else:
                self.logger.error("Given dbName ('{}') is not exist in the current DB-Structure".format(dbname), exc_info=self._logger_traceback)
                return None
        else:
            query = "select count(*) from {table_name}; ".format(table_name=tableName)


        try:
            cursor = self._db.cursor()
            cursor.execute(query)
            number = cursor.fetchone()
        except Exception as  exception:
            print_exc_plus() if self._ext_tb else ""
            self.logger.error("Something happens while getting of RowsNumber for '{}'-Table:  '{}'.".format(tableName, repr(exception) ), exc_info=self._logger_traceback)
            return False

        self.logger.debug("Number of Rows was returned")
        return number[0]
        #return [(column[1],column[2]) for column in columns]














##########################DB--Getters######################


    def getall(self, tableName, columns=False, select=False,  dbname=False, where=False, connector_where="AND", limit=-1, offset=-1):
        cursor = self._intern_getter(tableName, columns=columns, select=select,  dbname=dbname, where=where, connector_where=connector_where,limit=limit, offset=offset)

        if cursor:
            return cursor.fetchall()
        else:
            self.logger.debug("GetterError: Nor Cursor Element was passed from intern getter.")
            return []
            



    def lazyget(self, tableName, columns=False, select=False,  dbname=False, where=False, connector_where="AND", size_to_fetch=1000, output="list", limit=-1, offset=-1):
        if output == "list":
            for row in  self.getlistlazy(tableName, columns=columns, select=select,  dbname=dbname, where=where, connector_where=connector_where, size_to_fetch=size_to_fetch,limit=limit, offset=offset):
                yield row

        elif output == "dict":
            for getted_dict in  self.getdictlazy( tableName, columns=columns, select=select,  dbname=dbname, where=where, connector_where=connector_where, size_to_fetch=size_to_fetch,limit=limit, offset=offset):
                yield getted_dict

        else:
            self.logger.error("LazyGetter: '{}'-OutputFormat is not supported. Please use one of the following: '['list','dict']' ".format(output), exc_info=self._logger_traceback)
            yield False
            return 




    def getdictlazy(self, tableName, columns=False, select=False,  dbname=False, where=False, connector_where="AND", size_to_fetch=1000, limit=-1, offset=-1):
        list_with_keys = []
        if columns:
            if isinstance(columns, (unicode, str)):
                columns = [columns]
            list_with_keys += columns

        if not columns:
            columns = self.col(tableName, dbname=dbname)
            list_with_keys += columns

        if select:       
            if isinstance(select, (unicode, str)):
                select = [select]
            list_with_keys += select

        for row in self.getlistlazy( tableName, columns=columns, select=select,  dbname=dbname, where=where, connector_where=connector_where, size_to_fetch=size_to_fetch,limit=limit, offset=offset):
            yield { k:v for k,v in zip(list_with_keys,row)}



    def getlistlazy(self, tableName, columns=False, select=False,  dbname=False, where=False, connector_where="AND", size_to_fetch=1000, limit=-1, offset=-1):
        cursor = self._intern_getter(tableName, columns=columns, select=select,  dbname=dbname, where=where, connector_where=connector_where,limit=limit, offset=offset)

        if cursor:
            while True:
                # i +=1
                # p(i)
                results = cursor.fetchmany(size_to_fetch)
                if not results:
                    break
                for row in results:
                    yield row
        else:
            self.logger.debug("GetterError: Nor Cursor Element was passed from intern getter.")
            yield []
            return

 

    def _intern_getter(self, tableName, columns=False, select=False,  dbname=False, where=False, connector_where="AND", limit=-1, offset=-1):
        # return cursor object
        if not self._check_db_should_exist():
            return False
        if not self._check_if_table_exist(tableName, dbname=dbname):
            return False
        self._commit_if_inserts_was_did()


        if columns:
            if isinstance(columns, (str, unicode)):
                columns = [columns]
            if not self._check_if_given_columns_exist(tableName, columns, dbname=dbname):
                return False

            if select:
                if isinstance(select, (str, unicode)):
                    select = [select]
            else:
                select = []

            select_conditions = db_helper.list_of_select_objects_to_str(columns+select)
            if not  select_conditions:
                self.logger.error("TypeError: Given Columns should be given as a list. '{}' was given. ".format(type(columns)), exc_info=self._logger_traceback)
                return None
        elif select:
            if isinstance(select, (str, unicode)):
                select = [select]
            select_conditions = db_helper.list_of_select_objects_to_str(select)

            if not  select_conditions:
                self.logger.error("TypeError: Given Columns should be given as a list. '{}' was given. ".format(type(columns)), exc_info=self._logger_traceback)
                return None

        else:
            select_conditions = '*'


        if where:
            where_cond_as_str = db_helper.where_condition_to_str(where, connector=connector_where)
            #p(where_cond_as_str)
            if not where_cond_as_str:
                self.logger.error("GetAllError: Where-Condition(s) wasn't compiled to String!", exc_info=self._logger_traceback)
                return False

        if dbname:
            if dbname  not in self.dbnames:
                self.logger.error("Given dbName ('{}') is not exist in the current DB-Structure".format(dbname), exc_info=self._logger_traceback)
                return None
        else:
            dbname = "main"

        if where:
            query = 'SELECT {} FROM  {}.{} \nWHERE {} LIMIT {} OFFSET {};'.format(select_conditions, dbname, tableName, where_cond_as_str, limit, offset)
        else:
            query = 'SELECT {} FROM  {}.{} LIMIT {} OFFSET {};'.format(select_conditions, dbname, tableName, limit, offset)


        #p(query, c="m")
        try:
            cursor = self._db.cursor()
            cursor.execute(query)
            return cursor
        except Exception as  exception:
            print_exc_plus() if self._ext_tb else ""
            self.logger.error("Exception was throw:  '{}' for following query: '{}'".format( repr(exception), query.replace("\n", " ") ), exc_info=self._logger_traceback)
            return False




##########################DB-Setters##################



    def lazyinsert(self, table_name, inp_obj,  dbname=False):
        
        if isinstance(inp_obj, dict):
            if not self.insertdict(table_name, inp_obj, dbname):
                return False
        elif isinstance(inp_obj, list):
            if not self.insertlist(table_name, inp_obj, dbname):
                return False
        else:
            self.logger.error("Not Supported type of lazy_writer. This type was given: '{}'. Please use one of the supported types: ['dict','list',].".format(typ), exc_info=self._logger_traceback)
            return False

        self._lazy_writer_number_inserts_after_last_commit +=1

        if self._lazy_writer_number_inserts_after_last_commit >=  self._lazyness_border:
            self._commit()
            self._successful_commits_with_lazy_writer += 1
            self._lazy_writer_all_inserts_counter +=  self._lazy_writer_number_inserts_after_last_commit
            self._lazy_writer_number_inserts_after_last_commit = 0
            self.logger.debug("LazyWriter: Last {} inserts was committed in the DB. ".format(self._lazyness_border))
        return True

    def insertdict(self,table_name, inp_dict, dbname=False):
        if not isinstance(inp_dict, dict):
            self.logger.error("InsertDictError: Given object in not an dict!", exc_info=self._logger_traceback)
            return False
        #p(inp_dict)
        try:
            random_value  = random.choice(inp_dict.values())
            type_mask = [type(value) for value in inp_dict.values()]
            if len(set(type_mask)) == 1:
                if isinstance(random_value, (list,tuple)):
                    self.logger.debug("InsertDict: Many rows was found in the given dict. ")
                    if not self._insertdict_with_many_rows(table_name, inp_dict, dbname=dbname):
                        return False
                else:
                    self.logger.debug("InsertDict: One unique row was found in the given dict. ")
                    if not self._insertdict_with_one_row(table_name, inp_dict, dbname=dbname):
                        return False
            else:
                self.logger.debug("InsertDict: One unique row was found in the given dict. ")
                if not self._insertdict_with_one_row(table_name, inp_dict, dbname=dbname):
                    return False
            
            return True

        except Exception, e:
            print_exc_plus() if self._ext_tb else ""
            self.logger.error("InsertDictError: Following Exception was throw: '{}'".format(e), exc_info=self._logger_traceback)
            return False



    def _dict_values_to_list_of_tuples(self,inp_dict):
        dict_as_list = []
        for rows in inp_dict.itervalues():
            #p(rows, c="b")
            #p(tuple(rows), c="b")
            dict_as_list.append(tuple(rows))

        #p(dict_as_list, "111")
        output = zip(*dict_as_list)
        #p(output, "222")
        return output




    def _insertdict_with_many_rows(self,table_name, inp_dict_, dbname=False):
        if not self._check_db_should_exist():
            return False
        # Check if attributes and values have the same length
        if not isinstance(inp_dict_, dict):
            self.logger.error("InsertDictError: InputDict is not an 'dict'.", exc_info=self._logger_traceback)
            return False
        inp_dict = copy.deepcopy(inp_dict_)
        if not self._dict_preprocessing_bevore_inserting(inp_dict, "many"):
            return False

        columns = ', '.join(inp_dict.keys())
        placeholders = db_helper.values_to_placeholder(len(inp_dict))
        number_of_values = len(random.choice(inp_dict.values()))
        #p((number_of_values))

        data = self._dict_values_to_list_of_tuples(inp_dict)
        #p(data)
        if not data:
            self.logger.error("Insertion: Insertion was failed! ", exc_info=self._logger_traceback)
            return False
 

        if dbname:
            if dbname  not in self.dbnames:
                self.logger.error("Given dbName ('{}') is not exist in the current DB-Structure".format(dbname), exc_info=self._logger_traceback)
                return None
        else:
            dbname="main"

        query = 'INSERT INTO {}.{} ({}) VALUES ({})'.format(dbname,table_name, columns, placeholders) 
        #p(query, c="r")

        if table_name in self.tables(dbname=dbname):
            try:
                cursor = self._db.cursor()
                cursor.executemany(query, data)
                if table_name != "info":
                    self.all_inserts_counter +=number_of_values
                    self.number_of_new_inserts_after_last_commit += number_of_values

                return True
            except Exception as  exception:
                print_exc_plus() if self._ext_tb else ""
                self.logger.debug("Following Query could have an Error: '{}'.".format(query))

                if "has no column named" in str(exception):
                    self.logger.error("Insertion: One of the columns is not in the Table. See Exception:  '{}'. Current Insertion is not done.".format( repr(exception) ), exc_info=self._logger_traceback)
                else:
                    self.logger.error("Insertion: Something happens at the InsertCV-Method:  '{}'. Current Insertion was ignored.".format( repr(exception) ), exc_info=self._logger_traceback)
                return False

            if dbname:
                self.logger.debug("Insertion: One row was inserted into '{}.{}'-Table. ".format(table_name, dbname))
            else:
                self.logger.debug("Insertion: One row was inserted into '{}'-Table. ".format(table_name))
            return True
        else:
            self.logger.error("Insertion: Table ('{}') wasn't found or not exist. Please initialize the Info Table, before you may add any attributes.".format(table_name), exc_info=self._logger_traceback)
            return False


    def _dict_preprocessing_bevore_inserting(self, inp_dict, mode):
        try:
            for k,v in inp_dict.iteritems():
                if mode == "one":
                    if isinstance(v, (list,dict,tuple)):
                        inp_dict[k] = json.dumps(v)
                else:
                    values_list = []
                    for item in v:
                        if isinstance(item, (list,dict,tuple)):
                            values_list.append(json.dumps(item))
                        else:
                            values_list.append(item)
                    inp_dict[k] = values_list
            return True
        except Exception, e:
            print_exc_plus() if self._ext_tb else ""
            self.logger.error("DictPreprocessig: '{}' ".format(e), exc_info=self._logger_traceback)
            return False



    def _insertdict_with_one_row(self,table_name, inp_dict, dbname=False):
        if not self._check_db_should_exist():
            return False
        # Check if attributes and values have the same length
        if not isinstance(inp_dict, dict):
            self.logger.error("InsertDictError: InputDict is not form 'dict' Format.", exc_info=self._logger_traceback)
            return False
        inp_dict = copy.deepcopy(inp_dict)
        if not self._dict_preprocessing_bevore_inserting(inp_dict, "one"):
            return False

        columns = ', '.join(inp_dict.keys())
        placeholders = ':'+', :'.join(inp_dict.keys())

        if dbname:
            if dbname  not in self.dbnames:
                self.logger.error("Given dbName ('{}') is not exist in the current DB-Structure".format(dbname), exc_info=self._logger_traceback)
                return None
        else:
            dbname="main"

        main_query = 'INSERT INTO {}.{} (%s) VALUES (%s)'.format(dbname,table_name) 
        query = main_query  % (columns, placeholders)

        #p((query, inp_dict))
        if table_name in self.tables(dbname=dbname):
            try:
                cursor = self._db.cursor()
                cursor.execute(query, inp_dict)
                if table_name != "info":
                    self.all_inserts_counter +=1
                    self.number_of_new_inserts_after_last_commit += 1
                return True
            except Exception as  exception:
                print_exc_plus() if self._ext_tb else ""
                self.logger.debug("Following Query could have an Error: '{}'.".format(query))

                if "has no column named" in str(exception):
                    self.logger.error("Insertion: One of the columns is not in the Table. See Exception:  '{}'. Current Insertion is not done.".format( repr(exception) ), exc_info=self._logger_traceback)
                else:
                    self.logger.error("Insertion: Something happens at the InsertCV-Method:  '{}'. Current Insertion is not done.".format( repr(exception) ), exc_info=self._logger_traceback)
                return False

            if dbname:
                self.logger.debug("Insertion: One row was inserted into '{}.{}'-Table. ".format(table_name, dbname))
            else:
                self.logger.debug("Insertion: One row was inserted into '{}'-Table. ".format(table_name))
            return True
        else:
            self.logger.error("InsertError: Table ('{}') wasn't found or not exist. Please initialize the Info Table, before you may add any attributes.".format(table_name), exc_info=self._logger_traceback)
            return False



    def insertlist(self,table_name, inp_list, dbname=False):
        if not isinstance(inp_list, list):
            self.logger.error("InsertDictError: Given object in not an list!", exc_info=self._logger_traceback)
            return False
        #p(inp_list)
        try:
            random_value  = random.choice(inp_list)
            type_mask = [type(value) for value in inp_list]
            if len(set(type_mask)) == 1:
                if isinstance(random_value, (list,tuple)):
                    self.logger.debug("InsertList: Many rows was found in the given list. ")
                    if not self._insertlist_with_many_rows(table_name, inp_list, dbname=dbname):
                        return False
                else:
                    self.logger.debug("InsertList: One unique row was found in the given list. ")
                    if not self._insertlist_with_one_row(table_name, inp_list, dbname=dbname):
                        return False
            else:
                self.logger.debug("InsertList: One unique row was found in the given list. ")
                if not self._insertlist_with_one_row(table_name, inp_list, dbname=dbname):
                    return False
            
            return True

        except Exception, e:
            print_exc_plus() if self._ext_tb else ""
            self.logger.error("InsertListError: Following Exception was throw: '{}'".format(e), exc_info=self._logger_traceback)
            return False




    def _insertlist_with_many_rows(self,table_name, inp_list, dbname=False):
        if not self._check_db_should_exist():
            return False

        number  = len(inp_list[0])
        values_as_tuple = db_helper.values_to_tuple(inp_list, "many")

        if  not values_as_tuple:
            self.logger.error("Given  Values wasn't packet into the list.", exc_info=self._logger_traceback)
            return False

        if dbname:
            if dbname  not in self.dbnames:
                self.logger.error("Given dbName ('{}') is not exist in the current DB-Structure".format(dbname), exc_info=self._logger_traceback)
                return None
        else:
            dbname="main"

        query = 'INSERT INTO {}.{}  \nVALUES ({});'.format(dbname,table_name, db_helper.values_to_placeholder(number))
        #p((query, inp_list), c="m")
        if table_name in self.tables(dbname=dbname):
            try:
                cursor = self._db.cursor()
                #p((query, inp_list), c="b")
                cursor.executemany(query, values_as_tuple)
                if table_name != "info":
                    self.all_inserts_counter += len(inp_list[0])
                    self.number_of_new_inserts_after_last_commit += len(inp_list[0])
                return True
            except Exception as  exception:
                print_exc_plus() if self._ext_tb else ""
                self.logger.debug("Following Query could have an Error: '{}'.".format(query))
                self.logger.error("Something happens in the insertV_rows_as_list-Method:  '{}'. Item wasn't inserted.".format( repr(exception) ), exc_info=self._logger_traceback)
                return False

            if dbname:
                self.logger.debug("Insertion: One row was inserted into '{}.{}'-Table. ".format(table_name, dbname))
            else:
                self.logger.debug("Insertion: One row was inserted into '{}'-Table. ".format(table_name))

            return True
        else:
            self.logger.error("Table ('{}') wasn't found or not exist. Please initialize the Info Table, before you may add any attributes.".format(table_name), exc_info=self._logger_traceback)
            return False




    def _insertlist_with_one_row(self,table_name, inp_list, dbname=False):
        if not self._check_db_should_exist():
            return False

        if not isinstance(inp_list, (list, tuple)):
            self.logger.error("insertVError: Given Obj is not a list!", exc_info=self._logger_traceback)
            return False

        values_as_tuple = db_helper.values_to_tuple(inp_list, "one")
        number  = len(inp_list)
        #p(self.colt("documents"))
        if  not values_as_tuple:
            self.logger.error("Given  Values wasn't packet into the list.", exc_info=self._logger_traceback)
            return False

        if dbname:
            if dbname  not in self.dbnames:
                self.logger.error("Given dbName ('{}') is not exist in the current DB-Structure".format(dbname), exc_info=self._logger_traceback)
                return None
        else:
            dbname="main"
        #p(values_as_tuple, c="m")
        query = 'INSERT INTO {dbname}.{tableName}  \nVALUES ({values});'.format(values=db_helper.values_to_placeholder(number), tableName=table_name, dbname=dbname)
        #p((query, values_as_tuple), c="b")
        if table_name in self.tables(dbname=dbname):
            try:
                cursor = self._db.cursor()
                cursor.execute(query, values_as_tuple)
                if table_name != "info":
                    self.all_inserts_counter +=1
                    self.number_of_new_inserts_after_last_commit += 1
                #sys.exit()
                return True

            except Exception as  exception:
                print_exc_plus() if self._ext_tb else ""
                self.logger.debug("Following Query could have an Error: '{}'.".format(query))
                self.logger.error("Something happens in the InsertV-Method:  '{}'. Item wasn't inserted.".format( repr(exception) ), exc_info=self._logger_traceback)
                return False

            if dbname:
                self.logger.debug("Insertion: One row was inserted into '{}.{}'-Table. ".format(table_name, dbname))
            else:
                self.logger.debug("Insertion: One row was inserted into '{}'-Table. ".format(table_name))

            return True
        else:
            self.logger.error("Table ('{}') wasn't found or not exist. Please initialize the Info Table, before you may add any attributes.".format(table_name), exc_info=self._logger_traceback)
            return False











##########################DB-Other Functions###############





    def get_db(self):
        return self._db


    def drop_table(self, table_name, dbname=False):
        if not self._check_db_should_exist():
            return False
        self._commit_if_inserts_was_did()
        if dbname:
            if dbname  in self.dbnames:
                query = "DROP TABLE  {}.{};".format(dbname,table_name)
            else:
                self.logger.error("Given dbName ('{}') is not exist in the current DB-Structure".format(dbname), exc_info=self._logger_traceback)
                return None
        else:
            query = "DROP TABLE {};".format(table_name)

        #p(query)
        try:
            cursor = self._db.cursor()
            cursor.execute(query)
            #tables_exist = cursor.fetchall()
        except Exception as  exception:
            print_exc_plus() if self._ext_tb else ""
            self.logger.error("Something happens while dropping the '{}'-Table:  '{}'.".format(table_name, repr(exception) ), exc_info=self._logger_traceback)
            return False

        dbname = dbname if dbname else "main"
        self._commit()
        self.logger.debug("'{}'-Table was deleted from the DB (dbname: '{}')".format(table_name,dbname))
        self._update_temp_tablesList_in_instance()
        return True



    def update(self,table_name,columns_names,values, dbname=False, where=False, connector_where="AND"):
        # UPDATE COMPANY SET ADDRESS = 'Texas' WHERE ID = 6;

        if not self._check_db_should_exist():
            return False
        self._commit_if_inserts_was_did()
        # Check if attributes and values have the same length
        if len(columns_names) != len(values):
            self.logger.error("Length of given columns_names and values is not equal.", exc_info=self._logger_traceback)
            return False


        columns_and_values_as_str = db_helper.columns_and_values_to_str(columns_names,values)
        #p(columnsName_as_str, c="m")
        #p(values_as_str, c="m")
        ### Add Attributes

        if where:
            where_cond_as_str = db_helper.where_condition_to_str(where, connector=connector_where)
            if not where_cond_as_str:
                self.logger.error("GetAllError: Where-Condition(s) wasn't compiled to String!", exc_info=self._logger_traceback)
                return False

        if dbname:
            if dbname  in self.dbnames:
                if where:
                    query = 'UPDATE {dbname}.{tableName}  \nSET {col_and_val} WHERE {where};'.format(col_and_val=columns_and_values_as_str, dbname=dbname, tableName=table_name, where=where_cond_as_str)
                else:
                    query = 'UPDATE {dbname}.{tableName}  \nSET {col_and_val};'.format(col_and_val=columns_and_values_as_str, dbname=dbname, tableName=table_name)
            else:
                self.logger.error("Given dbName ('{}') is not exist in the current DB-Structure".format(dbname), exc_info=self._logger_traceback)
                return None
        else:
            if where:
                query = 'UPDATE {tableName}  \nSET {col_and_val} WHERE {where};'.format(col_and_val=columns_and_values_as_str, tableName=table_name, where=where_cond_as_str)
            else:
                query = 'UPDATE {tableName}  \nSET {col_and_val};'.format(col_and_val=columns_and_values_as_str, tableName=table_name)


        if table_name in self.tables(dbname=dbname):
            try:
                cursor = self._db.cursor()
                #p(query)
                cursor.execute(query)
                self._commit()
                return True
            except Exception as  exception:
                print_exc_plus() if self._ext_tb else ""
                self.logger.error("Something happens while updating the '{}'-Table:  '{}'.".format(table_name, repr(exception) ), exc_info=self._logger_traceback)
                return False
        else:
            self.logger.error("Table ('{}') wasn't found or not exist. Please initialize the Info Table, before you may add any attributes.".format(table_name), exc_info=self._logger_traceback)
            return False



    def rollback(self):
        '''
        -> rollback to roll back any change to the database since the last call to commit.
        -> Please remember to always call commit to save the changes. If you close the connection using close or the connection to the file is lost (maybe the program finishes unexpectedly), not committed changes will be lost
        '''
        if not self._check_db_should_exist():
            return False
        temp_number_of_new_insertion_after_last_commit = self.number_of_new_inserts_after_last_commit
        self._db.rollback()
        self.logger.info("ExternRollBack: '{}' insertions was rolled back.".format(temp_number_of_new_insertion_after_last_commit))
        self.number_of_new_inserts_after_last_commit = 0
        return temp_number_of_new_insertion_after_last_commit



    def commit(self):
        if not self._check_db_should_exist():
            return False

        #self._lazy_writer_counter = 0
        temp_number_of_new_insertion_after_last_commit = self.number_of_new_inserts_after_last_commit
        self._db.commit()
        self.logger.info("ExternCommitter: DB was committed ({} last inserts was wrote on the disk)".format(self.number_of_new_inserts_after_last_commit))
        # if self.number_of_new_inserts_after_last_commit>0:
            
        # else:
        #     self.logger.info("ExternCommitter: DB was committed (some changes was wrote on the disk)".format(self.number_of_new_inserts_after_last_commit))
        self.inserts_was_committed += self.number_of_new_inserts_after_last_commit
        self.number_of_new_inserts_after_last_commit = 0
        return temp_number_of_new_insertion_after_last_commit

    def _commit(self):
        if not self._check_db_should_exist():
            return False

        temp_number_of_new_insertion_after_last_commit = self.number_of_new_inserts_after_last_commit
        self._db.commit()
        self.logger.debug("InternCommitter: DB was committed ({} last insert(s) was wrote on the disk)".format(self.number_of_new_inserts_after_last_commit))
        # if self.number_of_new_inserts_after_last_commit>0:
            
        # else:
        #     self.logger.debug("InternCommitter: DB was committed (some changes was wrote on the disk)".format(self.number_of_new_inserts_after_last_commit))
        self.inserts_was_committed += self.number_of_new_inserts_after_last_commit
        self.number_of_new_inserts_after_last_commit = 0
        return temp_number_of_new_insertion_after_last_commit


    def close(self, for_encryption=False):
        try:
            self.commit()
            if self._db:
                self._db.close()
                self._clean_all_parameters_after_db_close()
            else:
                self.logger.critical("No activ DB was found. There is nothing to close!")
            

            if for_encryption:
                msg = "DBExit: En-/Decryption Process need to reopen the current DB."
            else:
                msg = "DBExit: DB was committed and closed. (all changes was saved on the disk)"
            
            self.logger.info(msg)
        except Exception,e:
            print_exc_plus() if self._ext_tb else ""
            self.logger.error("ClossingError: DB-Closing return an Error: '{}' ".format(e), exc_info=self._logger_traceback)
            sys.exit()


    def _close(self, for_encryption=False):
        try:
            self._commit()
            if self._db:
                self._db.close()
                self._clean_all_parameters_after_db_close()
            else:
                self.logger.critical("No activ DB was found. There is nothing to close!")
            
            if for_encryption:
                msg = "DBExit: Current DB was closed! En-/Decryption Process will reopen the current DB."
            else:
                msg = "DBExit: DB was committed and closed. (all changes was saved on the disk)"
            self.logger.debug(msg)

        except Exception,e:
            print_exc_plus() if self._ext_tb else ""
            self.logger.error("ClossingError: DB-Closing return an Error: '{}' ".format(e), exc_info=self._logger_traceback)
            sys.exit()






    def addtable(self, table_name, attributs_names_with_types_as_list_with_tuples,dbname=False, constraints=False) :
        
        if not self._check_db_should_exist():
            return False
        self._commit_if_inserts_was_did()

        if table_name not in self.tables(dbname=dbname):
            attributs_names_with_types_as_str = db_helper.columns_and_types_in_tuples_to_str(attributs_names_with_types_as_list_with_tuples)
            if not attributs_names_with_types_as_str:
                self.logger.error("Something was wrong by Converting attributes into string. Program was stoped!", exc_info=self._logger_traceback)
                return False

            if constraints:
                if dbname:
                    if dbname  in self.dbnames:
                        query = 'CREATE TABLE {}.{} ({}\n{});'.format(dbname,table_name,attributs_names_with_types_as_str, constraints)
                    else:
                        self.logger.error("Given dbName ('{}') is not exist in the current DB-Structure".format(dbname), exc_info=self._logger_traceback)
                        return False
                else:
                    query = 'CREATE TABLE {} ({}\n{});'.format(table_name,attributs_names_with_types_as_str, constraints)
            else:
                if dbname:
                    if dbname  in self.dbnames:
                        query = 'CREATE TABLE {}.{} ({});'.format(dbname,table_name,attributs_names_with_types_as_str)
                    else:
                        self.logger.error("Given dbName ('{}') is not exist in the current DB-Structure".format(dbname), exc_info=self._logger_traceback)
                        return False
                else:
                    query = 'CREATE TABLE {} ({});'.format(table_name,attributs_names_with_types_as_str)
            #p( query)
            try:
                cursor = self._db.cursor()
                cursor.execute(query)
                self._commit()
                dbname = "main" if not dbname else dbname
                self.logger.debug("'{}'-Table was added into '{}'-DB. ".format(table_name,dbname))
                self._update_temp_tablesList_in_instance()
                return True
            except sqlite.OperationalError, e:
                print_exc_plus() if self._ext_tb else ""
                if 'near "-"' in str(e):
                    self.logger.error("AddTableOperationalError: While adding Table-'{}'. Problem: '{}'. (It may be a Problem with using not allowed Symbols in the column name.  e.g.'-')\nProblem was found in the following query: '{}'.".format(table_name,e, query.replace("\n", "  ")), exc_info=self._logger_traceback)
                else:
                    self.logger.error("AddTableOperationalError: While adding Table-'{}'. Problem: '{}'. \nProblem was found in the following query: '{}'.".format(table_name,e, query.replace("\n", " ")), exc_info=self._logger_traceback)
                return False

        else:
            self.logger.error("'{}'-Table is already exist in the given DB. You can not initialize it one more time!".format(table_name), exc_info=self._logger_traceback)
            return False


    def change_key(self, new_key_to_encryption):
        if not self._check_db_should_exist():
            return False
        if not self._check_should_be_str_or_unicode(new_key_to_encryption):
            return False

        if self._encryption_key:
            try:
                cursor = self._db.cursor()
                cursor.execute("PRAGMA rekey = '{}';".format(new_key_to_encryption))
                self._commit()
                self._encryption_key = new_key_to_encryption
                self.logger.info("Encryption Key was changed!")
                return True
            except Exception as  exception:
                print_exc_plus() if self._ext_tb else ""
                self.logger.error("Something happens while changing of the encryption key:  '{}'.".format(repr(exception)), exc_info=self._logger_traceback)
                return False
        else:
            self.logger.warning("You cant change encryption key, because the current DataBase wasn't encrypted. You need first to encrypt the current DB and than you can change the encryption key.")
            return False

    def encrypte(self, key_to_encryption):
        '''
        set key
        '''
        if not self._check_db_should_exist():
            return False
        self._check_should_be_str_or_unicode(key_to_encryption)

        if self._encryption_key:
            self.logger.critical("You can not encrypte the current DB, because it is already encrypted. What you can, it is just to change already setted key of encryption.")
            return False

        path_to_temp_db = os.path.join(self.dirname(), "temp_encrypted.db")
        path_to_current_db = self.path()
        path_to_dir_with_current_db  = self.dirname()
        fname_of_the_current_db = self.fname()

        new_fname_of_encrypted_db= os.path.splitext(fname_of_the_current_db)[0]+"_encrypted"+os.path.splitext(fname_of_the_current_db)[1]
        new_path_to_current_encrypted_db = os.path.join(path_to_dir_with_current_db, new_fname_of_encrypted_db)
        #p(new_fname_of_encrypted_db)

        try:
            cursor = self._db.cursor()
            cursor.execute("ATTACH DATABASE '{}' AS temp_encrypted KEY '{}';".format(path_to_temp_db, key_to_encryption))
            cursor.execute("SELECT sqlcipher_export('temp_encrypted');")
            cursor.execute("DETACH DATABASE temp_encrypted;")
        except Exception as  exception:
            print_exc_plus() if self._ext_tb else ""
            self.logger.error("Something happens while Encryption:  '{}'.".format(repr(exception)), exc_info=self._logger_traceback)
            return False

        if os.path.isfile(path_to_temp_db):
            self._close(for_encryption=True)
            os.rename(path_to_current_db, path_to_current_db+".temp")
            os.rename(path_to_temp_db, new_path_to_current_encrypted_db)

            if os.path.isfile(new_path_to_current_encrypted_db) and self.connect(new_path_to_current_encrypted_db, encryption_key=key_to_encryption, reconnection=True, logger_debug=True):
                self.logger.info("Current DB was encrypted. NewName: {};  NewPath:'{}'.".format(new_fname_of_encrypted_db,new_path_to_current_encrypted_db)) 
                
                #self._reinitialize_logger(self, level=self._logger_level)
                os.remove(path_to_current_db+".temp")
                self.logger.debug("Temporary saved (old) DB was removed.")
                self._reattach_dbs_after_closing_of_the_main_db()
                self.logger.debug("DB-Encryption was end with success!")
                #p(self._db, c="m")
                return True
            else:
                self.logger.error("Encrypted DB wasn't found/connected. Encryption is fail! Roled back to non-encrypted DB.", exc_info=self._logger_traceback)
                os.rename(path_to_current_db+".temp", path_to_current_db)
                self.connect(path_to_current_db,reconnection=True,  logger_debug=True)
                return False

        else:
            self.logger.error("ENCRYPTION: TempDB wasn't found. Encryption is failed! Roled back to non-encrypted DB.", exc_info=self._logger_traceback)
            return False

        


    def decrypte(self):
        '''
        delete key
        '''
        if not self._check_db_should_exist():
            return False

        if not self._encryption_key:
            self.logger.critical("You can not decrypte the current DB, because it wasn't encrypted before.")
            return False

        path_to_temp_db = os.path.join(self.dirname(), "temp_decrypted.db")
        path_to_current_db = self.path()
        path_to_dir_with_current_db  = self.dirname()
        fname_of_the_current_db = self.fname()

        new_fname_of_encrypted_db= os.path.splitext(fname_of_the_current_db)[0]+"_decrypted"+os.path.splitext(fname_of_the_current_db)[1]
        new_path_to_current_encrypted_db = os.path.join(path_to_dir_with_current_db, new_fname_of_encrypted_db)
        #p(new_fname_of_encrypted_db)


        try:
            cursor = self._db.cursor()
            cursor.execute("ATTACH DATABASE '{}' AS temp_decrypted KEY '';".format(path_to_temp_db))
            cursor.execute("SELECT sqlcipher_export('temp_decrypted');")
            cursor.execute("DETACH DATABASE temp_decrypted;")
        except Exception as  exception:
            print_exc_plus() if self._ext_tb else ""
            self.logger.error("Something happens while Decryption:  '{}'.".format(repr(exception)), exc_info=self._logger_traceback)
            return False

        if os.path.isfile(path_to_temp_db):
            self._close(for_encryption=True)
            os.rename(path_to_current_db, path_to_current_db+".temp")
            os.rename(path_to_temp_db, new_path_to_current_encrypted_db)
            if os.path.isfile(new_path_to_current_encrypted_db) and self.connect(new_path_to_current_encrypted_db, reconnection=True, logger_debug=True):
                self.logger.info("Current DB was decrypted. NewName: {};  NewPath:'{}'.".format(new_fname_of_encrypted_db,new_path_to_current_encrypted_db)) 
                #self._reinitialize_logger(self, level=self._logger_level)
                os.remove(path_to_current_db+".temp")
                self.logger.debug("Temporary saved (old) DB was removed.")
                self._reattach_dbs_after_closing_of_the_main_db()
                self.logger.debug("DB-Decryption was end with success!")
                #p(self._db, c="m")
                return True
            else:
                self.logger.error("Decrypted DB wasn't found/connected. Decryption is fail! Roled back to encrypted DB.", exc_info=self._logger_traceback)
                os.rename(path_to_current_db+".temp", path_to_current_db)
                self.connect(path_to_current_db,reconnection=True,  logger_debug=True)
                return False

        else:
            self.logger.error("DECRYPTION: TempDB wasn't found. Encryption is failed! Roled back to encrypted DB.", exc_info=self._logger_traceback)
            return False
        

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
            self.logger.error("Given Object is not from following type: (str, unicode).", exc_info=self._logger_traceback)
            return False
        else:
            return True


    def _check_if_given_columns_exist(self, tableName,columns, dbname=False):
        for column in columns:
            if column not in  self.col(tableName):
                if "json_extract" not in column:
                    self.logger.error("Given Column '{}' is not exist in the following Table '{}' (dbname='{}') ".format(column,tableName,dbname), exc_info=self._logger_traceback)
                    return False
        
        return True

    def _check_if_table_exist(self,tableName, dbname=False):
        if tableName not in self.tables(dbname=dbname):
            self.logger.error("Given Table '{}' is not exist (dbname='{}')) ".format(tableName,dbname), exc_info=self._logger_traceback)
            return False
        else:
            return True

    def _check_db_should_exist(self):
        if not self._db: 
            self.logger.error("No active DB was found. You need to connect or initialize a DB first, before you can make any operation on the DB.", exc_info=self._logger_traceback)
            return False
        else:
            return True


    def _check_db_should_not_exist(self):
        if self._db: 
            self.logger.error("An active DB was found. You need to initialize new empty Instance of DB before you can do this operation.", exc_info=self._logger_traceback)
            return False
        else:
            return True


    def _db_should_be_a_corpus(self):

        if not self._check_db_should_exist():
            #p(".......")
            return False

        db_typ = self.get_attr(attributName="typ")

        if db_typ != "corpus":
            self.logger.error("Active DB is from typ '{}'. But it should be from typ 'corpus'. ".format(db_typ), exc_info=self._logger_traceback)
            return False
        return True


    def _db_should_be_stats(self):
        if not self._check_db_should_exist():
            return False
        db_typ = self.get_attr(attributName="typ")
        if db_typ != "stats":
            self.logger.error("Active DB is from typ '{}'. But it should be from typ 'stats'. ".format(db_typ), exc_info=self._logger_traceback)
            return False
        return True





    def _check_file_existens(self, path_to_file):
        if not os.path.isfile(path_to_file):
            self.logger.error("DB-File wasn't found: ('{}').".format(path_to_file), exc_info=self._logger_traceback)
            #os._exit(1)
            return False
        else:
            return True

    def _get_compile_options(self, db):
        if not isinstance(db, sqlite.Connection):
            self.logger.error("ExtensionLoaderError: Passed Obj is not an Sqlite-DB.", exc_info=self._logger_traceback)
            sys.exit()
        try:
            output_dict = defaultdict(list)            
            c = db.cursor()
            c.execute("PRAGMA compile_options;")
            fetched_data = c.fetchall()
            #p(fetched_data)
            for option in  fetched_data:
                if "=" in option[0]:
                    #p(option[0])
                    splitted_option = option[0].split("=")
                    output_dict[splitted_option[0]] = splitted_option[1]
                else:
                    #p(option[0],c="b")
                    output_dict["parameters"].append(option[0])

            return output_dict
        except:
            print_exc_plus() if self._ext_tb else ""
            self.logger.error("CompilerOptionsGetterError: Something wrong is happens.See following Exception: '{}' ".format(e), exc_info=self._logger_traceback)
            sys.exit()

    def _check_if_threads_safe(self):
        if not self.compile_options:
            self.logger.error("DB-Compile Options wasn't found.")
            return False
        try:
            if int(self.compile_options["THREADSAFE"]) == 0:
                self.logger.error("ThreadSafeCheckerError: Given Compilation of SQLITE3 Environment is unsafe to use SQLite in a multithreaded program. Following Tool (zas-rep-tool) was designed to work in multithreaded/multiprocessored Mode and requiring ThreadSafe (1 or 2) compilation of SQLITE3. Please recompile your SQLITE with one of the following options ['SQLITE_CONFIG_MULTITHREAD','SQLITE_CONFIG_SERIALIZED'). Read more here. 'https://www.sqlite.org/compile.html#threadsafe'. ")
                sys.exit()
            elif int(self.compile_options["THREADSAFE"]) == 1:
                self.logger.debug("ThreadSafeChecker: This SQLITE Compilation is safe for use in a multithreaded environment. Mode: Serialized (THREADSAFE=1). In serialized mode, SQLite can be safely used by multiple threads with no restriction. Read more: https://www.sqlite.org/threadsafe.html")
            
            elif int(self.compile_options["THREADSAFE"]) == 2:
                #self.logger.debug("ThreadSafeChecker: This SQLITE Compilation is safe for use in a multithreaded environment. Mode: Multi-thread (THREADSAFE=2). In this mode, SQLite can be safely used by multiple threads provided that no single database connection is used simultaneously in two or more threads. Read more: https://www.sqlite.org/threadsafe.html")
                self.logger.warning("ThreadSafeChecker: This SQLITE Compilation is safe for use in a multithreaded environment. Mode: Multi-thread (THREADSAFE=2) can be safely used by multiple threads provided that no single database connection is used simultaneously in two or more threads. Read more: https://www.sqlite.org/threadsafe.html")

        except Exception, e:
            print_exc_plus() if self._ext_tb else ""
            self.logger.error("ThreadSafeCheckerError: Something wrong is happens. See following Exception: '{}' ".format(e), exc_info=self._logger_traceback)
            sys.exit()



    def _check_db_compilation_options(self, db):
        self.compile_options = self._get_compile_options(db)
        self._check_if_threads_safe()
        self._load_json1_extention_if_needed(db)


    def _load_json1_extention(self,db):

        if not isinstance(db, sqlite.Connection):
            self.logger.error("ExtensionLoaderError: Passed Obj is not an Sqlite-DB.", exc_info=self._logger_traceback)
            sys.exit()
        try:
            db.enable_load_extension(True)
            db.load_extension(DBHandler.path_to_json1)
            self.logger.debug("ExtensionLoader: 'json1'-Extension was loaded into SQLite.")
            return True
        except sqlite.OperationalError,e:
            print_exc_plus() if self._ext_tb else ""
            self.logger.error("ExtensionLoaderError: 'json1'-Extension wasn't found in '{}'. Probably it wasn't compiled. Please compile this extension  before you can use it.".format(DBHandler.path_to_json1), exc_info=self._logger_traceback)
            sys.exit()
        except Exception, e:
            print_exc_plus() if self._ext_tb else ""
            self.logger.error("ExtensionLoaderError: Something wrong is happens. 'json1'-Extension wasn't loaded. See following Exception: '{}' ".format(e), exc_info=self._logger_traceback)
            return False


    def _load_json1_extention_if_needed(self, db):
        

        if not self.compile_options:
            self.logger.error("DB-Compile Options wasn't found.")
            return False

        try:
            if "ENABLE_JSON1" in self.compile_options["parameters"]:
                self.logger.debug("JSONExtentionChecker: Given Compilation of SQLITE3 Environment hat already enabled JSON Extension.")
                return True

            else:
                if "ENABLE_LOAD_EXTENSION" in self.compile_options["parameters"] or "OMIT_LOAD_EXTENSION" in self.compile_options["parameters"]:
                    if not self._load_json1_extention(db):
                        return False

                else:
                    self.logger.CRITICAL("ExtensionLoaderError: It seems like current Compilation of the SQLITE don't support loading of additional extension. But we will try to force it. ('ZAS-REP-TOOLS' requires loaded 'JSON1' extention. Please recompile your Version of SQLITE with following flags: 'SQLITE_OMIT_LOAD_EXTENSION' or 'SQLITE_ENABLE_JSON1'. See more here: https://www.sqlite.org/compile.html#threadsafe) ")
                    if not self._load_json1_extention(db):
                        return False
            return True

        except Exception, e:
            print_exc_plus() if self._ext_tb else ""
            self.logger.error("ThreadSafeCheckerError: Something wrong is happens. See following Exception: '{}' ".format(e), exc_info=self._logger_traceback)
            sys.exit()














###########################DB-Validation#######################



    def _validation_DBfile(self, path_to_db, encryption_key=False):
        if os.path.isfile(path_to_db):
            try:
                _db = sqlite.connect(path_to_db, check_same_thread=False)
                self._check_db_compilation_options(_db)
                c = _db.cursor()
                if encryption_key:
                    c.execute("PRAGMA key='{}'".format(encryption_key))
                c.execute("SELECT name FROM sqlite_master WHERE type='table';")
                tables = c.fetchall()

            except sqlite.DatabaseError, e:
                print_exc_plus() if self._ext_tb else ""
                if encryption_key:
                    self.logger.error("ValidationError: '{}'. Or maybe a given Key is incorrect. Please give another one.  PathToDB: '{}'. ".format( e, path_to_db), exc_info=self._logger_traceback)
                else:
                    self.logger.error("ValidationError: '{}'. PathToDB: '{}'. ".format( e, path_to_db), exc_info=self._logger_traceback)
                    return False
            except Exception as  exception:
                print_exc_plus() if self._ext_tb else ""
                self.logger.error("Something wrong happens while Validation '{}'. PathToDB: '{}'. ".format( repr(exception), path_to_db), exc_info=self._logger_traceback)
                return False


            try:
                c.execute("SELECT name FROM sqlite_master WHERE type='table';")
                tables = c.fetchall()

                ## check Row Numbers
                rowNumbes = c.execute("select count(*) from info; ").fetchone()[0]
                if rowNumbes > 1:
                    self.logger.error("ValidationError: Info-Table has more as 1 row. It is incorrect!", exc_info=self._logger_traceback)
                    return False
                elif rowNumbes ==0:
                    self.logger.error("ValidationError: Info-Table is empty. It is incorrect!", exc_info=self._logger_traceback)
                    return False


                try:
                    ## Check existents of attribute typ
                    get_typ= c.execute("SELECT typ FROM info; ")
                    get_typ = c.fetchone()
                    if get_typ[0] == "stats":
                        if not self._validate_statsDB(_db):
                            self.logger.warning("Validator is failed! Connected/Attached DB can not be used. Please choice another one.")
                            return False
                    elif get_typ[0] == "corpus":
                        if not self._validate_corpusDB(_db):
                            self.logger.warning("Validator is failed! Connected/Attached DB can not be used. Please choice another one.")
                            return False
                    else:
                        self.logger.error("ValidationError: Unsupported DB-Type '{}' was found.".format(get_typ[0]), exc_info=self._logger_traceback)
                        return False

                except sqlite.OperationalError,  e:
                    print_exc_plus() if self._ext_tb else ""
                    self.logger.error("ValidationError:  '{}'. Impossible to get DB-Typ. PathToDB: '{}'. ".format( e, path_to_db), exc_info=self._logger_traceback)
                    return False


            except Exception as  exception:
                print_exc_plus() if self._ext_tb else ""
                self.logger.error("ValidationError: Something wrong happens while Validation '{}'. PathToDB: '{}'. ".format( repr(exception), path_to_db), exc_info=self._logger_traceback)
                return False

            return True

        else:
            self.logger.error("Given DB-File is not exist: '{}'. ".format(path_to_db), exc_info=self._logger_traceback)
            return False





    def _validate_corpusDB(self, db):

        ### Step 1: Attributes
        attributs_and_types = [(attr[0], attr[1].split(' ', 1 )[0])  for attr in db_helper.default_tables["corpus"]["info"]]

        c = db.cursor()
        c.execute("PRAGMA table_info('info'); ")
        columns_and_types = c.fetchall()
        columns_and_types = [(col[1], col[2])for col in columns_and_types]


        if set(columns_and_types) !=set(attributs_and_types):
            self.logger.error("CorpusDBValidationError: Given Stats-DB contain not correct attributes. Following col_and_types was extracted: '{}' and they are incorrect. Please use following data as golden standard: '{}'. ".format(columns_and_types, attributs_and_types), exc_info=self._logger_traceback)
            return False


        ## Step 2: Table Names
        c.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = c.fetchall()
        default_tables = ["documents"]
        extracted_tnames = [table_name[0] for table_name in tables]
        for defaultTable in default_tables:
            if defaultTable not in extracted_tnames:
                self.logger.error("CorpusDBValidationError: '{}'-default-Table wasn't found in the given Corpus-DB.".format(defaultTable), exc_info=self._logger_traceback)
                return False




        return True

    def _validate_statsDB(self, db):

        ### Step 1: Attributes
        attributs_and_types = [(attr[0], attr[1].split(' ', 1 )[0])  for attr in db_helper.default_tables["stats"]["info"]]
        c = db.cursor()
        c.execute("PRAGMA table_info('info'); ")
        columns_and_types = c.fetchall()
        columns_and_types = [(col[1], col[2])for col in columns_and_types]

        if set(columns_and_types) !=set(attributs_and_types):
            self.logger.error("StatsDBValidationError: Given Stats-DB contain not correct attributes. Following col_and_types was extracted: '{}' and they are incorrect. Please use following data as golden standard: '{}'. ".format(columns_and_types, attributs_and_types), exc_info=self._logger_traceback)
            return False



        ## Step 2: Table Names
        c.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = c.fetchall()
        default_tables = ["repl_baseline", "redu_baseline","replications", "reduplications", "info"]
        extracted_tnames = [table_name[0] for table_name in tables]
        for defaultTable in default_tables:
            if defaultTable not in extracted_tnames:
                self.logger.error("StatsDBValidationError: '{}'-default-Table wasn't found in the given Stats-DB.".format(defaultTable), exc_info=self._logger_traceback)
                return False
        return True







###########################DB-OtherHelpers################





    def _reinitialize_logger(self,  level=False):
        level = level if  level else self._logger_level
        ## Logger Reinitialisation
        self.logger = main_logger(self.__class__.__name__, level=level, folder_for_log=self._logger_folder_to_save, use_logger=self._logger_usage, save_logs=self._logger_save_logs)
        self.logger.debug("Logger was reinitialized.")



    def _init_default_tables(self,typ, template=False, additional_columns_with_types=False):
        if template and template!="NULL":
            if template in DBHandler.templates:
                if additional_columns_with_types:
                    additional_columns_with_types += DBHandler.templates[template]
                else:
                    additional_columns_with_types = DBHandler.templates[template]
            else:
                self.logger.error("Given Template ('{}') is not exist".format(template), exc_info=self._logger_traceback)
                return False
        #p(additional_columns_with_types)
        if typ == "corpus":
            if not self._init_default_table("corpus", "documents", db_helper.default_tables["corpus"]["documents"]["basic"], additional_collumns_with_types=additional_columns_with_types, constraints=db_helper.default_constraints["corpus"]["documents"]):
                return False
        
        elif typ == "stats":
            for table_name, columns in  db_helper.default_tables[typ].iteritems(): #foo = data.get("a",{}).get("b",{}).get("c",False)
                if table_name == "info":
                    continue
                if not self._init_default_table(typ, table_name, columns, constraints=db_helper.default_constraints.get(typ, False).get(table_name, False)):
                    return False

        else:
            self.logger.error("Given typ of DB ('{}') is not exist.".format(typ), exc_info=self._logger_traceback)
            return False
        return True



    def _init_default_table(self, typ, tableName , default_collumns_with_types, additional_collumns_with_types=False, constraints=False):
        if typ.lower()=="corpus":
            if not self._db_should_be_a_corpus():
                return False
        elif typ.lower()=="stats":
            if not self._db_should_be_stats():
                return False
        else:
            self.logger.error("Not supported typ ('{}') of DB. Please use one of the following DB-Types: '{}'. ".format(typ, DBHandler.supported_db_typs), exc_info=self._logger_traceback)
            return False

        if additional_collumns_with_types:
            columns_and_types = default_collumns_with_types + additional_collumns_with_types
        else:
            columns_and_types = default_collumns_with_types
        constraints_in_str = db_helper.constraints_list_to_str(constraints)
        #attributs_names_with_types_as_str = db_helper.columns_and_types_in_tuples_to_str(columns_and_types)
        if not self.addtable( tableName, columns_and_types,constraints=constraints_in_str):
            self.logger.error("InitDefaultTableError: '{}'-Table wasn't added into the {}-DB.".format(tableName, typ), exc_info=self._logger_traceback)
            return False

        self.logger.debug("{}-Table in {} was initialized".format(tableName, typ))
        return True


    def _commit_if_inserts_was_did(self):
        if self.number_of_new_inserts_after_last_commit >0:
            self._commit()



    def _init_info_table(self, attributs_names):
        #str_attributs_names = db_helper.columns_and_types_in_tuples_to_str(attributs_names)
        if not self.addtable("info", attributs_names):
            return False

        self.logger.debug("Info-Table was initialized")
        return True



    def _get_tables_from_db(self,dbname=False):
        if not self._check_db_should_exist():
            return False
        self._commit_if_inserts_was_did()
        if dbname:
            if dbname  in self.dbnames:
                query = "SELECT name FROM {}.sqlite_master WHERE type='table';".format(dbname)
            else:
                self.logger.error("Given dbName ('{}') is not exist in the current DB-Structure".format(dbname), exc_info=self._logger_traceback)
                return None
        else:
            query = "SELECT name FROM sqlite_master WHERE type='table';"

        try:
            cursor = self._db.cursor()
            cursor.execute(query)
            tables_exist = cursor.fetchall()
            self._commit()
        except Exception as  exception:
            print_exc_plus() if self._ext_tb else ""
            self.logger.error("Something happens while Getting Tables:  '{}'.".format(repr(exception)), exc_info=self._logger_traceback)
            return False

        if dbname:
            self.logger.debug("TableNames was get directly from DB.  (dbname: '{}')".format(dbname))
        else:
            self.logger.debug("TableNames was get directly from DB.  (dbname: 'main')")
        
        return [table_name[0] for table_name in tables_exist]







    def _update_temp_tablesList_in_instance(self):
        if not self._check_db_should_exist():
            return False
        #p(self.dbnames, c="r")
        self._tables_dict = {}
        if self.dbnames:
            for DBName in self.dbnames:
                self._tables_dict[DBName] = self._get_tables_from_db(dbname=DBName)
        else:
            self._tables_dict['main'] = self._get_tables_from_db(dbname='main')
        
        self.logger.debug("Temporary TableList in the DB-Instance was updated!")




    def _get_indexes_from_db(self,dbname=False):
        if not self._check_db_should_exist():
            return False
        self._commit_if_inserts_was_did()
        if dbname:
            if dbname  in self.dbnames:
                query = "SELECT * FROM {}.sqlite_master WHERE type='index';".format(dbname)
            else:
                self.logger.error("Given dbName ('{}') is not exist in the current DB-Structure".format(dbname), exc_info=self._logger_traceback)
                return None
        else:
            query = "SELECT * FROM sqlite_master WHERE type='index';"

        try:
            cursor = self._db.cursor()
            cursor.execute(query)
            indexes_exist = cursor.fetchall()
            self._commit()
        except Exception as  exception:
            print_exc_plus() if self._ext_tb else ""
            self.logger.error("Something happens while Getting Indexes:  '{}'.".format(repr(exception)), exc_info=self._logger_traceback)
            return False

        if dbname:
            self.logger.debug("IndexesNames was get directly from DB.  (dbname: '{}')".format(dbname))
        else:
            self.logger.debug("IndexesNames was get directly from DB.  (dbname: 'main')")
        
        #return [index_name[0] for index_name in indexes_exist]
        #p(indexes_exist, c="r")
        return indexes_exist


    def _update_temp_indexesList_in_instance(self):
        if not self._check_db_should_exist():
            return False
        #p(self.dbnames, c="r")
        self._indexes_dict = {}
        if self.dbnames:
            for DBName in self.dbnames:
                self._indexes_dict[DBName] = self._get_indexes_from_db(dbname=DBName)
        else:
            self._indexes_dict['main'] = self._get_indexes_from_db(dbname='main')
        
        self.logger.debug("Temporary IndexesList in the DB-Instance was updated!")







    def _del_attached_db_from_a_config_list(self, dbname):
        i=0
        found = False
        if self._attachedDBs_config:
            if dbname not  in self.dbnames:
                self.logger.warning("Given AttachedDataBaseName  is not exist: '{}'.".format(dbname))
                return False
            configs = self._get_configs_from_attached_DBList(dbname)
            if configs:
                self._attachedDBs_config.pop(configs[1])
                self.logger.debug("Given AttachedDB '{}' was successfully deleted from the configs-list. ".format(dbname))
                return True
                
            else:
                self.logger.warning("Given AttachedDB  '{}' wasn't deleted from the configs-liss. ".format(dbname))
                return False
        else:
            self.logger.warning("List with attached DBs is already empty. You can not delete anything!")
            return False


    def _get_configs_from_attached_DBList(self, dbname):
        i=0
        found = False
        if self._attachedDBs_config:
            if dbname not  in self.dbnames:
                self.logger.warning("Given AttachedDataBaseName  is not exist: '{}'.".format(dbname))
                return False

            for attachedDB in self._attachedDBs_config:
                if attachedDB[1] == dbname:
                    #p((attachedDB[1], i))
                    found = i
                    break
                i=+1
            if isinstance(found, int):
                #self._attachedDBs_config.pop(found)
                self.logger.debug("Configs for '{}' was successfully found in the config-list of attached DBs. ".format(dbname))
                return (attachedDB, found)
            else:
                self.logger.warning("Configs for '{}' wasn't found!".format(dbname))
                return False

        else:
            self.logger.warning("Configs-List with attached DBs is already empty. ")
            return False



    def _get_all_attr_from_db(self,dbname=False):
        if not self._check_db_should_exist():
            return False
        self._commit_if_inserts_was_did()
        dbname = dbname if dbname else "main"

        if dbname:
            if dbname  in self.dbnames:
                query = 'SELECT * FROM  {}.info;'.format( dbname)
            else:
                self.logger.error("Given dbName ('{}') is not exist in the current DB-Structure".format(dbname), exc_info=self._logger_traceback)
                return None
        else:
            query = 'SELECT * FROM  info;'

        try:
            cursor = self._db.cursor()
            cursor.execute(query)
            attribut = cursor.fetchall()[0]
        except Exception as  exception:
            print_exc_plus() if self._ext_tb else ""
            self.logger.error("Something happens while Getting all Attributes from InfoTable of '{}'-DB: '{}'".format(dbname, exception), exc_info=self._logger_traceback)
            return False

        number_of_rows_info_table = self.rownum("info",dbname=False)
        if number_of_rows_info_table ==1:
            columns = self.col("info", dbname=dbname)
            return dict(zip(columns, list(attribut)))
        elif number_of_rows_info_table ==0:
            self.logger.error("Table 'info' is empty. Please set attributes bevor!", exc_info=self._logger_traceback)
            return None
        else:
            self.logger.error("Table 'info' has more as 1 row. It's not correct. Please delete not needed rows.", exc_info=self._logger_traceback)
            return None






    def _update_temp_attributsList_in_instance(self):
        if not self._check_db_should_exist():
            return False
        #p(self.dbnames, c="r")
        self._attributs_dict = {}
        if self.dbnames:
            for DBName in self.dbnames:
                attributes = self._get_all_attr_from_db(dbname=DBName)
                if attributes:
                    self._attributs_dict[DBName] = attributes
                else:
                    self.logger.error("Attributes wasn't updated!!!", exc_info=self._logger_traceback)
                    return False
        else:
            self._attributs_dict['main'] = self._get_all_attr_from_db(dbname='main')
        
        self.logger.debug("Temporary List with all Attributes in the DB-Instance was updated!")







    def _get_db_names_from_main_db(self):
        if not self._check_db_should_exist():
            return False
        self._commit_if_inserts_was_did()
        try:
            cur = self._db.cursor()
            cur.execute("PRAGMA database_list")
            rows = cur.fetchall()
        except Exception as  exception:
            print_exc_plus() if self._ext_tb else ""
            self.logger.error("Something happens while Getting DBNames:  '{}'.".format(repr(exception)), exc_info=self._logger_traceback)
            return False

        self.logger.debug("All DB-Names was taked directly from a Database.")
        if rows:
            return [ row[1] for row in rows]
        else:
            self.logger.critical("DBNamesGetter: No DB Names was returned from a DB")
            return []

    def _reattach_dbs_after_closing_of_the_main_db(self):
        if not self._check_db_should_exist():
            return False

        if self._attachedDBs_config_from_the_last_session:
            for attached_db in self._attachedDBs_config_from_the_last_session:
                #p(attached_db, c="r")
                self.attach(attached_db[0], encryption_key=attached_db[2], reattaching=True)
            self.logger.debug("All attached DB was re-attached in the new connected Database")
            return True
        else:
            self.logger.debug("There is no DBs to reattach (after closing of the main DB).")
            return False





    def _update_temp_list_with_dbnames_in_instance(self):
        self.dbnames
        if not self._check_db_should_exist():
            return False
        #p(self.dbnames, c="r")
        self.dbnames = self._get_db_names_from_main_db()
        #p(self.dbnames, c="m")
        if self.dbnames:
            self.logger.debug("Temporary List with DB-Names in the DB-Instance was updated!")
            return True
        else:
            self.logger.error("Empty List was returned.", exc_info=self._logger_traceback)
            return False




    def _clean_all_parameters_after_db_close(self):
        self._db = False
        self._encryption_key = False
        self.is_encrypted = False
        self._attachedDBs_config_from_the_last_session = self._attachedDBs_config
        self._attachedDBs_config = []
        self._tables_dict = {}
        self._indexes_dict = {}
        self._attributs_dict = {}
        self.dbnames = [] 
        self._lazy_writer_all_inserts_counter = 0
        self._lazy_writer_number_inserts_after_last_commit = 0
        self._lazyness_border = 0
        self._successful_commits_with_lazy_writer = 0
        self.all_inserts_counter = 0
        self.number_of_new_inserts_after_last_commit = 0
        self.inserts_was_committed = 0

        self.logger.debug("All intern Parameters was cleaned after DB-Close.")


