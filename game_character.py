class Character:
    def __init__(self, char_name):
        self.char_name = char_name
        self.conv = None

    def set_conv(self, conv):
        self.conv = conv

    def talk(self):
        return self.conv


class Enemy(Character):
    def __init__(self, en_name):
        Character.__init__(self, en_name)
        self.en_name = en_name
        self.weak = None

    def set_weak(self,weak):
        self.weak = weak

    def get_weak(self):
        return self.weak