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


import shutil
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
from collections import defaultdict
from raven import Client
from cached_property import cached_property
from encodings.aliases import aliases
from nltk.corpus import stopwords


from zas_rep_tools.src.utils.logger import Logger
from zas_rep_tools.src.utils.debugger import p
from zas_rep_tools.src.utils.error_tracking import initialisation
from zas_rep_tools.src.utils.helpers import send_email


abs_path_to_zas_rep_tools = os.path.dirname(os.path.dirname(os.path.dirname(inspect.getfile(Logger))))
abs_paths_to_stop_words = os.path.join(abs_path_to_zas_rep_tools, "data/stop_words/")


global last_error
last_error = ""




class Streamer(object):

    supported_languages_by_langid = [u'af', u'am', u'an', u'ar', u'as', u'az', u'be', u'bg', u'bn', u'br', u'bs', u'ca', u'cs', u'cy', u'da', u'de', u'dz', u'el', u'en', u'eo', u'es', u'et', u'eu', u'fa', u'fi', u'fo', u'fr', u'ga', u'gl', u'gu', u'he', u'hi', u'hr', u'ht', u'hu', u'hy', u'id', u'is', u'it', u'ja', u'jv', u'ka', u'kk', u'km', u'kn', u'ko', u'ku', u'ky', u'la', u'lb', u'lo', u'lt', u'lv', u'mg', u'mk', u'ml', u'mn', u'mr', u'ms', u'mt', u'nb', u'ne', u'nl', u'nn', u'no', u'oc', u'or', u'pa', u'pl', u'ps', u'pt', u'qu', u'ro', u'ru', u'rw', u'se', u'si', u'sk', u'sl', u'sq', u'sr', u'sv', u'sw', u'ta', u'te', u'th', u'tl', u'tr', u'ug', u'uk', u'ur', u'vi', u'vo', u'wa', u'xh', u'zh', u'zu']
    supported_languages_by_twitter = [u'fr', u'en', u'ar', u'ja', u'es', u'de', u'it', u'id', u'pt', u'ko', u'tr', u'ru', u'nl', u'fil', u'msa', u'zh-tw', u'zh-cn', u'hi', u'no', u'sv', u'fi', u'da', u'pl', u'hu', u'fa', u'he', u'ur', u'th', u'en-gb']
    NLTKlanguages= {u'ru': u'russian', u'fr': u'french', u'en': u'english', u'nl': u'dutch', u'pt': u'portuguese', u'no': u'norwegian', u'sv': u'swedish', u'de': u'german', u'tr': u'turkish', u'it': u'italian', u'hu': u'hungarian', u'fi': u'finnish', u'da': u'danish', u'es': u'spanish'}
    supported_languages = set(supported_languages_by_langid) & set(supported_languages_by_twitter )
    #p(supported_languages)
    #sys.exit()
    supported_encodings_types = set(aliases.values())
    # for k,v in NLTKlanguages.iteritems():
    #     if stopwords.words(v):
    #         p((k, v))
    #         print stopwords.words(v)

    # 


    stop_words_collection = {k:stopwords.words(v) for k,v in NLTKlanguages.iteritems()}
    stop_words_collection.update({u"de":os.path.join(abs_paths_to_stop_words, u"de.txt")}) # add my own set for german lang

    supported_stop_words = [k for k in stop_words_collection] # language naming should be the same as in this module "langid.classify(data["text"])[0]""

    # for k,v in stop_words_collection.iteritems():
    #     p((k, v))
    # sys.exit()


    supported_platforms= ["twitter"]
    #p(path_to_zas_rep_tools)

    def __init__(self, consumer_key, consumer_secret, access_token, access_token_secret, storage_path,
                platfrom="twitter", language=False, terms=False, stop_words=False, encoding="utf_8", email_addresse=False, ignore_rt=False, 
                folder_for_log_files=False,  use_logger=True, logger_level=logging.INFO, error_tracking=True):

        ## Logger Initialisation 
        global global_logger
        logger = Logger()
        self._folder_for_log_files = folder_for_log_files
        self._use_logger = use_logger
        
        
        
        self.logger = logger.myLogger("Streamer", self._folder_for_log_files, use_logger=self._use_logger, level=logger_level)
        global_logger = self.logger
        #p(global_logger)
        self.logger.debug('Beginn of creating an instance of Streamer()')


        #Input: Incaplusation:

        self._consumer_key = consumer_key
        self._consumer_secret = consumer_secret
        self._access_token = access_token
        self._access_token_secret = access_token_secret
        self._storage_path = storage_path
        self._platfrom = platfrom
        self._language = language # 
        self._terms = terms 
        self._stop_words = stop_words
        self._error_tracking = error_tracking
        self._encoding = encoding
        self._email_addresse = email_addresse
        self._ignore_retweets = ignore_rt

        self._streamer_settings = {"language":True if self._language else False, 
                     "terms":True if self._terms else False,
                     "stop_words":True if self._stop_words else False   }
        
        p(self._streamer_settings)

        # make Variable global for tweepy
        global ignore_retweets
        ignore_retweets = self._ignore_retweets

        #p(inpdata)
        #p(email_addresse)
        #InstanceAttributes: Initialization




        ## Error-Tracking:Initialization #1
        if self._error_tracking:
            self.client = initialisation()
            self.client.context.merge({'tags':  self.cleaned_instance_attributes()})
            global client
            client =self.client



        # Validation 
        self._validate_input()

        self.logger.debug('Intern InstanceAttributes was initialized')

        self.logger.debug('An instance of Streamer() was created ')


        if platfrom not in Streamer.supported_platforms:
            self.logger.error("Given Platform({}) is not supported. Please choice one of the following platforms: {}".format(platfrom,Streamer.supported_platforms))
            sys.exit()


        # if platfrom == "twitter":
        #     self.stream_twitter()


    def _get_stop_words(self):
        #p(Streamer.stop_words_collection[self._language], c="m")
        
        # to ensure the possibility to get intern stop_words_set

        if not self._language:
            language = str(self._language)
        else:
            language = self._language


        try:
            if isinstance(Streamer.stop_words_collection[language], (str,unicode)):
                if os.path.isfile(Streamer.stop_words_collection[language]):
                    stop_words = [line.strip() for line in codecs.open(Streamer.stop_words_collection[language], encoding=self._encoding)]
                    self.logger.debug("Stop words was read from a file")
                else:
                    self.logger.error("StopWordsGetterError: Given path to stop_words is not exist")
                    sys.exit()
            elif isinstance(Streamer.stop_words_collection[language], list):

                stop_words = Streamer.stop_words_collection[language]
                self.logger.debug("Stop words was read from a given list")
            else:
                self.logger.error("StopWordsGetterError: Not supported format of stop-words. Please give them as path of as a list.")
                sys.exit()
                
        except KeyError:
            self.logger.error("StopWordsGetterError: Stop-words for given language ('{}') wasn't found. Please import them into the Streamer using 'stop_words' parameter ".format(language) )
            sys.exit()

        return stop_words


    def cleaned_instance_attributes(self):
        #p(self.__dict__)
        exclude = ["_consumer_key","_consumer_secret","_access_token", "_access_token_secret", "client", "logger"]
        return {k:v for k,v in self.__dict__.iteritems() if k not in exclude} 

    def _validate_input(self):
        self._validate_given_language()

        if not self._stop_words:

            if self._language:
                if not self._terms and self._language not in Streamer.supported_stop_words:
                    self.logger.error("InputError: Terms or/and stop-words wasn't given. According the Twitter 'Developer Agreement and Policy' -  'terms' or/and 'stop-words' should be given. A Language is just an option and not obligatory for the Streamer. ")
                    sys.exit()
            else:
                if not self._terms:
                    self.logger.error("InputError: Nothing was given. Streamer need some input to initialize the Filtering. (Please give any terms/stop-words/language)  ")
                    sys.exit()

        
        self._evaluate_stop_words()
        self._evaluate_terms()
        self._validate_storage_path()
        self._validate_given_encoding()
        

    def _validate_storage_path(self):
        if not os.path.isdir(self._storage_path):
            try:
                os.makedirs(self._storage_path)
                self.logger.info("Following storage directory was created: '{}'. There you will find all streamed data.".format(os.path.join(os.getcwd(),self._storage_path)))
            except:
                self.logger.error("PathError: It wasn't possible to create following directory: '{}' ".format(os.path.join(os.getcwd(),self._storage_path)))
                sys.exit()



    def _validate_given_language(self):
        if self._language:
            if self._language not in Streamer.supported_languages:
                self.logger.error("Given Language ('{}'') is not supported. Please use one of the following languages: {}".format(self._language, Streamer.supported_languages))
                sys.exit()


    def get_track_terms(self):
        if not self._language:
            language = str(self._language)
        else:
            language = self._language


        all_terms_to_track = []
        if self._terms:
            if (self._terms and self._stop_words) or (self._terms and self._language):
                if  Streamer.stop_words_collection[language]:
                    all_terms_to_track = self._get_stop_words() + self._terms

            else:
                all_terms_to_track = self._terms
            
        elif not self._terms:
            if Streamer.stop_words_collection[language]:
                all_terms_to_track = self._get_stop_words()
            else:
                self.logger.error("InputError: Don't found any stop_words/terms. It is not allow to stream Twitter without any stop_words/terms.")      
                sys.exit()

        if len(all_terms_to_track) > 400:
            self.logger.error("InputError:  The Number of given stop_word/terms are exceeded (Twitter-API restriction). It is allow to track not more as 400 words. It was given '{}' words together. Please give less number of  stop_word/terms.\n\n  Following words was given: \n{} ".format(len(all_terms_to_track), all_terms_to_track) )
            sys.exit()
        #p(all_terms_to_track)
        return all_terms_to_track

    def _evaluate_terms(self):
        if self._terms:
            if isinstance(self._terms, (str,unicode)):
                if os.path.isfile(self._terms):
                    self._terms = [line.strip() for line in codecs.open(self._terms, encoding=self._encoding)]
                else:
                    self.logger.error("PathError: Given Path ({}) to terms are not exist".format(self._terms))
                    sys.exit()

            elif isinstance(self._terms, list):
                for term in self._terms:
                    if not isinstance(term, (str,unicode)):
                        self.logger.error("TypeError: Some of the given terms in the list is not string/unicode.")
                        sys.exit()


            else:
                self.logger.error("InputError:  Not supported format of terms. Please give them as path of as a list.")
                sys.exit()





    def _evaluate_stop_words(self):
        # change setting, if was toked intern stop_words set
        if self._language and not self._stop_words:
            if self._language in Streamer.supported_stop_words:
                self._streamer_settings["stop_words"] = True


        if self._stop_words:
            if self._language:
                if isinstance(self._stop_words, (str,unicode, list)):
                    if isinstance(self._stop_words, (str,unicode)):
                        if not  os.path.isfile(self._stop_words):
                            self.logger.error("InputError: Given path to stop words is not exist ({})".format(self._stop_words))
                            sys.exit()

                    Streamer.stop_words_collection[self._language] = self._stop_words


                else:
                    self.logger.error("InputError:  Not supported format of stop-words. Please give them as path of as a list.")
                    sys.exit()
            else:
                if isinstance(self._stop_words, (str,unicode, list)):

                    if isinstance(self._stop_words, (str,unicode)): 
                        if  self._stop_words in Streamer.supported_stop_words: # if will be used intern set of stop_words
                            Streamer.stop_words_collection[str(self._language)] = Streamer.stop_words_collection[self._stop_words]
                            return True

                        if not  os.path.isfile(self._stop_words):
                            self.logger.error("InputError: Given path to stop words is not exist ({})".format(self._stop_words))
                            sys.exit()
                    
                    elif isinstance(self._stop_words, list):
                        Streamer.stop_words_collection[str(self._language)] = self._stop_words

                    else:
                        self.logger.error("InputError:  Not supported format of stop-words. Please give them as path of as a list.")
                        sys.exit()


                else:
                    self.logger.error("InputError:  Not supported format of stop-words. Please give them as path of as a list.")
                    sys.exit()



    def _validate_given_encoding(self):
        if self._encoding not in Streamer.supported_encodings_types:
            self.logger.error("Given encoding ({}) is not supported. Choice one of the following encodings: {}".format(self._encoding, Streamer.supported_encodings_types))
            sys.exit()

    def get_supported_platforms(self):
        return Streamer.supported_platforms

    def get_supported_languages(self):
        return Streamer.supported_languages

    def get_exist_stop_words(self):
        return Streamer.supported_languages

    def _create_main_log_mag(self):
        msg_to_log = " >>>Streaming was started<<< "
        if self._language:
            msg_to_log = "{} for '{}' language".format(msg_to_log, self._language)

        if self._terms and self._language:
            msg_to_log = "{} and for given terms".format(msg_to_log)
        elif self._terms and not self._language:
            msg_to_log = "{} for given terms".format(msg_to_log)

        if (self._stop_words and self._language) or (self._stop_words and self._terms):
            msg_to_log = "{} and for given stop_words".format(msg_to_log)
        elif self._stop_words and not self._language and not self._terms:
            msg_to_log = "{} for given stop_words".format(msg_to_log)

        return msg_to_log

    def stream_twitter(self):
        global old_date
        global logfile
        global language
        global storage_path
        global email_addresse
        global file_selected
        global file_outsorted
        global file_undelivered
        global file_retweets
        global path_to_the_jsons
        global last_error
        #global last_error


        email_addresse= self._email_addresse
        language = self._language
        storage_path = self._storage_path
        #last_error = ""

        auth = tweepy.OAuthHandler(self._consumer_key, self._consumer_secret)
        auth.set_access_token(self._access_token, self._access_token_secret)
        api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())
        logfile = codecs.open(os.path.join(self._storage_path,"streaming.log"), 'a', encoding="utf-8")
        #localtime = time.asctime( time.localtime(time.time()) )
        
        # longer timeout to keep SSL connection open even when few tweets are coming in
        stream = tweepy.streaming.Stream(auth, CustomStreamListener(), timeout=1000.0)
        terms = self.get_track_terms()

        # open output file
        old_date = date.today()

        file_selected, file_outsorted, file_undelivered, file_retweets, path_to_the_jsons =  create_new_files_for_new_day(str(old_date), storage_path, language)
        
        #non_stop = True 
        last_5_error = []
        # stall_warnings - will inform you if you're falling behind. Falling behind means that you're unable to process tweets as quickly as the Twitter API is sending them to you.
        while True:
            #send_email("msm.filin@gmail.com", "Error", "Some error ")
            try:

                msg_to_log = self._create_main_log_mag()
                #log_msg = "\n{} Starting stream for '{}' language.\n" 
                logfile.write( "{} {} \n".format(time.asctime( time.localtime(time.time()) ) , msg_to_log)  )
                msg_settings = "StreamerFilterSetting: {}".format(self._streamer_settings)
                

                #stream.filter( track=terms, stall_warnings=True)
                #stream.filter(languages=[self._language],  stall_warnings=True)

                #p(terms, c= "m")
                if self._language:
                    log_msg_settings = "{} (l+t)".format(msg_settings)
                    logfile.write( "    {} \n".format(log_msg_settings) )
                    global_logger.info(log_msg_settings)
                    global_logger.info(msg_to_log)
                    stream.filter(languages=[self._language], track=terms, stall_warnings=True)
                else:
                    log_msg_settings = "{} (t)".format(msg_settings)
                    logfile.write( "    {} \n".format(log_msg_settings) )
                    global_logger.info(log_msg_settings)
                    global_logger.info(msg_to_log)
                    stream.filter( track=terms, stall_warnings=True)

                
            except KeyboardInterrupt:
                global_logger.info("Streaming was aborted. stopping all processes.....")
                log_msg = "    {} Stream was aborted by user 'KeyboardInterrupt' \n" 
                logfile.write(  log_msg.format(time.asctime(time.localtime(time.time())))  )


                logfile.close()
                file_selected.close()
                file_outsorted.close()
                file_undelivered.close()
                file_retweets.close()
                global_logger.info("All processes was correctly closed.")
                sys.exit(1)
                #os._exit(1)

            except Exception, e:


                if "Failed to establish a new connection" in str(e):
                    log_msg = "     {} No Internet Connection. Wait 15 sec.....  \n" 
                    logfile.write(  log_msg.format(time.asctime(time.localtime(time.time())))  )
                    global_logger.critical("No Internet Connection. Wait 15 sec.....")
                    time.sleep(15)
                else:
                    log_msg = "     {} Stream get an Error: '{}' \n" 
                    logfile.write(  log_msg.format(time.asctime(time.localtime(time.time())),e)  )
                    global_logger.critical("Streaming get an Error......‘{}‘".format(e))

                last_5_error.append(str(e))

                if len(last_5_error) >= 5:
                    if len(set(last_5_error)) ==1 :
                        log_msg = "     {} Stream was stopped after 5 same errors in stack: '{}' \n" 
                        logfile.write(  log_msg.format(time.asctime(time.localtime(time.time())),e)  )
                        msg = 'Hey,</br></br> Something was Wrong!  Streamer throw the following error-message and the Streaming Process was stopped:</br> <p style="margin-left: 50px;"><strong><font color="red">{}</strong> </font> </p> Please  check if everything is fine with this Process. </br></br> Greeting, </br>Your Streamer'.format(e)
                        last_error = str(e)
                        subject = "TwitterStreamer was stopped (Reason: last 5 errors are same)"
                        send_email(email_addresse, subject, msg)
                        global_logger.error("Stream was stopped after 5 same errors in stack")
                        os._exit(1)
                    else:
                        last_5_error = []



                if last_error != str(e):
                    msg = "Hey,</br></br> Something was Wrong!  Streamer throw the following error-message:</br> <p style='margin-left: 50px;''><strong><font color='red'>{}</strong> </font> </p> Please  check if everything is fine with this Process. </br></br> Greeting, </br>Your Streamer".format(e)
                    last_error = str(e)
                    send_email(email_addresse, 'Error: '+str(e), msg)

            except tweepy.TweepError, e:
                pass

                



class CustomStreamListener(tweepy.StreamListener):

    def __init__(self):


        logger = Logger()
        self.logger = Logger().myLogger("CustomStreamListener")


    def on_data(self, data):

        global old_date
        global file_selected
        global file_outsorted
        global file_undelivered
        global file_retweets
        global logfile
        global path_to_the_jsons
        global ignore_retweets
        global language

        new_date = date.today()
        #p(old_date, c="m")
        if not new_date == old_date:
            # file_selected.write('\n]') # close an json array
            # file_outsorted.write('\n]') # close an json array
            file_selected.close()
            file_outsorted.close()
            file_undelivered.close()
            file_retweets.close()
            #p(path_to_the_jsons)
            ziparch = shutil.make_archive("jsons", 'zip', path_to_the_jsons)
            
            shutil.move(ziparch, os.path.dirname(path_to_the_jsons))
            shutil.rmtree(path_to_the_jsons, ignore_errors=True)
            self.logger.info("All JSONS was archived")
            #p(ziparch)

            file_selected, file_outsorted, file_undelivered, file_retweets, path_to_the_jsons =  create_new_files_for_new_day(str(new_date), storage_path, language)
            # file_selected.write('[\n') # start a new json array
            # file_outsorted.write('[\n') # start a new json array
            
            old_date = new_date
            self.logger.info("New day was started!")



        data = json.loads(data)
        
        #p(data)
        #try:
        #
        try:
            tId = data["id"]


            # if tweets longer as 140 characters
            if "extended_tweet" in data:
                text = data["extended_tweet"]["full_text"].replace('\n', ' ').replace('\r', ' ')
            else:
                text = data["text"].replace('\n', ' ').replace('\r', ' ')


            # filter out all retweets
            lang = langid.classify(text)[0];
            if lang == language:

                if ignore_retweets:

                    if "retweeted_status" not in data:

                        file_selected.write(u"{} <t>{}</t>\n".format(unicode(tId),  text))


                else:

                    if "retweeted_status" in data:
                        file_retweets.write(unicode(tId)+"\n")


                        json_file = io.open(os.path.join(path_to_the_jsons, "{}.json".format(tId)), "a", encoding="utf-8")
                        json_file.write(unicode(json.dumps(data,
                                            indent=4, sort_keys=True,
                                            separators=(',', ': '), ensure_ascii=False)))
                        json_file.close()

                    
                    else:
                        file_selected.write(u"{} <t>{}</t>\n".format(unicode(tId),  text))
                        json_file = io.open(os.path.join(path_to_the_jsons, "{}.json".format(tId)), "a", encoding="utf-8")
                        json_file.write(unicode(json.dumps(data,
                                            indent=4, sort_keys=True,
                                            separators=(',', ': '), ensure_ascii=False)))
                        json_file.close()


            else:
                file_outsorted.write(u"{} <t>{}</t>\n".format(unicode(tId),  text))
                json_file = io.open(os.path.join(path_to_the_jsons, "{}.json".format(tId)), "a", encoding="utf-8")
                json_file.write(unicode(json.dumps(data,
                                    indent=4, sort_keys=True,
                                    separators=(',', ': '), ensure_ascii=False)))
                json_file.close()

            #self._output_file_other_tweets.write(  data["created_at"]+ data["id_str"]+ data["text"] + "\n"  )
        except KeyError, ke:
            #p(data)
            if "limit" in str(data):
                time_now = time.asctime( time.localtime(time.time()) )
                file_undelivered.write(u"{} {} \n".format( time_now, data) )
            else:
                self.logger.critical(str(repr(ke)))



    def on_error(self, status_code):
        #p(type(status_code))
        log_msg = "     {} Encountered error with status code (Streamer still be on): '{}' \n"
        logfile.write(  log_msg.format(time.asctime(time.localtime(time.time())),status_code)  )
        #self.logger.critical(log_msg)


        #return True # Don't kill the stream

        if status_code == 401:
            #print status_code
            logger_msg = "UnauthorizedError401: Your credentials are invalid or your system time is wrong.\nTry re-creating the credentials correctly again following the instructions here (https://developer.twitter.com/en/docs/basics/authentication/guides/access-tokens). \nAfter recreation you need to retype your data. Use: $ zas-rep-tools retypeTwitterData"
            self.logger.error(logger_msg)
            #return False
            os._exit(1)



        return True

    def on_timeout(self):
        logfile.write("    "+str(time.asctime( time.localtime(time.time()) )) + ' Timeout...' + "\n")
        self.logger.warning(" Timeout...")
        return True # Don't kill the stream






def create_new_files_for_new_day(current_data, storage_path, language):
    #p("new day")
    language = language if language else "none"
    path_to_the_day = os.path.join(storage_path, str(current_data))
    #p(path_to_the_day)
    path_to_the_jsons = os.path.join(path_to_the_day, "jsons")
    if not os.path.isdir(path_to_the_day):
        os.mkdir(path_to_the_day)
        

    if not os.path.isdir(path_to_the_jsons):
        os.mkdir(path_to_the_jsons)


    outfile_name = "tweets-" + current_data

    outfile_full_name = outfile_name + ".txt"
    language_outfile_name = "{}_{}".format( language,outfile_full_name)
    other_outfile_name =  "outsorted_{}".format(outfile_full_name)
    retweets_id_name =  "{}_retweets_{}".format(language,outfile_full_name)

    file_retweets = codecs.open(os.path.join(path_to_the_day, retweets_id_name), "a", encoding="utf-8")
    output_file_selected_tweets = codecs.open(os.path.join(path_to_the_day, language_outfile_name), "a", encoding="utf-8")
    output_file_outsorted_tweets = codecs.open(os.path.join(path_to_the_day,other_outfile_name), "a", encoding="utf-8")
    output_file_undelivered_tweets = codecs.open(os.path.join(path_to_the_day,"undelivered_"+outfile_name+ ".log"), "a", encoding="utf-8")
    return output_file_selected_tweets, output_file_outsorted_tweets, output_file_undelivered_tweets , file_retweets, path_to_the_jsons






