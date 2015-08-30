#!/usr/bin/python3.4

'''
    TaskJournal 
    
    developed by Birukus.com 

    Author: Biruh Tes birukus@birukus.com
    
    Date: 08/26/2015

'''

import pip

def install(package):
    pip.main(['install', package])

    # starting run method
if __name__ == "__main__":

    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print(" _____          _     __                               _ ")
    print("/__   \__ _ ___| | __ \ \  ___  _   _ _ __ _ __   __ _| |")
    print("  / /\/ _` / __| |/ /  \ \/ _ \| | | | '__| '_ \ / _` | |")
    print(" / / | (_| \__ \   </\_/ / (_) | |_| | |  | | | | (_| | |")
    print(" \/   \__,_|___/_|\_\___/ \___/ \__,_|_|  |_| |_|\__,_|_|")
    print("                                                         ")
    print("           by: Birukus (www.birukus.com)                 ")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("--                SETUP and INSTALL                    --")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    # install packages
    
    # websockets, asyncio    
    install('websockets')
    # plotting library 
    install('mpld3')
    