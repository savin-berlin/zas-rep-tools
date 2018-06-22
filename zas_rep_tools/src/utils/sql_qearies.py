#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# : SQL Helper 
# Author:
# c(Student) ->     {'Egor Savin'}
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

###Programm Info######

qeary_initialise_projects_in_mainDB = '''
CREATE TABLE "Projects" (
"Project_acronyme" TEXT  PRIMARY KEY,
"project_name" TEXT NOT NULL,
CONSTRAINT "Uniq_Template_ID" UNIQUE ("Project_acronyme")
CONSTRAINT "Uniq_Project_Name" UNIQUE ("project_name")
);
CREATE INDEX "ix_templates_template" ON "Projects" ("Project_acronyme" ASC);
'''


# qeary_initialise_corpora_in_mainDB = '''
# CREATE TABLE "Corpora" (
# "Project_acronyme" INTEGER NOT NULL,
# "lang_acronyme" INTEGER NOT NULL,
# "Corpus_ID" INTEGER NOT NULL,
# "corpus_name" TEXT NOT NULL,
# PRIMARY KEY ("Corpus_ID") ,
# CONSTRAINT "fk_Corpora_Templates_1" FOREIGN KEY ("Project_acronyme") REFERENCES "Projects" ("Project_acronyme"),
# CONSTRAINT "fk_Corpora_schema.Statistics_1" FOREIGN KEY ("Corpus_ID") REFERENCES "schema.Statistics" ("Corpus_ID"),
# CONSTRAINT "fk_Corpora_Languages_1" FOREIGN KEY ("lang_acronyme") REFERENCES "Languages" ("lang_acronyme"),
# CONSTRAINT "Uniq_Corpus_ID" UNIQUE ("Corpus_ID")
# );
# CREATE INDEX "ix_corpora_template_corpus" ON "Corpora" ("Project_acronyme" ASC, "Corpus_ID" ASC);
# '''


qeary_initialise_languages_in_mainDB = '''
CREATE TABLE "Languages" (
"lang_acronyme" TEXT PRIMARY KEY,
"lang_name" TEXT NOT NULL,
CONSTRAINT "Uniq_Language_Name" UNIQUE ("lang_name")
CONSTRAINT "Uniq_Language_acronym" UNIQUE ("lang_acronyme")
);
CREATE INDEX "ix_name" ON "Languages" ("lang_name");
CREATE INDEX "ix_id" ON "Languages" ("lang_acronyme");

'''





#######################################################################################
##################################PROJECTS#############################################
#######################################################################################



# qeary_initialise_corpora_in_ProjectDB = '''
# CREATE TABLE "{label_of_project}.Corpora" (
# "Project_acronyme" INTEGER NOT NULL,
# "lang_acronyme" INTEGER NOT NULL,
# "Corpus_ID" INTEGER NOT NULL,
# "corpus_name" TEXT NOT NULL,
# PRIMARY KEY ("Corpus_ID") ,
# CONSTRAINT "fk_{label_of_project}_Corpora_Projects_1" FOREIGN KEY ("Project_acronyme") REFERENCES "Projects" ("Project_acronyme"),
# CONSTRAINT "fk_{label_of_project}_Corpora_Languages_1" FOREIGN KEY ("lang_acronyme") REFERENCES "Languages" ("lang_acronyme"),
# CONSTRAINT "Uniq_{label_of_project}_Corpus_ID" UNIQUE ("Corpus_ID")
# );
# CREATE INDEX "ix_{label_of_project}_corpora_template_corpus" ON "{label_of_project}.Corpora" ("Project_acronyme" ASC, "{label_of_project}.Corpus_ID" ASC);
# '''

qeary_initialise_corpora_in_ProjectDB = '''
CREATE TABLE "Corpora" (
"Project_acronyme" INTEGER NOT NULL,
"lang_acronyme" INTEGER NOT NULL,
"Corpus_ID" INTEGER PRIMARY KEY,
"corpus_name" TEXT NOT NULL,
CONSTRAINT "fk_Corpora_Templates_1" FOREIGN KEY ("Project_acronyme") REFERENCES "Projects" ("Project_acronyme"),
CONSTRAINT "fk_Corpora_schema.Statistics_1" FOREIGN KEY ("Corpus_ID") REFERENCES "Statistics" ("Corpus_ID"),
CONSTRAINT "fk_Corpora_Languages_1" FOREIGN KEY ("lang_acronyme") REFERENCES "Languages" ("lang_acronyme"),
CONSTRAINT "Uniq_Corpus_ID" UNIQUE ("Corpus_ID")
);
CREATE INDEX "ix_corpora_template_corpus" ON "Corpora" ("Project_acronyme" ASC, "Corpus_ID" ASC);
'''



qeary_initialise_statistics_in_ProjectDB = '''
CREATE TABLE "Statistics" (
"corpus_ID" INTEGER NOT NULL,
"Stats_ID" INTEGER PRIMARY KEY,
"stat_name" TEXT NOT NULL,
CONSTRAINT "fk_Stats_Corpora_1" FOREIGN KEY ("corpus_ID") REFERENCES "Corpora" ("Corpus_ID"),
CONSTRAINT "Uniq_Stats_ID" UNIQUE ("Stats_ID")
);
CREATE INDEX "ix_statistics_corpus_stats" ON "Statistics" ("corpus_ID" ASC, "Stats_ID" ASC);
'''




# qeary_initialise_statistics_in_ProjectDB = '''
# CREATE TABLE "{label_of_project}.Statistics" (
# "corpus_ID" INTEGER NOT NULL,
# "Stats_ID" INTEGER NOT NULL,
# "stat_name" TEXT NOT NULL,
# PRIMARY KEY ("Stats_ID") ,
# CONSTRAINT "fk_{label_of_project}_Stats_Corpora_1" FOREIGN KEY ("corpus_ID") REFERENCES "{label_of_project}.Corpora" ("Corpus_ID"),
# CONSTRAINT "Uniq_{label_of_project}_Stats_ID" UNIQUE ("{label_of_project}.Stats_ID")
# );
# CREATE INDEX "ix_{label_of_project}_statistics_corpus_stats" ON "{label_of_project}.Statistics" ("{label_of_project}.corpus_ID" ASC, "{label_of_project}.Stats_ID" ASC);
# '''




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


qeary_insert_set = '''
INSERT INTO {tableName} SET 
{keys_and_values};
'''

qeary_insert_values_1 = '''
INSERT INTO {tableName} VALUES (
{values}
);
'''

qeary_insert_values_2 = '''
INSERT INTO {tableName} ({key_names})
VALUES ({values});
'''

# qeary_initialise_statistics_in_ProjectDB = '''

# '''


# qeary_initialise_statistics_in_ProjectDB = '''

# '''





# qeary_initialise_statistics_in_ProjectDB = '''

# '''


########
########
########
########
#temp#
#######




# qeary_initialise_corpora_in_ProjectDB = '''
# CREATE TABLE "Corpora" (
# "Project_acronyme" INTEGER NOT NULL,
# "lang_acronyme" INTEGER NOT NULL,
# "Corpus_ID" INTEGER NOT NULL,
# "corpus_name" TEXT NOT NULL,
# PRIMARY KEY ("Corpus_ID") ,
# CONSTRAINT "fk_Corpora_Templates_1" FOREIGN KEY ("Project_acronyme") REFERENCES "Projects" ("Project_acronyme"),
# CONSTRAINT "fk_Corpora_schema.Statistics_1" FOREIGN KEY ("Corpus_ID") REFERENCES "schema.Statistics" ("Corpus_ID"),
# CONSTRAINT "fk_Corpora_Languages_1" FOREIGN KEY ("lang_acronyme") REFERENCES "Languages" ("lang_acronyme"),
# CONSTRAINT "Uniq_Corpus_ID" UNIQUE ("Corpus_ID")
# );
# CREATE INDEX "ix_corpora_template_corpus" ON "Corpora" ("Project_acronyme" ASC, "Corpus_ID" ASC);
# '''



# qeary_initialise_statistics_in_ProjectDB = '''
# CREATE TABLE "twitter.Statistics" (
# "corpus_ID" INTEGER NOT NULL,
# "Stats_ID" INTEGER NOT NULL,
# "stat_name" TEXT NOT NULL,
# PRIMARY KEY ("Stats_ID") ,
# CONSTRAINT "fk_Stats_Corpora_1" FOREIGN KEY ("corpus_ID") REFERENCES "Corpora" ("Corpus_ID"),
# CONSTRAINT "Uniq_Stats_ID" UNIQUE ("Stats_ID")
# );
# CREATE INDEX "ix_statistics_corpus_stats" ON "twitter.Statistics" ("corpus_ID" ASC, "Stats_ID" ASC);
# '''




# qeary_initialise_documents_in_ProjectDB = '''
# CREATE TABLE "twitter.Documents" (
# "Corpus_ID" INTEGER NOT NULL,
# "Document_ID" INTEGER NOT NULL,
# "t_created_at" TEXT,
# "t_language" TEXT,
# "t_used_client" TEXT,
# "t_text" BLOB,
# "u_created_at" TEXT,
# "u_description" TEXT,
# "u_favourites" INTEGER,
# "u_followers" INTEGER,
# "u_friends" TEXT,
# "u_id" INTEGER,
# "u_lang" TEXT,
# "u_given_name" TEXT,
# "u_username" TEXT,
# "u_verified" TEXT,
# "u_location" TEXT,
# PRIMARY KEY ("Document_ID") ,
# CONSTRAINT "fk_tweets_Corpora_1" FOREIGN KEY ("Corpus_ID") REFERENCES "Corpora" ("Corpus_ID"),
# CONSTRAINT "Uniq_Tweet_ID" UNIQUE ("Document_ID")
# );
# CREATE INDEX "ix_tweets_corpus_tweet" ON "twitter.Documents" ("Corpus_ID" ASC, "Document_ID" ASC);
# '''








# qeary_initialise_replications_in_ProjectDB = '''
# CREATE TABLE "twitter.Replications" (
# "Stats_ID" INTEGER NOT NULL,
# "Repl_ID" INTEGER NOT NULL,
# "Document_ID" INTEGER NOT NULL,
# "token_nr" INTEGER,
# "word" TEXT,
# "rle" TEXT,
# "repl_letter" TEXT,
# "nr_of_repl" INTEGER,
# "index_of_repl" INTEGER,
# "context_left_1" TEXT,
# "context_left_2" TEXT,
# "context_left_3" TEXT,
# "context_right_1" TEXT,
# "context_right_2" TEXT,
# "context_right_3" TEXT,
# PRIMARY KEY ("Repl_ID") ,
# CONSTRAINT "fk_replications_Stats_1" FOREIGN KEY ("Stats_ID") REFERENCES "twitter.Statistics" ("Stats_ID"),
# CONSTRAINT "fk_replications_tweets_1" FOREIGN KEY ("Document_ID") REFERENCES "twitter.Documents" ("Document_ID"),
# CONSTRAINT "fk_replications_blogger_1" FOREIGN KEY ("Document_ID") REFERENCES "Bloggers" ("Blogger_ID"),
# CONSTRAINT "fk_replications_documents_1" FOREIGN KEY ("Document_ID") REFERENCES "Documents" ("Document_ID"),
# CONSTRAINT "Uniq_Repl_ID" UNIQUE ("Repl_ID")
# );
# CREATE INDEX "ix_replications_stats_docs_repl" ON "twitter.Replications" ("Stats_ID" ASC, "Document_ID" ASC, "Repl_ID" ASC);
# '''

# qeary_initialise_reduplications_in_ProjectDB = '''
# CREATE TABLE "twitter.Reduplications" (
# "Stats_ID" INTEGER NOT NULL,
# "Redu-ID" INTEGER NOT NULL,
# "Document_ID" INTEGER NOT NULL,
# "token_nr" INTEGER,
# "word" TEXT,
# "nr_of_redu" INTEGER,
# "scopus" INTEGER,
# "context_left_1" TEXT,
# "context_left_2" TEXT,
# "context_left_3" TEXT,
# "context_right_1" TEXT,
# "context_right_2" TEXT,
# "context_right_3" TEXT,
# PRIMARY KEY ("Redu-ID") ,
# CONSTRAINT "fk_twitter.Reduplications_twitter.Documents_1" FOREIGN KEY ("Document_ID") REFERENCES "twitter.Documents" ("Document_ID"),
# CONSTRAINT "Uniq_Redu-ID" UNIQUE ("Redu-ID")
# );
# CREATE INDEX "ix_reduplications_on_stats_docs_redu" ON "twitter.Reduplications" ("Stats_ID" ASC, "Document_ID" ASC, "Redu-ID" ASC);
# '''



# qeary_initialise_baseline_in_ProjectDB = '''
# CREATE TABLE "twitter.Baseline" (
# "Stats_ID" INTEGER NOT NULL,
# "word" TEXT NOT NULL,
# "redu_counts" INTEGER,
# "repl_counts" INTEGER,
# "all_counts" TEXT,
# "repl_IDs" TEXT,
# "rudi_IDs" TEXT,
# CONSTRAINT "fk_baseline_Stats_1" FOREIGN KEY ("Stats_ID") REFERENCES "twitter.Statistics" ("Stats_ID")
# );
# CREATE INDEX "ix_baseline_stats_word" ON "twitter.Baseline" ("Stats_ID" ASC, "word" ASC);
# '''


