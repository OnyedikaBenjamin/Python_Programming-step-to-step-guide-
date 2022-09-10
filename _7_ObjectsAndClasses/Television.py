class Television:

    def __init__(self):  # Define initializer
        self.channel = 1  # Create Instance Variables
        self.volume_level = 1
        self.on = False

    def isOn(self):
        self.on = True

    def isOff(self):
        self.on = False

    def getChannel(self):
        if self.on:
            return self.channel

    def setChannel(self, new_channel):
        if self.on:
            self.channel = new_channel

    def get_volume(self):
        if self.on:
            return self.volume_level

    def set_volume(self, new_volume):
        if self.on:
            self.volume_level = new_volume

    def channel_up(self):
        if self.on and self.getChannel() < 120:
            self.channel += 1

    def channel_down(self):
        if self.on and self.getChannel() > 1:
            self.channel -= 1

    def volume_up(self):
        if self.on and self.get_volume() < 7:
            self.volume_level += 1

    def volume_down(self):
        if self.on and self.get_volume() > 1:
            self.volume_level -= 1
