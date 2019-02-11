               if self._preprocession:
                    text_preprocessed = False
                    try:
                        preproc = self._preprocessing(row_as_dict[self._text_field_name],thread_name=thread_name, log_ignored=log_ignored, row=row_as_dict)
                        if preproc:
                            try:
                                if preproc[0] == "terminated":
                                    self.logger.critical("{} got an  Termination Command!! and was terminated. Reason: '{}'. ".format(thread_name,preproc[0]))
                                    self.threads_status_bucket.put({"name":thread_name, "status":"terminated", "desc":preproc[0]})
                                    self._terminated = True
                                    return False
                                else:
                                    text_preprocessed = json.dumps(preproc)
                            except:
                                    text_preprocessed = json.dumps(preproc)
                        else:
                            text_preprocessed = preproc
                        #p(text_preprocessed, "text_preprocessed")
                    except KeyError, e: 
                        print_exc_plus() if self._ext_tb else ""
                        msg = "PreprocessingError: (KeyError) See Exception: '{}'. Probably text_field wasn't matched. Possible Explanations:  1. The wrong text_field name was given or 2. matched file has not right structure (every text file should have min an text_element and an id_element)  or 3. ImplemenationError, where row  was given as list and not as dict.  Possible Solution: 1. Check if given file has an id and text element, if not, than you can sort this file out, to be sure, that every thing going right. And than create CorpusDB one more time. ".format(e)
                        #self.logger.error(msg, exc_info=self._logger_traceback)
                        self.threads_status_bucket.put({"name":thread_name, "status":"failed"})
                        if log_ignored:
                            self.logger.error_insertion(msg, exc_info=self._logger_traceback)
                    
                        #return False
                    except Exception, e:
                        self.logger.error("PreprocessingError:  See Exception: '{}'. ".format(e),  exc_info=self._logger_traceback)
                        self.threads_status_bucket.put({"name":thread_name, "status":"failed"})
                        return False


                    if text_preprocessed:
                        row_as_dict[self._text_field_name] = text_preprocessed
                    else:
                        #self._check_termination(thread_name=thread_name) 
                        #self.logger.warning("Text in the current DictRow (id='{}') wasn't preprocessed. This Row was ignored.".format(row_as_dict["id"]))
                        self.outsorted_insertion_status_general[thread_name] +=1
                        continue
                #else: