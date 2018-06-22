#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# : SQL Helper 
# Author:
# c(Student) ->     {'Egor Savin'}
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

###Programm Info######

import os
import sys
import regex

from zas_rep_tools.src.utils.debugger import p

attributs_order_corpus = ["id","name","platform_name","template_name","version","language","created_at","source","license","visibility","typ"]

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




attributs_names_stats = [
                            ("id", "INTEGER NOT NULL"),
                            ("corpus_id", "INTEGER NOT NULL"),
                            ("name", "TEXT NOT NULL"),
                            ("version", "TEXT"),
                            ("created_at", "TEXT NOT NULL"),
                            ("visibility", "TEXT NOT NULL"),
                            ("typ", "TEXT NOT NULL")
                        ]


def attributs_and_types_to_str(attributs_names):
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


def values_list_to_str(values):
    '''
    without Datatypes
    '''
    if isinstance(values, list):
        str_values = ""
        if len(values) > 1:
            i=1
            for attribut in values:
                if i < len(values):
                    str_values += "\n'{}', ".format(attribut)
                else:
                    str_values += "\n'{}' ".format(attribut)
                i+=1
        elif len(values) == 1:
            str_values += "'{}'".format(attribut[0])
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

