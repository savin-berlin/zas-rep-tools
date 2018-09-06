#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# : Corpus Module
# Author:
# c(Developer) ->     {'Egor Savin'}
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

###Programm Info######



import os
import time
import smtplib
import codecs
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from zas_rep_tools.src.utils.db_helper import DBErrorCatcher
import io
import json
import inspect
import zipfile
import socket
import sys
import logging
from ZODB import FileStorage, DB
from zc.lockfile import LockError
import transaction
import copy
import urllib2
import emoji
import re
import regex
import psutil
from decimal import Decimal, ROUND_HALF_UP, ROUND_UP, ROUND_HALF_DOWN, ROUND_DOWN
import threading
import inspect
import ctypes
from collections import OrderedDict
from multiprocessing import Process, RawValue
import traceback
from collections import defaultdict, Counter
import platform



from zas_rep_tools.src.utils.zaslogger import ZASLogger
from zas_rep_tools.src.utils.debugger import p



path_to_zas_rep_tools = os.path.dirname(os.path.dirname(os.path.dirname(inspect.getfile(p))))


modi = ["test", "dev","dev+","dev-", "prod", "free", "prod+t", "test+s+","test+s-", "silent", "prod+","prod-"]
punkt_str = set(""".!:;-"#$%&'()*+,/<=>?@[\\]^_`{|}~""")
emoticons = set([')','(','-(', '-)', '=p', ':-p','-p', '8-)',  '=)','=(', ':-)', ':)', '<3', '{}',  'o:-)', 'x-(',  ':-d',  ':-#', ':-(', ':(',   ':p', ':o', ':-|', 'x-p', ':-)*', ':-*', ':*', 'b-)', ':_(', ":'(", '\\:d/', '*-*', ':o3', '#-o', ':*)', '/_^', '>:)', '<><',  '(-}{-)', 'xd', '=d', ')-:', '(-:',  '=/', ':-)(-:', '<:3)~', '~,~', ':-b', '^_^', '<l:0', ':-/', '=8)', '@~)~',    ':s', ':-@', '=o', ':-o',  ':-q', ':>', ':-j', ':-&', '=-o', ':-\\', ':-e',  ';-)', ';)', '|-o', '(.v.)', '~:0', '(*v*)', '=^.^=', '</3','*<:o)', 'o.o','$_$', ':->', '8-#' ])



def function_name(n=-2):
    stack = traceback.extract_stack()
    try:
        filename, codeline, funcName, text = stack[n]
    except:
        funcName = None

    return funcName


def get_tb(n=-2):
    stack = traceback.extract_stack()
    filename, codeline, funcName, text = (None,None,None,None)
    try:
        filename, codeline, funcName, text = stack[n]
    except:
        filename, codeline, funcName, text = (None,None,None,None)

    return {"filename":filename, "codeline":codeline, "funcName":funcName, "text":text}

def get_module_name(n=-2):
    stack = traceback.extract_stack()
    try:
        filename, codeline, funcName, text = stack[n]
    except:
        funcName = None

    return os.path.splitext(os.path.basename(filename))[0]


class Status(object):
    # {"status":False, "track_id":track_id, "desc":"Table ('{}') wasn't found or not exist.".format(table_name), "level_name":"error_insertion", "action":"ignored"}
    collection_complete_status= defaultdict(lambda: defaultdict(dict))
    lock = threading.Lock()
    allow_full_tb = False
    allow_auto_func_names = False
    allow_auto_arginfo = False
    light_mode = True

    def __init__(self, status=None, track_id=None, desc=None, level=None, action=None, error_name=None, inp_obj = None, func_name=None, out_obj=0, exception=None, tb=None, local_var=None, arginfo=True, outsort=0, answer=0):
        #with Status.lock:
        #p((status,track_id),"status")
        self._status = {}
        if Status.light_mode:
            #p((status,track_id),"1status")
            if status==True:
                #p((status,track_id),"2status")
                self.module_name = None
                self.track_id = None
                self._status = {"status":status, "track_id":self.track_id, "out_obj":out_obj, "desc":desc, "outsort":outsort, "answer":answer}
            else:
                #p((status,track_id),"3status")
                self._create_case(status=status, track_id=track_id, desc=desc, level=level, action=action, error_name=error_name, inp_obj = inp_obj , func_name=func_name, out_obj=out_obj, exception=exception, tb=tb, local_var=local_var, arginfo=arginfo)

        else:
            #p((status,track_id),"4status")
            self._create_case(status=status, track_id=track_id, desc=desc, level=level, action=action, error_name=error_name, inp_obj = inp_obj , func_name=func_name, out_obj=out_obj, exception=exception, tb=tb, local_var=local_var, arginfo=arginfo)



    def _create_case(self,status=None, track_id=None, desc=None, level=None, action=None, error_name=None, inp_obj = None, func_name=None, out_obj=0, exception=None, tb=None, local_var=None, arginfo=True,outsort=0,answer=0):
        self.module_name = get_module_name(-3)
        #p(module_name)
        self.track_id =  track_id if track_id else SharedCounterExtern().incr()

        auto_func_name = None
        auto_tb = None
        arginfo = None
        #p((status,self.track_id,self.module_name),"5status")
        if Status.allow_auto_func_names:
            auto_func_name = {"-1":function_name(-1),"-2":function_name(-2), "-3":function_name(-3), "-4":function_name(-4),"-5":function_name(-5)}

        if Status.allow_full_tb:
            auto_tb={"-1":get_tb(-1),"-2":get_tb(-2), "-3":get_tb(-3), "-4":get_tb(-4),"-5":get_tb(-5), "-6":get_tb(-6)} 

        if Status.allow_auto_arginfo:
            arginfo = inspect.getargvalues(inspect.currentframe().f_back)
        #p(auto_func_name,"auto_func_name")
        #p(auto_tb,"auto_tb")
        #p(arginfo,"arginfo")

        #p(Status.allow_auto_arginfo, "Status.allow_auto_arginfo")
        #p(arginfo,"arginfo")
        #p((status,self.track_id,self.module_name),"6status")
        #p((Status.allow_full_tb, Status.allow_auto_func_names,Status.allow_auto_arginfo, ))
        self._status = {
                        "status":status,
                        "track_id":self.track_id,
                        "desc":desc,
                        "level":level,
                        "action":action,
                        "error_name":error_name,
                        "inp_obj":inp_obj,
                        "func_name":func_name,
                        "auto_func_name":auto_func_name,
                        "out_obj":out_obj,
                        "exception":exception,
                        "tb":tb,
                        "local_var":local_var,
                        "args":arginfo.args if arginfo else None,
                        "auto_tb":auto_tb,
                        "answer":answer,
                        # "varargs":str(arginfo.varargs),
                        # "keywords":str(arginfo.keywords),
                        "locals":{k:str(v) for k,v in arginfo.locals.iteritems()} if arginfo else None,
                        "outsort":outsort,
                        #"arginfo":inspect.formatargvalues(arginfo.args,arginfo.varargs, arginfo.keywords ,arginfo.locals),
                        #"arginfo":arginfo
                        }
        #p((status,self.track_id,self.module_name),"7status")
        Status.collection_complete_status[self.module_name][self.track_id] = self
        #p((status,self.track_id,self.module_name),"8status")

    def __delitem__(self,item_key):
        #p(self._status)
        del self._status[item_key]


    def __getitem__(self,item_key):
        with Status.lock:
            return self._status[item_key]
            #return copy.deepcopy(self._status[item_key])

    def __str__(self):
        outputstr = ""
        outputstr += ">>>>>>> {} <<<<<<<<\n".format(self.track_id)
        #p(self.__dict__, "self._status")

        for name, values in OrderedDict(self._status).iteritems():
            if not values:
                outputstr += "{}:{}\n".format(name, values)
            else:
                if name in ["locals", "auto_func_name"]:
                    outputstr += "{}: (".format(name)
                    for var_name, var_values  in OrderedDict(values).iteritems():
                        outputstr += "\n          {}:{}".format(var_name, repr(var_values))
                    outputstr += "\n          )\n".format()

                elif name in ["auto_tb"]:
                    outputstr += "{}: (".format(name)
                    for var_name, var_values  in OrderedDict(values).iteritems():
                        outputstr += "\n          {}: {{".format(var_name)
                        for tag_name, tag_value in OrderedDict(var_values).iteritems():
                            outputstr += "\n                 {}:{}".format(tag_name, repr(tag_value))
                        outputstr += "\n              }}\n".format()
                        #outputstr += "\n          {}:{}".format(var_name, var_values)
                    outputstr += "\n          )\n".format()
                # elif name == "auto_tb":
                #     pass
                # elif name == "auto_func_name":
                #     pass
                else:
                    outputstr += "{}:{}\n".format(name, repr(values))
        outputstr += "\n".format()
        return outputstr

    def __setitem__(self,item_key,item):
        with Status.lock:
            if self.module_name == None:
                pass
            else:
                if item_key == "track_id":
                    if item not in [track_id for module, module_data in Status.collection_complete_status.iteritems() for track_id in module_data]:
                        del Status.collection_complete_status[self.module_name][self.track_id]
                        self.track_id = item
                        self._status[item_key] = item
                        Status.collection_complete_status[self.module_name][self.track_id] = self
                    else:
                        raise KeyError, "Given track_id is already exist in the current collection!"
                else:
                    self._status[item_key] = item

    def get(self):
        with Status.lock:
            return copy.deepcopy(self._status)




def statusesTstring(module_name):
    outputstr = ""
    if module_name in Status.collection_complete_status:
        for k,v in OrderedDict(Status.collection_complete_status[module_name]).iteritems():
            outputstr += "{}".format(v)
        #p(outputstr)
        return outputstr
    return False



class SharedCounterExtern(object):
    val = RawValue('i', 0)
    lock = threading.Lock()
    def __init__(self, value=False, new=False):
        # RawValue because we don't need it to create a Lock:
        if value:
            SharedCounterExtern.val.value = value
            SharedCounterExtern.lock 

        if new:
            self.new()

    def __int__(self):
        return int(self.v())

    def __str__(self):
        return str(self.v())

    def incr(self, n=1):
        with SharedCounterExtern.lock:
            SharedCounterExtern.val.value += n
            return SharedCounterExtern.val.value

    def v(self):
        with SharedCounterExtern.lock:
            return SharedCounterExtern.val.value

    def clear(self):
        with SharedCounterExtern.lock:
            SharedCounterExtern.val.value = 0
            return SharedCounterExtern.val.value

    def new(self):
        SharedCounterExtern.val.value = 0



class SharedCounterIntern(object):
    #val = RawValue('i', 0)
    #lock = threading.Lock()
    def __init__(self, value=False, new=False):
        self.val = RawValue('i', 0)
        self.lock = threading.Lock()
        # RawValue because we don't need it to create a Lock:
        if value:
            self.val.value = value

        if new:
            self.new()

    def __int__(self):
        return int(self.v())

    def __str__(self):
        return str(self.v())

    def incr(self, n=1):
        with self.lock:
            self.val.value += n
            return self.val.value

    def v(self):
        with self.lock:
            return self.val.value

    def clear(self):
        with self.lock:
            self.val.value = 0
            return self.val.value

    def new(self):
       self.val.value = 0



class MyZODB(object):
    def __init__(self, path):
        self.path = path


    def open(self):
        #p(LockError)
        while True:
            try:       
                self.storage = FileStorage.FileStorage(self.path, read_only=False)
                self.db = DB(self.storage)
                self.my_transaction_manager = transaction.TransactionManager()
                self.conn = self.db.open(self.my_transaction_manager)
                break
            except LockError:
                pass



    def __getitem__(self,item_index):
        self.open()
        getted_item = copy.deepcopy(self.conn.root())
        self.close()
        return getted_item[item_index]



    def __str__(self):
        self.open()
        getted_str = str(self.conn.root())
        self.close()
        return getted_str


    def __get__(self, instance, owner):
        self.open()
        root =  copy.deepcopy(self.conn.root())
        self.close()
        return root

    def __setitem__(self,index,item):
        self.open()
        with self.my_transaction_manager as trans:
            #trans.note(u"incrementing x")
            self.conn.root()[index] = item

        self.close()

    def get_root(self):
        self.open()
        root =  copy.deepcopy(self.conn.root())
        self.close()
        return root

    def close(self):
        self.conn.close()
        #self.my_transaction_manager = False
        #self.my_transaction_manager.close()
        self.db.close()
        self.storage.close()

    def iteritems(self):
        self.open()
        root =  copy.deepcopy(self.conn.root())
        self.close()
        for k,v in root.iteritems():
            yield k,v
        #return iter([(x[0], x) for x in "alpha bravo charlie".split()])
        #return root

    def __iter__(self):
        self.open()
        getted_item = copy.deepcopy(self.conn.root())
        self.close()
        return iter(getted_item.keys())
        #return iter(self.settings.keys())

    def clean(self):
        self.open()
        with self.my_transaction_manager as trans:
            keys = [key for key in self.conn.root()]
            for key in keys:
                del self.conn.root()[key]
        self.close()
        return True


def levenstein(s1,s2):
    len_1=len(s1)
    len_2=len(s2)
    x =[[0]*(len_2+1) for _ in range(len_1+1)]#the matrix whose last element ->edit distance
    for i in range(0,len_1+1): #initialization of base case values
        x[i][0]=i

    for j in range(0,len_2+1):
        x[0][j]=j

    for i in range (1,len_1+1):
        for j in range(1,len_2+1):
            if s1[i-1]==s2[j-1]:
                x[i][j] = x[i-1][j-1] 

            else :
                x[i][j]= min(x[i][j-1],x[i-1][j],x[i-1][j-1])+1

    print x[i][j]



def NestedDictValues(d):
    '''
    $ a={4:1,6:2,7:{8:3,9:4,5:{10:5},2:6,6:{2:7,1:8}}}
    $ list(NestedDictValues(a))
    >>> [1, 2, 3, 4, 6, 5, 8, 7]
    '''
    for v1 in d.values():
        if isinstance(v1, dict):
            for v2 in NestedDictValues(v1):
                yield v2
        else:
            yield v1
#Rle().del_rep()

class Rle(object):
    def __init__(self, logger=False):
        #from zas_rep_tools.src.extensions.uniseg import graphemecluster as gc
        #self.gc = gc
        self.re_pattern_char_recognition= regex.compile(ur'[\ud800-\udbff][\udc00-\udfff]|.',regex.UNICODE)
        self.logger = logger

    def del_rep_from_sent(self, input_string):
        #time.sleep(8)
        count = 1
        prev = u''
        encoded = u""
        if not isinstance(input_string, list):
            msg = "RLE(del_rep_from_sent): Given Obj is not an list"
            if self.logger:
                self.logger.error(msg)
            else:
                print(msg) 
            return False

        for character in input_string:
            if not isinstance(character, unicode):
                character = character.decode("utf-8")

            if character != prev:
                if prev:
                    #entry = (prev,count)
                    #lst.append(entry)
                    if prev:
                        encoded +=  u"{} ".format(prev)
                    else:
                        encoded +=  u"{}".format(prev)
                    #print lst
                count = 1
                prev = character
            else:
                count += 1
        else:
            try:
                if prev:
                    encoded +=  u"{} ".format(prev)
                else:
                    encoded +=  u"{}".format(prev)
                return encoded.strip()
            except Exception as e:
                if self.logger:
                    self.logger.error("RLE: Exception encountered {e}".format(e=e),  exc_info=True)
                else:
                    print("Exception encountered {e}".format(e=e)) 


    def get_chars(self, input_string):
        #input_string = input_string.decode("utf-8")
        try:
            input_string = input_string.decode("utf-8")
        except (UnicodeEncodeError, AttributeError):
            pass
        except Exception as e:
            if self.logger:
                self.logger.error("RLE: Exception encountered: {e}".format(e=e),  exc_info=True)
            else:
                print("Exception encountered: {e}".format(e=e)) 
        try:
            input_string = self.re_pattern_char_recognition.findall(input_string)
        except TypeError:
            return input_string

        return input_string





    # def get_chars(self, input_string):
    #     #input_string = input_string.decode("utf-8")
    #     #input_string = self.re_pattern_char_recognition.findall(input_string)
    #     if isinstance(input_string, unicode):
    #         input_string = self.gc.grapheme_clusters(input_string)
    #     elif isinstance(input_string, str):
    #         input_string = self.gc.grapheme_clusters(unicode(input_string,"utf-8"))  

    #     # try:
    #     #     input_string = self.re_pattern_char_recognition.findall(input_string)
    #     # except TypeError:
    #     #     return input_string

    #     return input_string



    def del_rep(self, input_string):
        #time.sleep(8)
        count = 1
        prev = u''
        encoded = u""
        #lst = []

        # input_string = self.re_pattern_char_recognition.findall(input_string)
        # # if isinstance(input_string, unicode):
        # #     input_string = self.gc.grapheme_clusters(input_string)
        # # elif isinstance(input_string, str):
        # #     input_string = self.gc.grapheme_clusters(unicode(input_string,"utf-8"))  

        for character in self.get_chars(input_string):
            if character != prev:
                if prev:
                    #entry = (prev,count)
                    #lst.append(entry)
                    encoded +=  u"{}".format(prev)
                    #print lst
                count = 1
                prev = character
            else:
                count += 1
        else:
            try:
                #entry = (character,count)
                #lst.append(entry)
                encoded +=  u"{}".format(character)
                return encoded
            except Exception as e:
                if self.logger:
                    self.logger.error("RLE: Exception encountered {e}".format(e=e),  exc_info=True)
                else:
                    print("Exception encountered {e}".format(e=e)) 



    def get_repetativ_elems(self, encoded_rle_to_tuples, repeat_up=3):
        #p(encoded_rle_to_tuples)
        extracted_reps = []
        char_index = -1
        for char_container in encoded_rle_to_tuples:
            char_index += 1
            #rep_free_token += char_container[0]
            if char_container[1] >=  repeat_up:
                extracted_reps.append((char_container[0], char_container[1],char_index))
        return extracted_reps


    def rep_extraction_word(self,encoded_rle_to_tuples, repeat_up=3, get_rle_as_str=False):
        extracted_reps = []
        rep_free_word = ""
        char_index = -1
        #p(encoded_rle_to_tuples, "encoded_rle_to_tuples")
        if not get_rle_as_str:
            for char_container in encoded_rle_to_tuples:
                char_index += 1
                rep_free_word += char_container[0]
                if char_container[1] >=  repeat_up:
                    extracted_reps.append((char_container[0], char_container[1],char_index))
            
            return extracted_reps, rep_free_word
        else:
            #p(encoded_rle_to_tuples,"encoded_rle_to_tuples")
            rle_word = ""
            for char_container in encoded_rle_to_tuples:
                char_index += 1
                rep_free_word += char_container[0]
                rle_word += char_container[0]+"^"+str(char_container[1]) if char_container[1]> 1 else char_container[0]
                if char_container[1] >=  repeat_up:
                    extracted_reps.append((char_container[0], char_container[1],char_index))
            #p(rep_free_word, "rep_free_word", c="r")
            return extracted_reps, rep_free_word,rle_word


    def rep_extraction_sent(self,encoded_rle_to_tuples,mappped, repeat_up=2): #,rle_for_repl_in_text_container=False,repl_free_text_container=False,
        extracted_reps = []
        rep_free_sent = []
        char_index = -1
        #p(encoded_rle_to_tuples, "encoded_rle_to_tuples")
        #p(mappped,"mappped")
        #if not rle_for_repl_in_text_container:
        for char_container in encoded_rle_to_tuples:
            char_index += 1
            #p(repr(char_container[0]), "char_container[0]",c="m")
            #index_in_redu_free = 0
            rep_free_sent.append(char_container[0])
            if char_container[1] >=  repeat_up:
                extracted_reps.append({"word":char_container[0], "length":char_container[1], "start_index_in_orig":mappped[char_index], "index_in_redu_free":char_index})
                #extracted_reps.append((char_container[0], char_container[1],char_container[2],char_index))
        return extracted_reps, rep_free_sent





    def get_rep_free_word_from_rle_in_tuples(self, encoded_rle_to_tuples, decode_to_unicode=True):
        if decode_to_unicode:
            return u"".join([char[0] for char in encoded_rle_to_tuples])
        else:
            return "".join([char[0] for char in encoded_rle_to_tuples])


    def get_rep_free_sent_from_rle_in_tuples(self, encoded_rle_to_tuples, decode_to_unicode=True):
        if decode_to_unicode:
            return u" ".join([char[0].decode("utf-8") for char in encoded_rle_to_tuples])
        else:
            return " ".join([char[0] for char in encoded_rle_to_tuples])

    def convert_rle_intuples_to_rle_as_str(self, encoded_rle_to_tuples):
        pass



    def encode_to_tuples(self,input_string, mapping=False):
        count = 1
        prev = ''
        lst = []
        if mapping: mapped = []
        #p(input_string, "input_string")
        i = -1
        start_index = None
        for character in self.get_chars(input_string):
            i+=1

            if character != prev:
                if prev:
                    #p((character, prev, i,start_index))
                    #start_index = start_index if start_index else i
                    entry = (prev,count)
                    #p((prev,count,start_index), c="m")
                    lst.append(entry)

                    if mapping: mapped.append(start_index)
                    #print lst
                    start_index = None
                if start_index is None:
                    start_index = i
                count = 1
                prev = character
            else:
                count += 1
        else:
            try:
                entry = (character,count)
                if mapping: mapped.append(start_index)
                #p((character,count,i), c="r")
                lst.append(entry)
                #start_index = None
                if mapping:
                    return lst, mapped
                else:
                    return lst
            except Exception as e:
                if self.logger:
                    self.logger.error("RLE: Exception encountered {e}".format(e=e), exc_info=True)
                else:
                    print("Exception encountered {e}".format(e=e)) 
                if mapping:
                    return False, False
                else:
                    return False

    def decode_words_to_str(self,lst):
        try:
            q = ""
            #prev = ""
            for word, count in lst:
                q += (word+" ") * count
            return q.strip()
        except Exception, e:
            if self.logger:
                self.logger.error(" RLE:Exception encountered {e}".format(e=e),  exc_info=True)
            else:
                print("Exception encountered {e}".format(e=e)) 

    def decode_words_to_list(self,lst):
        try:
            q = []
            #prev = ""
            for word, count in lst:
                for c in xrange(count):
                    q.append(word)
            return q
        except Exception, e:
            if self.logger:
                self.logger.error(" RLE:Exception encountered {e}".format(e=e),  exc_info=True)
            else:
                print("Exception encountered {e}".format(e=e)) 




    def decode_letters_to_str(self,lst):
        try:
            q = ""
            for character, count in lst:
                q += character * count
            return q
        except Exception, e:
            if self.logger:
                self.logger.error("RLE: Exception encountered {e}".format(e=e), exc_info=True)
            else:
                print("Exception encountered {e}".format(e=e)) 



    def encode_str_to_str(self,input_string):
        count = 1
        prev = u''
        encoded = u""
        #lst = []
        # if isinstance(input_string, unicode):
        #     input_string = self.gc.grapheme_clusters(input_string)
        # elif isinstance(input_string, str):
        #     input_string = self.gc.grapheme_clusters(unicode(input_string,"utf-8"))  

        for character in self.get_chars(input_string):
            if character != prev:
                if prev:
                    #entry = (prev,count)
                    #lst.append(entry)
                    encoded +=  u"{}{}".format(prev,count)
                    #print lst
                count = 1
                prev = character
            else:
                count += 1
        else:
            try:
                #entry = (character,count)
                #lst.append(entry)
                encoded +=  u"{}{}".format(character,count)
                return encoded
            except Exception as e:
                if self.logger:
                    self.logger.error("RLE: Exception encountered {e}".format(e=e),  exc_info=True)
                else:
                    print("Exception encountered {e}".format(e=e)) 



    def decode_str_from_str(self,inp_str):

        pattern = regex.compile(r"(.+?)(\d+)")
        matched = regex.findall(pattern, inp_str)
        #p(matched)
        if not matched:
            if self.logger:
                self.logger.error("RLE: Given Str to encode had not correct structure!",  exc_info=True)
            else:
                print("RLE: Given Str to encode had not correct structure!")

        try:
            return self.decode_letters_to_str([(t[0], int(t[1])) for t in matched])
        except:
            if self.logger:
                self.logger.error("RLE: Given Str to encode had not correct structure!",  exc_info=True)
            else:
                print("RLE: Given Str to encode had not correct structure!")            

rle = Rle()


class LenGen(object):
    def __init__(self,gen,length):
        self.gen=gen
        self.length=length
    def __call__(self):
        return itertools.islice(self.gen(),self.length)
    def __len__(self):
        return self.length

    def __iter__(self):
        #self._gen = self.gen
        return self.gen



nextHighest = lambda seq,x: min([(i-x,i) for i in seq if x<=i] or [(0,None)])[1]
nextLowest  = lambda seq,x: min([(x-i,i) for i in seq if x>=i] or [(0,None)])[1]




def _async_raise(tid, exctype):
    """raises the exception, performs cleanup if needed"""
    if not inspect.isclass(exctype):
        raise TypeError("Only types can be raised (not instances)")
    res = ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, ctypes.py_object(exctype))
    if res == 0:
        raise ValueError("invalid thread id")
    elif res != 1:
        # """if it returns a number greater than one, you're in trouble, 
        # and you should call it again with exc=NULL to revert the effect"""
        ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, 0)
        raise SystemError("PyThreadState_SetAsyncExc failed")


class MyThread(threading.Thread):
    #http://tomerfiliba.com/recipes/Thread2/
    def _get_my_tid(self):
        """determines this (self's) thread id"""
        if not self.isAlive():
            raise threading.ThreadError("the thread is not active")
        
        # do we have it cached?
        if hasattr(self, "_thread_id"):
            return self._thread_id
        
        # no, look for it in the _active dict
        for tid, tobj in threading._active.items():
            if tobj is self:
                self._thread_id = tid
                return tid
        
        raise AssertionError("could not determine the thread's id")
    
    def raise_exc(self, exctype):
        """raises the given exception type in the context of this thread"""
        _async_raise(self._get_my_tid(), exctype)

    
    def terminate(self):
        """raises SystemExit in the context of the given thread, which should 
        cause the thread to exit silently (unless caught)"""
        self.raise_exc(SystemExit)
        print "'{}'-Thread was terminated.".format(self.name)  



def ngrams(token_list, n):
    return [tuple(token_list[i:i+n]) for i in xrange(len(token_list)-n+1)]

# class InternTuple()
#     def __init__(self):
#         adress = 0
#         self.table = {}



def char_is_punkt(character):
    return character in punkt_str


def text_is_punkt(text):
    for char in text:
        if char not in punkt_str:
            return False
    else:
        return True

#def text_is_punkt(text):
    # flags = set([True if character in punkt_str else False for character in text ])
    # if len(flags) == 1 and True in flags:
    #     return True 
    # return False

def text_is_emoji(text):
    flags = set([True if character in emoji.UNICODE_EMOJI else False for character in text ])
    if len(flags) == 1 and True in flags:
        return True 
    return False



# def is_emoticon(character):
#     #if character[0] in ['#', '$', ')', '(', '*', '-', '/', '8', ';', ':', '=', '<', '>', '@', '\\', '^', 'b', 'o', 'x', '{', '|', '~']:
#     return rle.del_rep(character) in emoticons1

def is_emoticon(character):
    #if character[0] in ['#', '$', ')', '(', '*', '-', '/', '8', ';', ':', '=', '<', '>', '@', '\\', '^', 'b', 'o', 'x', '{', '|', '~']:
    if character[0] in punkt_str:
        replfree = rle.del_rep(character)
        if replfree.lower() in emoticons:
            #### This is for those emoticons, like "))))", or "((((". But if character was replicated many times. if not, than it is just an punctuation symbol.
            if len(replfree) == 1:
                if len(character) > 1:
                    return True
                else:
                    return False
            else:
                return True
        else:
            return False
    else:
        return False




    
url_compiled_pattern = re.compile('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
def is_url(inptoken):
    urls = url_compiled_pattern.findall( inptoken)
    if urls:
        return True
    return False


def categorize_token(inptoken):
    try:
        if inptoken.isdigit():
            return "number"
        elif is_emoji(inptoken):
            return "EMOIMG"
        elif is_emoticon(inptoken):
            #print "-----", inptoken,is_emoticon(inptoken)
            return "EMOASC"
        elif text_is_punkt(inptoken):
            return "symbol"
        elif inptoken[0] == "@":
            return "mention"
        elif inptoken[0] == "#":
            return "hashtag"
        elif is_url(inptoken):
            return "URL"

        return "regular"
    except:
        return None


def categorize_token_list(inpliste):
    return [(token, categorize_token(token)) for token in inpliste]


def categorize_emoticon(inptoken):
    try:
        if is_emoji(inptoken):
            return "EMOIMG"
        elif is_emoticon(inptoken):
            return "EMOASC"
        return None
    except:
        return None

def recognize_emoticons_types(inpliste):
    output_list = []
    for token in inpliste:
        cat = categorize_emoticon(token[0])
        if cat:
            output_list.append((token[0], cat))
        else:
            output_list.append(token)
    return output_list

def get_categories(inpliste):
    return [ categorize_token(token) for token in inpliste]



def removetags(raw_html):
  cleanr = re.compile('<.*?>')
  cleantext = re.sub(cleanr, '', raw_html)
  return cleantext

def remove_html_codded_chars(raw_html):
    # &#13
  cleanr = re.compile('&.*?;')
  cleantext = re.sub(cleanr, '', raw_html)
  return cleantext


def text_has_punkt(text):
    for character in text:
        if character in punkt_str:
            return True
    return False


def is_emoji(character):
    return character in emoji.UNICODE_EMOJI




def text_has_emoji(text):
    for character in text:
        if character in emoji.UNICODE_EMOJI:
            return True
    return False



def internet_on():
    try:
        urllib2.urlopen('http://216.58.192.142', timeout=1)
        return True
    except urllib2.URLError as err:
        return False


def set_class_mode(mode):
    if  mode in  modi:
        if mode == "dev":
            logger_level = logging.DEBUG
            logger_traceback = True
            logger_save_logs = True
            save_status = True
            Status.allow_full_tb = True
            Status.allow_auto_func_names = True
            Status.allow_auto_arginfo = True
            Status.light_mode = False
            ZASLogger._save_lower_debug = True
            ZASLogger._set_functon_name_as_event_name = False
            ZASLogger._save_debug = True
            log_content = True
            save_settings = True
            logger_usage = True
            ext_tb = False
        elif mode == "dev-":
            logger_level = logging.INFO
            logger_traceback = True
            logger_save_logs = True
            save_status = True
            Status.allow_full_tb = False
            Status.allow_auto_func_names = True
            Status.allow_auto_arginfo = True
            Status.light_mode = False
            ZASLogger._save_lower_debug = True
            ZASLogger._set_functon_name_as_event_name = False
            ZASLogger._save_debug = True
            log_content = False
            save_settings = True
            logger_usage = True
            ext_tb = False
        elif mode == "dev+":
            logger_level = 9
            logger_traceback = True
            logger_save_logs = True
            save_status = True
            Status.allow_full_tb = True
            Status.allow_auto_func_names = True
            Status.allow_auto_arginfo = True
            Status.light_mode = False
            ZASLogger._save_lower_debug = True
            ZASLogger._set_functon_name_as_event_name = False
            ZASLogger._save_debug = True
            log_content = True
            save_settings = True
            logger_usage = True
            ext_tb = True
        elif mode == "test":
            logger_level = logging.ERROR
            logger_traceback = True
            Status.light_mode = True
            logger_save_logs = False
            ZASLogger._save_lower_debug = False
            ZASLogger._save_debug = False
            ZASLogger._set_functon_name_as_event_name = False
            save_status = False
            log_content = False
            save_settings = False
            logger_usage = True
            ext_tb = False
        elif mode == "prod":
            logger_level = logging.INFO
            logger_traceback = True
            logger_save_logs = True
            Status.light_mode = True
            ZASLogger._save_lower_debug = False
            ZASLogger._save_debug = False
            ZASLogger._set_functon_name_as_event_name = False
            save_status = False
            log_content = False 
            save_settings = True
            logger_usage = True
            ext_tb = False
        elif mode == "prod+":
            logger_level = logging.INFO
            logger_traceback = True
            logger_save_logs = True
            Status.light_mode = True
            ZASLogger._save_lower_debug = False
            ZASLogger._save_debug = False
            ZASLogger._set_functon_name_as_event_name = False
            save_status = False
            log_content =  True
            save_settings = True
            logger_usage = True
            ext_tb = False
        elif mode == "prod-":
            logger_level = logging.INFO
            logger_traceback = False
            logger_save_logs = False
            Status.light_mode = True
            ZASLogger._save_lower_debug = False
            ZASLogger._save_debug = False
            ZASLogger._set_functon_name_as_event_name = False
            save_status = False
            log_content = False 
            save_settings = False
            logger_usage = True
            ext_tb = False
        elif mode == "prod+t":
            logger_level = logging.INFO
            logger_traceback = True
            logger_save_logs = False
            Status.light_mode = True
            ZASLogger._save_lower_debug = False
            ZASLogger._save_debug = False
            ZASLogger._set_functon_name_as_event_name = False
            save_status = False
            log_content = False
            save_settings = False
            logger_usage = False
            ext_tb = False
        elif mode == "test+s+":
            logger_level = logging.INFO
            logger_traceback = True
            logger_save_logs = True
            Status.light_mode = True
            ZASLogger._save_lower_debug = True
            ZASLogger._save_debug = True
            save_status = True
            log_content = True
            Status.allow_full_tb = True
            Status.allow_auto_func_names = True
            Status.allow_auto_arginfo = True#
            ZASLogger._set_functon_name_as_event_name = True
            save_settings = True
            logger_usage = True
            ext_tb = False
        elif mode == "test+s-":
            logger_level = logging.ERROR
            logger_traceback = True
            logger_save_logs = True
            Status.light_mode = True
            ZASLogger._save_lower_debug = True
            ZASLogger._save_debug = True
            save_status = True
            log_content = False
            Status.allow_full_tb = True
            Status.allow_auto_func_names = True
            Status.allow_auto_arginfo = True#
            ZASLogger._set_functon_name_as_event_name = True
            save_settings = True
            logger_usage = True
            ext_tb = False
        elif mode == "silent":
            logger_level = logging.ERROR
            logger_traceback = False
            logger_save_logs = False
            Status.light_mode = True
            ZASLogger._save_lower_debug = False
            ZASLogger._save_debug = False
            save_status = False
            log_content = False
            Status.allow_full_tb = False
            Status.allow_auto_func_names = False
            Status.allow_auto_arginfo = False#
            ZASLogger._set_functon_name_as_event_name = False
            save_settings = False
            logger_usage = False
            ext_tb = False

            
    else:
        msg = "CorpusError: Given Mode '{}' is not supported. Please use one of the following modi: '{}'. ".format(mode,  modi)
        if platform.uname()[0].lower() !="windows":
            p(msg,"ERROR", c="r")
        else:
            print msg

    return logger_level, logger_traceback, logger_save_logs, save_status, log_content, save_settings, logger_usage, ext_tb

def print_mode_name(mode, logger):
    if  mode in  modi:
        if mode == "dev":
            logger.debug("DEVELOPING MODE was started!")
        elif mode == "dev-":
            logger.debug("DEVELOPING MODE(-) was started!")
        elif mode == "dev+":
            logger.debug("DEVELOPING MODE(+) was started!")
        elif mode == "test":
            logger.debug("TEST MODE was started!")
        elif mode == "prod":
            logger.debug("PRODUCTION Mode was started!")
        elif mode == "free":
            logger.debug("FREE Mode was started!")
    else:
        msg = "Given Mode '{}' is not supported. Please use one of the following modi: '{}'. ".format(mode,  modi)
        if platform.uname()[0].lower() !="windows":
            p(msg,"ERROR", c="r")
        else:
            print msg



def make_zipfile(output_filename, source_dir):
    relroot = os.path.abspath(os.path.join(source_dir, os.pardir))
    with zipfile.ZipFile(output_filename, "w", zipfile.ZIP_DEFLATED, allowZip64=True) as zip:
        for root, dirs, files in os.walk(source_dir):
            # add directory (needed for empty dirs)
            zip.write(root, os.path.relpath(root, relroot))
            for file in files:
                filename = os.path.join(root, file)
                if os.path.isfile(filename): # regular files only
                    arcname = os.path.join(os.path.relpath(root, relroot), file)
                    zip.write(filename, arcname)


def get_number_of_streams_adjust_cpu( min_files_pro_stream, row_number, stream_number, cpu_percent_to_get=50):
    if row_number <= 0: 
        return None

    if min_files_pro_stream <= 0:
        min_files_pro_stream = 1

    ## get possible thread number
    processors_number = psutil.cpu_count()
    if processors_number  > 1:
        processors_to_use = int((cpu_percent_to_get * processors_number) / 100.0) # to use 50% of CPUs
    else:
        processors_to_use  = 1

    if stream_number > processors_to_use:
        stream_number = processors_to_use

    
    temp_stream_number = int(Decimal(float(row_number) / min_files_pro_stream).quantize(Decimal('1.'), rounding=ROUND_DOWN))
    #p(temp_stream_number, "temp_stream_number", c="r")
    if  temp_stream_number <= stream_number:
        if temp_stream_number >0:
            return  temp_stream_number
        else:
            return 1
    else:
        return stream_number



# def get_number_of_threads_adjust_cpu( min_files_pro_thread, whole_file_number,  thread_number=False):
#     if whole_file_number <= 0: 
#         return None

#     processors_number = psutil.cpu_count()
#     if processors_number  > 1:
#         processors_to_use = int((50 * processors_number) / 100.0) # to use 50% of CPUs
#     else:
#         processors_to_use  = 1

#     if thread_number:
#         if thread_number < processors_to_use:
#             thread_number = thread_number
#         else:
#             thread_number = processors_to_use
#     else:
#         thread_number =  processors_to_use
#     threads_to_create = thread_number
#     #p((processors_number, processors_to_use, thread_number,threads_to_create, whole_file_number,min_files_pro_thread ))        
#     while threads_to_create != 1:
#         number_of_files_per_thread = whole_file_number/threads_to_create

#         if number_of_files_per_thread >= min_files_pro_thread:
#             break
#         else:
#             threads_to_create -=1
#             continue

#         if threads_to_create == 1:
#             break

#     return threads_to_create



def get_file_list(path, extention):
    if os.path.isdir(path):
        txt_files = [file for file in os.listdir(path) if extention in file]
        if txt_files:
            return  (path,txt_files)
        else:
            False
    else:
        return False


def instance_info(instance_dict, attr_to_ignore=False, attr_to_flag=False, attr_to_len=False, as_str=False):
    #instance_dict = json.loads(instance_dict)
    instance_dict = copy.deepcopy(instance_dict)
    #p(instance_dict)
    instance_dict = OrderedDict(instance_dict)
    if attr_to_ignore:
        for attr in  attr_to_ignore:
            if attr in instance_dict:
                del instance_dict[attr]

    if attr_to_flag:
        for attr in attr_to_flag:
            if attr in instance_dict:
                instance_dict[attr] = "|FLAG|:|True|" if instance_dict[attr] else "|FLAG|:|False|"

    if attr_to_len:
        for attr in attr_to_len:
            if attr in instance_dict:
                instance_dict[attr] = "|LEN|:|{}|".format(len(instance_dict[attr])) if isinstance(instance_dict[attr], (str, unicode, list,tuple, bool, int, dict)) else "|LEN|:|NOT_COUNTABLE|"

    if as_str:
        attr_as_str = ""
        for k,v in instance_dict.iteritems():
            attr_as_str += "\n    ---> {}  :  {} ".format(k,v)
        return attr_as_str
    else:
        return instance_dict


def paste_new_line():
    print "\n"

global last_path
last_path = ""



def write_data_to_json(path, data):
    global last_path
    if last_path == path: 
        p("WriteDataToJsonError'{}'-File was opened one more time.".format(last_path))
    #json_file = io.open(path, "w", encoding="utf-8")
    with  codecs.open(path, "w", encoding="utf-8") as f:
        f.write(unicode(json.dumps(data,
                            indent=4, sort_keys=True,
                            separators=(',', ': '), ensure_ascii=False)))
        last_path = path

#send_email("egor@savin.berlin", "dfghjkl", "fghjkl")

def send_email(toaddr,Subject, text):
    logger = main_logger("MailSender")

    if toaddr:
        fromaddr = 'zas.rep.tools@gmail.com'
        #toaddrs  = ['receiving@gmail.com']
        #Date: {time}<CRLF>
        #Message-ID: <AauNjVuMhvq0000007c@elsewhere.com><CRLF>
        #From: "Mr. Error Informer" <{fromaddr}><CRLF>
        #To: "Mrs. Someone" <{toaddr}><CRLF>
        msg = MIMEMultipart()
        msg['From'] = fromaddr
        msg['To'] = toaddr
        msg['Subject'] = Subject
        msg.attach(MIMEText(text, 'html'))
        server_answer = ''
        try_number= 0
        while True:
            try:
                #server = smtplib.SMTP('smtp.gmail.com:25')
                server = smtplib.SMTP_SSL('smtp.gmail.com:465')
                #server.starttls()
                server.login('zas.rep.tools@gmail.com', 'gxtgjjemskhndfag')
                server_answer = server.sendmail(fromaddr,toaddr ,msg.as_string())
                server.quit()

                logger_msg = "Email was send to: '{}'.\n (If you don't get an Email:  1) check if the given Address is correct; 2) or check also in your Spam-Folder;) ".format(toaddr)
                logger.info(logger_msg) 
            except socket.gaierror, e:
                if try_number==0:
                    logger_msg = "\rEmailSendingError: (Socket.gaierror) Smtplib returned  the following Problem: ‘{}‘. (Check your Internet Connection or DNS Server.)".format(e)
                    logger.error(logger_msg) 
                    print logger_msg
                time.sleep(30)
                try_number+=1
            except Exception, e:
                logger_msg = "\nEmailSendingError: SMTP-Server returned  the following Problem: ‘{}‘ ".format(e)
                print logger_msg
                logger.error(logger_msg) 
            finally:
                #p(server_answer)
                if server_answer:
                    logger_msg = "\nEmailSendingError: SMTP Server returned following error: ‘{}‘.".format(server_answer, "http://www.supermailer.de/smtp_reply_codes.htm")
                    return False
                
                break

#\033[1A