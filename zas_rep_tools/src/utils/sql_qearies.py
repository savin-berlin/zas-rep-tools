#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# : SQL Helper 
# Author:
# c(Student) ->     {'Egor Savin'}
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

###Programm Info######




#######################################################################################
##################################PROJECTS#############################################
#######################################################################################




qeary_initialise_twitter_documents_in_ProjectDB = '''
CREATE TABLE "Documents" (
"Corpus_ID" INTEGER NOT NULL,
"Document_ID" INTEGER  PRIMARY KEY,
"t_id" INTEGER NOT NULL,
"t_created_at" TEXT,
"t_language" TEXT,
"t_used_client" TEXT,
"text" BLOB,
"u_created_at" TEXT,
"u_description" TEXT,
"u_favourites" INTEGER,
"u_followers" INTEGER,
"u_friends" TEXT,
"u_id" INTEGER,
"u_lang" TEXT,
"u_given_name" TEXT,
"u_username" TEXT,
"u_verified" TEXT,
"u_location" TEXT,
CONSTRAINT "fk_tweets_Corpora_1" FOREIGN KEY ("Corpus_ID") REFERENCES "Corpora" ("Corpus_ID"),
CONSTRAINT "Uniq_Tweet_ID" UNIQUE ("Document_ID")
);
CREATE INDEX "ix_tweets_corpus_document" ON "Documents" ("Corpus_ID" ASC, "Document_ID" ASC);
'''



query_default_documents_in_ProjectDB= '''
CREATE TABLE "Documents" (
"Corpus_ID" INTEGER NOT NULL,
"Document_ID" INTEGER PRIMARY KEY,
{}
"text" BLOB,
CONSTRAINT "fk_blogger.Documents_Corpora_1" FOREIGN KEY ("Corpus_ID") REFERENCES "Corpora" ("Corpus_ID"),
CONSTRAINT "Uniq_Blogger_ID" UNIQUE ("Document_ID")
);
CREATE INDEX "ix_default_corpus_document" ON "Documents" ("Corpus_ID" ASC, "Document_ID" ASC);
'''

qeary_initialise_blogger_documents_in_ProjectDB = '''
CREATE TABLE "Documents" (
"Corpus_ID" INTEGER NOT NULL,
"Document_ID" INTEGER  PRIMARY KEY,
"blogger_id" INTEGER ,
"gender" TEXT,
"age" INTEGER,
"working_area" TEXT,
"star-constellation" TEXT,
"text" BLOB,
CONSTRAINT "fk_blogger.Documents_Corpora_1" FOREIGN KEY ("Corpus_ID") REFERENCES "Corpora" ("Corpus_ID"),
CONSTRAINT "Uniq_Blogger_ID" UNIQUE ("Document_ID")
);
CREATE INDEX "ix_blogger_corpus_document" ON "Documents" ("Corpus_ID" ASC, "Document_ID" ASC);
'''






qeary_initialise_replications_in_ProjectDB = '''
CREATE TABLE "Replications" (
"Stats_ID" INTEGER NOT NULL,
"Repl_ID" INTEGER  PRIMARY KEY,
"Document_ID" INTEGER NOT NULL,
"token_nr" INTEGER,
"word" TEXT,
"rle" TEXT,
"repl_letter" TEXT,
"nr_of_repl" INTEGER,
"index_of_repl" INTEGER,
"context_left_1" TEXT,
"context_left_2" TEXT,
"context_left_3" TEXT,
"context_right_1" TEXT,
"context_right_2" TEXT,
"context_right_3" TEXT,
CONSTRAINT "fk_replications_Stats_1" FOREIGN KEY ("Stats_ID") REFERENCES "Statistics" ("Stats_ID"),
CONSTRAINT "fk_replications_tweets_1" FOREIGN KEY ("Document_ID") REFERENCES "Documents" ("Document_ID"),
CONSTRAINT "fk_replications_blogger_1" FOREIGN KEY ("Document_ID") REFERENCES "Bloggers" ("Blogger_ID"),
CONSTRAINT "fk_replications_documents_1" FOREIGN KEY ("Document_ID") REFERENCES "Documents" ("Document_ID"),
CONSTRAINT "Uniq_Repl_ID" UNIQUE ("Repl_ID")
);
CREATE INDEX "ix_replications_stats_docs_repl" ON "Replications" ("Stats_ID" ASC, "Document_ID" ASC, "Repl_ID" ASC);
'''

qeary_initialise_reduplications_in_ProjectDB = '''
CREATE TABLE "Reduplications" (
"Stats_ID" INTEGER NOT NULL,
"Redu-ID" INTEGER  PRIMARY KEY,
"Document_ID" INTEGER NOT NULL,
"token_nr" INTEGER,
"word" TEXT,
"nr_of_redu" INTEGER,
"scopus" INTEGER,
"context_left_1" TEXT,
"context_left_2" TEXT,
"context_left_3" TEXT,
"context_right_1" TEXT,
"context_right_2" TEXT,
"context_right_3" TEXT,
CONSTRAINT "fk_twitter.Reduplications" FOREIGN KEY ("Document_ID") REFERENCES "Documents" ("Document_ID"),
CONSTRAINT "Uniq_Redu-ID" UNIQUE ("Redu-ID")
);
CREATE INDEX "ix_reduplications_on_stats_docs_redu" ON "Reduplications" ("Stats_ID" ASC, "Document_ID" ASC, "Redu-ID" ASC);
'''



qeary_initialise_baseline_in_ProjectDB = '''
CREATE TABLE "Baseline" (
"Stats_ID" INTEGER NOT NULL,
"word" TEXT NOT NULL,
"redu_counts" INTEGER,
"repl_counts" INTEGER,
"all_counts" TEXT,
"repl_IDs" TEXT,
"rudi_IDs" TEXT,
CONSTRAINT "fk_baseline_Stats_1" FOREIGN KEY ("Stats_ID") REFERENCES "Statistics" ("Stats_ID")
);
CREATE INDEX "ix_baseline_stats_word" ON "Baseline" ("Stats_ID" ASC, "word" ASC);
'''




###########






