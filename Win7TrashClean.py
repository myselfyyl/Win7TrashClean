

import os, exceptions

def removeFile( f ):
    print f
    try:
        if os.path.isdir( f ):
            files = os.listdir( f )
            if 0 < len( files ):
                for t in files:
                    removeFile( f + '\\' + t )
            os.removedirs( f )
        else:
            os.unlink( f )
    except exceptions.StandardError as e:
        print e
        
        
def removeFiles( files ):
    for f in files:
        removeFile( f )
        

if '__main__' == __name__ :
    dirs = ('C:\\windows\\temp', )
    for d in dirs:
        if os.path.exists( d ):
            files = os.listdir( d )
            removeFiles( map( lambda f: d + '\\' + f, files ) )

    raw_input('press any key to continue .')
