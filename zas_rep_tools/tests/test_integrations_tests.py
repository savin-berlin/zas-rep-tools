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
import sure
import copy
from nose.plugins.attrib import attr
from testfixtures import tempdir, TempDirectory
from distutils.dir_util import copy_tree 
import json
import csv
from collections import Counter, defaultdict


from zas_rep_tools.src.classes.configer import Configer
from zas_rep_tools.src.classes.stats import Stats
from zas_rep_tools.src.classes.corpus import Corpus
from zas_rep_tools.src.utils.debugger import p, wipd, wipdn, wipdl, wipdo
from zas_rep_tools.src.utils.basetester import BaseTester
import  zas_rep_tools.src.utils.db_helper as db_helper



import platform
if platform.uname()[0].lower() !="windows":
    import colored_traceback
    colored_traceback.add_hook()
else:
    import colorama



class TestZASIntergrationTests(BaseTester,unittest.TestCase):
    #_multiprocess_can_split_ = True
    _multiprocess_shared_  = True
    #@classmethod 
    def setUp(self):
        super(type(self), self).setUp()



    #@classmethod 
    def tearDown(self):
        super(type(self), self).tearDown()


####################################################################################################
####################################################################################################
###################### START STABLE TESTS #########################################################
####################################################################################################
####################################################################################################




    ###### xxx: 000 ######




    ##### xx :0== ######


    @attr(status='stable')
    #@wipd
    def test_data_insertion_000(self):
        stats = Stats(mode=self.mode)
        stats.should.be.a(Stats)

        

    ##### throws_exceptions:050  ######




#################################Beginn##############################################
############################INTERN METHODS###########################################
#####################################################################################

###################    :100############################################ 

    ###### ***** ######



    ###### ***** ######


    ###### ***** ######






#################################END#################################################
############################INTERN METHODS###########################################
#####################################################################################








#################################Beginn##############################################
############################EXTERN METHODS###########################################
#####################################################################################


###################  Corpus Initialization :500############################################ 


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






