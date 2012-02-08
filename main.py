#!/usr/bin/python2

'''
Created on Feb 6, 2012

@author: johannes
'''

import mumbleConnection
import thread
import time

asdf = None

if __name__ == '__main__':
    #print("lol.")
    asdf = mumbleConnection.mumbleConnection("some.server.name", "serverpasswordleaveitthereevenifyouhavenone", 1337, "lolbot", "robot_enrichment_center")
    asdf.connectToServer()
	
    # this infinity loop is there for structural purposes, do not remove it!
    while True:
        a = 3 
