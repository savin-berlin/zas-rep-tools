
import os
import logging

from zas_rep_tools.src.classes.Exporter import Exporter
from zas_rep_tools.src.classes.Reader import Reader
from zas_rep_tools.src.utils.recipes_test_db import *


path_to_zas_rep_tools = path_to_zas_rep_tools
fieldnames = blogger_columns
#####################
# Test Blogger Corpus#
#######Begin#########

path_to_test_sets_for_blogger_Corpus = "data/tests_data/Corpora/BloggerCorpus"
txt_blogger_hightrepetativ_set = "txt/HighRepetativSubSet"
txt_blogger_small_fake_set = "txt/SmallFakeSubset"
txt_blogger_small_set = "txt/SmallSubset"

csv_blogger_hightrepetativ_set = "csv/HighRepetativSubSet"
csv_blogger_small_fake_set = "csv/SmallFakeSubset"
#csv_blogger_small_fake_set = "csv/SmallSubset"


xml_blogger_hightrepetativ_set = "xml/HighRepetativSubSet"
xml_blogger_small_fake_set = "xml/SmallFakeSubset"
#xml_blogger_small_set = "xml/SmallSubset"


json_blogger_hightrepetativ_set = "json/HighRepetativSubSet"
json_blogger_small_fake_set = "json/SmallFakeSubset"
#json_blogger_small_set = "json/SmallSubset"


#######End###########
# Test Blogger Corpus#
#####################




def export_to_csv():

	#1 -hightrepetativ_set
	reader = Reader(os.path.join(path_to_zas_rep_tools,path_to_test_sets_for_blogger_Corpus , txt_blogger_hightrepetativ_set), "txt", regex_template="blogger", logger_level=logging.ERROR)
	exporter = Exporter(reader.getlazy(), logger_level=logging.ERROR)
	exporter.tocsv(".", "blogger_corpus",fieldnames, rows_limit_in_file=2)

	#2 - 
	reader = Reader(os.path.join(path_to_zas_rep_tools,path_to_test_sets_for_blogger_Corpus , txt_blogger_small_fake_set ), "txt", regex_template="blogger", logger_level=logging.ERROR)
	exporter = Exporter(reader.getlazy(), logger_level=logging.ERROR)
	exporter.tocsv(".", "blogger_corpus",fieldnames, rows_limit_in_file=2)

	#3
	reader = Reader(os.path.join(path_to_zas_rep_tools,path_to_test_sets_for_blogger_Corpus , txt_blogger_small_set), "txt", regex_template="blogger", logger_level=logging.ERROR)
	exporter = Exporter(reader.getlazy(), logger_level=logging.ERROR)
	exporter.tocsv(".", "blogger_corpus",fieldnames, rows_limit_in_file=5)



def export_to_xml():

	#1 -hightrepetativ_set
	reader = Reader(os.path.join(path_to_zas_rep_tools,path_to_test_sets_for_blogger_Corpus , txt_blogger_hightrepetativ_set), "txt", regex_template="blogger", logger_level=logging.ERROR)
	exporter = Exporter(reader.getlazy(), logger_level=logging.ERROR)
	exporter.toxml(".", "blogger_corpus", rows_limit_in_file=2)

	#2 - 
	reader = Reader(os.path.join(path_to_zas_rep_tools,path_to_test_sets_for_blogger_Corpus , txt_blogger_small_fake_set ), "txt", regex_template="blogger", logger_level=logging.ERROR)
	exporter = Exporter(reader.getlazy(), logger_level=logging.ERROR)
	exporter.toxml(".", "blogger_corpus", rows_limit_in_file=2)

	#3
	reader = Reader(os.path.join(path_to_zas_rep_tools,path_to_test_sets_for_blogger_Corpus , txt_blogger_small_set), "txt", regex_template="blogger", logger_level=logging.ERROR)
	exporter = Exporter(reader.getlazy(), logger_level=logging.ERROR)
	exporter.toxml(".", "blogger_corpus", rows_limit_in_file=5)



def export_to_json():

	#1 -hightrepetativ_set
	reader = Reader(os.path.join(path_to_zas_rep_tools,path_to_test_sets_for_blogger_Corpus , txt_blogger_hightrepetativ_set), "txt", regex_template="blogger", logger_level=logging.ERROR)
	exporter = Exporter(reader.getlazy(), logger_level=logging.ERROR)
	exporter.tojson(".", "blogger_corpus", rows_limit_in_file=2)

	#2 - 
	reader = Reader(os.path.join(path_to_zas_rep_tools,path_to_test_sets_for_blogger_Corpus , txt_blogger_small_fake_set ), "txt", regex_template="blogger", logger_level=logging.ERROR)
	exporter = Exporter(reader.getlazy(), logger_level=logging.ERROR)
	exporter.tojson(".", "blogger_corpus", rows_limit_in_file=2)

	#3
	reader = Reader(os.path.join(path_to_zas_rep_tools,path_to_test_sets_for_blogger_Corpus , txt_blogger_small_set), "txt", regex_template="blogger", logger_level=logging.ERROR)
	exporter = Exporter(reader.getlazy(), logger_level=logging.ERROR)
	exporter.tojson(".", "blogger_corpus", rows_limit_in_file=5)



def export_to_sqlite():

	#1 -hightrepetativ_set
	reader = Reader(os.path.join(path_to_zas_rep_tools,path_to_test_sets_for_blogger_Corpus , txt_blogger_hightrepetativ_set), "txt", regex_template="blogger", logger_level=logging.ERROR)
	exporter = Exporter(reader.getlazy(), logger_level=logging.ERROR)
	exporter.tosqlite(".", "blogger_corpus",fieldnames)

	#2 - 
	reader = Reader(os.path.join(path_to_zas_rep_tools,path_to_test_sets_for_blogger_Corpus , txt_blogger_small_fake_set ), "txt", regex_template="blogger", logger_level=logging.ERROR)
	exporter = Exporter(reader.getlazy(), logger_level=logging.ERROR)
	exporter.tosqlite(".", "blogger_corpus",fieldnames)

	#3
	reader = Reader(os.path.join(path_to_zas_rep_tools,path_to_test_sets_for_blogger_Corpus , txt_blogger_small_set), "txt", regex_template="blogger", logger_level=logging.ERROR)
	exporter = Exporter(reader.getlazy(), logger_level=logging.ERROR)
	exporter.tosqlite(".", "blogger_corpus",fieldnames)
