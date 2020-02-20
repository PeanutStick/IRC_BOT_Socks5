#!/usr/bin/python

'''
execute SSH command using tor script
author : 500 squad
peanuts for monkeys
'''

import socket,socks,paramiko,sys,requests
#import first
import urllib.request
import zirc, ssl, random ,asyncio ,os ,time, random
from datetime import datetime
from threading import Thread
print("test1")
        
def ssh_tor(username,passwd,host,port):
    def create_connection(address, timeout=None, source_address=None):
        sock = socks.socksocket()
        sock.connect(address)
        return sock
    print("test1")
    socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, "127.0.0.1", 9150) 
    socket.socket = socks.socksocket 
    socket.create_connection = create_connection 

    ##username = "user"
    ##passwd = "pass"
    ##host = "IP"
    ##port = "1234"
    print("test1")

    print("ok1")
    
    commande = ''
    a = ''
    global external_ip1
    external_ip1 = urllib.request.urlopen('https://ident.me').read().decode('utf8')
    #external_ip2 = urllib.request.urlopen('https://httpbin.org/ip').read().decode('utf8')
    
    print(external_ip1)
    #print(external_ip2)
    try:
     ssh = paramiko.SSHClient()
     ssh.set_missing_host_key_policy(
        paramiko.AutoAddPolicy())
     ssh.connect(host , port, username=username, 
        password=passwd)
     print("[+]Connection to %s established"%host)
     print("[+]ready to execute commands :D")
     
    except:
        print("Connection failed , check your information and tor connection.")
        sys.exit()
    
    while commande != 'exit':
         #display the pwd
         stdin, stdout, stderr = ssh.exec_command ("cd "+ a +';pwd')
         for line in stdout.read().splitlines():
              a = str(line)
         commande = input(a)
         stdin, stdout, stderr = ssh.exec_command ("cd "+ a +";"+ commande +";pwd")
         #stdin, stdout, stderr = ssh.exec_command (commande + ";pwd")
         time.sleep(1)
         i=0
         global linessh
         for linessh in stdout.read().splitlines():
              print (linessh)
         
              #il vas faloir ouvrir un thread ici vers sshrep

              
              

