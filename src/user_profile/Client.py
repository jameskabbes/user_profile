from parent_class import ParentClass
import kabbes_client
import user_profile
import py_starter as ps

class Client( user_profile.Profile ):

    BASE_CLIENT_DICT = {
        "user_to_load": ps.get_env_var('USER') if ps.get_env_var('USER') != None else 'USER',
        "_Dir": user_profile._Dir
    }

    _USER_PROFIlE_TRIGGER_BEG = '{-{'
    _USER_PROFIlE_TRIGGER_END = '}-}'

    def __init__( self, dict={}, **kwargs ):

        dict = ps.merge_dicts( self.BASE_CLIENT_DICT, dict )
        self.client = kabbes_client.Client( dict=dict, **kwargs )

        user_profile.Profile.__init__( self )

