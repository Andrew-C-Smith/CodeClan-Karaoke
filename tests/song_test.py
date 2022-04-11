import unittest
from src.songs import Song
from src.guests import Guest

class TestSong(unittest.TestCase):

    def setUp(self):
        self.song1 = Song("Wonderwall")
        
        

    def test_song_title(self):
        self.assertEqual("Wonderwall", self.song1.title)

