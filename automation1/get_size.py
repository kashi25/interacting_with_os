import os
rt= os.path.getsize("guest.txt")
print(rt)
ro = os.path.getmtime("guest.txt")
print(ro) #it is unique time stamp
