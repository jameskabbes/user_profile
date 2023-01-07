import kabbes_client
import kabbes_config
import user_profile
import py_starter as ps

class Client( kabbes_client.Client ):

    _USER_PROFIlE_TRIGGER_BEG = '{-{'
    _USER_PROFIlE_TRIGGER_END = '}-}'

    _CONFIG = {
        "user_to_load": ps.get_env_var('USER') if ps.get_env_var('USER') != None else 'USER',
        "_Dir": user_profile._Dir
    }

    def __init__( self, **kwargs ):

        kabbes_client.Client.__init__( self, **kwargs )
        self.load_user_profile()

    def load_user_profile( self ):

        if not self.cfg['profile.Path'].exists():
            self.create_profile()

        self.profile = kabbes_config.Config()
        self.profile.load_dict( self.cfg['profile.Path'].read_json_to_dict() ) 

    def get_template_Path( self ):

        template_Paths = self.cfg['templates.Dir'].list_contents_Paths(block_dirs=True,block_paths=False)

        # This will be an error, no template options present
        if len(template_Paths) == 0:
            print ('No templates available')
            assert False
        
        else:
            return ps.get_selection_from_list( list(template_Paths) )


    def create_profile( self ) -> None:

        template_Path = self.get_template_Path()

        #copy and paste the template
        print ('Generating your user Profile')
        template_Path.copy( Destination = self.cfg['profile.Path'], print_off = False )

        #read the contents of the newly created module
        template_contents = self.cfg['profile.Path'].read()

        #format the contents of the template 
        formatting_dict = {
            'id': self.cfg['user_to_load']
        }

        #enter values for all other values that couldn't be filled in
        formatting_values = ps.find_string_formatting( template_contents, trigger_beg=Client._USER_PROFIlE_TRIGGER_BEG,trigger_end=Client._USER_PROFIlE_TRIGGER_END )

        for formatting_value in formatting_values:
            stripped_value = ps.strip_trigger( formatting_value, Client._USER_PROFIlE_TRIGGER_BEG, Client._USER_PROFIlE_TRIGGER_END )

            if stripped_value not in formatting_dict:
                user_value = input('Enter a value for ' + str(stripped_value) + ': ')    
                formatting_dict[stripped_value] = user_value
        
        formatted_contents = ps.smart_format( template_contents, formatting_dict, trigger_beg=Client._USER_PROFIlE_TRIGGER_BEG,trigger_end=Client._USER_PROFIlE_TRIGGER_END  )

        #write the formatted info back
        self.cfg['profile.Path'].write( string = formatted_contents )
    
