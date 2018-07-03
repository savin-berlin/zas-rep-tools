#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# : Create Test DBs
# Author:
# c(Developer) ->     {'Egor Savin'}
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

###Programm Info######



from zas_rep_tools.src.classes.DBHandler import DBHandler



input_row1= ["schöööööönen","taaaaaag", "dirrrrrr"]
input_row2= ["kliiiiitze","kliiiiiittttzzzzeee", "kleeeeeinnn", "kleinnn"]
input_row3 = ["üblich","üüüüübbbbblllliiiiiichhh", "essss"]
input_row4 = ["😀","😀", "😀", "😀", "😀"]
input_row5 = ["pitty","piiittyyy", "day"]
input_row6 = ["доооооооброоооооггггоо","доброоогооо ", "дняяяяяяяяяяяяя"]

blog_value1 = [input_row1, u'm', u'27', u'IT', u'lion' ]
blog_value2 = [input_row2, u'm', u'23', u'Care', u'fish' ]
blog_value3 = [input_row3, u'm', u'27', u'IT', u'lion' ]
blog_value4 = [input_row4, u'm', u'27', u'IT', u'lion' ]
blog_value5 = [input_row5, u'm', u'27', u'IT', u'lion' ]
blog_value6 = [input_row6, u'm', u'22', u'Wirtschaft', u'Krebs' ]

twitter_value1= [input_row1, u"20/06/2014", u"de", u"Iphone", u"20/06/2011", u"Neiiiiin", 45, 76, 765, 34567890, u"en", u"uniqPerson", u"realBro", u"True" ]
twitter_value2= [input_row2, u"20/06/2014", u"de", u"Iphone", u"20/06/2011", u"Neiiiiin", 45, 76, 765, 34567890, u"en", u"uniqPerson", u"realBro", u"True" ]
twitter_value3= [input_row3, u"20/06/2014", u"de", u"Iphone", u"20/06/2011", u"Neiiiiin", 45, 76, 765, 34567890, u"en", u"uniqPerson", u"realBro", u"True" ]
twitter_value4= [input_row4, u"20/06/2014", u"de", u"Iphone", u"20/06/2011", u"Neiiiiin", 45, 76, 765, 34567890, u"en", u"uniqPerson", u"realBro", u"True" ]
twitter_value5= [input_row5, u"20/06/2014", u"de", u"Iphone", u"20/06/2011", u"Neiiiiin", 45, 76, 765, 34567890, u"en", u"uniqPerson", u"realBro", u"True" ]
twitter_value6= [input_row6, u"20/06/2014", u"de", u"Iphone", u"20/06/2011", u"Neiiiiin", 45, 76, 765, 34567890, u"en", u"uniqPerson", u"realBro", u"True" ]



#Blogger Corpus:
def create_blogger_corpus():
	db = DBHandler()
	db.init("corpus", ".", "blogger", "de", "extern", platform_name="blogs", license="MIT" , template_name="blogger", version="2", source="LanguageGoldMine", corpus_id="7614")

	columns = [ u'text', u'gender', u'age', u'working_area', u'star_constellation']

	db.insertCV("documents", columns, blog_value1)
	db.insertCV("documents", columns, blog_value2)
	db.insertCV("documents", columns, blog_value3)
	db.insertCV("documents", columns, blog_value4)
	db.insertCV("documents", columns, blog_value5)
	db.insertCV("documents", columns, blog_value6)

	path_to_db = db.path()
	db.close()
	return path_to_db




#Blogger Stats:
def create_blogger_stats():
	db = DBHandler()
	db.init("stats", ".", "blogger", "de", "extern", corpus_id="7614" , version="2", stats_id="3497")


	path_to_db = db.path()
	db.close()
	return path_to_db




######################
#Twitter Corpus:
def create_blogger_stats():
	db = DBHandler()
	db.init("corpus", ".", "streamed", "de", "intern", platform_name="twitter", license="MIT" , template_name="twitter", version="2", source="Twitter API", encryption_key="corpus", corpus_id="9588")
	
	columns = [ u'text', u't_created_at', u't_language', u't_used_client', u'u_created_at', u'u_description', u'u_favourites', u'u_followers', u'u_friends', u'u_id', u'u_lang', u'u_given_name', u'u_username', u'u_verified']

	db.insertCV("documents", columns, twitter_value1)
	db.insertCV("documents", columns, twitter_value2)
	db.insertCV("documents", columns, twitter_value3)
	db.insertCV("documents", columns, twitter_value4)
	db.insertCV("documents", columns, twitter_value5)
	db.insertCV("documents", columns, twitter_value6)

	path_to_db = db.path()
	db.close()
	return path_to_db




#
#Twitter Stats:
def create_blogger_stats():
	db = DBHandler()
	db.init("stats", ".", "streamed", "de", "intern", corpus_id="9588" , version="2", encryption_key="stats", stats_id="6361")

	path_to_db = db.path()
	db.close()
	return path_to_db



