# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 15:28:57 2019

@author: M MADHURI RAO
"""

import pyodbc
import json
output = []
def create_connection():
    connection = pyodbc.connect('Driver={SQL Server};'
                                'Server=MADHU\SQLEXPRESS;'#Server name 
                                'Database=py_DB;'# Database name
                                'uid=sa;pwd=12345') #Database username and password
    return connection;

connection=create_connection()

cursor=connection.cursor()
query='select name from master.sys.databases' 
q1=cursor.execute(query)
items=[]


for row in q1: 
    for key in cursor.description:
        items.append([value for value in row])
        

def reemovNestings(l): 
    
    for i in l: 
        if type(i) == list: 
            reemovNestings(i) 
        else: 
            output.append(i)

reemovNestings(items)
j=json.dumps({"name":output})
print(j)

