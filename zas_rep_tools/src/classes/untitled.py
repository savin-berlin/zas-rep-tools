last working version

    def _exctract_full_syntagmas(self,reconstr_tree, scope, redu_free_elem_length,syntagma_type="lexem"):
        #exactly_equal
        #try:
        output_ix = []
        output_words = ()
        output_doc_id = ()
        allowed_ids = ()
        start_new = False
        add = False
        #orig_first_word = inp_syntagma_splitted[0]
        #p((scope,{  d:{s:{t:ids for t, ids in s_data.iteritems()} for s, s_data in doc_data.iteritems()} for d, doc_data in reconstr_tree.iteritems()}),"reconstr_tree")
        i = 0
        for doc_id, doc_data in dict(sorted(reconstr_tree.items())).iteritems():
            
            redu_free_length = [l-1 for l in redu_free_elem_length[doc_id]] # convert length to index
            current_syn_ixs = ()
            current_syn_words = ()

            start_tok = None
            temp_tok = None
            last_token = None
            last_sent = None
            ix_ongoing = -1
            is_first = True
            temp_ids = ()
            for current_sent, sents_data in dict(sorted(doc_data.items())).iteritems():
                for current_tok in sorted(sents_data.keys()):
                    i+= 1
                  #  p((doc_id,current_sent,current_tok,start_tok, current_syn_ixs,current_syn_words))
                    if temp_tok:
                        tok_to_use = temp_tok
                    else:
                        tok_to_use = start_tok

                    if is_first:
                        is_first = False
                        # print "!!! 1111"
                        ### Initialisation
                        last_token = current_tok
                        start_tok = (current_sent,current_tok)
                        counter_full_syn = 1
                        current_syn_ixs += (start_tok,)
                        curr_rep = sents_data[current_tok]
                        current_syn_words += (curr_rep[0],)
                        temp_ids += tuple(curr_rep[1])
                    else:
                        if (tok_to_use[1]+counter_full_syn) == current_tok:
                            counter_full_syn += 1
                            add = True
                        else:
                            # print current_tok, (current_sent,last_sent), (last_token,redu_free_length[last_sent])
                            if current_tok==0 and ((current_sent-last_sent) == 1) and (last_token==redu_free_length[last_sent]): # if  the first token of the next sent build full_syntagma with the last token of the last sent
                                temp_tok = (current_sent, current_tok)
                                counter_full_syn = 1
                                add = True
                            else:
                                start_new = True

                        #i = 0
                        while True:
                            #i+=1
                            #if i >3: status = False
                            if start_new:
                                # p("STARTED",c="m")
                                start_new = False
                                add = True
                                # p(len(current_syn_ixs),"len(current_syn_ixs)")
                                if len(current_syn_ixs) == scope:
                                    # p("SAVED",c="m")
                                    output_ix.append(current_syn_ixs)
                                    output_words += ((current_syn_words),)
                                    output_doc_id += (doc_id,)
                                    allowed_ids += (temp_ids,)
                                
                                #if orig_first_word == sents_data[current_tok][0]:
                                # Clean old vars
                                temp_ids = ()
                                current_syn_ixs=()
                                current_syn_words = ()

                                #p(start_tok,"11start_tok")
                                temp_tok = None
                                start_tok = (current_sent,current_tok)
                                counter_full_syn = 1


                            if add:
                                add = False
                                # Create current vars
                                #counter_full_syn += 1
                                if current_syn_words:
                                    # p((i,current_syn_words[0], curr_rep[0],current_syn_words,current_syn_ixs,current_tok,sents_data[current_tok]),c="r")
                                    if current_syn_words[0] == sents_data[current_tok][0]:
                                        # p("START NEW",c="m")
                                        start_new = True
                                        continue

                                current_syn_ixs += ((current_sent,current_tok),)
                                curr_rep = sents_data[current_tok]
                                current_syn_words += (curr_rep[0],)
                                temp_ids += tuple(curr_rep[1])
                                break


                    last_token = current_tok
                last_sent = current_sent

            if len(current_syn_ixs) == scope:
                output_ix.append(current_syn_ixs)
                output_words += ((current_syn_words),)
                output_doc_id += (doc_id,)
                allowed_ids += (temp_ids,)


        if output_ix:
            self._process_extracted_full_syn(output_ix,output_words,output_doc_id, scope,syntagma_type)

        output_allowed_ids = ()
        for ids in  allowed_ids:
                output_allowed_ids += ids

        return output_ix, set(output_allowed_ids)
        # except Exception as e:
        #     self.logger.error("Throw Exception: '{}'".format(repr(e)))
        #     return False,False



