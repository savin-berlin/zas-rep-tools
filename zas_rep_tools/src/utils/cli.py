#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# : Utilities for Command Line Interface  
# Author:
# c(Student) ->     {'Egor Savin'}
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

###Programm Info######

from zas_rep_tools.src.utils.logger import Logger

import logging
import inspect
import os
import codecs
import ast
import re
import json


from zas_rep_tools.src.classes.corpus import Corpus
from zas_rep_tools.src.utils.debugger import p

path_to_zas_rep_tools = os.path.dirname(os.path.dirname(os.path.dirname(inspect.getfile(Corpus))))
path_to_file_with_twitter_creditials = "user-config/twitter_api_credentials.json"
path_to_file_with_user_agreements = "user-config/user_agreement.json"

def logger_initialisation(logger_name,use_logger, save_logs, logs_dir):
    # ##### Logger Initialisation: #######
    if (use_logger== "False" or use_logger== u"False"):
        use_logger = False

    if (save_logs== "True" or save_logs== u"True"):
        save_logs = True

    # use_logger = False if (use_logger== "False" or use_logger== u"False") else
    global logger 
    logger = Logger()
    logger = logger.myLogger2(folder_for_log=logs_dir, logger_name=logger_name, use_logger=use_logger, save_logs=save_logs)

    return logger


def was_user_asked_for_agreement():
    if os.path.isfile(os.path.join(path_to_zas_rep_tools, path_to_file_with_user_agreements)):
        agreement_data = get_agreement_data()
        try:
            agreement_data['error_tracking']
        except:
            return False

        return True
    else:
        return False


def get_agreement_data():
    if os.path.isfile(os.path.join(path_to_zas_rep_tools, path_to_file_with_user_agreements)):
        f = codecs.open(os.path.join(path_to_zas_rep_tools, path_to_file_with_user_agreements), "r", encoding="utf-8")
        agreement_data= json.load(f)
        return agreement_data

    return False

def respeak_agreement():
    ask_user_agreement()


def is_error_tracking_allowed():
    if os.path.isfile(os.path.join(path_to_zas_rep_tools, path_to_file_with_user_agreements)):
        agreement_data = get_agreement_data()
        if not agreement_data:
            return False

        if agreement_data['error_tracking'] == True:
            return True
        else:
            return False

def ask_user_agreement():
    print "\n\n----------------------------------------\n"
    print "----------------------------------------\n"
    print "1. Thank you for choosing this module. For making this tool better for you in the future we want to  tracking error automatically.\n Please answer yes/no if you agree or disagree with that.\n"
    input_var_1 = ""

    while input_var_1 not in ["yes", "no", True, False]:
        #p(input_var_1)
        input_var_1 = raw_input("Your answer: ")
        #p(input_var)
        if input_var_1 == "yes":
            print "\n\nThank you for allow error tracking."
            input_var_1 = True
        elif input_var_1 == "no":
            print "\n\nWe deactivate error tracking for this copy of the zas-rep-tool. Enjoy!=)=)=)"
            input_var_1 = False
        else: 
            print "We can not understand your answer. Please  choice one of the both possible answers ['yes','no']"


    print "\n\n----------------------------------------\n"
    print "----------------------------------------\n"
    print "2. For some functions we need your E-mail Address. (e.g. Send Error Messages, if streaming was stopped)\n    Your Email Address will be not given to the third party and you can every time delete it.\n    Just use following command 'zas-rep-tools deleteAllUserData' or 'zas-rep-tools respeakAgreement' \n\n (Please answer yes/no if you want to enter your Email Address)\n"
    

    input_var_2 = ""
    while input_var_2 not in ["yes", "no", True, False]:
        input_var_2 = raw_input("Your answer: ")
        if input_var_2 == "yes":


            input_var_3 = ""
            found = False
            while not found:
                if not found:
                    patter_email = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9.]+$)"
                    input_var_3 = raw_input("\nGive your Email Address: ")
                    matcher = re.match(patter_email, input_var_3)
                #p(matcher)
                if matcher:
                    found = True
                    email = matcher.group(0)
                    print "\n\nYour Email Address was added. "
                else:
                    print "Given Email Address is not valid. Please retype it"
                    #email = None


        elif input_var_2 == "no":
            print "\n\nWe deactivate email-communication for this copy of the zas-rep-tool. Enjoy!=)=)=)"
            email = False
        else: 
            print "We can not understand your answer. Choice one of the both possible answers ['yes','no']"
            #print "Exit...."
            #os._exit(1)
    #exit()
    if not os.path.isdir(os.path.join(path_to_zas_rep_tools,"user-config")):
        os.mkdir(os.path.join(path_to_zas_rep_tools,"user-config"))
    #email = "'{}'".format(email) if email else email


    user_agreements_data = {}
    user_agreements_data.update({'error_tracking': input_var_1, 'email': email, }) 
    
    json_file = codecs.open(os.path.join(path_to_zas_rep_tools, path_to_file_with_user_agreements), "w", encoding="utf-8")
    json_file.write(unicode(json.dumps(user_agreements_data,
                        indent=4, sort_keys=True,
                        separators=(',', ': '), ensure_ascii=False)))
    json_file.close()

    msg = u"\nYour agreement was saved in the following file:\n '{path}'.\n\n Every time in the future you can respeak this agreement.\nJust Use the following command: 'zas-rep-tools respeakAgreement' "
    
    print msg.format(path = os.path.join(path_to_zas_rep_tools, path_to_file_with_user_agreements) )
    #print "Your agreement was saved in the following file "+path_to_file_with_user_agreements + "Every time in the future you can respeak this agreement. For it you need just to change 'True'  to 'False'"





def ask_user_for_twitter_api_data():
    print "\n\n----------------------------------------\n"
    print "----------------------------------------\n"
    print "Bevore you can start with twitter streaming you need enter twitter credentials. \n You can consult a README File (https://github.com/savin-berlin/zas-rep-tools) under 'Start to use streamer' to see  how you can exactly get this data."
    consumer_key = raw_input("\nEnter consumer_key: ")
    consumer_secret = raw_input("Enter consumer_secret: ")
    access_token = raw_input("Enter access_token: ")
    access_token_secret = raw_input("Enter access_token_secret: ")
    
    print "\n\nThank you for entering your data. Do you want to save them on the disk? [yes,no]  \nIt can be helpful for you, if you want to use this streamer more often.\n Notice: You data will be save as plain text, without any encryption and could be visible."
    
    answer = ""
    while answer not in ["yes", "no", True, False]:
        answer = raw_input("\nYour answer: ")
        if answer == "no":
            answer = False
            print "\nYour Twitter API credentials will be just temporary used and after script execution immediately  deleted."
        elif answer == "yes":
            answer = True
        else: 
            print "We can not understand your answer. Please  choice one of the both possible answers ['yes','no']"


    if answer is True:
        api_data = {}
        api_data.update({'consumer_key': consumer_key, 'consumer_secret': consumer_secret, 'access_token':access_token, 'access_token_secret':access_token_secret})
        #file = codecs.open(os.path.join(path_to_zas_rep_tools, path_to_file_with_twitter_creditials), "w")
        #file.write("{} 'consumer_key':'{}','consumer_secret':'{}', 'access_token':'{}', 'access_token_secret':'{}' {}".format("{", consumer_key,consumer_secret,access_token,access_token_secret, "}") )
        #file.close()
        #p(api_data)
        json_file = codecs.open(os.path.join(path_to_zas_rep_tools, path_to_file_with_twitter_creditials), "w", encoding="utf-8")
        json_file.write(unicode(json.dumps(api_data,
                            indent=4, sort_keys=True,
                            separators=(',', ': '), ensure_ascii=False)))
        json_file.close()
        msg = "\nYour twitter API Data was saved in the following file:\n'{}'.\n Every time in the future you can re-speak this agreement and delete all saved user data.\nJust use following command 'zas-rep-tools deleteAllUserData'"
        print msg.format(os.path.join(path_to_zas_rep_tools, path_to_file_with_twitter_creditials))

    return consumer_key, consumer_secret, access_token, access_token_secret 


def was_user_asked_for_path_to_file_with_twitter_creditials():
    if os.path.isfile(os.path.join(path_to_zas_rep_tools, path_to_file_with_twitter_creditials)):
        #api_data = ast.literal_eval(codecs.open(os.path.join(path_to_zas_rep_tools, path_to_file_with_twitter_creditials), "r").read().strip() )
        f = codecs.open(os.path.join(path_to_zas_rep_tools, path_to_file_with_twitter_creditials), "r", encoding="utf-8")

        api_data = json.load(f)
        try:
            api_data['consumer_key']
        except:
            return False

        return True
    else:
        return False


def get_api_data():
    if os.path.isfile(os.path.join(path_to_zas_rep_tools, path_to_file_with_twitter_creditials)):
        #api_data = ast.literal_eval(codecs.open(os.path.join(path_to_zas_rep_tools, path_to_file_with_twitter_creditials), "r").read().strip() )
        f = codecs.open(os.path.join(path_to_zas_rep_tools, path_to_file_with_twitter_creditials), "r", encoding="utf-8")
        api_data = json.load(f)
        #return api_data
        return api_data["consumer_key"], api_data["consumer_secret"], api_data["access_token"], api_data["access_token_secret"] 

    return False


