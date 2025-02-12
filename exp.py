# pyside6-uic mainwindow.ui -o ui_mainwindow.py

import psutil
import ctypes
from ctypes import wintypes
import time
import datetime
import os


def data_time():
    now = datetime.datetime.now()
    start_s = now.strftime("%d.%m.%y %H:%M:%S")
    return start_s


tmp = "temp.txt"

now = datetime.datetime.now()
start = now.strftime("%d.%m.%y %H:%M:%S")

usr = os.getlogin()
print(data_time(), "Старт, пользователь: ",
      usr, ", что-бы завершить нажми CTRL-C")
pid_list = [1]
try:
    while True:

        pid = wintypes.DWORD()
        active = ctypes.windll.user32.GetForegroundWindow()
        active_window = ctypes.windll.user32.GetWindowThreadProcessId(
            active, ctypes.byref(pid))
        pid = pid.value

        for item in psutil.process_iter():
            if pid == item.pid and item.name() not in pid_list:
                del pid_list[0]
                name_aw = item.name()
                pid_list.append(name_aw)
                print(data_time(), name_aw)
                # write_temp(name=name_aw)
                with open(tmp, "a", encoding="utf8") as file:
                    file.write('\n' + "C " + start + ' По ' + data_time() +
                               '\n' + name_aw + '\n')

except KeyboardInterrupt:
    print("Пользователь завершил работу")
