import unittest
# from src.songs import Song
from src.guests import Guest

class TestGuests(unittest.TestCase):
    def setUp(self):
        self.guest = Guest("Ben", "Wonderwall", 20  )
        # self.person2 = Guest("Joe", "Song 2", 30)
        # self.person3 = Guest("Sarah", "Hello", 5)


    def test_guest_can_pay_entry(self):
        self.guest.reduce_cash(5)
        self.assertEqual(15, self.guest.cash)

  

