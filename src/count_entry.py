from pynput import mouse, keyboard
from datetime import datetime, timedelta
import json
import ast


class CountEntry(object):
    def __init__(self, *args, **kwargs):
        self.dirPath = str
        self.mintIncrement = 1
        self.mouse_click_count = 0
        self.key_press_count = 0

        self.today = datetime.today()
        self.addedTime = self.today + timedelta(minutes=self.mintIncrement)


    def _update_count(self):
        self.today = datetime.today()
        presentTime = datetime.strptime(format(self.today), '%Y-%m-%d %H:%M:%S.%f')

        if presentTime > self.addedTime:

            fileRead = open(f"{self.dirPath}/config/idlefile.txt", "r")
            data = fileRead.read()
            data = ast.literal_eval(data)
            clickCount = data['click']
            pressCount = data['press']
            
            fileWrite = open(f"{self.dirPath}/config/idlefile.txt", "w")
            message = {
                "click": clickCount + self.mouse_click_count,
                "press": pressCount + self.key_press_count
            }
            fileWrite.write(str(message))
            fileWrite.close()

            self.mouse_click_count = 0
            self.key_press_count = 0
            self.addedTime = self.today + timedelta(minutes=self.mintIncrement)
        return True

    def _on_press(self, key):
        self.key_press_count += 1
        print('key_press_count', self.key_press_count)
        self._update_count()
        return True
        

    def _on_click(self, x, y, button, pressed):
        self.mouse_click_count += 1
        print('mouse_click_count', self.mouse_click_count)
        self._update_count()
        return True

    def mainListener(self):
        print('call')
        with mouse.Listener(on_click=self._on_click) as listener:
            with keyboard.Listener(on_press=self._on_press) as listener:
                listener.join()


if __name__ == "__main__":
    count = CountEntry()
    count.mainListener()