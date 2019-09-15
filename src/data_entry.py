from pynput import mouse, keyboard
from datetime import datetime, timedelta
# import os.path, time
# print("last modified: %s" % time.ctime(os.path.getmtime("demofile2.txt")))
# print("created: %s" % time.ctime(os.path.getctime("demofile2.txt")))



def _update_time(message):
    interval = 10
    today = datetime.today()
    time = datetime.strptime(format(today), '%Y-%m-%d %H:%M:%S.%f')
    minute = time.minute
    

    if minute > interval:
        a = 60 / interval
        for i in range(int(a)):
            multiplyValue = interval * (i + 1)

            if multiplyValue > minute:
                deltaValue = multiplyValue - minute
                break
            else:
                deltaValue = multiplyValue - minute
                continue
    else:
        deltaValue = interval - minute

    date = today + timedelta(minutes=deltaValue)

    year = str(date.year)
    month = str(date.month)
    day = str(date.day)
    hour = str(date.hour)
    minuteNumber = str(date.minute)
    date_time = year + "-" + month + "-" + day + "-" + hour + "-" + minuteNumber

    f = open(f"./datafile-{date_time}.txt", "a")
    f.write(str(message))
    f.close()
    return True


def _on_press(key):
    _update_time("keypress\n")
    return True
    

# Collect events until released
key_listener = keyboard.Listener(on_press = _on_press)
key_listener.start()




def _on_click(x, y, button, pressed):
    _update_time(f"{button}\n")
    return True

with mouse.Listener(
    on_click = _on_click,
) as listener:
    listener.join()


# ...or, in a non-blocking fashion:
def mainListener():
    print('start activity monitor and entry')
    listener = mouse.Listener(on_click = _on_click)
    listener.start()


mainListener()