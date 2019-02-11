def encode(inp_str):
    counter = 1
    previos = ''
    outp_lst = []
    for char in inp_str:
        if char != previos:
            if previos:
                cur_entry = (previos,counter)
                outp_lst.append(cur_entry)
                #print outp_lst
            counter = 1
            previos = char
        else:
            counter += 1
    else:
        try:
            cur_entry = (char,counter)
            outp_lst.append(cur_entry)
            return (outp_lst, 1)
        except Exception as e:
            print("Exception encountered {e}".format(e=e)) 
            return (e, -1)
 
def decode(outp_lst):
    q = ""
    for char, counter in outp_lst:
        q += char * counter
    return q
 
#Method call
#val = encode("llllliiiiiife issssssss nnniiiicccceee")
#if val[1] == 1:
#    print(val[0])
#    print(decode(val[0]))
## [('l', 5), ('i', 6), ('f', 1), ('e', 1), (' ', 1), ('i', 1), ('s', 8), (' ', 1), ('n', 3), ('i', 4), ('c', 4), ('e', 3)]