#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# : SQL Helper 
# Author:
# c(Student) ->     {'Egor Savin'}
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

###Programm Info######

from __future__ import generators 

import os
import sys
import regex
import sqlite3

import functools

from zas_rep_tools.src.utils.debugger import p
from zas_rep_tools.src.utils.logger import Logger


########################################################################################
#########################Exception- Handling#############################################
########################################################################################



#__metaclass__ = ErrorCatcher
class DBErrorCatcher(type):


    # @classmethod
    # def __prepare__(metacls, name, bases, **kargs):
    # #kargs = {"myArg1": 1, "myArg2": 2}
    #     return super().__prepare__(name, bases, **kargs)


    def __new__(cls, name, bases, dct):
        #p(dct)
        if 'DBErrorCatcher' in dct:
            #p(dct['DBErrorCatcher'])
            if dct['DBErrorCatcher']:
                logger = Logger()
                logger = logger.errorLogger("DBErrorCatcher")
                for m in dct:
                    if hasattr(dct[m], '__call__'):
                        dct[m] = catch_exception(dct[m],logger)

        return type.__new__(cls, name, bases, dct)








# #__metaclass__ = ErrorCatcher
# class DBErrorCatcher(type):


#     @classmethod
#     def __prepare__(metacls, name, bases, **kargs):
#     #kargs = {"myArg1": 1, "myArg2": 2}
#         return super().__prepare__(name, bases, **kargs)


#     def __new__(cls, name, bases, dct, **kargs):
#         logger = Logger()
#         logger = logger.errorLogger("DBErrorCatcher")

#         for m in dct:
#             if hasattr(dct[m], '__call__'):
#                 dct[m] = catch_exception(dct[m],logger)
#         return type.__new__(cls, name, bases, dct)



#@catch_exception

def catch_exception(f,logger):
    @functools.wraps(f)
    def func(*args, **kwargs):
        #p(type(args[0]), c="r")
        #p(args[0].__dict__)
        #args[0].close()
        #args.__dict__
        #sys.exit()
        try:

            return f(*args, **kwargs)


        except sqlite3.DataError as e:
            msg = "sqlite3.DataError: '{}'-Function returned following Error: '{}'. ".format(f.__name__, e)
            logger.error(msg)
            sys.exit()
         
        except sqlite3.InternalError as e:
            msg = "sqlite3.InternalError: '{}'-Function returned following Error: '{}'. ".format(f.__name__, e)
            logger.error(msg)
            sys.exit()

         
        except sqlite3.IntegrityError as e:
            msg = "sqlite3.IntegrityError: '{}'-Function returned following Error: '{}'. ".format(f.__name__, e)
            logger.error(msg)
            sys.exit()

         
        except sqlite3.OperationalError as e:
            msg = "sqlite3.OperationalError: '{}'-Function returned following Error: '{}'. ".format(f.__name__, e)
            logger.error(msg)
            sys.exit()

         
        except sqlite3.NotSupportedError as e:
            msg = "sqlite3.NotSupportedError: '{}'-Function returned following Error: '{}'. ".format(f.__name__, e)
            logger.error(msg)
            sys.exit()

         
        except sqlite3.ProgrammingError as e:
            msg = "sqlite3.ProgrammingError: '{}'-Function returned following Error: '{}'. ".format(f.__name__, e)
            logger.error(msg)
            sys.exit()
         
        except Exception as e:
            msg = "OtherExceptions: '{}'-Function returned following Error: '{}'. ".format(f.__name__, e)
            #logger.error(msg)
            #p(logger, c="m")
            logger.error(msg)
            sys.exit()
    
    return func










########################################################################################
########################################################################################
########################################################################################
########################################################################################


########################################################################
##########################corpus#######################################
########################################################################




attributs_names_corpus = [
                            ("id", "INTEGER NOT NULL"),
                            ("name", "TEXT NOT NULL"),
                            ("platform_name", "TEXT NOT NULL"),
                            ("template_name", "TEXT"),
                            ("version", "TEXT"),
                            ("language", "TEXT NOT NULL"),
                            ("created_at", "TEXT NOT NULL"),
                            ("source", "TEXT"),
                            ("license", "TEXT"),
                            ("visibility", "TEXT NOT NULL"),
                            ("typ", "TEXT NOT NULL")
                        ]



### Documnets_Table (default)

default_columns_and_types_for_corpus_documents = [
                                ('docs_id','INTEGER PRIMARY KEY'),
                                ('text','BLOB NOT NULL'),
                                ]


default_constraints_for_corpus_documents = [
                        'CONSTRAINT "Uniq_Blogger_ID" UNIQUE ("docs_id")',

                        ]


default_index_for_corpus_documents = [
                        'CREATE INDEX "ix_doc_id" ON "documents" ("docs_id");',

                            ]



### Documnets_Table (special)

extended_columns_and_types_for_corpus_documents_twitter = [
                                ('t_created_at','TEXT NOT NULL'),
                                ('t_language','TEXT'),
                                ('t_used_client','TEXT'),
                                ('u_created_at','TEXT NOT NULL'),
                                ('u_description','TEXT'),
                                ('u_favourites','INTEGER'),
                                ('u_followers','INTEGER'),
                                ('u_friends','TEXT'),
                                ('u_id','INTEGER NOT NULL'),
                                ('u_lang','TEXT'),
                                ('u_given_name','TEXT NOT NULL'),
                                ('u_username','TEXT NOT NULL'),
                                ('u_verified','TEXT NOT NULL'),
                                ('u_location','TEXT'),
                                ]





extended_columns_and_types_for_corpus_documents_blogger =[
                                ('gender','TEXT NOT NULL'),
                                ('age','INTEGER NOT NULL'),
                                ('working_area','TEXT NOT NULL'),
                                ('star-constellation','TEXT NOT NULL'),
                                ]











########################################################################
##############################Stats#####################################
########################################################################


### Info_Table

attributs_names_stats = [
                            ("id", "INTEGER NOT NULL"),
                            ("corpus_id", "INTEGER NOT NULL"),
                            ("name", "TEXT NOT NULL"),
                            ("version", "TEXT"),
                            ("created_at", "TEXT NOT NULL"),
                            ("visibility", "TEXT NOT NULL"),
                            ("typ", "TEXT NOT NULL")
                        ]







### Baseline_Table (default)

default_columns_and_types_for_stats_baseline = [
                                ('word','TEXT PRIMARY KEY'),
                                ('redu_counts','INTEGER NOT NULL'),
                                ('repl_counts','INTEGER NOT NULL'),
                                ('all_counts','INTEGER NOT NULL'),
                                ('repl_IDs','BLOB NOT NULL'),
                                ('redu_IDs','BLOB NOT NULL'),
                                ]



default_indexes_for_stats_baseline = [
                                'CREATE INDEX "ix_word" ON "baseline" ("word");',
                                'CREATE INDEX "ix_all_counts" ON "baseline" ("all_counts");',                            
                                ]



### Replications_Table (default)

default_columns_and_types_for_stats_replications = [
                                ('repl_id','INTEGER PRIMARY KEY'),
                                ('docs_id','INTEGER NOT NULL'),
                                ('token_nr','INTEGER NOT NULL'),
                                ('word','TEXT NOT NULL'),
                                ('rle',' TEXT'),
                                ('repl_letter','TEXT NOT NULL'),
                                ('nr_of_repl','INTEGER NOT NULL'),
                                ('index_of_repl','INTEGER NOT NULL'),
                                ]


default_constrains_for_stats_replications = [
                                'CONSTRAINT "Uniq_Repl_ID" UNIQUE ("repl_id")',
                                ]


default_indexes_for_stats_replications = [
                                'CREATE INDEX "ix_replID" ON "stats.replications" ("repl_id");',
                                ]

### Reduplications_Table (default)



default_columns_and_types_for_stats_reduplications = [
                                ('redu_id','INTEGER PRIMARY KEY'),
                                ('docs_id','INTEGER NOT NULL'),
                                ('token_nr','INTEGER NOT NULL'),
                                ('word','TEXT NOT NULL'),
                                ('nr_of_redu','INTEGER NOT NULL'),
                                ('scopus','BLOB'),
                                ]


default_constrains_for_stats_reduplications = [
                                    'CONSTRAINT "Uniq_Redu-ID" UNIQUE ("redu_id")',
                                    ]


default_indexes_for_stats_reduplications = [
                                    'CREATE INDEX "ix_reduID" ON "stats.reduplications" ("redu-id");',
                                    ]







########################################################################
#########################Other  Helpers##################################
########################################################################

def ResultIter(cursor, arraysize=1000):
    'An iterator that uses fetchmany to keep memory usage down'
    while True:
        results = cursor.fetchmany(arraysize)
        if not results:
            break
        for result in results:
            yield result



def columns_and_values_to_str(columns_names,values):
    '''
    without Datatypes
    '''


    if isinstance(columns_names, list) and isinstance(values, list):
        str_columns_and_values = ""
        i=1
        for column, value in zip(columns_names,values):
            if value is None:
                value = "NULL"

            if value == "NULL":
                if len(columns_names) > 1:
                    if i < len(columns_names):
                        str_columns_and_values += "\n{}={}, ".format(column,value)
                    else:
                        str_columns_and_values += "\n{}={} ".format(column,value)

                    i+=1
                elif len(columns_names) == 1:
                    str_columns_and_values += "{}={}".format(column,value)

                else:
                    return False
            else:

                if len(columns_names) > 1:
                    if i < len(columns_names):
                        str_columns_and_values += "\n{}='{}', ".format(column,value)
                    else:
                        str_columns_and_values += "\n{}='{}' ".format(column,value)

                    i+=1
                elif len(columns_names) == 1:
                    str_columns_and_values += "{}='{}'".format(column,value)

                else:
                    return False
    else:
        return False

    return str_columns_and_values




def columns_and_types_in_tuples_to_str(attributs_names):
    '''
    use by table initialisation (with Datatypes)
    '''
    if isinstance(attributs_names, list):
        str_attributs_names = ""
        i=1
        for attribut in attributs_names:
            if not isinstance(attribut, tuple):
                return False

            if len(attributs_names) > 1:
                if i < len(attributs_names):
                    str_attributs_names += "\n{} {}, ".format(attribut[0], attribut[1])
                else:
                    str_attributs_names += "\n{} {} ".format(attribut[0], attribut[1])

                i+=1
            elif len(attributs_names) == 1:
                str_attributs_names += "\n{} {}\n".format(attribut[0], attribut[1])

            else:
                return False
    else:
        return False


    return str_attributs_names





def attributs_to_str(attributs_names):
    '''
    without Datatypes
    '''
    if isinstance(attributs_names, list):
        str_attributs_names = ""
        i=1
        for attribut in attributs_names:
            if not isinstance(attribut, tuple):
                return False

            if len(attributs_names) > 1:
                if i < len(attributs_names):
                    str_attributs_names += "\n{}, ".format(attribut[0])
                else:
                    str_attributs_names += "\n{} ".format(attribut[0])

                i+=1
            elif len(attributs_names) == 1:
                str_attributs_names += "{}".format(attribut[0])

            else:
                return False
    else:
        return False

    return str_attributs_names




def columns_list_to_str(attributs_names):
    '''
    without Datatypes
    '''
    if isinstance(attributs_names, list):
        str_attributs_names = ""
        i=1
        for attribut in attributs_names:

            if len(attributs_names) > 1:
                if i < len(attributs_names):
                    str_attributs_names += "\n{}, ".format(attribut)
                else:
                    str_attributs_names += "\n{} ".format(attribut)

                i+=1
            elif len(attributs_names) == 1:
                str_attributs_names += "{}".format(attribut)

            else:
                return False
    else:
        return False

    return str_attributs_names



def constrains_list_to_str(constrains):
    '''
    without Datatypes
    '''
    #p(constrains)
    if isinstance(constrains, list):
        str_constrains = ""
        i=0
        for constrain in constrains:
            if len(constrains) > 1:
                if i == 0:
                    str_constrains += ",\n{} ".format(constrain)
                elif i<0 and  i < len(constrains):
                    str_constrains += "\n{}, ".format(constrain)
                else:
                    str_constrains += "\n{} ".format(constrain)

                i+=1
            elif len(constrains) == 1:
                str_constrains += ",\n{}".format(constrain)

            else:
                return False
    else:
        return False

    #p(str_constrains, c="m")
    return str_constrains



def values_list_to_str(values):
    '''
    without Datatypes
    '''
    if isinstance(values, list):
        str_values = ""
        i=1
        for value in values:
            if value is None:
                value = "NULL"
            if value == "NULL":
                if len(values) > 1:
                    if i < len(values):
                        str_values += "\n{}, ".format(value)
                    else:
                        str_values += "\n{} ".format(value)
                    i+=1
                elif len(values) == 1:
                    str_values += "{}".format(value)
                else:
                    return False
            else:
                if len(values) > 1:
                    if i < len(values):
                        str_values += "\n'{}', ".format(value)
                    else:
                        str_values += "\n'{}' ".format(value)
                    i+=1
                elif len(values) == 1:
                    str_values += "'{}'".format(value)
                else:
                    return False
    else:
        return False

    return str_values



def get_file_name(prjFolder,DBname, language,visibility, typ, fileName=False):
    status = True
    i=0
    while status:
        #Created FileName
        if not fileName:
            if i==1:
                fileName = "{}_{}_{}_{}_{}".format(typ,DBname,language,visibility,i)
            else:
                fileName = "{}_{}_{}_{}".format(typ,DBname,language,visibility)
        else:
            if i>0:
                fileName_without_extension = os.path.splitext(fileName)[0]
                pattern = r"^(.*?)(_[0-9]*)$"
                matched = regex.findall(pattern,fileName_without_extension)
                #sys.exit()
                if matched:
                    fileName_without_extension = matched[0][0]

                fileName = fileName_without_extension+"_"+str(i)
                

        if i > 10000:
            print "Aborting!!! To avoid never-ending loop"
            sys.exit()

        i+=1
        #Add Extention
        if ".db" not in fileName:
            fileName = fileName+".db"

        #Create path_to_db
        path_to_db = os.path.join(prjFolder,fileName)

        #Check if this file already exist. and if yes, than change the name
        if not os.path.isfile(path_to_db):
            status = False
            return fileName,path_to_db




def create_id(name,lang, typ, visibility, number=False, corpus_id=False):
    if number:
        if corpus_id:
            return "{}.{}{}{}{}{}".format(corpus_id,name[0], lang[0], typ[0], visibility[0],number)
        else:
            return "{}{}{}{}{}".format(name[0], lang[0], typ[0], visibility[0], number)
    else:
        if corpus_id:
            return "{}.{}{}{}{}".format(corpus_id,name[0], lang[0], typ[0], visibility[0])
        else:
            return "{}{}{}{}".format(name[0], lang[0], typ[0], visibility[0])


def make_acronyme(full_name):
    '''
    Rules:
    take all first 3 consonant non-repetitive from the word

    Example:
    Full_name = "twitter"
    acronyme = "twt"
    '''
    acronyme = ''
    consonants = set("bcdfghjklmnpqrstvwxyz")
    i=0
    if isinstance(full_name, (str, unicode)):
        for char in full_name:
            if char in consonants:
                if len(acronyme)==0:
                        acronyme += char
                else:
                    if acronyme[-1]!= char:
                        acronyme += char
                i+=1

            if i >=3:
                return acronyme
    else:
        return False


    return acronyme











