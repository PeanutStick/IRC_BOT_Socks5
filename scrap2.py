#!/usr/bin/python
# -*- coding: utf-8 -*-

import urllib.request
import urllib.parse
import urllib.error
from bs4 import BeautifulSoup
import ssl
import json
#import ast
#import json
import os
from urllib.request import Request, urlopen

# For ignoring SSL certificate errors
print("ok")
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
#url = "https://www.youtube.com/watch?v=2BmGMi0IEx4"
# Input from user
def youtube(url):
#url = input('Enter Youtube Video Url- ')

# Making the website believe that you are accessing it using a mozilla browser
    url = str(url)
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(req).read()

    # Creating a BeautifulSoup object of the html page for easy extraction of data.

    soup = BeautifulSoup(webpage, 'html.parser')
    html = soup.prettify('utf-8')
    video_details = {}
    other_details = {}

    for span in soup.findAll('span',attrs={'class': 'watch-title'}):
        video_details['TITLE'] = span.text.strip()
        

    for script in soup.findAll('script',attrs={'type': 'application/ld+json'}):
            channelDesctiption = json.loads(script.text.strip())
            video_details['CHANNEL_NAME'] = channelDesctiption['itemListElement'][0]['item']['name']

    for div in soup.findAll('div',attrs={'class': 'watch-view-count'}):
        video_details['NUMBER_OF_VIEWS'] = div.text.strip()
        
       

    for span in soup.findAll('span',attrs={'class': 'yt-subscription-button-subscriber-count-branded-horizontal yt-subscriber-count'}):
        video_details['NUMBER_OF_SUBSCRIPTIONS'] = span.text.strip()
    global val
    val = "CHANNEL_NAME : " +video_details['CHANNEL_NAME']+"\n "+video_details['NUMBER_OF_VIEWS'][:-4]+" VIEWS."
##" TITLE : "+video_details['TITLE']+ 
##    print(video_details['TITLE'])
##    print(video_details['CHANNEL_NAME'])
##    print(video_details['NUMBER_OF_VIEWS'])
    return val
#youtube(url)




