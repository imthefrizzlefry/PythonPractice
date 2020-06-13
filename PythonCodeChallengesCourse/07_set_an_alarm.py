import sched
import time
import winsound as ws

def set_alarm(time_span, sound_file, message):
    s = sched.scheduler(time.time, time.sleep)
    s.enterabs(time_span, 1, print, argument=(message,))
    s.enterabs(time_span, 1, ws.PlaySound, argument=(sound_file, ws.SND_FILENAME))
    print("Alarm set for", time.asctime(time.localtime(time_span)))
    s.run()


if __name__ == "__main__":
    my_span = time.time() + 1
    my_sound = 'alarm.wav'
    my_message = "Wake Up!"

    set_alarm(my_span, my_sound, my_message)