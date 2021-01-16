import rotatescreen
import time

screen=rotatescreen.get_primary_display()
for i in range(20):
    time.sleep(4)
    screen.rotate_to(i*90%360)

