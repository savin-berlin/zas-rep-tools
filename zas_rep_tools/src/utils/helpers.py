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
        try:
            #server = smtplib.SMTP('smtp.gmail.com:25')
            server = smtplib.SMTP_SSL('smtp.gmail.com:465')
            #server.starttls()
            server.login('zas.rep.tools@gmail.com', 'gxtgjjemskhndfag')
            server_answer = server.sendmail(fromaddr,toaddr ,msg.as_string())
            server.quit()

            logger_msg = "Error-Email was send to: '{}'. (If you don't get an Email:  1) check if the given Address is correct; 2) or check also in your Spam-Folder;) ".format(toaddr)
            logger.info(logger_msg) 
        except Exception, e:
            logger_msg = "\nEmailSendingError: SMTP-Server returned  the following Problem: ‘{}‘ ".format(e)
            logger.error(logger_msg) 
        finally:
            #p(server_answer)
            if server_answer:
                logger_msg = "\nEmailSendingError: SMTP Server returned following error: ‘{}‘.".format(server_answer, "http://www.supermailer.de/smtp_reply_codes.htm")

                logger.error(logger_msg) 


             