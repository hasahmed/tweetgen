import os

class Util():
    def __init__(self):
        self._twitter_auth_file = os.path.join(os.path.expanduser("~"), ".twitter_auth")

    def key_value_parser(self, file_contents):
        '''
        Returns a dictionary representation of file contents that are in the format `key : value`.
        Is used in API for reading users `.twitter_auth` file
        '''
        if file_contents == '':
            return False # in the case that the file is empty
        file_contents = file_contents.split() # split by new lines into seperate words
        auth_dict = {} # the dictionary that we will store the authentication contents in
        for key, sep, value in self.chunker(file_contents, 3): # loop though every element in the file_contents array
            auth_dict[key] = value
        return auth_dict

    def chunker(self, seq, size):
        return (seq[pos:pos + size] for pos in range(0, len(seq), size))


    '''Verifies that the contents read in from .twitter_auth file are the proper format'''
    def verify_auth_dict(self, auth_dict):
        auth_keys = {
                'consumer_key',
                'consumer_secret',
                'access_token',
                'access_token_secret'
                }
        for key in auth_dict:
            if key not in auth_keys:
                return False
        return True

    def file_read(self, file_path):
        '''
        Returns a string containing the contents of the file at file_path
        '''
        f = open(file_path)
        contents = f.read()
        f.close()
        return contents

    def file_exists(self, file_path):
        return os.path.isfile(file_path)

    def get_twitter_auth(self):
        '''Uses all above functionality to read in the authentication information from .twiiter_auth file'''
        if self.file_exists(self._twitter_auth_file):
            file_contents = self.file_read(self._twitter_auth_file)
            auth_dict = self.key_value_parser(file_contents)
            if auth_dict and self.verify_auth_dict(auth_dict):
                return auth_dict
            return False
        return False
