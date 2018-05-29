#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# : XXX{Information about this code}XXX
# Author:
# c(Developer) ->     {'Egor Savin'}
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

###Programm Info######
#
#
#
#
#



import os
import copy
import sys
import regex
import logging
import sys
import signal

import io
import inspect
import time
from datetime import date
import tweepy
import langid
import unicodecsv as csv
import codecs
import json
import codecs
#from collections import defaultdict
from raven import Client
from cached_property import cached_property
from encodings.aliases import aliases


from zas_rep_tools.src.utils.logger import Logger
from zas_rep_tools.src.utils.debugger import p
from zas_rep_tools.src.utils.error_tracking import initialisation


abs_path_to_zas_rep_tools = os.path.dirname(os.path.dirname(os.path.dirname(inspect.getfile(Logger))))
abs_path_to_stop_words = os.path.join(abs_path_to_zas_rep_tools, "data/stop_words")


  



class Streamer(object):

    supported_encodings_types = set(aliases.values())
    
    path_to_stop_words = {"de":os.path.join(abs_path_to_stop_words, "de.txt")}


    supported_platforms= ["twitter"]
    supported_laguages = [k for k in path_to_stop_words] + ["own_stop_words"] # language naming should be the same as in this module "langid.classify(data["text"])[0]""
    #p(supported_laguages)

    #p(path_to_zas_rep_tools)
    def __init__(self, consumer_key, consumer_secret, access_token, access_token_secret, storage_path,
                platfrom="twitter", language="de", stop_words=False, encoding="utf_8",
                folder_for_log_files=False,  use_logger=True, logger_level=logging.INFO, error_tracking=True):



        ## Logger Initialisation 
        logger = Logger()
        self._folder_for_log_files = folder_for_log_files
        self._use_logger = use_logger
        self.logger = logger.myLogger("Streamer", self._folder_for_log_files, use_logger=self._use_logger, level=logger_level)

        self.logger.debug('Beginn of creating an instance of Streamer()')


        #Input: Incaplusation:

        self._consumer_key = consumer_key
        self._consumer_secret = consumer_secret
        self._access_token = access_token
        self._access_token_secret = access_token_secret
        self._storage_path = storage_path
        self._platfrom = platfrom
        self._language = language # 
        self._stop_words = stop_words 
        self._error_tracking = error_tracking
        self._encoding = encoding

        #p(inpdata)

        #InstanceAttributes: Initialization




        ## Error-Tracking:Initialization #1
        if self._error_tracking:
            self.client = initialisation()
            self.client.context.merge({'InstanceAttributes': self.__dict__})



        # Validation 
        self._validate_input()

        self.logger.debug('Intern InstanceAttributes was initialized')

        self.logger.debug('An instance of Streamer() was created ')



        if platfrom not in Streamer.supported_platforms:
            self.logger.error("Given Platform({}) is not supported. Please choice one of the following platforms: {}".format(platfrom,Streamer.supported_platforms))
            sys.exit()


        if platfrom == "twitter":
            self.stream_twitter()


    def _get_stop_words(self):
        path = Streamer.path_to_stop_words[self._language]
        if os.path.isfile(path ):
            stop_words = [line.strip() for line in codecs.open(path, encoding=self._encoding)]
            if len(stop_words)<= 400:
                return [line.strip() for line in codecs.open(path, encoding=self._encoding)]
            else:
                self.logger.error("The Number of the given stop words should be under 401 items.")
                sys.exit()
        else:
            self.logger.error("Given file with stop words is not exist {}".format(path))
            sys.exit()


    def _validate_input(self):
        self._evaluate_stop_words()
        self._validate_given_language()
        self._validate_storage_path()
        self._validate_given_encoding()
        

    def _validate_storage_path(self):
        if not os.path.isdir(self._storage_path):
            self.logger.error("Given path to storage directory ({}) is nor exist".format(self._storage_path))
            sys.exit()



    def _validate_given_language(self):
        if self._language not in Streamer.supported_laguages:
            self.logger.error("Given Language ({}) is not supported. Please use one of the following languages: {}".format(self._language, Streamer.supported_laguages))
            sys.exit()


        

    def _evaluate_stop_words(self):
        if self._stop_words:
            self._language = "own_stop_words"
            if isintance(self._stop_words, (str,unicode)):
                if os.path.isfile(self._stop_words):
                    path_to_stop_words[self._language] = self._stop_words
                    return True
                else:
                    self.logger.error("Given path to stop words is not exist ({})".format(self._stop_words))
                    sys.exit()

            if  not isintance(self._stop_words, list):
                self.logger.error("Given Stop Word is not a list. It should be a list or a path to the directory.")
                sys.exit()

    def _validate_given_encoding(self):
        if self._encoding not in Streamer.supported_encodings_types:
            self.logger.error("Given encoding ({}) is not supported. Choice one of the following encodings: {}".format(self._encoding, Streamer.supported_encodings_types))
            sys.exit()

    def get_supported_platforms(self):
        return Streamer.supported_platforms

    def get_supported_langauges():
        return Streamer.supported_laguages





    def stream_twitter(self):
        global old_date
        global logfile
        global language
        global storage_path
        language = self._language
        storage_path = self._storage_path

        auth = tweepy.OAuthHandler(self._consumer_key, self._consumer_secret)
        auth.set_access_token(self._access_token, self._access_token_secret)
        api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())
        logfile = codecs.open(os.path.join(self._storage_path,"streaming.log"), 'a', encoding="utf-8")
        #localtime = time.asctime( time.localtime(time.time()) )
        logfile.write( time.asctime( time.localtime(time.time())) + " Starting stream for '" + language + "' language \n")

        # longer timeout to keep SSL connection open even when few tweets are coming in
        stream = tweepy.streaming.Stream(auth, CustomStreamListener(), timeout=1000.0)
        terms = self._get_stop_words()

        # open output file
        old_date = date.today()

        global file_selected
        global file_outsorted
        global file_undelivered
        global unic

        file_selected, file_outsorted, file_undelivered, unic =  create_new_files_for_new_day(str(old_date), storage_path, language)
        
        #writer = csv.writer(outfile_name,quoting=csv.QUOTE_NONNUMERIC,lineterminator='\n', encoding='utf-8')
         
        try:
            print "Streaming was started"
            stream.filter(track=terms)
        except KeyboardInterrupt:
            logfile.write( "    " + time.asctime( time.localtime(time.time()) ) + " Stream was aborted  \n")
            print "Streaming was aborted. stopping....."

            file_selected.write('\n]') # close an json array
            file_outsorted.write('\n]') # close an json array
            file_selected.close()
            file_outsorted.close()
            file_undelivered.close()
            print "All files was correctly closed."
            sys.exit()
            #os._exit(1)
        except Exception, e:
            logfile.write( "    " + time.asctime( time.localtime(time.time()) ) + " Stream was stopped with  an Error  \n")
            print "Stream was stopped with an Error...... " + str(e)

            # file_selected.write('\n]') # close an json array
            # file_outsorted.write('\n]') # close an json array
            file_selected.close()
            file_outsorted.close()
            file_undelivered.close()
            print "All files was correctly closed."
            #sys.exit()
            os._exit(1)

        

def create_new_files_for_new_day(current_data, storage_path, language):
    path_to_the_day = os.path.join(storage_path, str(current_data))
    if not os.path.isdir(path_to_the_day):
        os.mkdir(path_to_the_day)


    outfile_name = "tweets-" + current_data
    #p(date, c="m")
    #p(datetime.datetime.strptime(date,'%m/%d/%Y'))
    #p(type(date))
    #str(date.strftime("%Y-%m-%d"))
    outfile_full_name = outfile_name + ".json"
    language_outfile_name = "{}_{}".format( language,outfile_full_name)
    other_outfile_name =  "other_{}".format(outfile_full_name)
    #global output_file_selected_tweets
    #global output_file_outsorted_tweets
    #global output_file_undelivered_tweets
    #p(storage_path)
    #p(path_to_the_day)
    #p(os.path.join(storage_path,path_to_the_day, language_outfile_name))
    unic = io.open(os.path.join(path_to_the_day, "aaaaaaa"+language_outfile_name), "a", encoding="utf-8")

    output_file_selected_tweets = codecs.open(os.path.join(path_to_the_day, language_outfile_name), "a", encoding="utf-8")
    output_file_outsorted_tweets = codecs.open(os.path.join(path_to_the_day,other_outfile_name), "a", encoding="utf-8")
    output_file_undelivered_tweets = codecs.open(os.path.join(path_to_the_day,"undelivered_"+outfile_name+ ".log"), "a", encoding="utf-8")
    output_file_selected_tweets.write('[\n') # start a new json array
    output_file_outsorted_tweets.write('[\n') # start a new json array
    return output_file_selected_tweets, output_file_outsorted_tweets, output_file_undelivered_tweets , unic





class CustomStreamListener(tweepy.StreamListener):



    def on_data(self, data):
        global old_date
        global file_selected
        global file_outsorted
        global file_undelivered
        global logfile
        global unic
        #global writer
        #global outfile_name
        new_date = date.today()
        
        if not new_date == old_date:
            # file_selected.write('\n]') # close an json array
            # file_outsorted.write('\n]') # close an json array
            file_selected.close()
            file_outsorted.close()
            file_undelivered.close()
            file_selected, file_outsorted, file_undelivered, unic =  create_new_files_for_new_day(str(old_date), storage_path, language)
            # file_selected.write('[\n') # start a new json array
            # file_outsorted.write('[\n') # start a new json array
            old_date = new_date

        data = json.loads(data)
        #p(data)
        try:
            try:
                #data["text"]
                lang = langid.classify(data["text"])[0];
                if lang == language:
                    #print status
                    #json_status= json.dumps(status)
                    
                    #json_status= status._json
                    #tweet = json.loads(json_status)
                    #print tweet
                    
                    #print json_status
                    #jsonfile = codecs.open("tweets.json", "a", encoding="utf-8")
                    unic.write(unicode(json.dumps(data,
                                        indent=4, sort_keys=True,
                                        separators=(',', ': '), ensure_ascii=False)))
                    file_selected.write(unicode(data)+"\n")


                    #self._output_file_de_tweets.write(  data["created_at"]+ data["id_str"]+ data["text"] + "\n"  )
                else:
                    file_outsorted.write(unicode(data)+"\n")
                    #self._output_file_other_tweets.write(  data["created_at"]+ data["id_str"]+ data["text"] + "\n"  )
            except KeyError:
                file_undelivered.write(time.asctime( time.localtime(time.time()) )+"  "+unicode(data)+"\n")

        except KeyboardInterrupt:
            logfile.write( "    " + time.asctime( time.localtime(time.time()) ) + " Stream was stopped  \n")
            print "Streaming was aborted. stopping....."
            # clean up
            # file_selected.write('\n]') # close an json array
            # file_outsorted.write('\n]') # close an json array
            file_selected.close()
            file_outsorted.close()
            file_undelivered.close()
            print "All files was correctly closed."
            sys.exit()
            #os._exit(1)
        except Exception, e:
            logfile.write( "    " + time.asctime( time.localtime(time.time()) ) + " Stream was stopped with  an Error  \n")
            print "Stream was stopped with an Error...... " + str(e)

            # file_selected.write('\n]') # close an json array
            # file_outsorted.write('\n]') # close an json array
            file_selected.close()
            file_outsorted.close()
            file_undelivered.close()
            print "All files was correctly closed."
            #sys.exit()
            os._exit(1)




    def on_error(self, status_code):
        #p(type(status_code))
        logfile.write("    "+str(time.asctime( time.localtime(time.time()) )) + ' Encountered error with status code:' + str(status_code) + "\n")
        #return True # Don't kill the stream

        if status_code == 401:
            print "UnauthorizedError401: Your credentials are invalid.\nTry re-creating the credentials correctly again following the instructions here (https://developer.twitter.com/en/docs/basics/authentication/guides/access-tokens). \nAfter recreation you need to retype your data. Use: $ zas-rep-tools retypeTwitterData"
            #return False
            os._exit(1)

        return True

    def on_timeout(self):
        logfile.write("    "+str(time.asctime( time.localtime(time.time()) )) + ' Timeout...' + "\n")
        return True # Don't kill the stream




