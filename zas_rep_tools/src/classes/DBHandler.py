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



import os
import copy
import sys
import regex
import logging


#from collections import defaultdict
from raven import Client
from cached_property import cached_property
#import sqlite3 as sqlite
from pysqlcipher import dbapi2 as sqlite
import glob
import shutil
from time import gmtime, strftime
import coloredlogs


from zas_rep_tools.src.utils.logger import Logger
from zas_rep_tools.src.utils.sql_helper import *
from zas_rep_tools.src.utils.db_helper import *
from zas_rep_tools.src.utils.debugger import p
from zas_rep_tools.src.utils.sql_qearies import * 
#from zas_rep_tools.src.utils.encryption import Encryptor, AESCipher
from zas_rep_tools.src.utils.helpers import path_to_zas_rep_tools
from zas_rep_tools.src.utils.error_tracking import initialisation





class DBHandler(object):
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

    supported_db_typs = ["stats", "corpus"]

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
        self.logger = logger.myLogger("DBHandler", self._folder_for_log_files, use_logger=self._use_logger, level=self._logger_level)
        self.logger.debug('Beginn of creating an instance of DB()')


        ## Developing Mode: Part 2:
        if self._developingMode:
            self.logger.info("DEVELOPING_MODE: was started")


        #Input: Incaplusation:
        self._error_tracking = error_tracking


        #InstanceAttributes: Initialization
        self._db = False
        self._encryption_key = False
        self.is_encrypted = False



        self._attachedDBs_config = []
        self._attachedDBs_config_from_the_last_session = [] 
        self._tables_dict = {}
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
                self.logger.error("'Platform_name' wasn't given. 'Corpus' initialization need 'platform_name'.")
                return False

            if not self.init_corpus(prjFolder, DBname, language,  visibility, platform_name, encryption_key=encryption_key,fileName=fileName, source=source, license=license, template_name=template_name, version=version, corpus_id=corpus_id, additional_columns_with_types_for_documents=additional_columns_with_types_for_documents):
                return False
            
            return True

        elif typ == "stats":
            if not corpus_id:
                self.logger.error("'Corpus_id' wasn't given. 'Stats' initialization need Corpus_id.")
                return False
                
            if not self.init_stats(prjFolder, DBname, language, visibility, corpus_id, encryption_key=encryption_key,fileName=fileName, version=version, stats_id=stats_id):
                return False
            
            return True

        else:
            self.logger.error("Given DB-Typ is not supported! Please one of the following  types: '{}'.".format(typ, supported_typs))
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
            corpus_id= create_id(DBname,language, typ, visibility)
        
        fileName,path_to_db = get_file_name(prjFolder,corpus_id,DBname,
                            language,visibility, typ,fileName, platform_name,
                            encrypted= True if encryption_key else False)

        
        ### Initialisation of DB
        if not self._check_db_should_not_exist():
            return False

        if os.path.isdir(prjFolder):

            if self._encryption_key:
                self._db = sqlite.connect(path_to_db)
                try:
                    c = self._db.cursor()
                    c.execute("PRAGMA key='{}'".format(self._encryption_key))
                    self._commit()
                    self.is_encrypted = True
                except Exception as  exception:
                    self.logger.error("Something happens while initialization of Corpus '{}'".format( exception))
                    return False

            else:
                self._db = sqlite.connect(path_to_db)

            self._update_temp_list_with_dbnames_in_instance()



            created_at = strftime("%Y-%m-%d %H:%M:%S", gmtime())
            attributs_list = DBHandler.default_attributs[typ]
            values = [corpus_id, DBname, platform_name, template_name, version, language, created_at, source,license,visibility,typ]
            
            if not self._init_info_table(attributs_list):
                self.logger.error("CorpusInitialisatioError: Corpus wasn't initialized because  info Table wasn't initialized. ")
                self._close()
                os.remove(path_to_db)
                return False

            if not self.add_attributs(attributs_list,values):
                self.logger.error("CorpusInitialisatioError: Corpus wasn't initialized because attributes wasn't added into   info Table. ")
                self._close()
                os.remove(path_to_db)

                return False
            #p(template_name)
            if not self._init_default_tables("corpus", template=template_name, additional_columns_with_types=additional_columns_with_types_for_documents):
                self.logger.error("CorpusInitialisatioError: Corpus wasn't initialized because  default Tables wasn't initialized. ")
                self._close()
                os.remove(path_to_db)
                return False
            #self._init_documents_table_in_corpus()
            self._commit()
            

            self.logger.info("Coprus-DB ({}) was initialized and saved on the disk: '{}'. ".format(fileName, path_to_db))
            self.logger.info("Corpus-DB ({}) was connected.".format(fileName))
            return True
        else:
            self.logger.error("Given Project Folder is not exist: '{}'. ".format(prjFolder))
            return False





    def init_stats(self, prjFolder, DBname, language, visibility, corpus_id,
                    encryption_key=False,fileName=False, version=False, stats_id=False):

        self._encryption_key = encryption_key

        ### Preprocessing: Create File_Name
        version = "NULL" if not version else version
        typ= "stats"

        if stats_id:
            stats_id= create_id(DBname,language, typ, visibility,corpus_id=corpus_id, stats_id=stats_id)
        else:
            stats_id= create_id(DBname,language, typ, visibility,corpus_id=corpus_id )

        
        if not stats_id:
            self.logger.error("Id wasn't created. Stats-ID was given without Corpus-ID. This is an illegal input.")
            return False


        fileName,path_to_db = get_file_name(prjFolder,stats_id,DBname,
                        language,visibility, typ, fileName,
                        encrypted= True if encryption_key else False)


        ### Initialisation of DB
        if not self._check_db_should_not_exist():
            return False

        if os.path.isdir(prjFolder):
            if self._encryption_key:
                self._db = sqlite.connect(path_to_db)
                try:
                    c = self._db.cursor()
                    c.execute("PRAGMA key='{}'".format(self._encryption_key))
                    self._commit()
                    self.is_encrypted = True
                except Exception as  exception:
                    self.logger.error("Something happens while initialization of Stats '{}'".format( exception))
                    return False

            else:
                self._db = sqlite.connect(path_to_db)

            self._update_temp_list_with_dbnames_in_instance()
            if not stats_id:
                stats_id= create_id(DBname,language, typ, visibility,corpus_id=corpus_id)
            created_at = strftime("%Y-%m-%d %H:%M:%S", gmtime())
            attributs_list = DBHandler.default_attributs[typ]
            values = [stats_id,corpus_id, DBname, version,  created_at, visibility,typ]


            if not self._init_info_table(attributs_list):
                self.logger.error("StatsInitialisatioError: Stats wasn't initialized because  info Table wasn't initialized. ")
                self._close()
                os.remove(path_to_db)
                return False

            if not self.add_attributs(attributs_list,values):
                self.logger.error("StatsInitialisatioError: Stats wasn't initialized because attributes wasn't added into   info Table. ")
                self._close()
                os.remove(path_to_db)
                return False

            if not self._init_default_tables("stats"):
                self.logger.error("StatsInitialisatioError: Corpus wasn't initialized because  default Tables wasn't initialized. ")
                self._close()
                os.remove(path_to_db)
                return False
            
            self._commit()
            #self.dbnames.append("main")

            
            self.logger.info("Stats-DB ({}) was initialized and saved on the disk: '{}'. ".format(fileName, path_to_db))
            self.logger.info("Stats-DB ({}) was connected.".format(fileName))
            return True
        else:
            self.logger.error("Given Project Folder is not exist: '{}'. ".format(prjFolder))
            return False



    def init_emptyDB(self, prjFolder, DBname, encryption_key=False):
        ### Preprocessing: Create File_Name
        self._encryption_key = encryption_key
        fileName,path_to_db = get_file_name_for_empty_DB(prjFolder,DBname,
                    encrypted= True if encryption_key else False)

        if os.path.isdir(prjFolder):

            if self._encryption_key:
                self._db = sqlite.connect(path_to_db)
                try:
                    c = self._db.cursor()
                    c.execute("PRAGMA key='{}'".format(self._encryption_key))
                    self._commit()
                    self.is_encrypted = True
                except Exception as  exception:
                    self.logger.error("Something happens while initialization of Corpus '{}'".format( exception))
                    return False

            else:
                self._db = sqlite.connect(path_to_db)

            self._update_temp_list_with_dbnames_in_instance()

            

            self.logger.info("Empty-DB ({}) was initialized and saved on the disk: '{}'. ".format(fileName, path_to_db))
            self.logger.info("Empty-DB ({}) was connected.".format(fileName))
            return True
        else:
            self.logger.error("Given Project Folder is not exist: '{}'. ".format(prjFolder))
            return False

















##########################DB-Connection#############################

    def connect(self,path_to_db, encryption_key=False, reconnection=False, logger_debug=False):
        if not self._check_file_existens(path_to_db):
            return False
        if not self._check_db_should_not_exist():
            return False
        self._encryption_key = encryption_key

        dbName = os.path.splitext(os.path.basename(path_to_db))[0]

        if not self._validation_DBfile( path_to_db, encryption_key=encryption_key):
            self.logger.error("ValidationError: DB cannot be connected!")
            return False


        if self._encryption_key:
            try:
                self._db = sqlite.connect(path_to_db)
                c = self._db.cursor()
                c.execute("PRAGMA key='{}'".format(self._encryption_key))
                self._commit()
                self.is_encrypted = True
            except Exception as  exception:
                self.logger.error("Something happens while DB-Connection '{}'. PathToDB: '{}'. ".format( repr(exception), path_to_db))
                return False

        else:
            self._db = sqlite.connect(path_to_db)

        try:
            self._update_temp_list_with_dbnames_in_instance()
            self._update_temp_tablesList_in_instance()
        except sqlite.DatabaseError, e:
            self.logger.error("DatabaseError: {}".format(e))
            return False

        
        self._update_temp_attributsList_in_instance()
        # except Exception, e:
        #     self.logger.error("Something goes wrong: ('{}')".format(e))
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
            self.logger.error("ValidationError: DB cannot be attached!")
            return False

        ### Check, if it is right DB and get name
        tempdb = DBHandler(logger_level=logging.ERROR)
        tempdb.connect(path_to_db, encryption_key=encryption_key)
        #dbName = "{}_{}".format(tempdb.typ(), tempdb.name())
        del tempdb
        self._reinitialize_logger()

        dbName = "_" + os.path.splitext(os.path.basename(path_to_db))[0]
        
        if self._encryption_key:
            if encryption_key:
                qeary = "ATTACH DATABASE '{path_to_db}' AS {dbName} KEY '{key}';".format(path_to_db=path_to_db, dbName=dbName, key=encryption_key)

            else:
                qeary = "ATTACH DATABASE '{path_to_db}' AS {dbName} KEY '';".format(path_to_db=path_to_db, dbName=dbName)

        else:
            if encryption_key:
                qeary = "ATTACH DATABASE '{path_to_db}' AS {dbName} KEY '{key}';".format(path_to_db=path_to_db, dbName=dbName, key=encryption_key)

            else:
                qeary = "ATTACH DATABASE '{path_to_db}' AS {dbName};".format(path_to_db=path_to_db, dbName=dbName)

        #p(qeary)
        if dbName not in self.dbnames:
            try:
                cursor = self._db.cursor()
                cursor.execute(qeary)
            except Exception as  exception:
                if "unrecognized token" in str(exception):
                    self.logger.error("DBAttachError:  While attaching of the '{}'-DB attacher get an following error: '{}'. Probably you used not allowed characters in the db or file name. (e.g. '.' not allowed).".format(dbName, repr(exception) ))
                else:    
                    self.logger.error("DBAttachError: Something happens while attaching of '{}'-DB: '{}'".format(dbName, repr(exception) ))
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
            self.logger.error("DB '{}' is already attached. You can not attached same DB more as 1 time!".format(dbName))
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
                        self.logger.error("'{}' DB wasn't re-attached".format(dbname_to_retach))

                else:
                    self.logger.error("'{}' DB wasn't detached.".format(attached_db_name))
                #self.attach()
                # else:
                #     self.logger.error("Given Attached DB wasn't detached! DBName: '{}'. ".format(attached_db_name))
                #     return False
            else:
                self.logger.error("Given dbName ('{}') is not exist in the current DB-Structure.".format(attached_db_name))
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
                    qeary = "DETACH DATABASE '{}';".format( attached_db_name)
                    
                    try:
                        cursor = self._db.cursor()
                        cursor.execute(qeary)
                        self.logger.debug("'{}'-DB was detached.".format(attached_db_name))

                        detached_dbs.append( configs[0])
                    except Exception as  exception:
                        self.logger.error("Something happens while detaching of '{}'-DB: '{}'".format(attached_db_name, repr(exception) ))
                else:
                    self.logger.error("Given Attached DB '{}' is not in the Config-List of AttachedDBs. ".format(attached_db_name))
                    return False
            else:
                self.logger.error("Given dbName ('{}') is not exist in the current DB-Structure".format(attached_db_name))
                return False


        self._update_temp_list_with_dbnames_in_instance()
        self._update_temp_tablesList_in_instance()
        self._update_temp_attributsList_in_instance()
        return detached_dbs






##########################DB-Attributes#####################



    def add_attributs(self,attributs_names, values, dbname=False):
        if not self._check_db_should_exist():
            return False
        self._commit_if_inserts_was_did()

        if self.insertCV("info", [attr[0] for attr in attributs_names], values, dbname=dbname):
            self._update_temp_attributsList_in_instance()
            return True
        else:
            self.logger.error("Attributes wasn't added into InfoTable (dbName:{})".format(dbname))
            return False
        #p(attributName_as_str, c="m")
        #p(values_as_str, c="m")
        ### Add Attributes



    def update_attr(self,attribut_name, value, dbname=False):
        ### Exception Handling
        dbname = dbname if dbname else "main"
        if not self._check_db_should_exist():
            return False
        self._commit_if_inserts_was_did()
        # Check if attributes and values have the same length
        if not isinstance(attribut_name, (str, unicode)):
            self.logger.error("Given AttributName should be an string or unicode object.")
            return None

        # if given attribute exist in the Info_Table
        if not filter(lambda x: unicode(attribut_name) == unicode(x), self.col("info")):
            self.logger.error("Given Attribute ('{}') is not exist in this DataBase.".format(attribut_name))
            return None


        if dbname  in self.dbnames:
            qeary = 'UPDATE {}.info  \nSET {}="{}";'.format(dbname,attribut_name,value)
        else:
            self.logger.error("Given dbName ('{}') is not exist in the current DB-Structure".format(dbname))
            return None
        
        ### Update Attribute
        if "info" in self.tables(dbname=dbname):
            try:
                cursor = self._db.cursor()
                cursor.execute(qeary)
                self._commit()
                self._update_temp_attributsList_in_instance()
                return True
            except Exception as  exception:
                self.logger.error("Something happens while detaching of '{}'-DB: '{}'".format(attached_db_name, repr(exception) ))
                return False
        else:
            self.logger.error("Info-Table is wasn't found or not exist. Please initialize the Info Table, bevor you may add any attributes.")
            return False




    def get_attr(self,attributName, dbname=False):
        if not self._check_db_should_exist():
            return False
        if not isinstance(attributName, (str, unicode)):
            self.logger.error("Given AttributName should be an string or unicode object.")
            return None

        dbname = dbname if dbname else "main" 

        if not self._attributs_dict:
            self.logger.warning("Temporary AttributesList is empty")
            return None

        # if given attribute exist in the Info_Table
        if attributName not in self._attributs_dict[dbname]:
            self.logger.error("Given Attribute ('{}') is not exist in this '{}'-DB.".format(attributName,dbname))
            return None


        if dbname:
            if dbname  in self.dbnames:
                return self._attributs_dict[dbname][attributName]
            else:
                self.logger.error("Given dbName ('{}') is not exist in the current DB-Structure".format(dbname))
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
                    self.logger.error("Given dbName ('{}') is not exist in the current DB-Structure".format(dbname))
                    return None
            else:
                return self._attributs_dict

        else:
            self.logger.error("Info-Table wasn't found or not exist. Please initialize the Info Table, bevor you may add any attributes.")
            return None

















##########################DB-Execute Commands#####################



    def execute(self, qeary):
        if not self._check_db_should_exist():
            return False
        self._commit_if_inserts_was_did()
        try:
            cur = self._db.cursor()
            cur.execute(qeary)
            return cur.execute(qeary)
        except Exception as  exception:
            self.logger.error("Something happens while execution of the following qeary: '{}'.".format(qeary))
            return False

        
    def executescript(self, qeary):
        if not self._check_db_should_exist():
            return False
        self._commit_if_inserts_was_did()
        try:
            cur = self._db.cursor()
            cur.execute(qeary)
            return cur.executescript(qeary)
        except Exception as  exception:
            self.logger.error("Something happens while execution of the following qeary: '{}'.".format(qeary))
            return False













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
                self.logger.error("Given dbName ('{}') is not exist in the current DB-Structure".format(dbname))
                return []

        else:
            self.logger.debug("Table names was returned for 'main' DB. (from temp list)")
            if len(self._tables_dict)>0:
                return self._tables_dict["main"]
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
            self.logger.error("Something happens while getting DB-FileName:  '{}'.".format( repr(exception) ))
            return False

        if dbname:
            if dbname  in self.dbnames:
                for row in rows:
                    if row[1] == dbname:
                        return os.path.basename(row[2])
            else:
                self.logger.error("Given dbName ('{}') is not exist in the current DB-Structure".format(dbname))
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
            self.logger.error("Something happens while getting DB-Path:  '{}'.".format( repr(exception) ))
            return False
        ## check existents of the dbName
        if dbname:
            if dbname  in self.dbnames:
                for row in rows:
                    if row[1] == dbname:
                        return row[2]
            else:
                self.logger.error("Given dbName ('{}') is not exist in the current DB-Structure".format(dbname))
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
            self.logger.error("Something happens while getting DB-DirName:  '{}'.".format( repr(exception) ))
            return False

        ## check existents of the dbName
        if dbname:
            if dbname  in self.dbnames:
                for row in rows:
                    if row[1] == dbname:
                        return os.path.dirname(row[2])
            else:
                self.logger.error("Given dbName ('{}') is not exist in the current DB-Structure".format(dbname))
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
            self.logger.error("Something happens while getting Paths of AttachedDBs:  '{}'.".format( repr(exception) ))
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
            self.logger.error("Something happens while getting FileName of AttachedDBs:  '{}'.".format( repr(exception) ))
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
            self.logger.error("Something happens while getting of AttachedDBs:  '{}'.".format( repr(exception) ))
            return False

        return [ row[1] for row in rows if row[1]!= "main"]





    def col(self, tableName,dbname=False):
        if not self._check_db_should_exist():
            return False
        self._commit_if_inserts_was_did()

        if not filter(lambda x: unicode(tableName) == unicode(x), self.tables(dbname=dbname)):
            self.logger.error("Given Table is not exist: ('{}').".format(tableName))
            return None

        ## check existents of the dbName
        if dbname:
            if dbname  in self.dbnames:
                query = "PRAGMA {dbname}.table_info('{table_name}'); ".format(table_name=tableName, dbname=dbname)
            else:
                self.logger.error("Given dbName ('{}') is not exist in the current DB-Structure".format(dbname))
                return None
        else:
            query = "PRAGMA table_info('{table_name}'); ".format(table_name=tableName)

        try:
            cursor = self._db.cursor()
            cursor.execute(query)
            columns = cursor.fetchall()
        except Exception as  exception:
            self.logger.error("Something happens while getting of TableColumns for '{}'-Table:  '{}'.".format(tableName, repr(exception) ))
            return False

        self.logger.debug("Columns for Table '{}'  was returned (dbName:'{}')".format(tableName,dbname))
        return [column[1] for column in columns]



    def colt(self, tableName,dbname=False):
        if not self._check_db_should_exist():
            return False
        self._commit_if_inserts_was_did()

        if not filter(lambda x: unicode(tableName) == unicode(x), self.tables(dbname=dbname)):
            self.logger.error("Given Table is not exist: ('{}').".format(tableName))
            return None

        ## check existents of the dbName
        if dbname:
            if dbname  in self.dbnames:
                query = "PRAGMA {dbname}.table_info('{table_name}'); ".format(table_name=tableName, dbname=dbname)
            else:
                self.logger.error("Given dbName ('{}') is not exist in the current DB-Structure".format(dbname))
                return None
        else:
            query = "PRAGMA table_info('{table_name}'); ".format(table_name=tableName)

        try:
            cursor = self._db.cursor()
            cursor.execute(query)
            columns = cursor.fetchall()
        except Exception as  exception:
            self.logger.error("Something happens while getting of Types of TableColumns for '{}'-Table:  '{}'.".format(tableName, repr(exception) ))
            return False

        self.logger.debug("Columns with types for Table '{}'  was returned (dbName:'{}')".format(tableName,dbname))
        return [(column[1],column[2]) for column in columns]



    def rownum(self, tableName,dbname=False):
        if not self._check_db_should_exist():
            return False
        self._commit_if_inserts_was_did()
        ## check existents of the tableName
        if not filter(lambda x: unicode(tableName) == unicode(x), self.tables(dbname=dbname)):
            self.logger.error("Given Table is not exist: ('{}').".format(tableName))
            return None

        ## check existents of the dbName
        if dbname:
            if dbname  in self.dbnames:
                query = "select count(*) from {dbname}.{table_name}; ".format(table_name=tableName, dbname=dbname)
            else:
                self.logger.error("Given dbName ('{}') is not exist in the current DB-Structure".format(dbname))
                return None
        else:
            query = "select count(*) from {table_name}; ".format(table_name=tableName)


        try:
            cursor = self._db.cursor()
            cursor.execute(query)
            number = cursor.fetchone()
        except Exception as  exception:
            self.logger.error("Something happens while getting of RowsNumber for '{}'-Table:  '{}'.".format(tableName, repr(exception) ))
            return False

        self.logger.debug("Number of Rows was returned")
        return number[0]
        #return [(column[1],column[2]) for column in columns]














##########################DB--Getters######################



    def getlazy(self, tableName, columns=False,  dbname=False, size_to_get=1000,  where=False, connector_where="AND"):
        if not self._check_db_should_exist():
            yield False
            return
        if not self._check_if_table_exist(tableName, dbname=dbname):
            yield False
            return
        self._commit_if_inserts_was_did()


        if columns:
            if not self._check_if_given_columns_exist(tableName, columns, dbname=dbname):
                yield False
                return
            columns_str = columns_list_to_str(columns)
            if not  columns_str:
                self.logger.error("TypeError: Given Columns should be given as a list. '{}' was given. ".format(type(columns)))
                yield None
                return
        else:
            columns_str = '*'


        if where:
            where_cond_as_str = where_condition_to_str(where, connector=connector_where)
            if not where_cond_as_str:
                self.logger.error("GetAllError: Where-Condition(s) wasn't compiled to String!")
                yield False
                return 

        if dbname:
            if dbname  in self.dbnames:
                if where:
                    qeary = 'SELECT {} FROM  {}.{} WHERE {};'.format(columns_str, dbname, tableName, where_cond_as_str)
                else:
                    qeary = 'SELECT {} FROM  {}.{};'.format(columns_str, dbname, tableName)
            else:
                self.logger.error("Given dbName ('{}') is not exist in the current DB-Structure".format(dbname))
                yield None
                return
        else:
            if where:
                qeary = 'SELECT {} FROM  {} WHERE {};'.format(columns_str, tableName, where_cond_as_str)
            else:
                qeary = 'SELECT {} FROM  {};'.format(columns_str, tableName)

        try:
            cursor = self._db.cursor()
            cursor.execute(qeary)
        except Exception as  exception:
            self.logger.error("Something happens by LazyGetter:  '{}'.".format( repr(exception) ))
            yield False
            return
        #i=0
        while True:
            # i +=1
            # p(i)
            results = cursor.fetchmany(size_to_get)
            if not results:
                break
            for row in results:
                yield row







    def getall(self, tableName, columns=False,  dbname=False, where=False, connector_where="AND"):
        if not self._check_db_should_exist():
            return False
        if not self._check_if_table_exist(tableName, dbname=dbname):
            return False
        self._commit_if_inserts_was_did()
        #p(dbname)
        if columns:
            if not self._check_if_given_columns_exist(tableName, columns, dbname=dbname):
                return False
            columns_str = columns_list_to_str(columns)
            if not  columns_str:
                self.logger.error("TypeError: Given Columns should be given as a list. '{}' was given. ".format(type(columns)))
                return None
        else:
            columns_str = '*'


        if where:
            where_cond_as_str = where_condition_to_str(where, connector=connector_where)
            if not where_cond_as_str:
                self.logger.error("GetAllError: Where-Condition(s) wasn't compiled to String!")
                return False

        if dbname:
            if dbname  in self.dbnames:
                if where:
                    qeary = 'SELECT {} FROM  {}.{} \nWHERE {};'.format(columns_str, dbname, tableName, where_cond_as_str)
                else:
                    qeary = 'SELECT {} FROM  {}.{};'.format(columns_str, dbname, tableName)
            else:
                self.logger.error("Given dbName ('{}') is not exist in the current DB-Structure".format(dbname))
                return None
        else:
            if where:
                qeary = 'SELECT {} FROM  {} \nWHERE {};'.format(columns_str, tableName, where_cond_as_str)
            else:
                qeary = 'SELECT {} FROM  {};'.format(columns_str, tableName)

        #p(qeary)
        try:
            cursor = self._db.cursor()
            cursor.execute(qeary)
            results = cursor.fetchall()
            return results
        except Exception as  exception:
            self.logger.error("Something happens at the GetAll-Method:  '{}'.".format( repr(exception) ))
            return False

        




    def getone(self, tableName, columns=False,  dbname=False, where=False, connector_where="AND"):
        if not self._check_db_should_exist():
            yield False
            return
        if not self._check_if_table_exist(tableName, dbname=dbname):
            yield False
            return
        self._commit_if_inserts_was_did()

        if columns:
            if not self._check_if_given_columns_exist(tableName, columns, dbname=dbname):
                yield False
                return
            columns_str = columns_list_to_str(columns)
            if not  columns_str:
                self.logger.error("TypeError: Given Columns should be given as a list. '{}' was given. ".format(type(columns)))
                yield None
                return
        else:
            columns_str = '*'


        if where:
            where_cond_as_str =  where_condition_to_str(where, connector=connector_where)
            if not where_cond_as_str:
                self.logger.error("GetAllError: Where-Condition(s) wasn't compiled to String!")
                yield False
                return 


        if dbname:
            if dbname  in self.dbnames:
                if where:
                    qeary = 'SELECT {} FROM  {}.{} \nWHERE {};'.format(columns_str, dbname, tableName, where_cond_as_str)
                else:
                    qeary = 'SELECT {} FROM  {}.{};'.format(columns_str, dbname, tableName)
            else:
                self.logger.error("Given dbName ('{}') is not exist in the current DB-Structure".format(dbname))
                yield None
                return 
        else:
            if where:
                qeary = 'SELECT {} FROM  {} \nWHERE {};'.format(columns_str, tableName, where_cond_as_str)
            else:
                qeary = 'SELECT {} FROM  {};'.format(columns_str, tableName)

        try:
            cursor = self._db.cursor()
            cursor.execute(qeary)
        except Exception as  exception:
            self.logger.error("Something happens at the GetOne-Method:  '{}'.".format( repr(exception) ))
            yield False
            return 

        while True:
            results = cursor.fetchone()
            if not results:
                break

            yield results
  


    def getlimit(self, limit, tableName, columns=False,  dbname=False,  where=False, connector_where="AND"):
        if not self._check_db_should_exist():
            return False
        if not self._check_if_table_exist(tableName, dbname=dbname):
            return False
        self._commit_if_inserts_was_did()

        if columns:
            if not self._check_if_given_columns_exist(tableName, columns, dbname=dbname):
                return False
            columns_str = columns_list_to_str(columns)
            if not  columns_str:
                self.logger.error("TypeError: Given Columns should be given as a list. '{}' was given. ".format(type(columns)))
                return None
        else:
            columns_str = '*'


        if where:
            where_cond_as_str = where_condition_to_str(where)
            if not where_cond_as_str:
                self.logger.error("GetAllError: Where-Condition(s) wasn't compiled to String!")
                return False

        if dbname:
            if dbname  in self.dbnames:
                if where:
                    qeary = 'SELECT {} FROM  {}.{}  \n WHERE {} \n LIMIT {};'.format(columns_str, dbname, tableName, where_cond_as_str,limit)
                else:
                    qeary = 'SELECT {} FROM  {}.{} LIMIT {};'.format(columns_str, dbname, tableName, limit)
            else:
                self.logger.error("Given dbName ('{}') is not exist in the current DB-Structure".format(dbname))
                return None
        else:
            if where:
                qeary = 'SELECT {} FROM  {}  \n WHERE {} \n LIMIT {};'.format(columns_str, tableName, where_cond_as_str, limit)
            else:
                qeary = 'SELECT {} FROM  {} LIMIT {};'.format(columns_str, tableName, limit)

        #p(qeary)
        try:
            cursor = self._db.cursor()
            cursor.execute(qeary)
            results = cursor.fetchall()
            return results
        except Exception as  exception:
            self.logger.error("Something happens at the GetLimit-Method:  '{}'.".format( repr(exception) ))
            return False
  















##########################DB-Setters##################




    def insertlazy(self, table_name, typ, columns_names=False,values=False, dbname=False):
        self._lazy_writer_number_inserts_after_last_commit +=1
        # self.writer_counter
        # self._lazyness_border

        if typ.lower() == "cv":
            if columns_names and values:
                self.insertCV(table_name,columns_names, values, dbname)
            else:
                self.logger.error("LazyWriterError: Columns_names or Values wasn't given.")
                return False

        elif typ.lower() == "v":
            if values:
                self.insertV(table_name, values, dbname)
            else:
                self.logger.error("LazyWriterError: Values wasn't given.")
                return False

        elif typ.lower() == "csvs":
            if columns_names and values:
                self.insertCsVs(table_name,columns_names, values, dbname)
            else:
                self.logger.error("LazyWriterError: Columns_names or Values wasn't given.")
                return False

        else:
            self.logger.error("Not Supported type of lazy_writer. This type was given: '{}'. Please use one of the supported types: ['cv','v', 'csvs'].".format(typ))
            return False


        if self._lazy_writer_number_inserts_after_last_commit >=  self._lazyness_border:
            self._commit()
            self._successful_commits_with_lazy_writer += 1
            self._lazy_writer_all_inserts_counter +=  self._lazy_writer_number_inserts_after_last_commit
            self._lazy_writer_number_inserts_after_last_commit = 0
            self.logger.debug("LazyWriter: Last {} inserts was committed in the DB. ".format(self._lazyness_border))




    def insertCV(self,table_name,columns_names,values, dbname=False):
        # INSERT INTO users (email, user_name, create_date)
        # VALUES ("foo@bar.com", "foobar", "2009-12-16");


        if not self._check_db_should_exist():
            return False
        # Check if attributes and values have the same length
        if len(columns_names) != len(values):
            self.logger.error("Length of given columns_names and values is not equal.")
            return False


        columnsName_as_str = columns_list_to_str(columns_names)
        values_as_str = values_list_to_str(values)
        #p(values_as_str, c="r")
        if not columnsName_as_str or not values_as_str:
            self.logger.error("Given Columns or Values wasn't packed into the list.")
            return False
        #p(columnsName_as_str, c="m")
        #p(values_as_str, c="m")
        ### Add Attributes

        if dbname:
            if dbname  in self.dbnames:
                qeary = 'INSERT INTO {dbname}.{tableName} ({columns}) \nVALUES ({values});'.format(columns=columnsName_as_str,values=values_as_str, tableName=table_name, dbname=dbname)
            else:
                self.logger.error("Given dbName ('{}') is not exist in the current DB-Structure".format(dbname))
                return None
        else:
            qeary = 'INSERT INTO {tableName} ({columns}) \nVALUES ({values});'.format(columns=columnsName_as_str,values=values_as_str, tableName=table_name)

        #p(qeary)
        if table_name in self.tables(dbname=dbname):
            try:
                cursor = self._db.cursor()
                cursor.execute(qeary)
                if table_name != "info":
                    self.all_inserts_counter +=1
                    self.number_of_new_inserts_after_last_commit += 1
            except Exception as  exception:
                self.logger.debug("Following Qeary could have an Error: '{}'.".format(qeary))

                if "has no column named" in str(exception):
                    self.logger.error("One of the columns is not in the Table. See Exception:  '{}'. Current Insertion is not done.".format( repr(exception) ))
                else:
                    self.logger.error("Something happens at the InsertCV-Method:  '{}'. Current Insertion is not done.".format( repr(exception) ))
                return False

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
        if not self._check_db_should_exist():
            return False
        # Check if attributes and values have the same length

        values_as_str = values_list_to_str(values)

        if  not values_as_str:
            self.logger.error("Given  Values wasn't packet into the list.")
            return False
        #p(columnsName_as_str, c="m")
        #p(values_as_str, c="m")
        ### Add Attributes

        if dbname:
            if dbname  in self.dbnames:
                qeary = 'INSERT INTO {dbname}.{tableName}  \nVALUES ({values});'.format(values=values_as_str, tableName=table_name, dbname=dbname)
            else:
                self.logger.error("Given dbName ('{}') is not exist in the current DB-Structure".format(dbname))
                return None
        else:
            qeary = 'INSERT INTO {tableName}  \nVALUES ({values});'.format(values=values_as_str, tableName=table_name)

        #p(qeary, c="m")
        if table_name in self.tables(dbname=dbname):
            try:
                cursor = self._db.cursor()
                cursor.execute(qeary)
                if table_name != "info":
                    self.all_inserts_counter +=1
                    self.number_of_new_inserts_after_last_commit += 1
            except Exception as  exception:
                self.logger.debug("Following Qeary could have an Error: '{}'.".format(qeary))
                self.logger.error("Something happens at the InsertV-Method:  '{}'. Current Insertion is not done.".format( repr(exception) ))
                return False

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
        return False

        if table_name != "info":
            self.all_inserts_counter +=1
            #!!!!!self.number_of_new_inserts_after_last_commit + = "" insert number of insertion















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
                self.logger.error("Given dbName ('{}') is not exist in the current DB-Structure".format(dbname))
                return None
        else:
            query = "DROP TABLE {};".format(table_name)

        #p(query)
        try:
            cursor = self._db.cursor()
            cursor.execute(query)
            #tables_exist = cursor.fetchall()
        except Exception as  exception:
            self.logger.error("Something happens while dropping the '{}'-Table:  '{}'.".format(table_name, repr(exception) ))
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
            self.logger.error("Length of given columns_names and values is not equal.")
            return False


        columns_and_values_as_str = columns_and_values_to_str(columns_names,values)
        #p(columnsName_as_str, c="m")
        #p(values_as_str, c="m")
        ### Add Attributes

        if where:
            where_cond_as_str = where_condition_to_str(where, connector=connector_where)
            if not where_cond_as_str:
                self.logger.error("GetAllError: Where-Condition(s) wasn't compiled to String!")
                return False

        if dbname:
            if dbname  in self.dbnames:
                if where:
                    qeary = 'UPDATE {dbname}.{tableName}  \nSET {col_and_val} WHERE {where};'.format(col_and_val=columns_and_values_as_str, dbname=dbname, tableName=table_name, where=where_cond_as_str)
                else:
                    qeary = 'UPDATE {dbname}.{tableName}  \nSET {col_and_val};'.format(col_and_val=columns_and_values_as_str, dbname=dbname, tableName=table_name)
            else:
                self.logger.error("Given dbName ('{}') is not exist in the current DB-Structure".format(dbname))
                return None
        else:
            if where:
                qeary = 'UPDATE {tableName}  \nSET {col_and_val} WHERE {where};'.format(col_and_val=columns_and_values_as_str, tableName=table_name, where=where_cond_as_str)
            else:
                qeary = 'UPDATE {tableName}  \nSET {col_and_val};'.format(col_and_val=columns_and_values_as_str, tableName=table_name)


        if table_name in self.tables(dbname=dbname):
            try:
                cursor = self._db.cursor()
                #p(qeary)
                cursor.execute(qeary)
                self._commit()
                return True
            except Exception as  exception:
                self.logger.error("Something happens while updating the '{}'-Table:  '{}'.".format(table_name, repr(exception) ))
                return False
        else:
            self.logger.error("Table ('{}') wasn't found or not exist. Please initialize the Info Table, before you may add any attributes.".format(table_name))
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
            self.logger.error("ClossingError: DB-Closing return an Error: '{}' ".format(e))
            sys.exit()


    def _close(self, for_encryption=False):
        try:
            self.commit()
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
            self.logger.error("ClossingError: DB-Closing return an Error: '{}' ".format(e))
            sys.exit()






    def addtable(self, table_name, attributs_names_with_types_as_list_with_tuples,dbname=False, constrains=False) :
        
        if not self._check_db_should_exist():
            return False
        self._commit_if_inserts_was_did()

        if table_name not in self.tables(dbname=dbname):
            attributs_names_with_types_as_str = columns_and_types_in_tuples_to_str(attributs_names_with_types_as_list_with_tuples)
            if not attributs_names_with_types_as_str:
                self.logger.error("Something was wrong by Converting attributes into string. Program was stoped!")
                return False

            if constrains:
                if dbname:
                    if dbname  in self.dbnames:
                        qeary = 'CREATE TABLE {}.{} ({}\n{});'.format(dbname,table_name,attributs_names_with_types_as_str, constrains)
                    else:
                        self.logger.error("Given dbName ('{}') is not exist in the current DB-Structure".format(dbname))
                        return False
                else:
                    qeary = 'CREATE TABLE {} ({}\n{});'.format(table_name,attributs_names_with_types_as_str, constrains)
            else:
                if dbname:
                    if dbname  in self.dbnames:
                        qeary = 'CREATE TABLE {}.{} ({});'.format(dbname,table_name,attributs_names_with_types_as_str)
                    else:
                        self.logger.error("Given dbName ('{}') is not exist in the current DB-Structure".format(dbname))
                        return False
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
            except sqlite.OperationalError, e:
                if 'near "-"' in str(e):
                    self.logger.error("AddTableOperationalError: While adding Table-'{}'. Problem: '{}'. (It may be a Problem with using not allowed Symbols in the column name.  e.g.'-')\nProblem was found in the following query: '{}'.".format(table_name,e, qeary.replace("\n", "  ")))
                else:
                    self.logger.error("AddTableOperationalError: While adding Table-'{}'. Problem: '{}'. \nProblem was found in the following query: '{}'.".format(table_name,e, qeary.replace("\n", " ")))
                return False

        else:
            self.logger.error("'{}'-Table is already exist in the given DB. You can not initialize it one more time!".format(table_name))
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
                self.logger.error("Something happens while changing of the encryption key:  '{}'.".format(repr(exception)))
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
            self.logger.error("Something happens while Encryption:  '{}'.".format(repr(exception)))
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
                self.logger.error("Encrypted DB wasn't found/connected. Encryption is fail! Roled back to non-encrypted DB.")
                os.rename(path_to_current_db+".temp", path_to_current_db)
                self.connect(path_to_current_db,reconnection=True,  logger_debug=True)
                return False

        else:
            self.logger.error("ENCRYPTION: TempDB wasn't found. Encryption is failed! Roled back to non-encrypted DB.")
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
            self.logger.error("Something happens while Decryption:  '{}'.".format(repr(exception)))
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
                self.logger.error("Decrypted DB wasn't found/connected. Decryption is fail! Roled back to encrypted DB.")
                os.rename(path_to_current_db+".temp", path_to_current_db)
                self.connect(path_to_current_db,reconnection=True,  logger_debug=True)
                return False

        else:
            self.logger.error("DECRYPTION: TempDB wasn't found. Encryption is failed! Roled back to encrypted DB.")
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
            self.logger.error("Given Object is not from following type: (str, unicode).")
            return False
        else:
            return True


    def _check_if_given_columns_exist(self, tableName,columns, dbname=False):
        for column in columns:
            if column not in  self.col(tableName):
                self.logger.error("Given Column '{}' is not exist in the following Table '{}' (dbname='{}') ".format(column,tableName,dbname))
                return False
        
        return True

    def _check_if_table_exist(self,tableName, dbname=False):
        if tableName not in self.tables(dbname=dbname):
            self.logger.error("Given Table '{}' is not exist (dbname='{}')) ".format(tableName,dbname))
            return False
        else:
            return True

    def _check_db_should_exist(self):
        if not self._db: 
            self.logger.error("No active DB was found. You need to connect or initialize a DB first, before you can make some operation on the DB.")
            return False
        else:
            return True


    def _check_db_should_not_exist(self):
        if self._db: 
            self.logger.error("An active DB was found. You need to initialize new empty Instance of DB before you can do this operation.")
            return False
        else:
            return True


    def _db_should_be_a_corpus(self):

        if not self._check_db_should_exist():
            #p(".......")
            return False

        db_typ = self.get_attr(attributName="typ")

        if db_typ != "corpus":
            self.logger.error("Active DB is from typ '{}'. But it should be from typ 'corpus'. ".format(db_typ))
            return False
        return True


    def _db_should_be_stats(self):
        if not self._check_db_should_exist():
            return False
        db_typ = self.get_attr(attributName="typ")
        if db_typ != "stats":
            self.logger.error("Active DB is from typ '{}'. But it should be from typ 'stats'. ".format(db_typ))
            return False
        return True





    def _check_file_existens(self, path_to_file):
        if not os.path.isfile(path_to_file):
            self.logger.error("DB-File wasn't found: ('{}').".format(path_to_file))
            #os._exit(1)
            return False
        else:
            return True










###########################DB-Validation#######################





    def _validation_DBfile(self, path_to_db, encryption_key=False):
        if os.path.isfile(path_to_db):

                try:
                    _db = sqlite.connect(path_to_db)
                    c = _db.cursor()
                    if encryption_key:
                        c.execute("PRAGMA key='{}'".format(encryption_key))
                    c.execute("SELECT name FROM sqlite_master WHERE type='table';")
                    tables = c.fetchall()

                except sqlite.DatabaseError, e:
                    if encryption_key:
                        self.logger.error("ValidationError: '{}'. Or maybe a given Key is incorrect. Please give another one.  PathToDB: '{}'. ".format( e, path_to_db))
                    else:
                        self.logger.error("ValidationError: '{}'. PathToDB: '{}'. ".format( e, path_to_db))
                        return False
                except Exception as  exception:
                    self.logger.error("Something wrong happens while Validation '{}'. PathToDB: '{}'. ".format( repr(exception), path_to_db))
                    return False


                try:
                    c.execute("SELECT name FROM sqlite_master WHERE type='table';")
                    tables = c.fetchall()




                    ## check Row Numbers
                    rowNumbes = c.execute("select count(*) from info; ").fetchone()[0]
                    if rowNumbes > 1:
                        self.logger.error("ValidationError: Info-Table has more as 1 row. It is incorrect!")
                        return False
                    elif rowNumbes ==0:
                        self.logger.error("ValidationError: Info-Table is empty. It is incorrect!")
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
                            self.logger.error("ValidationError: Unsupported DB-Type '{}' was found.".format(get_typ[0]))
                            return False

                    except sqlite.OperationalError,  e:
                        self.logger.error("ValidationError:  '{}'. Impossible to get DB-Typ. PathToDB: '{}'. ".format( e, path_to_db))
                        return False


                except Exception as  exception:
                    self.logger.error("ValidationError: Something wrong happens while Validation '{}'. PathToDB: '{}'. ".format( repr(exception), path_to_db))
                    return False



                return True

        else:
            self.logger.error("Given DB-File is not exist: '{}'. ".format(path_to_db))
            return False





    def _validate_corpusDB(self, db):

        ### Step 1: Attributes
        attributs_and_types = [(attr[0], attr[1].split(' ', 1 )[0])  for attr in attributs_names_corpus]

        c = db.cursor()
        c.execute("PRAGMA table_info('info'); ")
        columns_and_types = c.fetchall()
        columns_and_types = [(col[1], col[2])for col in columns_and_types]


        if set(columns_and_types) !=set(attributs_and_types):
            self.logger.error("CorpusDBValidationError: Given Stats-DB contain not correct attributes. Following col_and_types was extracted: '{}' and they are incorrect. Please use following data as golden standard: '{}'. ".format(columns_and_types, attributs_and_types))
            return False


        ## Step 2: Table Names
        c.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = c.fetchall()
        default_tables = ["documents"]
        extracted_tnames = [table_name[0] for table_name in tables]
        for defaultTable in default_tables:
            if defaultTable not in extracted_tnames:
                self.logger.error("CorpusDBValidationError: '{}'-default-Table wasn't found in the given Corpus-DB.".format(defaultTable))
                return False




        return True

    def _validate_statsDB(self, db):

        ### Step 1: Attributes
        attributs_and_types = [(attr[0], attr[1].split(' ', 1 )[0])  for attr in attributs_names_stats]
        c = db.cursor()
        c.execute("PRAGMA table_info('info'); ")
        columns_and_types = c.fetchall()
        columns_and_types = [(col[1], col[2])for col in columns_and_types]

        if set(columns_and_types) !=set(attributs_and_types):
            self.logger.error("StatsDBValidationError: Given Stats-DB contain not correct attributes. Following col_and_types was extracted: '{}' and they are incorrect. Please use following data as golden standard: '{}'. ".format(columns_and_types, attributs_and_types))
            return False



        ## Step 2: Table Names
        c.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = c.fetchall()
        default_tables = ["baseline", "replications", "reduplications"]
        extracted_tnames = [table_name[0] for table_name in tables]
        for defaultTable in default_tables:
            if defaultTable not in extracted_tnames:
                self.logger.error("StatsDBValidationError: '{}'-default-Table wasn't found in the given Stats-DB.".format(defaultTable))
                return False
        return True







###########################DB-OtherHelpers################





    def _reinitialize_logger(self,  level=False):
        level = level if  level else self._logger_level
        #level=logging.INFO
        #p(self._logger_level, c="r")
        #coloredlogs.install(level=self._logger_level)
        #coloredlogs.install(level=self._logger_level)
        #self.logger.setLevel(self._logger_level)
        self.logger = Logger().myLogger("DBHandler", self._folder_for_log_files, use_logger=self._use_logger, level=level)
        #self.logger.debug('Beginn of creating an instance of DB()')
        self.logger.debug("Logger was reinitialized.")



    def _init_default_tables(self,typ, template=False, additional_columns_with_types=False):
        if template and template!="NULL":
            if template in DBHandler.templates:
                if additional_columns_with_types:
                    additional_columns_with_types += DBHandler.templates[template]
                else:
                    additional_columns_with_types = DBHandler.templates[template]
            else:
                self.logger.error("Given Template ('{}') is not exist".format(template))
                return False
        #p(additional_columns_with_types)
        if typ == "corpus":
            if not self._init_default_table("corpus", "documents", default_columns_and_types_for_corpus_documents, additional_collumns_with_types=additional_columns_with_types, constrains=default_constraints_for_corpus_documents):
                return False
        
        elif typ == "stats":
            if not self._init_default_table("stats", "baseline", default_columns_and_types_for_stats_baseline,  additional_collumns_with_types=additional_columns_with_types): 
                return False

            if not self._init_default_table("stats", "replications", default_columns_and_types_for_stats_replications,  additional_collumns_with_types=additional_columns_with_types, constrains=default_constrains_for_stats_replications):
                return False

            if not self._init_default_table("stats", "reduplications", default_columns_and_types_for_stats_reduplications,  additional_collumns_with_types=additional_columns_with_types, constrains=default_constrains_for_stats_reduplications):
                return False


        else:
            self.logger.error("Given typ of DB ('{}') is not exist.".format(typ))
            return False


        return True


    def _init_default_table(self, typ, tableName , default_collumns_with_types, additional_collumns_with_types=False, constrains=False):
        if typ.lower()=="corpus":
            if not self._db_should_be_a_corpus():
                return False
        elif typ.lower()=="stats":
            if not self._db_should_be_stats():
                return False
        else:
            self.logger.error("Not supported typ ('{}') of DB. Please use one of the following DB-Types: '{}'. ".format(typ, DBHandler.supported_db_typs))
            return False

        if additional_collumns_with_types:
            columns_and_types = default_collumns_with_types + additional_collumns_with_types
        else:
            columns_and_types = default_collumns_with_types
        constrains_in_str = constrains_list_to_str(constrains)
        #attributs_names_with_types_as_str = columns_and_types_in_tuples_to_str(columns_and_types)
        if not self.addtable( tableName, columns_and_types,constrains=constrains_in_str):
            self.logger.error("InitDefaultTableError: '{}'-Table wasn't added into the {}-DB.".format(tableName, typ))
            return False

        self.logger.debug("{}-Table in {} was initialized".format(tableName, typ))
        return True


    def _commit_if_inserts_was_did(self):
        if self.number_of_new_inserts_after_last_commit >0:
            self._commit()



    def _init_info_table(self, attributs_names):
        #str_attributs_names = columns_and_types_in_tuples_to_str(attributs_names)
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
                self.logger.error("Given dbName ('{}') is not exist in the current DB-Structure".format(dbname))
                return None
        else:
            query = "SELECT name FROM sqlite_master WHERE type='table';"

        try:
            cursor = self._db.cursor()
            cursor.execute(query)
            tables_exist = cursor.fetchall()
        except Exception as  exception:
            self.logger.error("Something happens while Getting Tables:  '{}'.".format(repr(exception)))
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
                qeary = 'SELECT * FROM  {}.info;'.format( dbname)
            else:
                self.logger.error("Given dbName ('{}') is not exist in the current DB-Structure".format(dbname))
                return None
        else:
            qeary = 'SELECT * FROM  info;'

        try:
            cursor = self._db.cursor()
            cursor.execute(qeary)
            attribut = cursor.fetchall()[0]
        except Exception as  exception:
            self.logger.error("Something happens while Getting all Attributes from InfoTable of '{}'-DB: '{}'".format(dbname, exception))
            return False

        number_of_rows_info_table = self.rownum("info",dbname=False)
        if number_of_rows_info_table ==1:
            columns = self.col("info", dbname=dbname)
            return dict(zip(columns, list(attribut)))
        elif number_of_rows_info_table ==0:
            self.logger.error("Table 'info' is empty. Please set attributes bevor!")
            return None
        else:
            self.logger.error("Table 'info' has more as 1 row. It's not correct. Please delete not needed rows.")
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
                    self.logger.error("Attributes wasn't updated!!!")
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
            self.logger.error("Something happens while Getting DBNames:  '{}'.".format(repr(exception)))
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
            self.logger.error("Empty List was returned.")
            return False



    def _clean_all_parameters_after_db_close(self):
        self._db = False
        self._encryption_key = False
        self.is_encrypted = False
        self._attachedDBs_config_from_the_last_session = self._attachedDBs_config
        self._attachedDBs_config = []
        self._tables_dict = {}
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


