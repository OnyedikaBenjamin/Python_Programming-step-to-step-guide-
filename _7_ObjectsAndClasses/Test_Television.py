from Television import Television

my_tv = Television()     # Tv object


# When the tv is on,
my_tv.isOn()
my_tv.volume_up()
my_tv.channel_up()
print("The current volume of My Tv is", my_tv.get_volume())
print("The current channel of My Tv is", my_tv.getChannel())
print()
my_tv.isOn()
my_tv.set_volume(6)
my_tv.setChannel(80)
print("The current volume of My Tv is", my_tv.get_volume())
print("The current channel of My Tv is", my_tv.getChannel())
print()
# When the Tv is off nothing can be done.
my_tv.isOff()
my_tv.set_volume(6)
my_tv.setChannel(80)
print("The current volume of My Tv is", my_tv.get_volume())
print("The current channel of My Tv is", my_tv.getChannel())
