import os #manipular o sistema operacional 
from functions.wishlist_handler import claim_gift

class TestBase(object):

    def setup(self):
        
        os.environ["dbname"] = 'wishlist'
        os.environ["user"] = 'isabelle'
        os.environ["password"] = 'postgres'
        os.environ["host"] = 'localhost'
        os.environ["port"] = '5432'

    def test_base(self):
        
        event = {'pathParameters':{"id":1}}

        claim_gift(event,None)