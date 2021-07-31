
# 使用threading模块创建线程
# 创建4个线程， 然后分别用for循环执行4次start()和join()方法，每个子线程分别执行输出3次
import threading,time
  
def process():
    for i in range(3):
        time.sleep(1)
        print("thread name is %s" % threading.currentThread().name)


if __name__ == '__main__':
    print("----主线程开始----")
    # 创建4个线程，存入列表
    threads = [threading.Thread(target=process) for i in range(4)]
    for t in threads:
        t.start()       # 开启线程
    for t in threads:
        t.join()        # 等待子线程结束
    print("---主线程结束---")
   
  
  
# 使用thread子类创建线程
# 创建一个继承threading.Thread线程类的子类subthread，并定义一个run()方法。
# 实例化SubThread类创建2个线程，并且调用start(*)方法开启线程，会自动调用run()方法。
import threading
import time


class SubThread(threading.Thread):
    def run(self):
        for i in range(3):
            time.sleep(1)
            msg = "子线程" + self.name + "执行,i=" + str(i)      # name属性中保存的是当前线程的名字
            print(msg)


if __name__ == '__main__':
    print('---主线程开始---')
    t1 = SubThread()        # 创建子线程t1
    t2 = SubThread()        # 创建子线程t2
    t1.start()              # 启动子线程t1
    t2.start()              # 启动子线程t2
    t1.join()               # 等待子线程t1
    t2.join()               # 等待子线程t2
    print('---主线程结束---')

    
    
# 验证线程之间是否可以共享信息。顶一个全局变量g_gum,分别创建2个子线程g_num执行不同的操作，并输出操作后的结果。
# 定义一个全局变量g_num，赋值为100，然后创建2个线程：一个线程将g_num增加50，一个线程将g_num减少50。如果g_num最终结果为100，则说明线程之间可以共享数据。
from threading import Thread
import time


def plus():
    print("---子线程1开始---")
    global g_num
    g_num -= 50
    print('g_num is %d' % g_num)
    print('---子线程1结束---')


def minus():
    time.sleep(1)
    print('---子线程2开始---')
    global g_num
    g_num += 50
    print('g_num is %d' % g_num)
    print('---子线程2结束---')


g_num = 100     # 定义一个全局变量
if __name__ == '__main__':
    print('---主线程开始---')
    print('g_num is %d' % g_num)
    t1 = Thread(target=plus)        # 实例化线程t1
    t2 = Thread(target=minus)       # 实例化线程t2
    t1.start()      # 开启线程t1
    t2.start()      # 开启线程t2
    t1.join()       # 等待t1线程结束
    t2.join()       # 等待t2线程结束
    print('---主线程结束---')
