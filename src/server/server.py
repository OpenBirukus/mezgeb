'''
    TaskJournal 
    
    developed by Birukus.com 

    Author: Biruh Tes birukus@birukus.com
    
    Date: 08/26/2015

'''

__author__ = 'barukasu'

import asyncio
import websockets

import db

class server:
    '''
    Server class:
    This class manages the websocket server
    '''
    
    # member variables
    port = 8888
    dbpath = './test/db'
    
    def __init__(self, dbpath='./test/db', port=8888):
        '''
        Main constructor
        '''
        # copy user input
        self.port = port
        self.dbpath = dbpath
        
    def connect(self):
        '''
        
        '''