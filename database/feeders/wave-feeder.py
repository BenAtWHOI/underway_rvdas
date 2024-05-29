#!/usr/bin/env python
# efc 2023 store UDP message in sqlite database

import socket
import json
import sqlite3
import time

while True: 
    # UDP message from wave server
    port = 55710
    sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    sock.bind(("",port))
    
    # Receive and store udp msg
    data, addr = sock.recvfrom(1024)
    msg = data.decode()
    string = msg.split()
    #print (string)
 
    # Define variables 
    timestamp = int(time.time())
    
    id1 = "WaveHeight"  
    value1 = string[7][:-1]
    unit1 = " m"
    
    id2 = "WaveDirection" 
    value2 = int(float(string[6][:-1]))
    unit2 = "°"
    
    id3 = "WavePeriod" 
    value3 = string[5][:-1]
    unit3 = " s"
    
    id4 = "CurrentSpeed" 
    value4 = string[8][:-1]
    unit4 = " m/s"
    
    id5 = "CurrentDirection"     
    value5 = int(float(string[9][:-1]))
    unit5 = "°"

    # Connect to sqlite db
    dbfile = "armstrong.db"
    conn = sqlite3.connect(dbfile)
    cursor = conn.cursor()
    table = cursor.execute("""SELECT name FROM sqlite_master WHERE type='table' AND name='array'; """).fetchall()
 
    if table == []: # Check if table exists
        print ("Table does not exist")
        
    else: # Write to the sqlite database
        
        cursor.execute("REPLACE INTO array (id, timestamp, value, unit) VALUES (?, ?, ?, ?)", (id1, timestamp, value1, unit1))
        
        cursor.execute("REPLACE INTO array (id, timestamp, value, unit) VALUES (?, ?, ?, ?)", (id2, timestamp, value2, unit2))
                  
        cursor.execute("REPLACE INTO array (id, timestamp, value, unit) VALUES (?, ?, ?, ?)", (id3, timestamp, value3, unit3))

        cursor.execute("REPLACE INTO array (id, timestamp, value, unit) VALUES (?, ?, ?, ?)", (id4, timestamp, value4, unit4))
        
        cursor.execute("REPLACE INTO array (id, timestamp, value, unit) VALUES (?, ?, ?, ?)", (id5, timestamp, value5, unit5))
        
        conn.commit()
        conn.close()
