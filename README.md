***Notice: 
*** 1. This Package still to be in the developing proccess.
*** 2. This Package support Error Tracking in the real time. If you will have some problem, this will be send directly to the developers. 

# System level

#### System Requirements

    python 2.7
    pip
    virtualenv 

#### System Requirements (installation)
    sudo apt-get install python-pip
    pip install virtualenv 

---
---
---
---




# Package level

### Installation 

This guide assumes `virtualenv`. It is used to isolate the environment and dependences.

    $ virtualenv env 
    $ . env/bin/activate
    $ pip install -e .
---
---





### Testing
This guide assumes 'nosetests' for testing this package 

##### run tests: 

    $ nosetests --rednose -a status='stable'
    
<!-- ##### Errors

Those 2 types of errors are allowed during the testing process (Overall there is 3 errors):

1. "ImportError: C extension: hashtable not built. If you want to import pandas from the source directory, you may need to run 'python setup.py build_ext --inplace --force' to build the C extensions first."
2. "\__name__ must be set to a string object" -->

---
---
<!-- 

### Additional Data 
##### Test Corpora 
This package contains 3 tests corpora. You will find them here:

    'twotxt_corpus_tools/twotxt_corpus_tools/test_corpora' 
--- -->

### __Usage__
#### __CLI__
This package include/support command line interface 

    $ zas-rep-tools
<!--     **if you want to give current path
    $ (pwd; echo segments; echo vot; echo votvoiced;) | xargs zas-vot-tools
    $ zas-vot-tools . segments vot votvoiced
    --> 
<!-- Following tools can be used with 'corpus-tools':

    annotate
    mkcorp
    tfidf -->


##### __Notice:__   

Reader:
    -> support 96 diff encodings. To see which exactly use "zas-rep-tools encodings" in the Terminal
    PlainTextCorpusReader:
        -> all txt files should be in the same folder
        -> 

Streamer:
    Start to use streamer:
    -> Register as a Twitter user (https://twitter.com).
    -> Create a new Twitter application (https://apps.twitter.com) and receive consumer key and secret.
    -> After the step above, you will be redirected to your app's page. Create an access token in the "Your access token" section.
    -> could be just be given up to 400 terms/stops_words
    -> just stream for language is not allow, terms should be given also 
    Languages
        -> twitter supported languages
            https://developer.twitter.com/en/docs/developer-utilities/supported-languages/api-reference/get-help-languages.html
        -> langid suppported languages
            https://github.com/saffsd/langid.py
        -> should be given as (ISO 639-1 codes given) 
    Stop_word:
        -> there is a good and filtered stop-word just for german language on board. 
        -> another stop-words, which are not really filtered and could be same in the another languages was toked from nltk.corpus.stopword. ["dutch","finnish","german","italian", "portuguese","spanish","turkish","danish","english", "french","hungarian","norwegian","russian","swedish"]
        -> supported stop words_ [u'ru', u'fr', u'en', u'nl', u'pt', u'no', u'sv', u'de', u'tr', u'it', u'hu', u'fi', u'da', u'es']
        -> wenn die Sprache gegeben ist, und keine Stop-words explizit gegeben wurden, dann sucht das Tool in dem internen-set of stop-words, wenn erfolgreich, dann wird dieses Set genommen. 
    Strategie:
        ->  Tip: l+t liefert viel mehr von den Tweets aus einer bestimmten Sprache!!! (ung. 35-45 % mehr als die "t" strategie) also, Empfehlung: zu den stopp-words immer die Sprache bestimmen
        -> können ausgewählt werden
        -> retweets können ignoriert werden
        -> wenn keine Strategie explizit ausgewählt ist, dann ermittelt das Tool anhand von den vorhandenen Daten selst die beste Strategie 
    used-terms
        -> können nach Wusnch sicherheitshalber auf den Disk gespeichert werden

    input stop_words/terms
        - could be given, 
            -> as path_to txt file, each word each line
            -> just for stop_words -> a langauge code for exist intern stop-words set
            -> a comma-separated-string as a given set(!! without any spaces in-between) 
    $ zas-rep-tools streamTwitter ./ -l de




##### __Descriptions:__   
<!-- 
1.  __annotate__    

    __Usage:__ corpus-tools annotate [OPTIONS] PATHS_TO_REFERENZ_CORPORA 
PATHS_TO_CORPORA_TO_ANNOTATE KEY_WORDS FEATURES

    __Options__:   
        __-s, --save_in PATH__  Enter path to save annotated corpora   
        __-afh, --ask_for_help (True/False)__ Ask client/user for help during annotations prozess   
        __-n, --number_of_top_results INTEGER__ How much top results of tfidf should be used   
        __-ss, --show_statistics (True/False)__ How much top results of tfidf  should be used   
        __-sa, --show_attention (True/False)__ Show attention message, if  something are wrong during tfidf  computations process   
        __-nr, --ngram_range <INTEGER INTEGER>...__   Enter ngramm range, for tfidf algorithm. *for using ngramms   
        __-l, --language TEXT (german|english)__ Enter corpora language   
        __-sr, --show_rules  True|False__ Print found rules(top tfidf)   
        __-stem, --stemm   (True|False)__ Stemmen corpora       
        __-min, --min_df INTEGER__     Is used for removing terms that appear too  infrequently. #for tfidf     
        __-max, --max_df FLOAT__   Is used for removing terms that appear too frequently, also known as "corpus-specific stop words" #for tfidf  
        __-r, --report (True|False)__     Print Annotations Report  
        __--help__          Show this message and exit.     

    __Examples__:   
    *if __one input corpus__ is given*

    ```
    $ corpus-tools annotate csl_corp.txt pc_brack.txt 'Betriebssystem, HDD' ''{computer.os}', '{computer.hard_drive}''
    ```
    
    *if __many input corpora__ are given*
    ```
    $ corpus-tools annotate 'csl_corp.txt, pc_corp.txt' 'pc_brack.txt, csl_corp.txt' 'Betriebssystem, HDD' ''{computer.os}', '{computer.hard_drive}''
    ```
    *Using some __options__*
    ```
    corpus-tools annotate 'DE/BNP_Paribas_cleaned.txt, DE/CS_AnnualReport_DE_cleaned.txt, DE/CS-Newsletter-DE_cleaned.txt' DE/BNP_Paribas_cleaned.txt 'Performance' '{FUND:PERFORMANCE}'  -n 5  -ss True  -nr 1 5 -sr True -afh True -sa True
    ```
    
2. __mkcorp__    

    __Usage:__ corpus-tools mkcorp [OPTIONS] [PATHS]...
    
    __Options:__   
    __-sav, --save_in PATH__     Enter path to save exported corpora   
    __-cat, --category TEXT__    Enter category name, if you want to insert this tag into corpus    
    __-exp, --type_of_export TEXT (txt)__     Enter data type for export corpora.     
    __-imp, --type_of_import TEXT (txt|csv)__ )    Enter data type for import corpora  *necessary, if file extension is not given.    
    __-tef, --text_field TEXT__         To change default Text-Field-Designation  *only for CSV File.    
    __-urf, --url_field TEXT__  To change default URL-Field-Designation *only for CSV File.    
    __-tif, --titel_field TEXT__    To change default Titel-Field-Designation *only for CSV File.    
    __-idf, --id_field TEXT__     To change default ID-Field-Designation *only for CSV File.    
    __-ice, --ingnore_content_err (True/False)__ Ignore all content validations errors *only for CSV File.    
    __-vae, --valid_err(True/False)__ See all validations errors  *only for CSV File.    
    __--help__         Show this message and exit.    

    __Examples:__
    FOR STANDARD(product description corpora) CSV HEADERS [Titel, Text, URL, ...]
    *without otions:*
     ```
    corpus-tools mkcorp notebooks-brack.ch.pl.csv pc-brack.ch.pl.csv
     ```
    *with some options*
     ```
     corpus-tools mkcorp notebooks-brack.ch.pl.csv pc-brack.ch.pl.csv -sav mkcorp -cat computer -vae True
      ```
      
      FOR NOT-STANDARD CSV HEADERS [.....]
      *if you want to read csv-file with non-standard headers, you need to enter new headers name*
       ```
       corpus-tools mkcorp funds/BNP_Paribas_cleaned.csv -vae True -tif Fonds -tef Kommentar -sav mkcorp
        ```
      
     
3.  __tfidf__   

    __Usage__:  corpus-tools tfidf [OPTIONS] GIVEN_WORD [PATHS]  

    __*Options*__:       
    __-n, --number_of_top_results INTEGER__  How much top results of tfidf should be used   
    __-ss, --show_statistics (True/False)__      Show statistics while computation of tfidf    
    ___-sa, --show_attention (True/False)__ Show attention message, if something is wrong during tfidf computations process     
    __-nr, --ngram_range <INTEGER INTEGER>...___ Enter ngramm range, for tfidf algorithm. *for using ngramms    
    ___-l, --language TEXT  (german|english)___ Enter corpora language    
    __-stem, --stemm  (True|False)__ Stemmen corpora    
    __-min, --min_df INTEGER|FLOAT__ Is used for removing terms that appear too infrequently. #for tfidf     
    __-max, --max_df INTEGER|FLOAT__ Is used for removing terms thatappear too frequently, also known as  "corpus-specific stop words" #for tfidf     
    __-uad, --use_as_document TEXT (texts|sents|corpus)__ Use as documents for tfidf computations *for tfidf     
    __--help__      Show this message and exit.    

    __Examples__:    
    *without options*  
    ```
    corpus-tools tfidf Betriebssystem csl_corp.txt pc_brack.txt
    ```
    with some options  
     ```
     corpus-tools tfidf Performance ACATIS_examples.txt     BNP_Paribas_cleaned.txt MMD_cleaned.txt -n 10 -nr 1 3 -stem True -l german -max 0.5 -min 1
     ```
---

##### Classes   
This package include: 7 independed classes:   

    Corpus; include (Text, Sentence)
    Exporter
    Reader
    Statistics
    Annotator


###### Statistics   
Following parameters can be used:

1. __use_as_document__:('Text'/'Corpus'/'Sentences') for fix on, what par of corpus/corpora will be used as documents.      
2. __number_of_top_results__:(Number) Number of and results/rules   
3. __stemm__(True/False): should text to be stemmed    
4. __ngram_range__(Number_up,Number_to): which ngramm should be account while computations prozess    
5. __show_statistics__(True/False): should be statistics showed during prozess   
6. __show_attention__(True/False): should be some heplfull message showed or not. sometimes it is possible to predict, if end result will be good or not  
7. __ask_user_for_help__(True/false): Should user be asked for help during tfidf computational process   
8. __language__(german/english):    

---

##### Scripts
This package include following scripts:

    sent_segmentator
     -->
---
#### Bib:
This package include unclude following collection of functions 

    debugger




zas-vot-tools strat1 sets/train_set sets/eval_set  segments voiceless voiced vlwindow vcwindow /Volumes/ZAS_Egor/test/experiments

















