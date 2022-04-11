import unittest
from src.rooms import Rooms
from src.songs import Song
from src.guests import Guest

class TestRooms(unittest.TestCase):
    def setUp(self):
        self.song = Song("Wonderwall")
        self.song1 = Song("Hey Jude")
        self.guest = Guest("Sophie", "Your Song", 200)

        self.room= Rooms("Main Hall", 200)

    def test_song_list_has_none(self):
        self.assertEqual(0, len(self.room.songs))


    def test_song_list_has_two(self):
        self.room.add_song(self.song)
        self.room.add_song(self.song1)
        self.assertEqual(2, len(self.room.songs))


    def test_new_song_exists(self):
        self.room.add_song(self.song)
        self.assertEqual(1, len(self.room.songs))


    def test_guest_list_has_one(self):
        self.room.add_guest(self.guest)
        self.assertEqual(1, len(self.room.guests))

    def test_guest_is_removed(self):
        self.room.add_guest(self.guest)
        self.room.remove_guest(self.guest)
        self.assertEqual(0, len(self.room.guests))

    def test_guest_list_over_capacity(self):
        for banana in range (0,201):
            self.room.add_guest(self.guest)
        # self.room.add_guest(self.guest)
        self.assertEqual(200, len(self.room.guests))
        self.assertEqual(1, len(self.room.queue))