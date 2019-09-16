from pynput import mouse, keyboard
from datetime import datetime, timedelta


class CountEntry(object):
    def __init__(self, *args, **kwargs):
        self.mouse_click_count = 0
        self.key_press_count = 0

    def _update_count(self):
        f = open(f"./idlefile.txt", "w")
        message = {
            "click": self.mouse_click_count,
            "press": self.key_press_count
        }
        f.write(str(message))
        f.close()
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