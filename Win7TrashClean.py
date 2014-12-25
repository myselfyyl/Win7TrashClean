#!/bin/python

import os, exceptions, logging

def removeFile( f ):
    print f
    try:
        if os.path.isdir( f ):
            files = os.listdir( f )
            if 0 < len( files ):
                for t in files:
                    removeFile( f + os.sep + t )
            os.removedirs( f )
        else:
            os.unlink( f )
        logging.info( f )
    except exceptions.StandardError as e:
        pass
        
        
def removeFiles( files ):
    for f in files:
        removeFile( f )
        

if '__main__' == __name__ :
    logname = os.path.join( os.getcwd(), "CleanLog.txt" )

    if os.path.exists( logname ):
        os.unlink( logname )
        
    logging.basicConfig( filename = logname, level = logging.INFO )
    
    dirs = ('C:\\windows\\temp', )
    for d in dirs:
        if os.path.exists( d ):
            files = os.listdir( d )
            removeFiles( map( lambda f: d + os.sep + f , files ) )

    raw_input('press any key to continue .')
