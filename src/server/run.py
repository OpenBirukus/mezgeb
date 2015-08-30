#!/home/codio/.parts/bin/python3.4
'''
    TaskJournal 
    
    developed by Birukus.com 

    Author: Biruh Tes birukus@birukus.com
    
    Date: 08/26/2015

'''
import os
import server
import argparse

def startServer(port, dbpath):
    '''
    starts the server 
    '''
    
    
def stopServer(port, dbpath): 
    '''
    stops the server 
    '''
    
    
    
# starting run method
if __name__=="__main__":

    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print(" _____          _     __                               _ ")
    print("/__   \__ _ ___| | __ \ \  ___  _   _ _ __ _ __   __ _| |")
    print("  / /\/ _` / __| |/ /  \ \/ _ \| | | | '__| '_ \ / _` | |")
    print(" / / | (_| \__ \   </\_/ / (_) | |_| | |  | | | | (_| | |")
    print(" \/   \__,_|___/_|\_\___/ \___/ \__,_|_|  |_| |_|\__,_|_|")
    print("                                                         ")
    print("           by: Birukus (www.birukus.com)                 ")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("--                SERVER: run                          --")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    parser = argparse.ArgumentParser(description='TaskJournal: start server')

    # input database path 
    parser.add_argument('-db','--dbpath', metavar='N', type=str, nargs='+',
                       help='path to task-journal file database',dest='dbpath')
    # input port number
    parser.add_argument('-p','--port', metavar='N', type=int, nargs='+',
                       help='port number for websocket server',dest='port')
    # start 
    parser.add_argument('-s','--start',action="store_true", default=False,
                       help='port number for websocket server',dest='start')
    # stop
    parser.add_argument('-k','--stop',action="store_true", default=False,
                       help='port number for websocket server',dest='stop')
    args = parser.parse_args()
    
    # test the db path and check if the path exists
    if args.dbpath:
        if not os.path.isdir(args.dbpath):
            print(" Error: user specified dbpath does not exist. dbpath="+args.dbpath)

    # TODO
    # start server as a daemon
    # 
    print(args.dbpath)
    print("dbpath %s, port %d, start %d  stop %d"%(args.dbpath[0],args.port[0],args.start,args.stop))
    
    print("-------------------------------")
    print("-- TaskJournal Shuttind Down --")
    print("-------------------------------")