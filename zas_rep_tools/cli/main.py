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

#from zas_rep_tools.src.utils.logger import Logger
from zas_rep_tools.src.utils.cli_helper import *
from zas_rep_tools.src.classes.Reader import  Reader
from zas_rep_tools.src.classes.DBHandler import DBHandler
from zas_rep_tools.src.classes.Streamer import Streamer
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
def implemented(corpus_name, rep_type, search_type, case, context, context_left, context_right, scopus, refer,
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

    #Add
    corpus = Corpus(name, plattform_name, template_name, version, language, source, typ)
    corpus.saveOnDisc(path) 
    corpus.commit()
    corpus.export() 
    corpus.addData(path_to_data, typ_of_data) # use reader on stream 

    configs.addCorpus(name,path,corpus_id) 


    #Open/Import
    corpus = Corpus(path_to_corp) 

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
#@click.option('--logs_dir', '-l', default="logs")
def streamTwitter( path_to_save,language,stop_words,terms,encoding,ignore_rt, filter_strategie, save_used_terms, logs_dir, use_logger_for_classes, use_logger_for_script, save_logs):
    # $ zas-vot-tools strat1 sets/train_set sets/eval_set  segments voiceless voiced vlwindow vcwindow experiments
    logger = logger_initialisation("streamTwitter" ,use_logger_for_script, save_logs, logs_dir)
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
                    encoding=encoding, ignore_rt=ignore_rt, save_used_terms=save_used_terms, filterStrat=filter_strategie)
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
