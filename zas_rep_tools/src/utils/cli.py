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

from zas_rep_tools.src.classes.corpus import Corpus
from zas_rep_tools.src.utils.debugger import p

path_to_zas_rep_tools = os.path.dirname(os.path.dirname(os.path.dirname(inspect.getfile(Corpus))))


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
	if os.path.isfile(os.path.join(path_to_zas_rep_tools, "user-config/user_agreement.txt")):
		agreement_data = ast.literal_eval(codecs.open(os.path.join(path_to_zas_rep_tools, "user-config/user_agreement.txt"), "r").read().strip() )
		try:
			agreement_data['error_tracking']
		except:
			return False

		return True
	else:
		return False


def get_agreement_data():
	if os.path.isfile(os.path.join(path_to_zas_rep_tools, "user-config/user_agreement.txt")):
		agreement_data = ast.literal_eval(codecs.open(os.path.join(path_to_zas_rep_tools, "user-config/user_agreement.txt"), "r").read().strip() )
		return agreement_data

	return False



def is_error_tracking_allowed():
	if os.path.isfile(os.path.join(path_to_zas_rep_tools, "user-config/user_agreement.txt")):
		agreement_data = get_agreement_data()
		if not agreement_data:
			return False

		if agreement_data['error_tracking'] == True:
			return True
		else:
			return False

def ask_user_agreement():
	print "\nThank you for choosing this module. For making this tool better for you in the future we want to  automatically error tracking. Please write yes/no if you agree or disagree with that."
	input_var = raw_input("Your answer: ")
	#p(input_var)
	if input_var == "yes":
		print "\n\nThank you for allow error tracking."
		input_var = True
	elif input_var == "no":
		print "\n\nWe deactivate error tracking for this copy of this tool. Enjoy using of this tool."
		input_var = False
	else: 
		print "We can not understand your answer. Please reopen this program and choice one of the both possible answers ['yes','no']"
		print "Exit...."
		os._exit(1)

	if not os.path.isdir(os.path.join(path_to_zas_rep_tools,"user-config")):
		os.mkdir(os.path.join(path_to_zas_rep_tools,"user-config"))

	file = codecs.open(os.path.join(path_to_zas_rep_tools, "user-config/user_agreement.txt"), "w")
	file.write("{}'error_tracking':{} {}".format("{", input_var, "}") )
	file.close()
	print "Your agreement was saved in the following file "+"user-config/user_agreement.txt" + "Every time in the future you can respeak this agreement. For it you need just to change 'True'  to 'False'"


path_to_twitter_data = "user-config/twitter_api_data.txt"


def ask_user_for_twitter_api_data():
	print "\n\nBevore you can start with twitter streaming you need enter twitter credentials. \n You can consult a README File (https://github.com/savin-berlin/zas-rep-tools) under 'Start to use streamer' to see  how you can exactly get this data."
	consumer_key = raw_input("consumer_key: ")
	consumer_secret = raw_input("consumer_secret: ")
	access_token = raw_input("access_token: ")
	access_token_secret = raw_input("access_token_secret: ")
	
	print "\n\nThank you for entering your data. Do you want to save them on the disk? [yes,no]  \nIt can be helpful for you, if you want to use this streamer more often.\n Notice: You data will be save without decryption and can be visible to another users of this computer, which has also admin rights."
	answer = raw_input("Your answer: ")
	if answer == "no":
		answer = False
		print "\nYour Twitter API credentials will be just temporary used and after script execution immediately  deleted."
	elif answer == "yes":
		answer = True
	else: 
		print "We can not understand your answer. Please reopen this program and choice one of the both possible answers ['yes','no']"
		print "Exit...."
		os._exit(1)

	if answer is True:
		file = codecs.open(os.path.join(path_to_zas_rep_tools, path_to_twitter_data), "w")
		file.write("{} 'consumer_key':'{}','consumer_secret':'{}', 'access_token':'{}', 'access_token_secret':'{}' {}".format("{", consumer_key,consumer_secret,access_token,access_token_secret, "}") )
		file.close()
		print "Your twitter API Data was saved in the following file '"+path_to_twitter_data + "'. Every time in the future you can respeak this agreement and delete this file."

	return consumer_key, consumer_secret, access_token, access_token_secret 


def was_user_asked_for_path_to_twitter_data():
	if os.path.isfile(os.path.join(path_to_zas_rep_tools, path_to_twitter_data)):
		api_data = ast.literal_eval(codecs.open(os.path.join(path_to_zas_rep_tools, path_to_twitter_data), "r").read().strip() )
		try:
			api_data['consumer_key']
		except:
			return False

		return True
	else:
		return False


def get_api_data():
	if os.path.isfile(os.path.join(path_to_zas_rep_tools, path_to_twitter_data)):
		api_data = ast.literal_eval(codecs.open(os.path.join(path_to_zas_rep_tools, path_to_twitter_data), "r").read().strip() )
		#return api_data
		return api_data["consumer_key"], api_data["consumer_secret"], api_data["access_token"], api_data["access_token_secret"] 

	return False

