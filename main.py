#!/usr/bin/python2

'''
Created on Feb 6, 2012

@author: johannes
'''

import mumbleConnection
import thread
import time

asdf = None

def lol():
    return "lol!"

if __name__ == '__main__':
    #print("lol.")
    asdf = mumbleConnection.mumbleConnection("someserver.name", "password", 1337, "lolbot", "robot_enrichment_center")
    asdf.connectToServer()
    asdf.addChatCallback("wtf", lol)	
    # this infinity loop is there for structural purposes, do not remove it!
    while asdf.running:
        a = 3 
