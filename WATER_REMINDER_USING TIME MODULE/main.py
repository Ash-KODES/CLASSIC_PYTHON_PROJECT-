import time

from plyer import notification

if __name__ == "__main__": ####this line is written to make sure that this code wont just run if we are importing to in different file/code
    while True:
        notification.notify(
        title = "PLEASE DRINK WATER", 
        message = "YOU HAVE TO SHRED", 
        app_icon = "~/Documents/Ash-KODES/PYTHON/PROJECTS/WATER_REMINDER_USING TIME MODULE/W.ico",
        timeout=10
    )
    time.sleep(60*60)
    
    
   

