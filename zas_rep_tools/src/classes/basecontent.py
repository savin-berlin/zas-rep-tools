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
import gc
import logging
import psutil

from zas_rep_tools.src.utils.error_tracking import initialisation
from zas_rep_tools.src.utils.traceback_helpers import print_exc_plus
from zas_rep_tools.src.utils.zaslogger import ZASLogger
from zas_rep_tools.src.utils.helpers import set_class_mode, print_mode_name,  instance_info, Status,function_name,  statusesTstring

from zas_rep_tools.src.utils.debugger import p


class BaseContent(object):

    def __init__(self, mode="error", save_settings=False, save_status=False,
                    logger_folder_to_save=False,  logger_usage=True,
                    logger_level=logging.INFO, log_content=False, 
                    logger_save_logs=False, logger_traceback=False, 
                    error_tracking=True,  ext_tb=False, clear_logger=True,
                    raise_exceptions=True,**kwargs):

        ## Set Mode: Part 1 (Set Parameters)
        self._mode = mode
        if mode != "free":
            _logger_level, _logger_traceback, _logger_save_logs, _save_status, _log_content, _save_settings, _logger_usage, _ext_tb= set_class_mode(self._mode)
            logger_level = _logger_level if _logger_level!=None else logger_level
            logger_traceback = _logger_traceback if _logger_traceback!=None else logger_traceback
            logger_save_logs = _logger_save_logs if _logger_save_logs!=None else logger_save_logs
            save_status = _save_status if _save_status!=None else save_status
            log_content = _log_content if _log_content!=None else log_content
            save_settings = _save_settings if _save_settings!=None else save_settings
            logger_usage = _logger_usage if _logger_usage!=None else logger_usage
            ext_tb = _ext_tb if _ext_tb!=None else ext_tb



        ## Step 2: Instance Encapsulation
        ## 2.General Parameters
        self._save_settings = save_settings
        self._save_status = save_status
        self._error_tracking = error_tracking
        self._ext_tb = ext_tb

        ## 2.2 Logger Parameters
        self._logger_level = logger_level
        self._logger_traceback =logger_traceback
        self._logger_save_logs = logger_save_logs
        self._logger_folder_to_save = logger_folder_to_save
        self._logger_usage = logger_usage
        self._log_content = log_content
        self._clear_logger = clear_logger
        self._raise_exceptions = raise_exceptions

        
        self._is_destructed = False
        self.class_name = self.__class__.__name__

        ## Logger Initialisation
        self.L = ZASLogger(self.class_name, level=self._logger_level,
                            folder_for_log=self._logger_folder_to_save,
                            logger_usage=self._logger_usage,
                            save_logs=self._logger_save_logs)
        self.logger = self.L.getLogger()

        self.logger.debug('Beginn of creating an instance of {}()'.format(self.__class__.__name__))

        ## Set Mode: Part 2 (Print setted Mode)
        print_mode_name(self._mode, self.logger)


        ## Error-Tracking:Initialization #1
        if self._error_tracking:
            self.client = initialisation()
            self.client.context.merge({'InstanceAttributes': self.__dict__})

        self.logger.debug('All Base-Parameters was initialized.')

        super(BaseContent, self).__init__(**kwargs)


    def __del__(self):
        proc = psutil.Process()
        p( proc.open_files() )

        for proc in psutil.process_iter():
            p("<<<")
            proc = psutil.Process()
        
            p( proc.open_files() )
            for f in proc.open_files():
               print f
            p(">>>")
           #p( proc.open_files() )
        if not self._is_destructed:
            if self._logger_usage:
                if self._save_settings:
                    #p(self.__class__.__name__)
                    inp_dict = { k:v if isinstance(v, (str, unicode, bool, int)) else str(v) for k,v in self.__dict__.iteritems()}
                    self.logger.settings("InstanceDestructionAttributes: {}".format( instance_info(inp_dict, attr_to_len=False, attr_to_flag=False, as_str=True)))
                    #p(inp_dict)

                if self._save_status:
                    statuses_as_str = statusesTstring(str(self.__class__.__name__).lower())
                    if statuses_as_str:
                        self.logger.status(statuses_as_str)
                
                try:
                    self.L._close_handlers()
                    del self.L
                    gc.collect()
                except:
                    pass
                self._is_destructed = True


    def _log_settings(self,attr_to_flag=False,attr_to_len=False):
        if self._save_settings:
            if self._logger_save_logs:
                attr_to_flag = attr_to_flag
                attr_to_len = attr_to_len
                inp_dict = { k:v if isinstance(v, (str, unicode, bool, int)) else str(v) for k,v in self.__dict__.iteritems()}
                self.logger.settings("InstanceInitializationAttributes: {}".format( instance_info(inp_dict, attr_to_len=attr_to_len, attr_to_flag=attr_to_flag, as_str=True)))
                

    # def _destruct_instance(self):
    #     #del self
    #     gc.collect()



class BaseDB(object):
    def __init__(self, optimizer=False, make_backup=True,  lazyness_border=100000,
                isolation_level=False, in_memory=False,thread_safe=True,
                rewrite=False, stop_if_db_already_exist=False, replace_double_items=True, 
                use_cash=False, stop_process_if_possible=True,
                optimizer_page_size = 4096,
                optimizer_cache_size=1000000, # The cache_size pragma can get or temporarily set the maximum size of the in-memory page cache.
                optimizer_locking_mode="EXCLUSIVE",
                optimizer_synchronous="OFF",
                optimizer_journal_mode="MEMORY",
                optimizer_temp_store="MEMORY",
                #backup_bevore_first_insert=True,
                **kwargs):


        #Input: Encapsulation:
        self._rewrite = rewrite
        self._stop_if_db_already_exist = stop_if_db_already_exist
        self._make_backup = make_backup
        #self._backup_bevore_first_insert = backup_bevore_first_insert
        self._lazyness_border = lazyness_border
        self._optimizer = optimizer
        self._in_memory = in_memory
        self._thread_safe = thread_safe
        self._use_cash = use_cash
        self._isolation_level = isolation_level # None, "EXCLUSIVE", "DEFERRED", "IMMEDIATE"
        self._optimizer_page_size = optimizer_page_size
        self._optimizer_cache_size = optimizer_cache_size
        self._optimizer_locking_mode = optimizer_locking_mode
        self._optimizer_synchronous = optimizer_synchronous
        self._optimizer_journal_mode = optimizer_journal_mode
        self._optimizer_temp_store = optimizer_temp_store
        self._replace_double_items = replace_double_items
        self._stop_process_if_possible = stop_process_if_possible

        super(BaseDB, self).__init__(**kwargs)



