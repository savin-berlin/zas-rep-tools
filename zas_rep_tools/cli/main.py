#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# : Command Line Interface  
# Author:
# c(Student) ->     {'Egor Savin'}
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

###Programm Info######


import click
import shutil
import os
import inspect
import sys
import logging
import ast
import json
from blessings import Terminal
import enlighten

#from zas_rep_tools.src.utils.zaslogger import ZASLogger
from zas_rep_tools.src.utils.cli_helper import set_main_folders, get_cli_logger, validate_corp_dbname, strtobool, get_corp_dbname, _get_status_bars_manager, _get_new_status_bar
from zas_rep_tools.src.utils.helpers import set_class_mode
from zas_rep_tools.src.classes.reader import  Reader
from zas_rep_tools.src.classes.corpus import  Corpus
from zas_rep_tools.src.utils.corpus_helpers import  CorpusData

from zas_rep_tools.src.classes.stats import  Stats
from zas_rep_tools.src.classes.exporter import  Exporter
from zas_rep_tools.src.classes.dbhandler import DBHandler
from zas_rep_tools.src.classes.streamer import Streamer
from zas_rep_tools.src.utils.debugger import p
from zas_rep_tools.src.classes.ToolConfiger import ToolConfiger



answer_error_tracking = None
project_folder = None
email = None
twitter_creditials = None
configer_obj = None
#logger = None
main_folders = set_main_folders(project_folder)




supported_commands = {
        "configer": {
                        "prjdir":["clean", "set", "reset", "print"],
                        "error_track":["set", "reset", "respeak","print"],
                        "twitter":["set", "reset", "respeak","print"],
                        "email":["set", "reset", "respeak","print"],
                        "user_data":["clean", "location","print"],

                    },
        "corpora": ["add", "del", "names", "meta", "basic_stats", "update_attr", "export", "used_tools"],

        }





@click.group()
def main():
    global answer_error_tracking
    global project_folder
    global email
    global twitter_creditials
    global configer_obj
    global main_folders


    configer_obj = ToolConfiger(mode="error") 
    configer_obj.get_data_from_user(rewrite=False)

    answer_error_tracking = configer_obj._user_data['error_tracking']
    project_folder = configer_obj._user_data['project_folder']
    if not project_folder:
        configer_obj.logger.error("ProjectDirectory wasn't given. Please Give first a new ProjectDirectory, before starting to use this tool.")
        return False
    
    else:
        if not os.path.isdir(project_folder):
            configer_obj.logger.error("ProjectDirectory is not exist or given path to this directory is illegal. ('{}') Please give one ProjectDirectory, which are also exist".format(project_folder))
            return False
    
    main_folders = set_main_folders(project_folder)

    email = configer_obj._user_data['email']
    twitter_creditials = configer_obj._user_data['twitter_creditials']





@main.command('configer')
@click.argument('command1')
@click.argument('command2')
@click.option('--mode', '-m', default="prod")
@click.option('--logdir', '-ld', default="logs")
def configer(command1,command2,  mode,logdir ):
    # $ zas-vot-tools strat1 sets/train_set sets/eval_set  segments voiceless voiced vlwindow vcwindow experiments
    logger = get_cli_logger(mode,logdir)
    #p(command,"command")
    func_name = "configer"
    if command1 not in supported_commands[func_name]:
        logger.error(" Given Command ('{}') is illegal for '{}'. Please use one of the following commands: '{}' ".format(command1,func_name,supported_commands[func_name] ))
        return False
    if command2 not in supported_commands[func_name][command1]:
        logger.error(" Given Command ('{}') is illegal for '{}'->{}. Please use one of the following commands: '{}' ".format(command2,func_name,command1,supported_commands[func_name][command1] ))
        return False

    if command1 == "prjdir":
        if command2 in ["set", "reset"]:
            #p(configer_obj, "configer_obj")
            configer_obj._cli_menu_get_from_user_project_folder()
        elif command2 == "clean":
            if os.isdir(project_folder):
                os.remove(project_folder)
                os.makedirs(project_folder)
            else:
                logger.error("Current ProjectDirectory is not exist.")
                return False
        elif command2 == "print":
            print "ProjectDirectory: '{}'. ".format(project_folder)

    elif command1 == "error_track":
        if command2 in ["set", "reset", "respeak"]:
            configer_obj._cli_menu_error_agreement()
        elif command2 == "print":
            print ">>> Error_tracking: {};".format( configer_obj._user_data["error_tracking"])
    
    elif command1 == "twitter":
        if command2 in ["set", "reset", "respeak"]:
            configer_obj._cli_menu_get_from_user_twitter_credentials()
        elif command2 == "print":
            print ">>> Twitter_creditials: {};".format( configer_obj._user_data["twitter_creditials"])
    

    elif command1 == "email":
        if command2 in ["set", "reset", "respeak"]:
            configer_obj._cli_menu_get_from_user_emails()
        elif command2 == "print":
            print ">>> Email: {};".format( configer_obj._user_data["email"])
    
    
    elif command1 == "user_data":
        if command2 == "clean":
            configer_obj._user_data.clean()
        elif command2 == "location":
            print "ProjectDirectory: '{}'. ".format(project_folder)
            print "ConfigsData: '{}'. ".format(configer_obj._path_to_user_config_data)
        elif command2 == "print":
            #import json
            for cat in configer_obj._user_data:
                print ">>> {}: '{}';".format(cat.upper(), configer_obj._user_data[cat])



### all DB


@main.command('corpora')
@click.argument('command1')
### DB ###
@click.option('--status_bar', '-sb', default=True,type=bool)
@click.option('--end_file_marker', '-efm', default=-1)
@click.option('--use_end_file_marker', '-uefm', default=False,type=bool)
@click.option('--tok_split_camel_case', '-tscc', default=True,type=bool)
@click.option('--make_backup', '-m', default=True,type=bool)
@click.option('--lazyness_border', '-lb', default=100000)
@click.option('--thread_safe', '-ts', default=True,type=bool)
@click.option('--rewrite', '-rw', default=False,type=bool)
@click.option('--stop_if_db_already_exist', '-sidae', default=True,type=bool)
@click.option('--use_cash', '-us', default=False,type=bool)
@click.option('--backup_bevore_first_insert', '-ba', default=True,type=bool)
@click.option('--optimizer', '-opt', default=True,type=bool)
@click.option('--optimizer_page_size', '-optps', default=4096)
@click.option('--optimizer_cache_size', '-optcs', default=1000000)
@click.option('--optimizer_locking_mode', '-optlm', default="EXCLUSIVE") #, type=click.Choice(['md5', 'sha1'])
@click.option('--optimizer_synchronous', '-optsyn', default="OFF")
@click.option('--optimizer_journal_mode', '-optjm', default="MEMORY")
@click.option('--optimizer_temp_store', '-optts', default="MEMORY")
@click.option('--stop_process_if_possible', '-stopproc', default=True,type=bool) # if wrong option was selected, than it stop the process already at the begin, if the error was recognized.


## Corp ####
@click.option('--dbname', '-dbn', default=False)
@click.option('--language', '-lang', default=False)
@click.option('--visibility', '-vis', default=False)
@click.option('--platform_name', '-platf', default=False)
@click.option('--encryption_key', '-encrkey', default=False)
@click.option('--db_file_name', '-dbfn', default=False)
@click.option('--source', '-src', default=False)
@click.option('--license', '-lic', default=False)
@click.option('--template_name', '-templ', default=False)
@click.option('--version', '-ver', default=False)
@click.option('--additional_columns_with_types_for_documents', '-additcols', default=False)
@click.option('--corpus_id_to_init', '-optsyn', default=False)
@click.option('--tokenizer', '-tok', default=True)
@click.option('--pos_tagger', '-ptager', default=False)
@click.option('--sentiment_analyzer', '-sentim', default=False)
@click.option('--sent_splitter', '-sentspl', default=True)
@click.option('--preprocession', '-preproc', default=True,type=bool)
@click.option('--lang_classification', '-langclas', default=False)
@click.option('--del_url', '-durl', default=False,type=bool)
@click.option('--del_punkt', '-dpnkt', default=False,type=bool)
@click.option('--del_num', '-dnum', default=False,type=bool)
@click.option('--del_mention', '-dment', default=False,type=bool)
@click.option('--del_hashtag', '-dhash', default=False,type=bool)
@click.option('--del_html', '-dhtml', default=False,type=bool)
@click.option('--case_sensitiv', '-case', default=False,type=bool)
@click.option('--emojis_normalization', '-emojnorm', default=True,type=bool)
@click.option('--text_field_name', '-texname', default="text")
@click.option('--id_field_name', '-idname', default="id")

## Reader
@click.option('--path_to_read', '-ptr', default=False)
@click.option('--file_format_to_read', '-readtyp', default=False)
@click.option('--reader_regex_template', '-readregextempl', default=False)
@click.option('--reader_regex_for_fname', '-readregexpattern', default=False)
@click.option('--read_from_zip', '-zipread', default=False,type=bool)
@click.option('--reader_formatter_name', '-formatter', default=False)
@click.option('--reader_ignore_retweets', '-retweetsignr', default=True,type=bool)

#@click.option('--dbname', '-checkname', default=False)
#@click.option('--encryption_key', '-encrkeycheck', default=False)
@click.option('--value', '-val', default=False)
@click.option('--attr_name', '-attr', default=False)
@click.option('--type_to_export', '-exptyp', default=False)
@click.option('--export_dir', '-expdir', default=False)
@click.option('--export_name', '-expdir', default=False)


@click.option('--stream_number', '-sn', default=1)

@click.option('--mode', '-m', default="prod+")
@click.option('--logdir', '-ld', default="logs")
def corpora(command1,
            status_bar, end_file_marker, use_end_file_marker, tok_split_camel_case, make_backup, lazyness_border, thread_safe, 
            rewrite, stop_if_db_already_exist, use_cash, backup_bevore_first_insert, optimizer, optimizer_page_size, 
            optimizer_cache_size, optimizer_locking_mode, optimizer_synchronous, optimizer_journal_mode, optimizer_temp_store,stop_process_if_possible,
            
            dbname,language, visibility, platform_name,encryption_key, db_file_name,source,  license, 
            template_name, version,additional_columns_with_types_for_documents,corpus_id_to_init,
            tokenizer, pos_tagger, sentiment_analyzer, sent_splitter, preprocession, lang_classification, del_url, del_punkt, 
            del_num, del_mention, del_hashtag, del_html, case_sensitiv, emojis_normalization, text_field_name, id_field_name, 

            path_to_read, file_format_to_read, reader_regex_template, reader_regex_for_fname, read_from_zip, 
            reader_formatter_name, reader_ignore_retweets,

            stream_number, value, attr_name,type_to_export, export_dir, export_name,

            mode,logdir ):
    # $ zas-vot-tools strat1 sets/train_set sets/eval_set  segments voiceless voiced vlwindow vcwindow experiments
    



    logger = get_cli_logger(mode,logdir)
    func_name = "corpora"
    #p(command,"command")
    if command1 not in supported_commands[func_name]:
        logger.error(" Given Command ('{}') is illegal for '{}'. Please use one of the following commands: '{}' ".format(command1,func_name,supported_commands[func_name] ))
        return False


    if command1 == "add":
        if not strtobool(path_to_read) or not strtobool(file_format_to_read):
            logger.error("ObligatoryMetaDataForReaderMissing: If you want to add new Corpus, you need first give location to the raw text collection, from which than a new corpus will be created and also the file_type of those input text elements. For doing that please use following options: ['path_to_read', 'file_format_to_read']\n For example: 'zas-rep-tools corpora add --path_to_read . --file_format_to_read json'. ")
            return False

        if not strtobool(dbname) or not strtobool(language) or not  strtobool(visibility) or not  strtobool(platform_name):
            logger.error("ObligatoryMetaDataForCorpusMissing: If you want to add new Corpus, you need to set also following obligatory meta data: ['dbname', 'language',  'visibility', 'platform_name']\n For example: 'zas-rep-tools corpora add --dbname streamed --language de  --visibility intern --platform_name twitter'. ")
            return False


        if file_format_to_read == "json":
            if not reader_formatter_name:
                logger.warning("If you want to create TwitterCorpus from JSON, than set following Option:  '--reader_formatter_name twitter'. Otherwise ignore this warning.  ")



        reader = Reader(strtobool(path_to_read), strtobool(file_format_to_read),  regex_template=reader_regex_template,
                        regex_for_fname=reader_regex_for_fname, read_from_zip=read_from_zip,
                        end_file_marker = end_file_marker, send_end_file_marker=use_end_file_marker, stop_process_if_possible=stop_process_if_possible,
                        formatter_name=strtobool(reader_formatter_name), text_field_name = text_field_name, id_field_name=id_field_name,
                        ignore_retweets=reader_ignore_retweets, mode=mode)
        if reader._get_number_of_left_over_files() == 0:
            logger.error("No one file was found in the given path ('{}'). Please check the correctness of the given path or  give other (correct one) path to the text data. If you want to search also in zips, than set following option: '--read_from_zip True'".format(reader._inp_path))
            return False
        corp = Corpus(mode=mode, error_tracking=answer_error_tracking, status_bar=status_bar,
                end_file_marker=end_file_marker, use_end_file_marker=use_end_file_marker, tok_split_camel_case=tok_split_camel_case,
                make_backup=make_backup, lazyness_border=lazyness_border, thread_safe=thread_safe, rewrite=rewrite, stop_if_db_already_exist=stop_if_db_already_exist,
                use_cash=use_cash, backup_bevore_first_insert=backup_bevore_first_insert, optimizer=optimizer,optimizer_page_size=optimizer_page_size, 
                optimizer_cache_size=optimizer_cache_size, optimizer_locking_mode=optimizer_locking_mode, optimizer_synchronous=optimizer_synchronous,
                optimizer_journal_mode=optimizer_journal_mode, optimizer_temp_store=optimizer_temp_store,stop_process_if_possible=stop_process_if_possible)
                
        
        corp.init(main_folders["corp"],  dbname, language,  visibility, platform_name,
                    encryption_key=encryption_key, fileName=db_file_name, source=source, license=license,
                    template_name=strtobool(template_name), version=version, additional_columns_with_types_for_documents=strtobool(additional_columns_with_types_for_documents),
                    corpus_id=strtobool(corpus_id_to_init),
                    tokenizer=strtobool(tokenizer),pos_tagger=strtobool(pos_tagger),sentiment_analyzer=strtobool(sentiment_analyzer),
                    sent_splitter=strtobool(sent_splitter),preprocession=preprocession, lang_classification=strtobool(lang_classification),
                    del_url=del_url,del_punkt=del_punkt,del_num=del_num,del_mention=del_mention,del_hashtag=del_hashtag,del_html=del_html,
                    case_sensitiv=case_sensitiv, emojis_normalization=emojis_normalization,text_field_name=text_field_name,id_field_name=id_field_name)
        
        
        status = corp.insert(reader.getlazy(stream_number=stream_number), text_field_name=text_field_name,  create_def_indexes=True)
        if not status or corp.corpdb.rownum("documents") == 0:
            corp_fname = corp.corpdb.fname()
            #corp.corpdb.commit()
            #import shutil
            
            corp._close()
            os.remove(os.path.join(main_folders["corp"],corp_fname))
            logger.info("InsertionProecess into '{}'-CorpDB is failed. Corpus was deleted.".format(corp_fname))
        else:
            corp.corpdb.commit()
            corp.close()

    elif command1 == "del":
        if not dbname:
            logger.error("'--dbname' is not given. (you can also give tag 'all' instead of the dbname)")
        if dbname == "all":
            #os.remove()
            shutil.rmtree(main_folders["corp"], ignore_errors=True)
            logger.info("All CorpDB was removed.")
        else:
            files = get_corp_dbname(main_folders)
            if dbname in files:
                os.remove(os.path.join(main_folders["corp"], dbname))
                logger.info("'{}'-CorpDB was removed".format(dbname))
            elif dbname in [os.path.splitext(fname)[0] for fname in files]:
                os.remove(os.path.join(main_folders["corp"], dbname)+".db")
                logger.info("'{}'-CorpDB was removed".format(dbname))
            else:
                logger.error("Given fname ('{}') wasn't found and can not be removed.".format(dbname))
                return False

    elif command1 == "names":
        files = get_corp_dbname(main_folders)
        validated,possibly_encrypted,wrong,opened_db = validate_corp_dbname(files)
        print ">>> {} DBs was found <<<  ".format(len(files))
        print " '{}'-From them was validated:".format(len(validated))
        for i, fname in enumerate(validated):
            print "       {}. '{}';".format(i, fname)
        if possibly_encrypted:
            print "\n  '{}'-From them are possibly encrypted or not from the right format:".format(len(possibly_encrypted))
            for i, fname in enumerate(possibly_encrypted):
                print "       {}. '{}';".format(i, fname)

        #p(files)

    elif command1 == "meta":
        if not dbname:
            logger.error("'--dbname' is not given. (you can also give tag 'all' instead of the dbname)")
            return False

        files = get_corp_dbname(main_folders)
        validated,possibly_encrypted,wrong,opened_db = validate_corp_dbname(files)
        if dbname == "all":
            for db in opened_db:
                print("\n >>>> {} <<<<".format(db.fname()))
                for k,v in db.get_all_attr().items():
                    print "    {} = '{}';".format(k,v)


            print "\n\nNotice! with 'all'-Argument could be checked just not-encrypted DBs. If you want to check encrypted DB use additional to dbname also  '--encryption_key'"

        else:
            if dbname in files:
                if dbname in validated:
                    ix = validated.index(dbname)
                    db = opened_db[ix]
                    print("\n >>>> {} <<<<".format(db.fname()))
                    for k,v in db.get_all_attr().items():
                        print "    {} = '{}';".format(k,v)
                elif dbname in possibly_encrypted:
                    if not encryption_key:
                        logger.error("To return MetaData for encrypted DBs '--encryption_key' should be given as option.")
                    else:
                        h = DBHandler(mode="blind")
                        h.connect(os.path.join(main_folders["corp"],dbname),encryption_key=encryption_key)
                        try:
                            if h.typ() == "corpus":
                                print("\n >>>> {} <<<<".format(h.fname()))
                                for k,v in h.get_all_attr().items():
                                    print "    {} = '{}';".format(k,v)
                            else:
                                logger.error("'{}'-DB is not an CorpusDB or given encryption key ('{}') is wrong. ".format(dbname,encryption_key))
                                return False
                        except:
                            logger.error("'{}'-DB wasn't opened. Possibly this DB is damaged or the encryption key was wrong'{}' ".format(dbname,encryption_key))
                            return False
                
            elif dbname in [os.path.splitext(fname)[0] for fname in files]:
                spl1 = [os.path.splitext(fname)[0] for fname in validated]
                spl2 = [os.path.splitext(fname)[0] for fname in possibly_encrypted]
                if dbname in spl1:
                    ix = spl1.index(dbname)
                    db = opened_db[ix]
                    print("\n >>>> {} <<<<".format(db.fname()))
                    for k,v in db.get_all_attr().items():
                        print "    {} = '{}';".format(k,v)
                
                elif dbname in spl2:
                    if not encryption_key:
                        logger.error("To return MetaData for encrypted DBs '--encryption_key' should be given as option.")
                    else:
                        h = DBHandler(mode="blind")
                        h.connect(os.path.join(main_folders["corp"],dbname)+".db",encryption_key=encryption_key)
                        try:
                            if h.typ() == "corpus":
                                print("\n >>>> {} <<<<".format(h.fname()))
                                for k,v in h.get_all_attr().items():
                                    print "    {} = '{}';".format(k,v)
                            else:
                                logger.error("'{}'-DB is not an CorpusDB or given encryption key ('{}') is wrong. ".format(dbname,encryption_key))
                                return False
                        except:
                            logger.error("'{}'-DB wasn't opened. Possibly this DB is damaged or the encryption key was wrong'{}' ".format(dbname,encryption_key))
                            return False


                else:
                    logger.error("Given fname ('{}') wasn't validated. It means, that possibly it is not a CorpusDB or it is just encrypted!".format(dbname))
                    return False
            else:
                logger.error("Given fname ('{}') wasn't found!".format(dbname))
                return False


    elif command1 == "basic_stats":
        if not dbname:
            logger.error("'--dbname' is not given. (you can also give tag 'all' instead of the dbname)")
            return False

        files = get_corp_dbname(main_folders)
        validated,possibly_encrypted,wrong,opened_db = validate_corp_dbname(files)
        if dbname == "all":
            for db in opened_db:
                print("\n >>>> {} <<<<".format(db.fname()))
                print "    doc_num = '{}';".format(db.get_attr("doc_num"))
                print "    sent_num = '{}';".format(db.get_attr("sent_num"))
                print "    token_num = '{}';".format(db.get_attr("token_num"))

            print "\n\nNotice! with 'all'-Argument could be checked just not-encrypted DBs. If you want to check encrypted DB use additional to dbname also  '--encryption_key'"

        else:
            if dbname in files:
                if dbname in validated:
                    ix = validated.index(dbname)
                    db = opened_db[ix]
                    print("\n >>>> {} <<<<".format(db.fname()))
                    print "    doc_num = '{}';".format(db.get_attr("doc_num"))
                    print "    sent_num = '{}';".format(db.get_attr("sent_num"))
                    print "    token_num = '{}';".format(db.get_attr("token_num"))
                elif dbname in possibly_encrypted:
                    if not encryption_key:
                        logger.error("To return MetaData for encrypted DBs '--encryption_key' should be given as option.")
                    else:
                        h = DBHandler(mode="blind")
                        h.connect(os.path.join(main_folders["corp"],dbname),encryption_key=encryption_key)
                        try:
                            if h.typ() == "corpus":
                                print("\n >>>> {} <<<<".format(h.fname()))
                                print "    doc_num = '{}';".format(h.get_attr("doc_num"))
                                print "    sent_num = '{}';".format(h.get_attr("sent_num"))
                                print "    token_num = '{}';".format(h.get_attr("token_num"))
                            else:
                                logger.error("'{}'-DB is not an CorpusDB or given encryption key ('{}') is wrong. ".format(dbname,encryption_key))
                                return False
                        except:
                            logger.error("'{}'-DB wasn't opened. Possibly this DB is damaged or the encryption key was wrong'{}' ".format(dbname,encryption_key))
                            return False
                
            elif dbname in [os.path.splitext(fname)[0] for fname in files]:
                spl1 = [os.path.splitext(fname)[0] for fname in validated]
                spl2 = [os.path.splitext(fname)[0] for fname in possibly_encrypted]
                if dbname in spl1:
                    ix = spl1.index(dbname)
                    db = opened_db[ix]
                    print("\n >>>> {} <<<<".format(db.fname()))
                    print "    doc_num = '{}';".format(db.get_attr("doc_num"))
                    print "    sent_num = '{}';".format(db.get_attr("sent_num"))
                    print "    token_num = '{}';".format(db.get_attr("token_num"))
                
                elif dbname in spl2:
                    if not encryption_key:
                        logger.error("To return MetaData for encrypted DBs '--encryption_key' should be given as option.")
                    else:
                        h = DBHandler(mode="blind")
                        h.connect(os.path.join(main_folders["corp"],dbname)+".db",encryption_key=encryption_key)
                        try:
                            if h.typ() == "corpus":
                                print("\n >>>> {} <<<<".format(h.fname()))
                                print "    doc_num = '{}';".format(h.get_attr("doc_num"))
                                print "    sent_num = '{}';".format(h.get_attr("sent_num"))
                                print "    token_num = '{}';".format(h.get_attr("token_num"))
                            else:
                                logger.error("'{}'-DB is not an CorpusDB or given encryption key ('{}') is wrong. ".format(dbname,encryption_key))
                                return False
                        except:
                            logger.error("'{}'-DB wasn't opened. Possibly this DB is damaged or the encryption key was wrong'{}' ".format(dbname,encryption_key))
                            return False


                else:
                    logger.error("Given fname ('{}') wasn't validated. It means, that possibly it is not a CorpusDB or it is just encrypted!".format(dbname))
                    return False
            else:
                logger.error("Given fname ('{}') wasn't found!".format(dbname))
                return False


    elif command1 == "update_attr":
        if not dbname or  not attr_name or not value:
            logger.error("Command is incomplete: '--dbname' or '--attr_name' or '--value' is not given.")
        else:
            files = get_corp_dbname(main_folders)
            if dbname in files:
                pass
            elif dbname in [os.path.splitext(fname)[0] for fname in files]:
                dbname = dbname+".db"
            else:
                logger.error("Given fname ('{}') wasn't found and can not be removed.".format(dbname))
                return False
            
            try:
                db = DBHandler(mode="error")
                db.connect(os.path.join(main_folders["corp"],dbname),encryption_key=encryption_key)
                if db._db:
                    if db.typ() == "corpus":
                        if attr_name not in db.get_all_attr():
                            logger.error("Given Attribute ('{}') is not exist in this DataBase.".format(attr_name))
                            return False

                        db.update_attr(attr_name,value)
                        db._commit()
                        updated_attr = db.get_attr(attr_name)
                        #p((updated_attr, value))
                        if str(value) != str(updated_attr):
                            logger.error("Update of the given Attribute ('{}') failed.".format(attr_name))
                            return 
                        else:
                            logger.info("Given Attribute ('{}') in the '{}'-DB was updated to '{}'.".format(attr_name,dbname, value))
                            return True
                    else:
                        logger.error("'{}'-DB is not an CorpusDB or given encryption key ('{}') is wrong. ".format(dbname,encryption_key))
                        return False
                else:
                    #p(type(strtobool(encryption_key)), "strtobool(encryption_key)")
                    if strtobool(encryption_key):
                        logger.error("'{}'-DB wasn't opened. Possibly this DB is damaged or the encryption key was wrong'{}' ".format(dbname,encryption_key))
                    else:
                        logger.error("'{}'-DB wasn't opened. Possibly this DB is damaged or is encrypted. Please use '--encryption_key' option to set an encryption_key ".format(dbname,encryption_key))
                    return False
            except:
                if strtobool(encryption_key):
                    logger.error("'{}'-DB wasn't opened. Possibly this DB is damaged or the encryption key was wrong'{}' ".format(dbname,encryption_key))
                else:
                    logger.error("'{}'-DB wasn't opened. Possibly this DB is damaged or is encrypted. Please use '--encryption_key' option to set an encryption_key ".format(dbname,encryption_key))
                return False

    elif command1 == "export":
        if not dbname or  not type_to_export or not export_dir or not export_name:
            logger.error("Command is incomplete:   '--dbname' or '--type_to_export' or '--export_dir' or '--export_name' is not given.")
        else:
            files = get_corp_dbname(main_folders)

            if dbname in files:
                pass
            elif dbname in [os.path.splitext(fname)[0] for fname in files]:
                dbname = dbname+".db"
            else:
                logger.error("Given fname ('{}') wasn't found and can not be removed.".format(dbname))
                return False

            corp = Corpus(mode="error")
            corp.open(os.path.join(main_folders["corp"],dbname),encryption_key=encryption_key)

            def intern_getter():
                if status_bar:
                    status_bars_manager = _get_status_bars_manager()
                    status_bar_start = _get_new_status_bar(None, status_bars_manager.term.center("Exporter") , "", counter_format=status_bars_manager.term.bold_white_on_green("{fill}{desc}{fill}"),status_bars_manager=status_bars_manager)
                    status_bar_start.refresh()
                #if status_bar:
                    status_bar_current = _get_new_status_bar(num, "Exporting:", "row",status_bars_manager=status_bars_manager)
                
                for item in corp.docs(output="dict"):
                    if status_bar:
                        status_bar_current.update(incr=1)
                    yield item

                if status_bar:
                    status_bar_total_summary = _get_new_status_bar(None, status_bars_manager.term.center("Exported:  Rows: '{}'; ".format(num) ), "",  counter_format=status_bars_manager.term.bold_white_on_green('{fill}{desc}{fill}\n'),status_bars_manager=status_bars_manager)
                    status_bar_total_summary.refresh()
                    status_bars_manager.stop()


            if corp.corpdb._db:
                num = corp.corpdb.rownum("documents")
                exporter = Exporter(intern_getter(),rewrite=False,silent_ignore=False , mode="error")
                if type_to_export not in Exporter.supported_file_formats:
                    logger.error("Given Export Type ('{}') is not supported.".format(type_to_export))
                    return False
 
                if type_to_export == "csv":
                    #p(cols,"cols")
                    cols = corp.corpdb.col("documents")
                    exporter.tocsv(export_dir, export_name, cols)
                elif type_to_export == "xml":
                    exporter.toxml(export_dir, export_name)
                elif type_to_export == "json":
                    exporter.tojson(export_dir, export_name)
                else:
                    logger.error("Given Export Type ('{}') is not supported.".format(type_to_export))
                    return False


            else:
                #p(type(strtobool(encryption_key)), "strtobool(encryption_key)")
                if strtobool(encryption_key):
                    logger.error("'{}'-DB wasn't opened. Possibly this DB is damaged or given  encryption key ('{}') is wrong. ".format(dbname,encryption_key))
                else:
                    logger.error("'{}'-DB wasn't opened. Possibly this DB is damaged or is encrypted. Please use '--encryption_key' option to set an encryption_key ".format(dbname,encryption_key))
                return False


    elif command1 == "used_tools":
        term = Terminal()
        for tool_name, data in CorpusData.info.items():
            print "\n\n\n\n"
            print term.bold_white_on_magenta("   >>>>>  {}  <<<<< ".format(tool_name))
            if tool_name == "tagger":
                for tagger_name, infos in data.items():
                    print term.bold_white_on_cyan("      TaggerName:  {}  ".format(tagger_name))
                    print "\t\t"+json.dumps(CorpusData.info[tool_name][tagger_name], sort_keys=True, indent=5).replace("\n", "\n\t")
                    print "\n\n"
            else:
                print "\t"+json.dumps(CorpusData.info[tool_name], sort_keys=True, indent=5).replace("\n", "\n\t")







@main.command('stats')
@click.argument('command1')
@click.option('--status_bar', '-sb', default=True,type=bool)
@click.option('--end_file_marker', '-efm', default=-1)
@click.option('--use_end_file_marker', '-uefm', default=False,type=bool)
@click.option('--tok_split_camel_case', '-tscc', default=True,type=bool)
@click.option('--make_backup', '-m', default=True,type=bool)
@click.option('--lazyness_border', '-lb', default=100000)
@click.option('--thread_safe', '-ts', default=True,type=bool)
@click.option('--rewrite', '-rw', default=False,type=bool)
@click.option('--stop_if_db_already_exist', '-sidae', default=False,type=bool)
@click.option('--use_cash', '-us', default=False,type=bool)
@click.option('--backup_bevore_first_insert', '-ba', default=True,type=bool)
@click.option('--optimizer', '-opt', default=True,type=bool)
@click.option('--optimizer_page_size', '-optps', default=4096)
@click.option('--optimizer_cache_size', '-optcs', default=1000000)
@click.option('--optimizer_locking_mode', '-optlm', default="EXCLUSIVE")
@click.option('--optimizer_synchronous', '-optsyn', default="OFF")
@click.option('--optimizer_journal_mode', '-optjm', default="MEMORY")
@click.option('--optimizer_temp_store', '-optts', default="MEMORY")
@click.option('--stop_process_if_possible', '-stopproc', default=True,type=bool) # if wrong option was selected, than it stop the process already at the begin, if the error was recognized.



@click.option('--mode', '-m', default="prod-")
@click.option('--logdir', '-ld', default="logs")
def stats(command1,
            status_bar, end_file_marker, use_end_file_marker, tok_split_camel_case, make_backup, lazyness_border, thread_safe, 
            rewrite, stop_if_db_already_exist, use_cash, backup_bevore_first_insert, optimizer, optimizer_page_size, 
            optimizer_cache_size, optimizer_locking_mode, optimizer_synchronous, optimizer_journal_mode, optimizer_temp_store,
            stop_process_if_possible,
            mode,logdir ):
    # $ zas-vot-tools strat1 sets/train_set sets/eval_set  segments voiceless voiced vlwindow vcwindow experiments
    logger = get_cli_logger(mode,logdir)
    func_name = "stats"
    #p(command,"command")
    if command1 not in supported_commands[func_name]:
        logger.error(" Given Command ('{}') is illegal for '{}'. Please use one of the following commands: '{}' ".format(command1,func_name,supported_commands[func_name] ))
        return False


    if command1 == "add":
        pass
        # Stats(error_tracking=answer_error_tracking, status_bar=status_bar,
        #         end_file_marker=end_file_marker, use_end_file_marker=use_end_file_marker, tok_split_camel_case=tok_split_camel_case,
        #         make_backup=make_backup,  lazyness_border=lazyness_border, thread_safe=thread_safe, rewrite=rewrite, stop_if_db_already_exist=stop_if_db_already_exist,
        #         use_cash=use_cash, backup_bevore_first_insert=backup_bevore_first_insert, optimizer=optimizer,optimizer_page_size=optimizer_page_size, 
        #         optimizer_cache_size=optimizer_cache_size, optimizer_locking_mode=optimizer_locking_mode, optimizer_synchronous=optimizer_synchronous,
        #         optimizer_journal_mode=optimizer_journal_mode, optimizer_temp_store=optimizer_temp_store, )


    elif command1 == "del":
        pass

    elif command1 == "names":
        pass

    elif command1 == "meta":
        pass

    elif command1 == "attr":
        pass

    elif command1 == "export":
        pass







@main.command('streamTwitter')
@click.argument('path_to_save',type=click.Path())
@click.option('--language', '-l', default=False, type=click.Choice(list(Streamer.supported_languages)+ [False,"False", "false"]))
@click.option('--stop_words', '-sw', default=False)
@click.option('--terms', '-t', default=False)
@click.option('--encoding', '-e', default='utf_8', type=click.Choice(list(Streamer.supported_encodings_types)))
@click.option('--ignore_rt', '-irt', default=False, type=bool)
@click.option('--filter_strategie', '-f', default=False, type=click.Choice(list(["t", "t+l", "False", False, "false"])))
@click.option('--save_used_terms', '-sut', default=True, type=bool)
@click.option('--logs_dir', '-ld', default="logs")
@click.option('--use_logger_for_classes', '-lc', default=True,type=bool)
@click.option('--use_logger_for_script', '-ls', default=True,type=bool)
@click.option('--save_logs', '-sl', default=True,type=bool)
@click.option('--logger_level', '-ll', default=logging.INFO)
#@click.option('--logs_dir', '-l', default="logs")
def streamTwitter( path_to_save,language,stop_words,terms,encoding,ignore_rt, filter_strategie, save_used_terms, logs_dir, use_logger_for_classes, use_logger_for_script, save_logs, logger_level):
    # $ zas-vot-tools strat1 sets/train_set sets/eval_set  segments voiceless voiced vlwindow vcwindow experiments
    #logger = logger_initialisation("streamTwitter" ,use_logger_for_script, save_logs, logs_dir)
    this_function_name = sys._getframe().f_code.co_name
    logger = main_logger(this_function_name, level=logger_level, folder_for_log=logs_dir, use_logger=use_logger_for_script, save_logs=save_logs)
    #p(list(Streamer.supported_languages)+ [False,"False"])
    #p(type(ignore_rt))
    #ignore_rt = bool(ignore_rt)
    #save_used_terms = bool(save_used_terms)

    if not  was_user_asked_for_path_to_file_with_twitter_creditials():
        consumer_key, consumer_secret, access_token, access_token_secret  = ask_user_for_twitter_api_data()
    else:
        consumer_key, consumer_secret, access_token, access_token_secret = get_api_data()

    #p(get_api_data())
    #p(agreement_data['email'])


    if stop_words and  not os.path.isfile(stop_words):
        if stop_words not in Streamer.stop_words_collection:
            stop_words = stop_words.split(",")
            logger.info("Recognized stop-words: {}".format(stop_words))

    if terms and not os.path.isfile(terms):
        terms = terms.split(",")
        logger.info("Recognized terms: {}".format(terms))


    stream = Streamer(consumer_key, consumer_secret, access_token, access_token_secret, path_to_save, platfrom="twitter",
                    language=language, email_addresse=email, stop_words=stop_words, terms=terms,
                    encoding=encoding, ignore_rt=ignore_rt, save_used_terms=save_used_terms, filterStrat=filter_strategie,
                    logger_level=logger_level, logger_usage=use_logger_for_classes, logger_save_logs= save_logs)
    stream.stream_twitter()




@main.command('streamerInfo')
@click.argument('command')
@click.option('--logs_dir', '-ld', default="logs")
@click.option('--use_logger_for_classes', '-lc', default=True)
@click.option('--use_logger_for_script', '-ls', default=True)
@click.option('--save_logs', '-sl', default=True)
#@click.option('--logs_dir', '-l', default="logs")
def streamerInfo(command, logs_dir, use_logger_for_classes, use_logger_for_script, save_logs):
    # $ zas-vot-tools strat1 sets/train_set sets/eval_set  segments voiceless voiced vlwindow vcwindow experiments
    logger = logger_initialisation("streamerInfo" ,use_logger_for_script, save_logs, logs_dir)
    possible_commands = ["enc", "lang", "nltk_lang", "twitter_lang", "classiefier_lang", "stop_words", "platforms"]


    if command not in possible_commands:
        logger.error("Given Command {} is not exist. Please use one of the following commands: {}".format(command, possible_commands))
 
    if command == "enc":
        print Streamer.supported_encodings_types

    if command == "lang":
        print Streamer.supported_languages

    if command == "nltk_lang":
        print [k for k in Streamer.NLTKlanguages] 

    if command == "twitter_lang":
        print Streamer.supported_languages_by_twitter

    if command == "classiefier_lang":
        print Streamer.supported_languages_by_langid

    if command == "stop_words":
        print Streamer.supported_stop_words



    if command == "platforms":
        print Streamer.supported_platforms


    #print Streamer.supported_encodings_types


# @main.command('retypeTwitterData')
# @click.option('--logs_dir', '-l', default="logs")
# @click.option('--use_logger_for_classes', '-lc', default=True)
# @click.option('--use_logger_for_script', '-ls', default=True)
# @click.option('--save_logs', '-sl', default=True)
# #@click.option('--logs_dir', '-l', default="logs")
# def retypeTwitterData( logs_dir, use_logger_for_classes, use_logger_for_script, save_logs):
#     # $ zas-vot-tools strat1 sets/train_set sets/eval_set  segments voiceless voiced vlwindow vcwindow experiments
#     logger = logger_initialisation("streamTwitter" ,use_logger_for_script, save_logs, logs_dir)


#     ask_user_for_twitter_api_data()



# @main.command('deleteAllUserData')
# @click.option('--logs_dir', '-l', default="logs")
# @click.option('--use_logger_for_classes', '-lc', default=True)
# @click.option('--use_logger_for_script', '-ls', default=True)
# @click.option('--save_logs', '-sl', default=True)
# #@click.option('--logs_dir', '-l', default="logs")
# def deleteAllUserData( logs_dir, use_logger_for_classes, use_logger_for_script, save_logs):
#     # $ zas-vot-tools strat1 sets/train_set sets/eval_set  segments voiceless voiced vlwindow vcwindow experiments
#     logger = logger_initialisation("streamTwitter" ,use_logger_for_script, save_logs, logs_dir)


#     path_to_zas_rep_tools = os.path.dirname(os.path.dirname(os.path.dirname(inspect.getfile(Streamer))))
#     shutil.rmtree(os.path.join(path_to_zas_rep_tools, "user-config"), ignore_errors=True)


# @main.command('respeakAgreement')
# @click.option('--logs_dir', '-l', default="logs")
# @click.option('--use_logger_for_classes', '-lc', default=True)
# @click.option('--use_logger_for_script', '-ls', default=True)
# @click.option('--save_logs', '-sl', default=True)
# #@click.option('--logs_dir', '-l', default="logs")
# def respeakAgreement( logs_dir, use_logger_for_classes, use_logger_for_script, save_logs):
#     # $ zas-vot-tools strat1 sets/train_set sets/eval_set  segments voiceless voiced vlwindow vcwindow experiments
#     logger = logger_initialisation("streamTwitter" ,use_logger_for_script, save_logs, logs_dir)
#     print "\nRespeaking-Process was started:\n\n"
#     respeak_agreement()

#     #path_to_zas_rep_tools = os.path.dirname(os.path.dirname(os.path.dirname(inspect.getfile(Streamer))))
#     #shutil.rmtree(os.path.join(path_to_zas_rep_tools, "user-config"), ignore_errors=True)






if __name__ == "__main__":
    main()
