 
# ZAS-REP-TOOLS

Current Tool was developed in the frame of the linguistics Study/Project *"The Pragmatic Status of Iconic Meaning in Spoken Communication: Gestures, Ideophones, Prosodic Modulations* ([PSIMS](http://www.zas.gwz-berlin.de/psims.html)) as the Bachelor Thesis.
___



* **Project Members:**
     - [Susanne Fuchs](mailto:fuchs@leibniz-zas.de)
     - [Aleksandra Ćwiek](mailto:cwiek@leibniz-zas.de)
     - [Egor Savin](mailto:work@savin.berlin)
     - [Cornelia Ebert](mailto:ebert@leibniz-zas.de)
     - [Manfred Krifka](mailto:krifka@leibniz-zas.de)



*  **Bachelor Thesis Appraisers:**
    - [Ulf Leser](mailto:leser@informatik.hu-berlin.de)  
    - [Susanne Fuchs](mailto:fuchs@leibniz-zas.de)  


* **Tool-Developer:**
    - [Egor Savin](mailto:work@savin.berlin)

---



**ZAS-REP-TOOLS** is a bundle of Tools for automatic extraction and quantification of the repetitions from the unstructured textual Data Collections for different languages with additional Search Engine wrapped around extracted data +  on-board supplied Twitter Streamer to collect real-time tweets. 




---

**<span style="color:red;">For a quick-start,</span>** first [download and install all dependencies](#dependencies) , then [download and compile the code](#settingup) and afterwards go to the [Tutorials](#tutorials) section to begin.

___


<br/>
<br/>


<a name="toc"/>

## Table of Contents

1. [Hardware Requirements](#requirements)

2. [Dependencies Installation](#dependencies)
    - On Linux 
    - On Windows 
    - On MacOS 

3. [Setting up](#settingup)

4. [Definitions](#definitions)
   -  Repetition
   -  Full Repetitiveness

5. [Functionality](#functionality)
   - Classes
   - CLI-Functions 
   - Multiprocessing
   - NLP-Methods
   - InternDataBase-Structure
     - SQLite
     - ZODB
   - Additional Features
     - Formatters
     - Templates

6. [WorkFlow](#workflow)

7. [Tutorials](#tutorials)
   - Python Package Tutorial 
   -  Command line Tutorial

8. [Input/Output](#input/output)
   - File Formats
   - Output Statistics

9. [Citing ZAS-REP-TOOLS](#citing)



10. [Possible errors and warnings](#errors)

11. [Acknowledgements](#acknowledgements)

---
---

<br/>



---

<br/>

<a name="requirements"/>
<p style='text-align: right;'>  <sub> <a href="#toc">Back to top</a>
</sub> </p>

## 1. Hardware Requirements
 


||  Minimum:    | Average:  |
|:--------------:   |:----------------: | :----------------:    |
| CPU | 2 Core 2 GHz | 4 Core 2.6 GHz  |
| RAM | 8 GB | 16 GB    |



<br/>



---

<br/>



<a name="dependencies"/>
<p style='text-align: right;'>  <sub> <a href="#toc">Back to top</a>
</sub> </p>

## 2. Dependencies


In order to use ZAS-REP-TOOLS you'll need the following installed Dependencies in addition to the source code provided here:

* [Python (both Versions: 2.7 + 3.5 or later)](https://www.python.org/download/releases/2.7.6>)
* [JAVA JDC](https://www.oracle.com/technetwork/java/javase/downloads/java-archive-downloads-javase6-419409.html) 
* [GCC, the GNU Compiler Collection](http://gcc.gnu.org/install/download.html)
* [SQLite3](https://www.sqlite.org/download.html)
* [NoseTests](https://nose.readthedocs.io/en/latest/)
* [Pysqlcipher](https://github.com/leapcode/pysqlcipher)
* Git



#### Dependencies Installation 
following installation commands should be seeing as just an idea how and could become incorrect with time. Important is, that all above listed Dependencies are installed, before you can start to SetUp the Tool. 

<sub>*$ - symbol ensure the begin of the command, which should be copy-pasted into the terminal window.*</sub>

##### On Linux (UbuntuOS 16.04.5 LTS)
    0. open Terminal/Bash/Shell

    1. Add other repositories
        $  sudo add-apt-repository "deb http://archive.canonical.com/ubuntu saucy partner"
        $ sudo add-apt-repository "deb http://us.archive.ubuntu.com/ubuntu/ saucy universe multiverse"
        $ sudo add-apt-repository "deb http://us.archive.ubuntu.com/ubuntu/ saucy-updates universe multiverse"

    2. Upgrade default linux tools
        $ sudo apt-get update
        $ sudo apt-get upgrade

    3. Install additional SW
        $ sudo apt-get install python-setuptools python-dev  build-essential autoconf libtiff5-dev libjpeg8-dev zlib1g-dev libfreetype6-dev liblcms2-dev libwebp-dev tcl8.6-dev tk8.6-dev python-tk  libtool pkg-config python-opengl python-pyrex python-pyside.qtopengl idle-python2.7 qt4-dev-tools qt4-designer libqtgui4 libqtcore4 libqt4-xml libqt4-test libqt4-script libqt4-network libqt4-dbus python-qt4 python-qt4-gl libgle3 python-dev libssl-dev g++ openssl git

    2. Python Installation
        -> python + pip 
            $ sudo add-apt-repository ppa:jonathonf/python-3.6
            $ sudo apt-get update
            $ sudo apt install python2.7 python-pip python3.6 python3-pip  virtualenv curl
            $ sudo -H pip2 install --upgrade pip setuptools
            $ sudo -H pip3 install --upgrade pip setuptools
                --- ensure to have python3.6 http://ubuntuhandbook.org/index.php/2017/07/install-python-3-6-1-in-ubuntu-16-04-lts/
            $ alias python3=python3.6

        -> Additional Python3 packages, which will not be installed automatically 
            $ sudo -H python3 -m pip install somajo someweta

        
    4. Sqlite + Pysqlcipher
        $ sudo apt-get install sqlite3 sqlcipher
        $ sudo -H python2 -m pip install pysqlcipher --install-option="--bundled"
        

    5. JAVA 
        $ sudo add-apt-repository ppa:linuxuprising/java
        $ sudo apt-get update
        $ sudo apt-get install oracle-java11-installer 
            
    6. GIT LFS
        $ sudo apt-get install software-properties-common
        $ sudo add-apt-repository ppa:git-core/ppa
        $ apt-get update
        $ curl -s https://packagecloud.io/install/repositories/github/git-lfs/script.deb.sh | sudo bash
        $ sudo apt-get install git-lfs
        $ git lfs install



<br/>

##### On Windows (Win10)
  (this tool could be invoked just up from the Windows10 Version)


    1. Microsoft Visual C++ Compiler for Python 2.7
       (https://www.microsoft.com/en-us/download/details.aspx?id=44266)
    2. Enable in Features - "Windows Subsystem for Linux"
        (https://docs.microsoft.com/en-us/windows/wsl/install-win10)
    3. Enable in Settings - "Developer Mode"
        (https://www.wikihow.com/Enable-Developer-Mode-in-Windows-10)
    4. Install Ubuntu 16.04 from the Windows Store
        (https://devtidbits.com/2017/11/09/ubuntu-linux-on-windows-10-how-to/)
    5. goes to Ubuntu Bash 
    6. goes now above to the part with instructions for Linux
    *** root path to Ubuntu Directory on Windows: C:\Users\<username>\AppData\Local\Packages\CanonicalGroupLimited.UbuntuonWindows_79rhkp1fndgsc\LocalState\rootfs\home




<br/>

##### On macOS (10.13.6)
    0. open Terminal
    1. Install brew
        $ /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
    2. Install Python
        -> python ( pip (2+3)
            $ brew install python2 python3
            $ sudo python2 -m ensurepip
            $ sudo python3 -m ensurepip

         Ensure to have Python3.6 and not later version:
            $ brew unlink python3
            $ brew install https://raw.githubusercontent.com/Homebrew/homebrew-core/f2a764ef944b1080be64bd88dca9a1d80130c558/Formula/python.rb
            $ brew link python3

            $ pip2 install --upgrade pip setuptools wheel 
            $ pip3 install --upgrade pip setuptools wheel
            $ pip2 install virtualenv
        -> Additional python packages (for Python3)
            (which will not be installed automatically)  
            $ sudo python3 -m pip install somajo someweta


    3. Sqlite + Pysqlcipher + Git LFS
            $ brew install sqlite openssl sqlcipher git-lfs
            $ sudo -H python2 -m pip install pysqlcipher --install-option="--bundled"
            $ git lfs install
            
     4. Last Java Version (for TweetNLP Tokenizer and POS Tagger)
            $ brew cask install java


<br/>



---

<br/>

<a name="settingup"/>
<p style='text-align: right;'>  <sub> <a href="#toc">Back to top</a>
</sub> </p>

## 3. Setting up

<sub>*Set background color of your terminal to dark (ex. black, dark blue etc.)*</sub>


##### Package Installation 

    0. open Terminal
    1. $ cd <path_to_directory_where_to_locate_package>
    2. $ git clone https://github.com/savin-berlin/zas-rep-tools.git
    3. $ git clone https://github.com/savin-berlin/zas-rep-tools-data.git
    4. $ virtualenv env
    5. $ . env/bin/activate
    6. $ sudo python2 -m pip install pysqlcipher 
    7. $ sudo -H python2 -m pip install zas-rep-tools-data/
    8. $ sudo -H python2 -m pip install zas-rep-tools/
    9. $ cd zas-rep-tools/zas_rep_tools/tests
    10. $ nosetests -s -v --rednose
    11. $ sudo zas-rep-tools configer





<br/>



---

<br/>

<a name="definitions"/>
<p style='text-align: right;'>  <sub> <a href="#toc">Back to top</a>
</sub> </p>

## 4. Definitions




   -  **Repetitions** (rep)
    We differentiate between two main types of repetitions:

     * **Replications** (repl)
        -> every Repetition on the letter level up from 3 repetitions (excluded: web links)
        -       ex. 'veeeeeerrrry'
                    (Following letters was replicated: 'e', 'r')
     * **Reduplications** (redu)
        -> every Repetition on the word level
        -       ex. 'very very very'
                    (Following word was reduplicated: 'very' ) 

    And one additional compound repetitions:
    * **Replications in Reduplications**
        -        ex. 'veeeerrrryyy veeery very vvvverryyy'
                    (Here is to see one reduplication of the word 'very' with the length 4 and also 3 uniq and 6 exhausted replications)

   - ****Length**** 
     * **Replications**
        -> The Number of the replicated letters 
        -       ex: 'verrrry'
                    ('r' was replicated and has length of 4)
     * **Reduplications**
        -> The Number of the words in one reduplication
        -       ex: 'very very very much much much much'
                    (There is two reduplications: 'very', 'much'. Reduplication of 'very' has length of 3 and the length of the reduplication for 'much' = 4.)



   - **Uniq vs. Exhausted Re(du)plication**
     <sub>(Every repetitions could be quantified in the uniq or exhausted way)</sub>
     
     * **Replications**
        -> Every reduplicated letter will be counted once as exhausted replication and each word contained one or many replications will be counted once as uniq replication. 
        -        ex: 'vvvvveeery'
                    **Exhausted**
                        = 2, ('v', 'e' was replicated)
                    **Uniq**
                        = 1 (because word 'very' contain any replications, but the word will be counted just once for this category)
                
     * **Reduplications**
        -> Every reduplicated word will be counted once as uniq reduplication and the length of the reduplication will be counted as exhausted reduplication. 
        -       ex: 'very very very or not very very but very'
                    **Uniq**
                        For 'very' = 2 (not 3) 
                    **Exhausted**
                        For 'very' = 5 (not 6)


   - **Syntagma**
        Combination/Group of words according to the rules of syntax for current language (each word could be also combinated with an empty word).
            -   ex: 'very much', 'very'

   - **Scope**
        The length of syntagma
        -       ex: 'very much' = 2; 'very'=1;


   -  **Full Repetitiveness**
    <sub>(Each syntagma with scope > 1 have an additional attribute - full-repetitiveness.)</sub>
    
      **Replications**
        If Every element of an syntagma was replicated, than Full-Repetitiveness for this Syntagma is True.
            -   ex: 'iiii llllovvveee verrry muuuuch', 'veryyyy verrryy muccchhhh', 'verrrrryyy muchhhhhh'
      **Reduplications**
        If every element of an syntagma was reduplicated, than Full-Repetitiveness for this Syntagma is True.
            -   ex: 'very very very much much', "veeeerrryyy veeerryy mmmuuccc muuucch much "


<br/>



---

<br/>
            
<a name="functionality"/>
<p style='text-align: right;'>  <sub> <a href="#toc">Back to top</a>
</sub> </p>

## 5. Functionality
5.1 **CLI-Functions**
Current CommandLineInterface support interaction for following entry points: 

- configer
    <sub>Set/Delete/reset all user information</sub>
- corpora
    <sub>Working with corpus DataBases</sub>
- stats
    <sub>Working with Statistics DataBases</sub>
- streamer
    <sub>Stream Twitter Data</sub>

In the following part you can see a small explanation to each entry point:

-           $ zas-rep-tools configer
     - prjdir
        <sub>Folder where all User Data will be saved for current copy of the Tool.</sub>
        - clean
        - set
        - reset
        - print
     - error_track 
        <sub>current tool support error tracking and report to the developers</sub>
        - set
        - reset
        - respeak
        - print
     - twitter
        <sub>This function set twitter credentials for the streamer</sub>
        - set
        - reset
        - respeak
        - print
     - email 
        <sub>to get error reports from twitter streamer per email, please give your emails</sub>
        - set
        - reset
        - respeak
        - print
     - user_data 
        - clean
        - location
        - print 

<br>

-           $ zas-rep-tools corpora

    - add
        <sub>create and add new corpus into project folder from given text collection</sub>
    - del
        <sub> delete existing corpus via name from project folder</sub>
    - names
        <sub> print all names from existing corpora in the project folder</sub>
    - meta
        <sub> print all meta-data for corpus via corp-name</sub>
    - basic_stats
        <sub> print all general statistics for corpus via corp-name</sub>
    - update_attr
        <sub> change meta-data for corpus via  corp-name</sub>
    - export
        <sub> export corpus into other file type (xml, csv, json) </sub>
    - used_tools
        <sub> print all used NLP methods and tools</sub>
    - clean_dir 
        <sub> delete corrupted corpora from project folder </sub>
    - cols
        <sub> print column names for given table in corpus</sub>
    - doc
        <sub> print all content for given doc via doc_id </sub>
    - ids
        <sub> print ids for all docs in corpus via corp-name</sub>


 <br>

-           $ zas-rep-tools stats

    - compute
        <sub>create and add compute (from given corpus) new stats-db and locate into project folder</sub>
    - del
        <sub> delete existing stats-db via name from project folder</sub>
    - names
        <sub> print all names of existing stats-db in the project folder</sub>
    - meta
        <sub> print all meta-data for stats-db via name</sub>
    - basic_stats
        <sub> print all general statistics for stats-db via name</sub>
    - update_attr
        <sub> change meta-data in stats-db via name</sub>
    - export
        <sub> export statistics as csv, xml, json </sub>
    - clean_dir
        <sub> delete corrupted stats-db from project folder </sub>
    - recompute
        <sub> recompute stats-db with other full-repetativenes marker </sub>
    - optimize
        <sub> spaces and speed optimization via stats-db freezing </sub>
    - recreate_indexes
        <sub> recreate indexes in an stats-db for better performance </sub>



-           $ zas-rep-tools streamTwitter


 
-           $ zas-rep-tools streamerInfo



 
-           $ zas-rep-tools help

<br>


5.2 **Multiprocessing**
    Current Tool support multiprocessing. Just set 'stream_number'-Option to more as 1 to ensure the process to be executed parallel.

<br>

5.3 **NLP-Methods**
Used NLP-Methods:

- Tokenization 
- Sent-Segmentation
- POS-Tagging
- Sentiment Analysis
- Steaming
- RLE (run length encoding)

<br>

5.4 **InternDataBase-Structure** (SQLite)

- **Corpus**
    - Tables: 
        - Documents
        - Info
    - Meta-Data:
     (id,name,platform_name,template_name,version,language,created_at,source,license,visibility,typ,tokenizer,sent_splitter,pos_tagger,sentiment_analyzer,preprocession,del_url,del_punkt,del_num,del_mention,del_hashtag,del_html,case_sensitiv,lang_classification,emojis_normalization,sent_num,token_num,doc_num,text_field_name,id_field_name,locked)



- **Stats**
    - Tables: 
        - Replications
        - Reduplications 
        - Baseline 
        - Info 
    - Meta-Data:
        (id, corpus_id, name, version, created_at, visibility, typ, db_frozen, context_lenght, language, repl_up, ignore_hashtag, ignore_url, ignore_mention, ignore_punkt, ignore_num, force_cleaning, case_sensitiv, full_repetativ_syntagma, min_scope_for_indexes, locked, pos_tagger, sentiment_analyzer, baseline_delimiter)

<br>

5.5 **Additional Features**

 - **Formatters**
    Are there to help for better reading or the unstructured data.
    Existing Formatters: ["twitterstreamapi", "sifter"]

 - **Templates**
    Predefinition of corpus-DB for different exiting projects, which contain information about columns for the documents-table
    Existing Templates: ["twitter","blogger"]



<br/>




---

<br/>

<a name="workflow"/>
<p style='text-align: right;'>  <sub> <a href="#toc">Back to top</a>
</sub> </p>

## 6. WorkFlow

Step 1: Corpus Data Base Creation 

        $ zas-rep-tools corpora add

Step 2: Stats DataBase Computation 

        $ zas-rep-tools stats compute

Step 3: Export of the computed Statistics 

        $ zas-rep-tools stats export


<a name="tutorials"/>
<p style='text-align: right;'>  <sub> <a href="#toc">Back to top</a>
</sub> </p>

## 7. Tutorials

<br/>



---

<br/>

<a name="input/output"/>
<p style='text-align: right;'>  <sub> <a href="#toc">Back to top</a>
</sub> </p>

## 8. Input/Output

<br/>



---

<br/>

<a name="citing"/>
<p style='text-align: right;'>  <sub> <a href="#toc">Back to top</a>
</sub> </p>

## 9. Citing ZAS-REP-TOOLS


### How do I Cite AutoVOT in my articles?

***If possible to cite a program, the following format is recommended (adjusting retrieval dates and versions as necessary):***

* Savin, E., Fuchs, S., Ćwiek, A. (2018). ZAS-VOT-TOOLS: A tool for automatic extraction and quantification of the repetition from the written language. [Computer program]. Version 0.1, retrieved August 2018 from https://github.com/savin-berlin/zas-rep-tools.

<br/>



---

<br/><br/>



<a name="errors"/>
<p style='text-align: right;'>  <sub> <a href="#toc">Back to top</a>
</sub> </p>

## 10. Possible errors and warnings




#### 1. Error: 'Too many open files:'
#####Solutions: 
1. Increase the max number of open files in system:

###### macOS:
    $ sudo launchctl limit maxfiles 3000000 3000000
    $ sysctl -a | grep kern.maxfiles

    (If still not be worked, that test every component separated)


###### Ubuntu:
    $ cat /proc/sys/fs/file-max
    $ ulimit -n 300000
    $ ulimit -n

#### 2. Error: "MemoryError"
It means that your Computer dont have enought of the RAM or the Swap is to short. Please try to increase Swap on your computer. 

###### Ubuntu:
    $ size="8G" && file_swap=/swapfile_$size.img && sudo touch $file_swap && sudo fallocate -l $size /$file_swap && sudo mkswap /$file_swap && sudo swapon -p 20 /$file_swap

    $ sudo swapon --show
    $ free -h

#### 3. Error: In Windows Environment - to long reaction 

    If during the installation process some commands needs more as 5-10 min than try to push "ENTER" Button to ensure the refreshing of the command line 


<br/>



---

<br/>


<a name="acknowledgements"/>
<p style='text-align: right;'>  <sub> <a href="#toc">Back to top</a>
</sub> </p>

## 11. Acknowledgements


#### A big Thank to the following Peoples, who makes this work and current results possible:

- [Susanne Fuchs](mailto:fuchs@leibniz-zas.de) <sup>*(Linguistic & Organization )*</sup>
- [Ulf Leser](mailto:leser@informatik.hu-berlin.de) <sup>*(Computer Science & Organization )*</sup>
- [Aleksandra Ćwiek](mailto:cwiek@leibniz-zas.de) <sup>*(Linguistic)*</sup>
- [Bodo Winter](mailto:bodo@bodowinter.com) <sup>*(Statistical & linguistic Expertise)*</sup>
- [Stephanie Solt](mailto:solt@leibniz-zas.de) <sup>*(Semantics&Pragmatics)*</sup>
- [Dominik Koeppl](mailto:dominik.koeppl@uni-dortmund.de) <sup>*(Combinatorics on Words)*</sup>
- [Tatjana Scheffler](mailto:tatjana.scheffler@uni-potsdam.de) <sup>*(NLP+Twitter expertise)*</sup>
- [Stefan Thater](mailto:stth@coli.uni-saarland.de) <sup>*(NLP expertise)*</sup>
- [Katarzyna Stoltmann](mailto:stoltmann@leibniz-zas.de) <sup>*(Linguistic & NLP)*</sup>
- [Christina Beckmann](mailto:beckmann@leibniz-zas.de) <sup>*(Bibliographical Expertise)*</sup>
- [Tomasz Kociumaka](mailto:kociumaka@mimuw.edu.pl) <sup>*(Combinatorics on Words)*</sup>
- [Frantisek Franek](mailto:franek@mcmaster.ca) <sup>*(Combinatorics on Words)*</sup>


<br/>


<p align="center">
<table style="width:100%">

  <tr>
    <th><img src="http://www.zas.gwz-berlin.de/uploads/pics/dfg_logo_blau_klein_1a3937.jpg"></th>
    <th><img src="http://www.zas.gwz-berlin.de/uploads/pics/xprag_logo_32.jpg"></th> 
    <th><img src="http://www.zas.gwz-berlin.de/typo3temp/pics/6969c56953.png"></th>
  </tr>
  <tr>
  <td colspan = "3">
    <center>
    <img src="http://www.zas.gwz-berlin.de/fileadmin/images/logo2011.png">
    </center>
  </td>
</tr>
    <tr>
   <td colspan = "3">
    <p>
      <center>
        This research was supported  by an DFG and XPRAG.de  grants   <br/>  to the Leibniz-Center General Linguistics.
      </center>
    </p>
  </td>
</tr>
</table>
</p>


