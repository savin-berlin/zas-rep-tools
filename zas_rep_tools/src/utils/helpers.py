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
import psutil
from decimal import Decimal, ROUND_HALF_UP, ROUND_UP, ROUND_HALF_DOWN, ROUND_DOWN



from zas_rep_tools.src.utils.logger import main_logger
from zas_rep_tools.src.utils.debugger import p



path_to_zas_rep_tools = os.path.dirname(os.path.dirname(os.path.dirname(inspect.getfile(p))))


modi = ["test", "dev", "prod", "free", "prod+t", "test+s"]
punkt_str = """!"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"""
emoticons = ['(.V.)', 'O:-)', 'X-(', '~:0', ':-D', '(*v*)', ':-#', '</3', '=^.^=', '*<:o)', 'O.o', 'B-)', ':_(', ":'(", '\\:D/', '*-*', ':o3', '#-o', ':*)', '//_^', '>:)', '<><', ':-(', ':(', ':-(', '=P', ':-P', '8-)', '$_$', ':->', '=)', ':-)', ':)', '<3', '{}', ':-|', 'X-p', ':-)*', ':-*', ':*', '(-}{-)', 'XD', '=D', ')-:', '(-:', '<3', '=/', ':-)(-:', '<:3)~', '~,~', ':-B', '^_^', '<l:0', ':-/', '=8)', '@~)~~~~', '=(', ':-(', ':(', ':S', ':-@', '=O', ':-o', ':-)', ':)', ':-Q', ':>', ':P', ':o', ':-J', ':-&', '=-O', ':-\\', ':-E', '=D', ';-)', ';)', '|-O', '8-#']


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


class Rle(object):
    def __init__(self, logger=False):
        from uniseg import graphemecluster as gc
        self.gc = gc
        self.logger = logger

    def del_rep(self, input_string):
        count = 1
        prev = u''
        encoded = u""
        #lst = []
        if isinstance(input_string, unicode):
            input_string = self.gc.grapheme_clusters(input_string)
        elif isinstance(input_string, str):
            input_string = self.gc.grapheme_clusters(unicode(input_string,"utf-8"))  

        for character in input_string:
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


    def encode_to_tuples(self,input_string):
        count = 1
        prev = ''
        lst = []
        if isinstance(input_string, unicode):
            input_string = self.gc.grapheme_clusters(input_string)
        elif isinstance(input_string, str):
            input_string = self.gc.grapheme_clusters(unicode(input_string,"utf-8"))  

        for character in input_string:
            if character != prev:
                if prev:
                    entry = (prev,count)
                    lst.append(entry)
                    #print lst
                count = 1
                prev = character
            else:
                count += 1
        else:
            try:
                entry = (character,count)
                lst.append(entry)
                return lst
            except Exception as e:
                if self.logger:
                    self.logger.error("RLE: Exception encountered {e}".format(e=e), exc_info=True)
                else:
                    print("Exception encountered {e}".format(e=e)) 
                   
                return False

    def decode_words_to_str(self,lst):
        try:
            q = ""
            for word, count in lst:
                q += (word+" ") * count
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
        if isinstance(input_string, unicode):
            input_string = self.gc.grapheme_clusters(input_string)
        elif isinstance(input_string, str):
            input_string = self.gc.grapheme_clusters(unicode(input_string,"utf-8"))  

        for character in input_string:
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
        try:
            q = ""
            if isinstance(inp_str, unicode):
                inp_str = self.gc.grapheme_clusters(inp_str)
            else:
                inp_str = self.gc.grapheme_clusters(unicode(inp_str,"utf-8")) 
            inp_str = list(inp_str)
            i = 0
            for character,count  in zip(inp_str,inp_str[1:]):
                #print character, "  ",count
                for i in xrange(int(count)):
                    q +=  character 
            return q
        except Exception, e:
            if self.logger:
                self.logger.error("RLE: Exception encountered {e}".format(e=e),  exc_info=True)
            else:
                print("Exception encountered {e}".format(e=e)) 




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





def char_is_punkt(character):
    return character in punkt_str


def text_is_punkt(text):
    flags = set([True if character in punkt_str else False for character in text ])
    if len(flags) == 1 and True in flags:
        return True 
    return False

def text_is_emoji(text):
    flags = set([True if character in emoji.UNICODE_EMOJI else False for character in text ])
    if len(flags) == 1 and True in flags:
        return True 
    return False

def is_emoticon(character):
    return character in emoticons
    

def is_url(inptoken):
    urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', inptoken)
    if urls:
        return True
    return False


def categorize_token(inptoken):
    try:
        if char_is_emoji(inptoken):
            return "emoji"
        elif is_emoticon(inptoken):
            return "emoticon"
        elif text_is_punkt(inptoken):
            return "symbol"
        elif is_url(inptoken):
            return "URL"
        elif inptoken.isdigit():
            return "number"
        elif inptoken[0] == "@":
            return "mention"
        elif inptoken[0] == "#":
            return "hashtag"


        return "regular"
    except:
        return None


def categorize_token_list(inpliste):
    return [(token, categorize_token(token)) for token in inpliste]



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


def char_is_emoji(character):
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
        elif mode == "test":
            logger_level = logging.ERROR
            logger_traceback = True
            logger_save_logs = False
        elif mode == "prod":
            logger_level = logging.INFO
            logger_traceback = True
            logger_save_logs = None
        elif mode == "prod+t":
            logger_level = logging.INFO
            logger_traceback = True
            logger_save_logs = None
        elif mode == "test+s":
            logger_level = logging.ERROR
            logger_traceback = True
            logger_save_logs = True

            
    else:
        msg = "CorpusError: Given Mode '{}' is not supported. Please use one of the following modi: '{}'. ".format(mode,  modi)
        if platform.uname()[0].lower() !="windows":
            p(msg,"ERROR", c="r")
        else:
            print msg

    return logger_level, logger_traceback, logger_save_logs

def print_mode_name(mode, logger):
    if  mode in  modi:
        if mode == "dev":
            logger.debug("DEVELOPING MODE was started!")
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


def get_number_of_streams_adjust_cpu( min_files_pro_stream, row_number, stream_number):
    if row_number <= 0: 
        return None

    if min_files_pro_stream <= 0:
        min_files_pro_stream = 1

    ## get possible thread number
    processors_number = psutil.cpu_count()
    if processors_number  > 1:
        processors_to_use = int((50 * processors_number) / 100.0) # to use 50% of CPUs
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


def paste_new_line():
    print "\n"

global last_path
last_path = ""

def write_data_to_json(path, data):
    global last_path
    if last_path == path: 
        p((path, data))

    json_file = io.open(path, "w", encoding="utf-8")
    json_file.write(unicode(json.dumps(data,
                        indent=4, sort_keys=True,
                        separators=(',', ': '), ensure_ascii=False)))
    last_path = path
    json_file.close()

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