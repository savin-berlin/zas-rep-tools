#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# : Tests for XXX Module
# Author:
# c(Developer) ->     {'Egor Savin'}
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

###Programm Info######
#
#
#
#
#

import unittest
import os
import logging


import codecs
import sure
import inspect
import copy
from collections import defaultdict
from nose.plugins.attrib import attr
from testfixtures import tempdir, TempDirectory
from distutils.dir_util import copy_tree 
import glob

from zas_rep_tools.src.classes.Corpus import BloggerCorpus

from zas_rep_tools.src.utils.debugger import p, wipd, wipdn, wipdl, wipdo
from zas_rep_tools.src.utils.logger import Logger





class TestZAScorpusBloggerCorpus(unittest.TestCase):
    def setUp(self):



        ######## Folders Creation ##############
        ########### Begin ######################
        path_to_zas_rep_tools = os.path.dirname(os.path.dirname(os.path.dirname(inspect.getfile(BloggerCorpus))))
        #p(path_to_zas_rep_tools)


        relativ_path_to_small_subset = "data/tests_data/Corpora/BloggerCorpus/SmallSubset"
        relativ_path_to_the_middle_subset = "data/tests_data/Corpora/BloggerCorpus/MiddleSubset"
        relativ_path_to_the_hightrepetativ_subset = "data/tests_data/Corpora/BloggerCorpus/HighRepetativSubSet"
        self.abs_path_to_small_subset = os.path.join(path_to_zas_rep_tools,relativ_path_to_small_subset)
        self.abs_path_to_middle_subset = os.path.join(path_to_zas_rep_tools,relativ_path_to_the_middle_subset)
        self.abs_path_to_hightrepetativ_subset = os.path.join(path_to_zas_rep_tools,relativ_path_to_the_hightrepetativ_subset)

        self.tempdir = TempDirectory()
        self.tempdir.makedir('TestCorpus')
        self.temp_abs_path_to_small_subset = os.path.join(self.tempdir.path, 'SmallSubset')
        self.temp_abs_path_to_middle_subset = os.path.join(self.tempdir.path, 'MiddleSubset')
        self.temp_abs_path_to_hightrepetativ_subset = os.path.join(self.tempdir.path, 'HighRepetativSubSet')
        #p(self.temp_abs_path_to_small_subset)
        copy_tree(self.abs_path_to_small_subset,self.temp_abs_path_to_small_subset)
        copy_tree(self.abs_path_to_middle_subset,self.temp_abs_path_to_middle_subset)
        copy_tree(self.abs_path_to_hightrepetativ_subset,self.temp_abs_path_to_hightrepetativ_subset)
        

        ## create test-data
        self.small_subset = {os.path.join(self.temp_abs_path_to_small_subset,file):codecs.open(os.path.join(self.temp_abs_path_to_small_subset,file), "r").read() for file in os.listdir(self.temp_abs_path_to_small_subset)}
        self.middle_subset = {os.path.join(self.temp_abs_path_to_small_subset,file):codecs.open(os.path.join(self.temp_abs_path_to_small_subset,file), "r").read() for file in os.listdir(self.temp_abs_path_to_small_subset)}
        self.hightrepetativ_subset = {os.path.join(self.temp_abs_path_to_small_subset,file):codecs.open(os.path.join(self.temp_abs_path_to_small_subset,file), "r").read() for file in os.listdir(self.temp_abs_path_to_small_subset)}
        #p(self.small_subset)

        ######## Folders Creation ##############
        ########### End #####################
        
       



    def tearDown(self):
        self.tempdir.cleanup()


####################################################################################################
####################################################################################################
###################### START STABLE TESTS #########################################################
####################################################################################################
####################################################################################################


###################INITIALISATION:000############################################



    ###### xxx: 000 ######




    ##### xx :0== ######


    #@attr(status='stable')
    @wipd
    def test_initialisation_001(self):
        BloggerCorp = BloggerCorpus(self.small_subset)

        

    ##### throws_exceptions:050  ######




#################################Beginn##############################################
############################INTERN METHODS###########################################
#####################################################################################

###################    :100############################################ 

    ###### ***** ######

    #@attr(status='stable')
    #@wipd
    #def test_XXX_name_100(self):
    ##self.logger_initialisation()
    #   pass

    ###### ***** ######


    ###### ***** ######






#################################END#################################################
############################INTERN METHODS###########################################
#####################################################################################








#################################Beginn##############################################
############################EXTERN METHODS###########################################
#####################################################################################


###################    :500############################################ 
    ###### ***** ######
   

   



#################################END##################################################
############################EXTERN METHODS############################################
######################################################################################





####################################################################################################
####################################################################################################
###################### STOP STABLE TESTS #########################################################
####################################################################################################
####################################################################################################


























####################################################################################################
####################################################################################################
###################### START WORK_IN_PROGRESS (wipd) TESTS #########################################
####################################################################################################
####################################################################################################











####################################################################################################
####################################################################################################
###################### STOP WORK_IN_PROGRESS (wipd) TESTS #########################################
####################################################################################################
####################################################################################################







