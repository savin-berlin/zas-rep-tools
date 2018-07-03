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
from zas_rep_tools.src.utils.logger import Logger
import io
import json
import inspect
import zipfile
import socket


path_to_zas_rep_tools = os.path.dirname(os.path.dirname(os.path.dirname(inspect.getfile(Logger))))


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


def write_data_to_json(path, data):
    json_file = io.open(path, "a", encoding="utf-8")
    json_file.write(unicode(json.dumps(data,
                        indent=4, sort_keys=True,
                        separators=(',', ': '), ensure_ascii=False)))
    json_file.close()

#send_email("egor@savin.berlin", "dfghjkl", "fghjkl")

def send_email(toaddr,Subject, text):
    logger = Logger().myLogger("MailSender")
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