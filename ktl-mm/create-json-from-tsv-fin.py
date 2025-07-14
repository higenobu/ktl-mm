#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import os
from datetime import timedelta
import time
import datetime
import argparse
import json
import sys
import csv

#main**************
args = sys.argv
#read res-filename from ww.config(filenm,modelno)
with open(args[1],encoding='utf-8') as h:
    
    reader = csv.reader(h,delimiter='\t')
    lg = [row for row in reader]
newsdic={}



writefile=args[2]
with open(writefile, 'w',encoding='utf-8') as f:
  
    
  k=0  
  for j in range(len(lg)):
    k+=1
    #if (k>400):
    #    break
    cont=lg[j][0]
    
    #label=int(lg[j][1])
    #use integer as label
    ct=cont.strip()
    ct=ct.replace(" ・ "," ")
    ct=ct.replace("＞"," ")
    ct=ct.replace("〜"," ")
    ct=ct.replace(" ━"," ")
    ct=ct.replace("－"," ")
    print (ct)
    newsdic["sentence"]=ct

    #newsdic["label"]=label
    f.write(json.dumps(newsdic,ensure_ascii=False))
     
#/transformers/examples/pytorch/language-modeling
        
#python3 create-json-from-tsv-withouttag.py y-debug.tsv y-debug-mail.json   
#python3 create-json-from-tsv-withouttag-eval.py y-debug.tsv y-debug-eval.json   

     