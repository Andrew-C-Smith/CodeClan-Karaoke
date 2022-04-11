class Rooms:
    def __init__(self, room_name, capacity):
        self.room_name = room_name
        self.capacity = capacity
        self.guests = []
        self.songs =[]
        self.queue = []

    def add_song(self, song):
        self.songs.append(song)
        

  

    def add_guest(self, guest):
        if len(self.guests) < self.capacity:
            self.guests.append(guest)
        else:
            self.queue.append(guest)
    
            
    def remove_guest(self, guest):
        self.guests.remove(guest)

