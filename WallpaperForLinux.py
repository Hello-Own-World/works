import time
import os

PATH = ["/home/alex/Pictures/Wallpapers/1.jpg",
        "/home/alex/Pictures/Wallpapers/2.png",
        "/home/alex/Pictures/Wallpapers/3.jpg",
        "/home/alex/Pictures/Wallpapers/4.png",
        "/home/alex/Pictures/Wallpapers/5.jpg",
        "/home/alex/Pictures/Wallpapers/6.jpg",]

def change_BG_lin (path):
    os.system(f"gsettings set org.gnome.desktop.background picture-uri {path}")

while True:
    hour = time.localtime()
    if hour[3] >= 7 and hour[3] < 9 :
        change_BG_lin(PATH[0])
        print(hour,"1")
        time.sleep(((9-hour[3])*60 - hour[4])*60)
    elif hour[3] >= 9 and hour[3] < 14:
        change_BG_lin(PATH[1])
        print(hour,"2")
        time.sleep(((14-hour[3])*60 - hour[4])*60)
    elif hour[3] >= 14 and hour[3] < 18:
        change_BG_lin(PATH[2])
        print(hour,"3")
        time.sleep(((18-hour[3])*60 - hour[4])*60)
    elif hour[3] >= 18 and hour[3] < 20:
        change_BG_lin(PATH[3])
        print(hour,"4")
        time.sleep(((20-hour[3])*60 - hour[4])*60)
    elif hour[3] >= 20 and hour[3] < 24:
        change_BG_lin(PATH[4])
        print(hour,"5")
        time.sleep(((24-hour[3])*60 - hour[4])*60)
    elif hour[3] >= 0 and hour[3] < 7:
        change_BG_lin(PATH[5])
        print(hour,"6")
        time.sleep(((7-hour[3])*60 - hour[4])*60)