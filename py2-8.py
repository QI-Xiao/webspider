import threading
import time


# def action(arg):
#     time.sleep(1)
#     print('the arg is:%s\r' % arg)
#
#
# for i in range(4):
#     t = threading.Thread(target=action, args=(i,))
#     t.start()
#
# print('main thread end!')


class MyThread(threading.Thread):
    def __init__(self, arg):
        super(MyThread, self).__init__()
        self.arg = arg

    def run(self):
        time.sleep(1)
        print('the arg is:%s\r' % self.arg)


for i in range(4):
    t = MyThread(i)
    t.start()

print('main thread end!')
