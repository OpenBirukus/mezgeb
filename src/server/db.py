'''
    TaskJournal 
    
    developed by Birukus.com 

    Author: Biruh Tes birukus@birukus.com
    
    Date: '2015-08-27'

'''
__author__ = 'barukasu'

import os,sys

class db:
    '''
    db class:
    This manages the interface with the file-based db
    '''
    
    def __init__(self,dbpath):
        '''
        Constructor
        @param dbpath: directory path to db 
        '''
        self.dbpath= dbpath 