#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import os
import psycopg2
from datetime import timedelta
import time
import datetime
import json
import sys
import csv








def sel_news():
  
  #dbname=drive_config.read_config('/tmp/configfile')
  now=datetime.datetime.now()
  yes=now + timedelta(days=-1)
  ydate=yes.strftime("%Y-%m-%d")
  dbname='newsdb'
  items=[]
  conn = psycopg2.connect(dbname=dbname, user="postgres", password="postgres")
  cur = conn.cursor()
  encode='utf-8'
  cur.execute("set client_encoding to '%s'" % encode)
  try:
    rows=[]
    #sql = """select "a0" from  nsnote where "患者"=%s order by "ObjectID" desc limit 20"""
    sql ='select cont from  news'
    print (sql)
    cur.execute(sql)

    rows = cur.fetchall()
    
    return rows
    
    
  except (Exception, psycopg2.DatabaseError) as error:
    pass
  finally:
    if conn is not None:
      conn.close()


def ins_news(cont):
  dbname='newsdb'
  now=datetime.datetime.now()
  nextday=now + timedelta(days=1)
  ndate=nextday.strftime("%Y-%m-%d")
  #print (rr)
  #2020-11-26
  table_name='scrapedata'
  
  space=' '
  conn = psycopg2.connect(dbname=dbname, user="postgres", password="postgres")
  cur = conn.cursor()
  for j in range(len(cont)):
    if (j==0):
      vlist="'"+cont[j]+"'"

    else:
      vlist=vlist+','+"'"+cont[j]+"'"

    
  #print (vlist)
  
  try:
    sql = 'INSERT INTO "'+table_name+'"'+ ' (news,sdate,title,cont,url,contid) '+ 'values('+vlist+')'
    print (sql)
    cur.execute(sql)
    conn.commit()
  except (Exception, psycopg2.DatabaseError) as error:
    print (error)
    pass
  finally:
    if conn is not None:
      conn.close()
  return 
  



#check duplicate and use this module fro copy from nsnote to nsnotex2 , nsnotex4

    



    
    


if __name__=='__main__':
  args = sys.argv
  fname=args[1]
  print (fname)
  ff=open(fname,'r',encoding='utf-8')
  news=ff.readline()
  ls=[]
  k=0
  while (news):
      k+=1
      news=news.strip('\n')
      nn=news.split('\t')
      if (k==1):
        news=ff.readline()
        continue
      ls.append(nn)
      news=ff.readline()
  ff.close()
  
  

  for i in range(len(ls)):
        
    cont='' 
    if (len(ls[i])):
      for j in range(len(ls[i])):
        cont=cont+','+ls[i][j]
    print (cont)    
    if (i<100000):
      ins_news(ls[i])
    else:
      break

  
