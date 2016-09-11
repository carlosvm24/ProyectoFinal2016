import threading
from time import sleep


def print_number(number):
    sleep(1)
    print (threading.currentThread())

thread_list = []
i = 0
for i in range(5):
    t = threading.Thread(target=print_number, name='Thread ' + str(i+1), args=(i,))
    thread_list.append(t)

for thread in thread_list:
    thread.start()

for thread in thread_list:
    thread.join()
