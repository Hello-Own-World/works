# HelloOwnWorld 13.02.20
# A simple program to change wallpapers during the day (Windows)
import time
import ctypes
SPI_SETDESKWALLPAPER = 20

# List of paths to images  
PATH = ["C:\\Users\\Alex\\Pictures\\Wallpapers\\1.png",
        "C:\\Users\\Alex\\Pictures\\Wallpapers\\2.png",
        "C:\\Users\\Alex\\Pictures\\Wallpapers\\3.png",
        "C:\\Users\\Alex\\Pictures\\Wallpapers\\4.png",
        "C:\\Users\\Alex\\Pictures\\Wallpapers\\5.png",
        "C:\\Users\\Alex\\Pictures\\Wallpapers\\6.png"]

def change_BG (path):
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, path, 3)


while True:
    hour = time.localtime()
    if hour[3] >= 7 and hour[3] < 9 : #Time period for first picture
        change_BG(PATH[0])
        print(hour,"1") #Marker
        time.sleep(((9-hour[3])*60 - hour[4])*60) #Timer to stop cycle ,or cycle will be calling function always
    elif hour[3] >= 9 and hour[3] < 14:
        change_BG(PATH[1])
        print(hour,"2")
        time.sleep(((14-hour[3])*60 - hour[4])*60)
    elif hour[3] >= 14 and hour[3] < 18:
        change_BG(PATH[2])
        print(hour,"3")
        time.sleep(((18-hour[3])*60 - hour[4])*60)
    elif hour[3] >= 18 and hour[3] < 20:
        change_BG(PATH[3])
        print(hour,"4")
        time.sleep(((20-hour[3])*60 - hour[4])*60)
    elif hour[3] >= 20 and hour[3] < 24:
        change_BG(PATH[4])
        print(hour,"5")
        time.sleep(((24-hour[3])*60 - hour[4])*60)
    elif hour[3] >= 0 and hour[3] < 7:
        change_BG(PATH[5])
        print(hour,"6")
        time.sleep(((7-hour[3])*60 - hour[4])*60)
