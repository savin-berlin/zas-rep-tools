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

from zas_rep_tools.src.utils.logger import main_logger
from zas_rep_tools.src.utils.cli_helper import *
from zas_rep_tools.src.classes.reader import  Reader
from zas_rep_tools.src.classes.dbhandler import DBHandler
from zas_rep_tools.src.classes.streamer import Streamer
from zas_rep_tools.src.utils.debugger import p



@click.group()
def main():
    ### agreement
    if not  was_user_asked_for_agreement():
        ask_user_agreement()

    global agreement_data
    agreement_data = get_agreement_data()

    answer_error_tracking = is_error_tracking_allowed()


    #### projects folder
    if not  was_user_asked_for_path_to_projects_folder():
        ask_user_for_projects_folder()


    global db_settings
    db_settings = get_db_settings()


    ### error-tracking
    answer_error_tracking = is_error_tracking_allowed()





@main.command('implemented')
@click.argument('corpus_name')
@click.argument('rep_type') #["rep","red","repinred"]
@click.argument('search_type') # ["exact", "explor"]
@click.option('--case_sensitiv', '-ca', default=True)
@click.option('--context', '-co', default=0)
@click.option('--context_left', '-co', default=0)
@click.option('--context_right', '-co', default=0)
@click.option('--scopus', '-s', default=0)
@click.option('--refer', '-r', default=[])
@click.option('--logs_dir', '-l', default="logs")
@click.option('--use_logger_for_classes', '-lc', default=True)
@click.option('--use_logger_for_script', '-ls', default=True)
@click.option('--save_logs', '-sl', default=True)
#@click.option('--logs_dir', '-l', default="logs")
def implemented(corpus_name, rep_type, search_type, case_sensitiv, context, context_left, context_right, scopus, refer,
            logs_dir, use_logger_for_classes, use_logger_for_script, save_logs):
    # $ zas-vot-tools strat1 sets/train_set sets/eval_set  segments voiceless voiced vlwindow vcwindow experiments
    logger = logger_initialisation("implemented" ,use_logger_for_script, save_logs, logs_dir)



@main.command('test')
@click.argument('path')
@click.option('--logs_dir', '-l', default="logs")
@click.option('--use_logger_for_classes', '-lc', default=True)
@click.option('--use_logger_for_script', '-ls', default=True)
@click.option('--save_logs', '-sl', default=True)
#@click.option('--logs_dir', '-l', default="logs")
def test(path, logs_dir, use_logger_for_classes, use_logger_for_script, save_logs):
    # $ zas-vot-tools strat1 sets/train_set sets/eval_set  segments voiceless voiced vlwindow vcwindow experiments
    logger = logger_initialisation("to_implement" ,use_logger_for_script, save_logs, logs_dir)
    #db = DB(developingMode = True)
    db = DB()
    #p(path)
    #db.init_corpus(path, "twitter_streamed_de", "de", "twitter", "intern")
    db.connect(path)

    # db.insert_row("documents", [u'docs_id', u'text'], ["1","hjk"])
    # db.insert_row("documents", [u'docs_id', u'text'], ["2","hjk"])
    # db.insert_row("documents", [u'docs_id', u'text'], ["3","hjk"])
    # db.insert_row("documents", [u'docs_id', u'text'], ["4","hjk"])
    # db.insert_row("documents", [u'docs_id', u'text'], ["5","hjk"])
    # db.insert_row("documents", [u'docs_id', u'text'], ["6","hjk"])



    for item in db.lazy_getter("documents", size_to_get=4):
        p(item)
    #db.getone("documents")
    db.commit()

    # for item in db.lazy_getter("documents"):
    #     p(item)



@main.command('to_implement')
@click.argument('corpus_name')
@click.argument('rep_type') #["rep","red","repinred"]
@click.argument('search_type') # ["exact", "explor"]
@click.option('--case', '-ca', default="senstitiv")
@click.option('--context', '-co', default=0)
@click.option('--context_left', '-co', default=0)
@click.option('--context_right', '-co', default=0)
@click.option('--scopus', '-s', default=0)
@click.option('--refer', '-r', default=[])
@click.option('--logs_dir', '-l', default="logs")
@click.option('--use_logger_for_classes', '-lc', default=True)
@click.option('--use_logger_for_script', '-ls', default=True)
@click.option('--save_logs', '-sl', default=True)
#@click.option('--logs_dir', '-l', default="logs")
def to_implement(corpus_name, rep_type, search_type, case, context, context_left, context_right, scopus, refer,
            logs_dir, use_logger_for_classes, use_logger_for_script, save_logs):
    # $ zas-vot-tools strat1 sets/train_set sets/eval_set  segments voiceless voiced vlwindow vcwindow experiments
    logger = logger_initialisation("to_implement" ,use_logger_for_script, save_logs, logs_dir)


    ################################
    ######### New IDEAS #############

    # Step 1: Initialisation 
    ## platforms
    configs = Configer()
    configs.addPlatform(name)


    ## templates
    configs.addTemplate(name, columns)
    configs.save(path_to_configs)


    #Open other configs
    configs = Configer(path_to_configs)
    configs.templates()
    configs.platforms()





    #Step 2: Add or Import Corpus

    reader = Reader(path_to_files, file_format)

    #Initialize new one
    corpus = Corpus()
    corpus.init(name, plattform_name, template_name, version, language, source, typ)
    stats = stats.init(name, version, language, typ)
    #corpus.saveOnDisc(path) 
    corpus.commit()
    corpus.export() 
    corpus.insert(reader, statsDB=stats) # use reader on stream 

    configs.addCorpus(corpus) 


    #Open/Import
    corpus = Corpus()
    corpus.open(path_to_corpDB) 

    if corpus.id not in configs.corporaIDs:
        configs.addCorpus(name,path,corpus_id)






    #Step 3: (Re-) Compute or Import Statistics
    stats = Stats(name, corpus_id)


    if stats.id not in configs.statsIDs:
        configs.addStats(name,path,corpus_id, stats_id)








    #Step 4: Get needed Stats
    getted_stats = stats.repl(search_pattern="['very','tiny'] or False", context="5|0", interpunktion="True|False",case="lower|senstitiv",meta_data="True|False") #if search_pattern is False then give all data
    getted_stats = stats.redu(search_pattern="['very','tiny'] or False", context="5|0", interpunktion="True|False",case="lower|senstitiv",meta_data="True|False")
    getted_stats = stats.replINredu()


    export = StatsExporter(getted_stats)
    export.csv(path_to_save)


    #Step 5: Additional
    #Info about
        # added Corpora
        # computed Stats
        # added templates 
        # added platforms
        # 
    # Delete
        # Stats
        # Corpus
        # Clean project Folder
        # user config 
    # Export Corpus into other DATAFORMAT
    # COnvert Corpus into other DATAFORMAT (NOT!!! if time will available)








    ################################
    ################################
    #old IDEAS########
    db = DB("path_to")
    db.connect()

    db.tables()
    db.templates()
    db.corpora()
    db.stats()
    #db.baseline()
    #db.documents()



    db.add_template()
    db.add_corp(pfad_to_corp, name_of_template)
    db.del_corp(corp_name)



    # Stats
    db.compute_stats(corpus_name,name, context_size=3)
    db.del_stats()
    db.get_baselines(stats_name)
    db.get_stats(stats_name, typ="repl|redu", scopus=2, case="lower|sensitiv", pattern=[('very','much'),('kind','of')], context_size=3)




    # EXPORT
    db.export_corpus(corpus_name, output_type="JSON|XML|CSV|TXT")
    db.export_stats(stats_name, output_type="JSON|XML|CSV|TXT")









@main.command('findRep')
@click.argument('corpus_name')
@click.argument('rep_type') #["rep","red","repinred"]
@click.argument('search_type') # ["exact", "explor"]
@click.option('--case', '-ca', default="senstitiv")
@click.option('--context', '-co', default=0)
@click.option('--context_left', '-co', default=0)
@click.option('--context_right', '-co', default=0)
@click.option('--scopus', '-s', default=0)
@click.option('--refer', '-r', default=[])
@click.option('--logs_dir', '-l', default="logs")
@click.option('--use_logger_for_classes', '-lc', default=True)
@click.option('--use_logger_for_script', '-ls', default=True)
@click.option('--save_logs', '-sl', default=True)
#@click.option('--logs_dir', '-l', default="logs")
def findRep(corpus_name, rep_type, search_type, case, context, context_left, context_right, scopus, refer,
            logs_dir, use_logger_for_classes, use_logger_for_script, save_logs):
    # $ zas-vot-tools strat1 sets/train_set sets/eval_set  segments voiceless voiced vlwindow vcwindow experiments
    logger = logger_initialisation("findRep" ,use_logger_for_script, save_logs, logs_dir)

    if not is_project_folder_still_exist():
        sys.exit()






@main.command('extractRep')
@click.argument('corpus_name')
@click.argument('rep_type') #["rep","red","repinred"]
@click.argument('output_file_name') #["rep","red","repinred"]
@click.option('--output_file_format', '-f', default=False)
@click.option('--stats_name', '-s', default=False)
@click.option('--stats_version', '-s', default=False)
@click.option('--case_sensitiv', '-cs', default=False)
@click.option('--search_pattern', '-p', default=False)
@click.option('--meta_data', '-md', default=False)
@click.option('--linguistic_data', '-ld', default=False)
@click.option('--context', '-c', default=False)
@click.option('--scope', '-c', default="*")
@click.option('--baseline', '-b', default=True)
@click.option('--syntagma_delimiter', '-sd', default=":")
@click.option('--paradima_delimiter', '-pd', default=",")
def extractRep(corpus_name, rep_type, output_file_name, output_file_format,stats_name, stats_version, case_sensitiv, search_pattern,meta_data,linguistic_data,context, scope,baseline, syntagma_delimiter, paradima_delimiter):
    '''
    syntagma_delimiter = ":"
    paradima_delimiter = ","
    '''
    if corpus_need(rep_type, case_sensitiv, context, scope):
        if corpus_name not in Configer.corpora():
            self.logger.error("Given CorpusName '{}' is not exist".format(corpus_name))
        corp = Configer.get_corp(corpus_name)

    stats = Configer.get_stats(corpus_name, stats_name, stats_version)

    splitted_rep_type = rep_type.split("+")
    repl = True if "repl" in splitted_rep_type else False
    redu = True if "redu" in splitted_rep_type else False
    if search_pattern:
        splitted_search_pattern_syntagma = search_pattern.split(syntagma_delimiter)
        splitted_search_pattern_paradigma = [syntagma.split(paradima_delimiter) for syntagma in splitted_search_pattern_syntagma]
    scope = len(splitted_search_pattern_paradigma) if search_pattern else scope
    splitted_context = context.split(syntagma_delimiter)
    if len(splitted_context) > 2:
        self.logger.error("Context expression can have max two borders. '{}'-borders are given. Check '{}'. ".format(len(splitted_context), splitted_context))
    context_left=splitted_context[0] if len(splitted_context)==2 else splitted_context[0]
    context_right = splitted_context[1] if len(splitted_context)==2 else splitted_context[0]
    
    if meta_data:
        splitted_meta_data = meta_data.split(paradima_delimiter)

    if linguistic_data:
        splitted_linguistic_data = linguistic_data.split(paradima_delimiter)

    stats.export(output_file_name, output_file_format=output_file_format,baseline=baseline, repl=repl, redu=redu, search_pattern=splitted_search_pattern_paradigma, scope=scope, context_left=context_left, context_right=context_right, meta_data=splitted_meta_data, linguistic_data=splitted_linguistic_data)






@main.command('addCorp')
@click.argument('paths_to_corp', nargs=-1, type=click.Path())
@click.argument('corpus_name')
@click.argument('corpus_language')
@click.argument('corpus_ordninance') # ["documents","categories"] 
@click.option('--main_cat', '-mc', default=None)
@click.option('--logs_dir', '-l', default="logs")
@click.option('--use_logger_for_classes', '-lc', default=True)
@click.option('--use_logger_for_script', '-ls', default=True)
@click.option('--save_logs', '-sl', default=True)
#@click.option('--logs_dir', '-l', default="logs")
def addCorp(paths_to_corp, corpus_name, corpus_language, corpus_ordninance, main_cat,
            logs_dir, use_logger_for_classes, use_logger_for_script, save_logs):
    # $ zas-vot-tools strat1 sets/train_set sets/eval_set  segments voiceless voiced vlwindow vcwindow experiments
    logger = logger_initialisation("addCorp" ,use_logger_for_script, save_logs, logs_dir)

    if not is_project_folder_still_exist():
        sys.exit()


@main.command('encodings')
def encodings():
    # $ zas-vot-tools strat1 sets/train_set sets/eval_set  segments voiceless voiced vlwindow vcwindow experiments
    #logger = logger_initialisation("encodings" ,use_logger_for_script, save_logs, logs_dir)
    print Reader.supported_encodings_types




@main.command('delCorp')
@click.argument('corpus_name')
@click.option('--logs_dir', '-l', default="logs")
@click.option('--use_logger_for_classes', '-lc', default=True)
@click.option('--use_logger_for_script', '-ls', default=True)
@click.option('--save_logs', '-sl', default=True)
#@click.option('--logs_dir', '-l', default="logs")
def delCorp(corpus_name, logs_dir, use_logger_for_classes, use_logger_for_script, save_logs):
    # $ zas-vot-tools strat1 sets/train_set sets/eval_set  segments voiceless voiced vlwindow vcwindow experiments
    logger = logger_initialisation("delCorp" ,use_logger_for_script, save_logs, logs_dir)

    if not is_project_folder_still_exist():
        sys.exit()



@main.command('corpInfo')
@click.option('--corpname', '-n', default=None)
@click.option('--logs_dir', '-l', default="logs")
@click.option('--use_logger_for_classes', '-lc', default=True)
@click.option('--use_logger_for_script', '-ls', default=True)
@click.option('--save_logs', '-sl', default=True)
#@click.option('--logs_dir', '-l', default="logs")
def corpInfo(corpname, logs_dir, use_logger_for_classes, use_logger_for_script, save_logs):
    # $ zas-vot-tools strat1 sets/train_set sets/eval_set  segments voiceless voiced vlwindow vcwindow experiments
    logger = logger_initialisation("corpInfo" ,use_logger_for_script, save_logs, logs_dir)

    if not is_project_folder_still_exist():
        sys.exit()




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
                    language=language, email_addresse=agreement_data['email'], stop_words=stop_words, terms=terms,
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


@main.command('retypeTwitterData')
@click.option('--logs_dir', '-l', default="logs")
@click.option('--use_logger_for_classes', '-lc', default=True)
@click.option('--use_logger_for_script', '-ls', default=True)
@click.option('--save_logs', '-sl', default=True)
#@click.option('--logs_dir', '-l', default="logs")
def retypeTwitterData( logs_dir, use_logger_for_classes, use_logger_for_script, save_logs):
    # $ zas-vot-tools strat1 sets/train_set sets/eval_set  segments voiceless voiced vlwindow vcwindow experiments
    logger = logger_initialisation("streamTwitter" ,use_logger_for_script, save_logs, logs_dir)


    ask_user_for_twitter_api_data()



@main.command('deleteAllUserData')
@click.option('--logs_dir', '-l', default="logs")
@click.option('--use_logger_for_classes', '-lc', default=True)
@click.option('--use_logger_for_script', '-ls', default=True)
@click.option('--save_logs', '-sl', default=True)
#@click.option('--logs_dir', '-l', default="logs")
def deleteAllUserData( logs_dir, use_logger_for_classes, use_logger_for_script, save_logs):
    # $ zas-vot-tools strat1 sets/train_set sets/eval_set  segments voiceless voiced vlwindow vcwindow experiments
    logger = logger_initialisation("streamTwitter" ,use_logger_for_script, save_logs, logs_dir)


    path_to_zas_rep_tools = os.path.dirname(os.path.dirname(os.path.dirname(inspect.getfile(Streamer))))
    shutil.rmtree(os.path.join(path_to_zas_rep_tools, "user-config"), ignore_errors=True)


@main.command('respeakAgreement')
@click.option('--logs_dir', '-l', default="logs")
@click.option('--use_logger_for_classes', '-lc', default=True)
@click.option('--use_logger_for_script', '-ls', default=True)
@click.option('--save_logs', '-sl', default=True)
#@click.option('--logs_dir', '-l', default="logs")
def respeakAgreement( logs_dir, use_logger_for_classes, use_logger_for_script, save_logs):
    # $ zas-vot-tools strat1 sets/train_set sets/eval_set  segments voiceless voiced vlwindow vcwindow experiments
    logger = logger_initialisation("streamTwitter" ,use_logger_for_script, save_logs, logs_dir)
    print "\nRespeaking-Process was started:\n\n"
    respeak_agreement()

    #path_to_zas_rep_tools = os.path.dirname(os.path.dirname(os.path.dirname(inspect.getfile(Streamer))))
    #shutil.rmtree(os.path.join(path_to_zas_rep_tools, "user-config"), ignore_errors=True)





@main.command('convertCorp')
@click.argument('paths_to_corp')
@click.argument('path_to_save', type=click.Path())
@click.argument('format_to_save')
@click.option('--logs_dir', '-l', default="logs")
@click.option('--use_logger_for_classes', '-lc', default=True)
@click.option('--use_logger_for_script', '-ls', default=True)
@click.option('--save_logs', '-sl', default=True)
#@click.option('--logs_dir', '-l', default="logs")
def convertCorp(corpus_language, path_to_save,format_to_save, logs_dir, use_logger_for_classes, use_logger_for_script, save_logs):
    # $ zas-vot-tools strat1 sets/train_set sets/eval_set  segments voiceless voiced vlwindow vcwindow experiments
    logger = logger_initialisation("convertCorp" ,use_logger_for_script, save_logs, logs_dir)





@main.command('extractCorp')
@click.argument('corpus_name')
@click.argument('path_to_save', type=click.Path())
@click.argument('format_to_save')
@click.option('--logs_dir', '-l', default="logs")
@click.option('--use_logger_for_classes', '-lc', default=True)
@click.option('--use_logger_for_script', '-ls', default=True)
@click.option('--save_logs', '-sl', default=True)
#@click.option('--logs_dir', '-l', default="logs")
def extractCorp(corpus_name, path_to_save,format_to_save, logs_dir, use_logger_for_classes, use_logger_for_script, save_logs):
    # $ zas-vot-tools strat1 sets/train_set sets/eval_set  segments voiceless voiced vlwindow vcwindow experiments
    logger = logger_initialisation("extractCorp" ,use_logger_for_script, save_logs, logs_dir)
 
    if not is_project_folder_still_exist():
        sys.exit()


@main.command('changeProjectsFolder')
@click.option('--logs_dir', '-l', default="logs")
@click.option('--use_logger_for_classes', '-lc', default=True)
@click.option('--use_logger_for_script', '-ls', default=True)
@click.option('--save_logs', '-sl', default=True)
#@click.option('--logs_dir', '-l', default="logs")
def changeProjectsFolder( logs_dir, use_logger_for_classes, use_logger_for_script, save_logs):
    # $ zas-vot-tools strat1 sets/train_set sets/eval_set  segments voiceless voiced vlwindow vcwindow experiments
    logger = logger_initialisation("extractCorp" ,use_logger_for_script, save_logs, logs_dir)

    change_projects_folder()


if __name__ == "__main__":
    main()
