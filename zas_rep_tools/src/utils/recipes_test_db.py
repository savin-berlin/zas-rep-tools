#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# : Create Test DBs
# Author:
# c(Developer) ->     {'Egor Savin'}
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

###Programm Info######

import os
import inspect
import logging
import sys

from zas_rep_tools.src.classes.DBHandler import DBHandler
from zas_rep_tools.src.utils.debugger import p


# name = init_data_blogger["name"]
# language = init_data_blogger["language"]
# visibility = init_data_blogger["visibility"]
# platform_name = init_data_blogger["platform_name"]
# license = init_data_blogger["license"]
# template_name = init_data_blogger["template_name"]
# version = init_data_blogger["version"]
# source = init_data_blogger["source"]
# encryption_key = init_data_blogger["encryption_key_corp"]
# corpus_id = init_data_blogger["corpus_id"]
# stats_id = init_data_blogger["stats_id"]
# typ= "corpus"


# name = init_data_blogger["name"]
# language = init_data_blogger["language"]
# visibility = init_data_blogger["visibility"]
# version = init_data_blogger["version"]
# encryption_key = init_data_blogger["encryption_key_stats"]
# corpus_id = init_data_blogger["corpus_id"]
# stats_id = init_data_blogger["stats_id"]
# typ= "stats"


# name = init_data_twitter["name"]
# language = init_data_twitter["language"]
# visibility = init_data_twitter["visibility"]
# version = init_data_twitter["version"]
# encryption_key = init_data_twitter["encryption_key_stats"]
# corpus_id = init_data_twitter["corpus_id"]
# stats_id = init_data_twitter["stats_id"]
# typ= "stats"



path_to_zas_rep_tools = os.path.dirname(os.path.dirname(os.path.dirname(inspect.getfile(DBHandler))))
path_to_testdbs =  "data/tests_data/testDBs/testFolder"
db_blogger_plaintext_corp = "7614_corpus_blogs_bloggerCorpus_en_extern_plaintext.db"
db_twitter_encrypted_corp = "9588_corpus_twitter_streamed_de_intern_encrypted.db"
db_blogger_plaintext_stats = "7614_3497_stats_bloggerCorpus_en_extern_plaintext.db"
db_twitter_encrypted_stats = "9588_6361_stats_streamed_de_intern_encrypted.db"

blogger_columns = [ u"blogger_id",u'text', u'gender', u'age', u'working_area', u'star_constellation']

init_data_blogger = {
                "name":"bloggerCorpus",
                "language":"en",
                "visibility":"extern",
                "platform_name":"blogs",
                "license":"CreativCommon",
                "template_name":"blogger",
                "version":"1",
                "source":"LanguageGoldMine",
                "encryption_key_corp":"corpus",
                "encryption_key_stats":"stats",
                "corpus_id":7614,
                "stats_id": 3497
                }

init_data_twitter = {
                "name":"streamed",
                "language":"de",
                "visibility":"intern",
                "platform_name":"twitter",
                "license":"Twitter Developer Agreement",
                "template_name":"twitter",
                "version":"1",
                "source":"Twitter API",
                "encryption_key_corp":"corpus",
                "encryption_key_stats":"stats",
                "corpus_id":9588,
                "stats_id": 6361
                }

columns_in_doc_table_blogger = [ u"blogger_id",u'text', u'gender', u'age', u'working_area', u'star_constellation']
columns_in_doc_table_twitter = [ u'text', u't_created_at', u't_language', u't_used_client', u'u_created_at', u'u_description', u'u_favourites', u'u_followers', u'u_friends', u'u_id', u'u_lang', u'u_given_name', u'u_username', u'u_verified']



input_row1= ["schöööööönen","taaaaaag", "dirrrrrr"]
input_row2= ["kliiiiitze","kliiiiiittttzzzzeee", "kleeeeeinnn", "kleinnn"]
input_row3 = ["üblich","üüüüübbbbblllliiiiiichhh", "essss"]
input_row4 = ["😀","😀", "😀", "😀", "😀"]
input_row5 = ["pitty","piiittyyy", "day"]
input_row6 = ["доооооооброоооооггггоо","доброоогооо ", "дняяяяяяяяяяяяя"]


blog_value1 = [ 322624,input_row1, u'm', 27, u'IT', u'lion' ]
blog_value2 = [ 324114,input_row2, u'm', 23, u'Care', u'fish' ]
blog_value3 = [ 416465,input_row3, u'm', 27, u'IT', u'lion' ]
blog_value4 = [ 873465,input_row4, u'm', 27, u'IT', u'lion' ]
blog_value5 = [ 843863,input_row5, u'm', 27, u'IT', u'lion' ]
blog_value6 = [ 479304,input_row6, u'm', 22, u'Wirtschaft', u'Krebs' ]


twitter_value1= [input_row1, u"20/06/2014", u"de", u"Iphone", u"20/06/2011", u"Neiiiiin", 45, 76, 765, 34567890, u"en", u"uniqPerson", u"realBro", u"True" ]
twitter_value2= [input_row2, u"20/06/2014", u"de", u"Iphone", u"20/06/2011", u"Neiiiiin", 45, 76, 765, 34567890, u"en", u"uniqPerson", u"realBro", u"True" ]
twitter_value3= [input_row3, u"20/06/2014", u"de", u"Iphone", u"20/06/2011", u"Neiiiiin", 45, 76, 765, 34567890, u"en", u"uniqPerson", u"realBro", u"True" ]
twitter_value4= [input_row4, u"20/06/2014", u"de", u"Iphone", u"20/06/2011", u"Neiiiiin", 45, 76, 765, 34567890, u"en", u"uniqPerson", u"realBro", u"True" ]
twitter_value5= [input_row5, u"20/06/2014", u"de", u"Iphone", u"20/06/2011", u"Neiiiiin", 45, 76, 765, 34567890, u"en", u"uniqPerson", u"realBro", u"True" ]
twitter_value6= [input_row6, u"20/06/2014", u"de", u"Iphone", u"20/06/2011", u"Neiiiiin", 45, 76, 765, 34567890, u"en", u"uniqPerson", u"realBro", u"True" ]



#Blogger Corpus:
def create_blogger_test_corpus(path_to_testdbs):
    DBname = init_data_blogger["name"]
    language = init_data_blogger["language"]
    visibility = init_data_blogger["visibility"]
    platform_name = init_data_blogger["platform_name"]
    license = init_data_blogger["license"]
    template_name = init_data_blogger["template_name"]
    version = init_data_blogger["version"]
    source = init_data_blogger["source"]
    encryption_key = init_data_blogger["encryption_key_corp"]
    corpus_id = init_data_blogger["corpus_id"]
    stats_id = init_data_blogger["stats_id"]

    db = DBHandler(logger_level=logging.ERROR)
    db.init("corpus", path_to_testdbs, DBname, language, visibility, platform_name=platform_name, license=license , template_name=template_name, version=version , source=source, corpus_id=corpus_id)

    #p((columns_in_doc_table_blogger , blog_value1))
    #p((columns_in_doc_table_blogger, [type(value) for value in blog_value1]), c="m")
    db.insertCV("documents", columns_in_doc_table_blogger , blog_value1)
    db.insertCV("documents", columns_in_doc_table_blogger , blog_value2)
    db.insertCV("documents", columns_in_doc_table_blogger , blog_value3)
    db.insertCV("documents", columns_in_doc_table_blogger , blog_value4)
    db.insertCV("documents", columns_in_doc_table_blogger , blog_value5)
    db.insertCV("documents", columns_in_doc_table_blogger , blog_value6)

    path_to_db = db.path()
    db.close()
    return path_to_db





#Blogger Stats:
def create_blogger_test_stats(path_to_testdbs):
    DBname = init_data_blogger["name"]
    language = init_data_blogger["language"]
    visibility = init_data_blogger["visibility"]
    version = init_data_blogger["version"]
    encryption_key = init_data_blogger["encryption_key_stats"]
    corpus_id = init_data_blogger["corpus_id"]
    stats_id = init_data_blogger["stats_id"]

    db = DBHandler(logger_level=logging.ERROR)
    db.init("stats", path_to_testdbs, DBname, language, visibility, corpus_id=corpus_id , version=version, stats_id=stats_id)


    path_to_db = db.path()
    db.close()
    return path_to_db




######################
#Twitter Corpus:
def create_twitter_test_corpus(path_to_testdbs):
    DBname = init_data_twitter["name"]
    language = init_data_twitter["language"]
    visibility = init_data_twitter["visibility"]
    platform_name = init_data_twitter["platform_name"]
    license = init_data_twitter["license"]
    template_name = init_data_twitter["template_name"]
    version = init_data_twitter["version"]
    source = init_data_twitter["source"]
    encryption_key = init_data_twitter["encryption_key_corp"]
    corpus_id = init_data_twitter["corpus_id"]
    stats_id = init_data_twitter["stats_id"]
    db = DBHandler(logger_level=logging.ERROR)
    db.init("corpus", path_to_testdbs, DBname, language, visibility, platform_name=platform_name, license=license , template_name=template_name, version=version , source=source, corpus_id=corpus_id, encryption_key=encryption_key)


    db.insertCV("documents", columns_in_doc_table_twitter, twitter_value1)
    db.insertCV("documents", columns_in_doc_table_twitter, twitter_value2)
    db.insertCV("documents", columns_in_doc_table_twitter, twitter_value3)
    db.insertCV("documents", columns_in_doc_table_twitter, twitter_value4)
    db.insertCV("documents", columns_in_doc_table_twitter, twitter_value5)
    db.insertCV("documents", columns_in_doc_table_twitter, twitter_value6)

    path_to_db = db.path()
    db.close()
    return path_to_db




#
#Twitter Stats:
def create_twitter_test_stats(path_to_testdbs):
    DBname = init_data_twitter["name"]
    language = init_data_twitter["language"]
    visibility = init_data_twitter["visibility"]
    version = init_data_twitter["version"]
    encryption_key = init_data_twitter["encryption_key_stats"]
    corpus_id = init_data_twitter["corpus_id"]
    stats_id = init_data_twitter["stats_id"]

    db = DBHandler(logger_level=logging.ERROR)
    db.init("stats", path_to_testdbs, DBname, language, visibility, corpus_id=corpus_id , version=version, stats_id=stats_id, encryption_key=encryption_key)

    path_to_db = db.path()
    db.close()
    return path_to_db



def create_all_test_dbs_if_not_exist():

    
    #p(os.path.join(path_to_zas_rep_tools,db_blogger_relativ_path_to_plaintext_corp))
    #Blogger
    if not os.path.isfile(os.path.join(path_to_zas_rep_tools,path_to_testdbs,db_blogger_plaintext_corp)):
        create_blogger_test_corpus(os.path.join(path_to_zas_rep_tools,path_to_testdbs))
    if not os.path.isfile(os.path.join(path_to_zas_rep_tools,path_to_testdbs,db_blogger_plaintext_stats)):
        create_blogger_test_stats(os.path.join(path_to_zas_rep_tools,path_to_testdbs))

    #Twitter
    if not os.path.isfile(os.path.join(path_to_zas_rep_tools,path_to_testdbs,db_twitter_encrypted_corp)):
        create_twitter_test_corpus(os.path.join(path_to_zas_rep_tools,path_to_testdbs))
    if not os.path.isfile(os.path.join(path_to_zas_rep_tools,path_to_testdbs,db_twitter_encrypted_stats)):
        create_twitter_test_stats(os.path.join(path_to_zas_rep_tools,path_to_testdbs))

