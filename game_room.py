class Room:

    def __init__(self, name):
        self.name = name
        self.des = None
        self.linked_room = {}

    def set_des(self, des):
        self.des = des

    def get_des(self):
        return self.des

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_char(self, char):
        self.char = char

    def get_char(self):
        return self.char

    def set_char_des(self, char_det):
        self.char_det = char_det

    def get_char_des(self):
        return self.char_det


    def link_room(self, room_to_link, dir):
        self.linked_room[dir] = room_to_link

    def get_det(self):
        for dir in self.linked_room:
            room = self.linked_room[dir]
            print('The', room.get_name(), 'is', dir)

    def move(self, dir):
        if dir in self.linked_room:
            return self.linked_room[dir]
        else:
            print('You can not go that way')
            return self