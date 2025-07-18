#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import csv
import pprint

import mojimoji

from textformatting import ssplit
from pyknp import Juman

args = sys.argv
#print('args1:[{}]'.format(args[1]))
jumanpp = Juman("jumanpp",multithreading=True)

with open(args[1]) as f:
    reader = csv.reader(f, delimiter='\t')
    ls = [row for row in reader]

#    r = ls[4]
#    print(r)
#    sentences = ssplit(ls[4][0])
#    print('step1 : {}'.format(sentences))
#    for i in range(len(l)):        
#        print('step1-{} : {}'.format(i,l[i][0]))
#        sentences = ssplit(l[i][0])

    result_ls = []
    j=0
    for l in ls:
        #print('step1:[{}]'.format(l[0]))
        j+=1
        if (j==26064 or j==32824 or j==41195):
            continue
        print (j)
        sentences = ssplit(l[0])
        #print (sentences[0])
        result_strs = ''
        for sentence in sentences:
            #print (sentence)
            result = jumanpp.analysis(sentence)
#            print('step2 : {}'.format(result))

            result_str = ''
            for mrph in result.mrph_list():
#                print('[{}]'.format(mrph.midasi))
#                print(mrph.${attribute})
                if result_str == '':
#                    result_str = '{}'.format(mrph.midasi)
                    result_str = '{}'.format(mojimoji.han_to_zen(mrph.midasi))
#                    print('s1[{}]'.format(result_str))
                else:
                    midasi_alt = mojimoji.han_to_zen(mrph.midasi)
                    if midasi_alt != "　":
#                        print('s3[{}]'.format(midasi_alt))
#                        result_str = '{} {}'.format(result_str,mrph.midasi)
                        result_str = '{} {}'.format(result_str,midasi_alt)
#                        print('s4[{}]'.format(result_str))

#            print('step2:[{}]'.format(result_str))
            if result_strs == '':
                result_strs = '{}'.format(result_str)
            else:
                result_strs = '{} {}'.format(result_strs,result_str)

        result_ls.append(result_strs)
    
#    print(result_ls)
    #print(result_ls[0])

    result_rows = []

    for i in range(len(result_ls)):
#        print('[{}][{}]'.format(result_ls[i],ls[i][1]))
        result_rows.append([ result_ls[i], ls[i][1] ])
    
#    print(result_rows)
#    print(result_rows[0])

with open(args[2], 'w') as f:
    writer = csv.writer(f, delimiter='\t')
    writer.writerows(result_rows)
