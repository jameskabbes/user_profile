### Test

from . import profile_import

import dir_ops as do
import os

_Dir = do.Dir( os.path.abspath( __file__ ) ).ascend()   #Dir that contains the package 
_src_Dir = _Dir.ascend()                                  #src Dir that is one above
_repo_Dir = _src_Dir.ascend()                    
_cwd_Dir = do.Dir( do.get_cwd() )

templates_Dir = do.Dir( _Dir.join( 'Templates' ) )
users_Dir = do.Dir( _Dir.join( 'Users' ) )

###
#  
###
profile = profile_import.init()
