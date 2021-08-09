
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
    
    
    
# 使用多线程的互斥锁模拟多人购票功能
# 这里使用多线程和互斥锁模拟实现多人同时订购电影票的功能，假设电影院某个场次只有100张电影票，10个用户同事抢购该电影票，每出售一张，显示一次剩余的电影票张数。
# 创建了10个线程，全部执行task()函数，为解决资源竞争问题，使用mutex.acquire()函数实现资源锁定，第一个获取资源的线程锁定后，其他线程等待mutex.release()解锁。所以每次只有一个线程执行task()函数。
# 使用互斥锁时，要避免死锁。在多任务系统下，当一个或多个线程等待系统资源，而资源又被线程本身或其他线程占用时，就形成了死锁。
from threading import Thread, Lock
import time

n = 100     # 共100张票


def task():
    global n
    mutex.acquire()     # 上锁
    temp = n        # 赋值给临时变量
    time.sleep(0.1)     # 休眠0.1秒
    n = temp - 1        # 数量减少1
    print("购买成功，剩余%d张电影票" % n)
    mutex.release()     # 释放锁


if __name__ == '__main__':
    mutex = Lock()      # 实例化Lock类
    t_l = []        # 初始化一个列表
    for i in range(10):
        t = Thread(target=task)     # 实例化线程类
        t_l.append(t)       # 将线程实例存入列表中
        t.start()       # 创建线程
    for t in t_l:
        t.join()        # 等待子线程结束

        
        
    
    # 使用Queue队列实现在线程间通信
    # 顶一个生产者类Producer，定义一个消费者类Consumer。生产者生成5件产品，依次写入队列，而消费者依次从队列中取出产品。
#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from queue import Queue
import random, threading, time


# 生产者类
class Producer(threading.Thread):
    def __init__(self, name, queue):
        threading.Thread.__init__(self, name=name)
        self.data = queue

    def run(self):
        for i in range(5):
            print("生产者%s将产品%d加入队列！" % (self.getName(), i))
            self.data.put(i)
            time.sleep(random.random())
        print("生产者%s完成！" % self.getName())


# 消费者类
class Consumer(threading.Thread):
    def __init__(self, name, queue):
        threading.Thread.__init__(self, name=name)
        self.data = queue

    def run(self):
        for i in range(5):
            val = self.data.get()
            print("消费者%s将产品%d从队列中取出！" % (self.getName(), val))
            time.sleep(random.random())
            print("消费者%s完成！" % self.getName())


if __name__ == '__main__':
    print('---主线程开始---')
    queue = Queue()         # 实例化队列
    producer = Producer('Producer', queue)          # 实例化线程Producer，并传入队列作为参数
    consumer = Consumer('Consumer', queue)          # 实例化线程Consumer，并传入队列作为参数
    producer.start()            # 启动线程Producer
    consumer.start()            # 启动线程Consumer
    producer.join()             # 等待线程Producer结束
    consumer.join()             # 等待线程Consumer结束
    print('---主线程结束---')

    
    
# Process类的方法和属性的使用
# Process类的方法和属性的使用，创建2个子进程，分别使用os模块和time模块输出父进程和子进程的ID以及子进程的时间，并调用Process类的name和pid属性。
# 第一次实例化Process类时，会为name属性默认赋值为“Process-1”，第二次则默认为“process-2”，但是由于在实例化进程p2时，设置了name属性为“mrsoft”，所以p2.name的值为“mrsoft”而不是“Process-2”。

# -*- coding:utf-8 -*-

from multiprocessing import Process
import time
import os


# 两个子进程将会调用的两个方法

def child_1(interval):
    print('子进程(%s)开始执行，父进程为(%s)' % (os.getpid(), os.getpid()))
    t_start = time.time()           # 计时开始
    time.sleep(interval)            # 程序将会被挂起interval秒
    t_end = time.time()             # 计时结束
    print("子进程(%s)执行时间为'%0.2f'秒" % (os.getpid(), t_end - t_start))


def child_2(interval):
    print("子进程(%s)开始执行，父进程为(%s)" % (os.getpid(), os.getpid()))
    t_start = time.time()               # 计时开始
    time.sleep(interval)                # 程序将会被挂起interval秒
    t_end = time.time()                 # 计时结束
    print("子进程(%s)执行时间为'%0.2f'秒" % (os.getpid(), t_end - t_start))


if __name__ == '__main__':
    print("---父进程开始执行---")
    print("父进程PID：%s" % os.getpid())                # 输出当前程序的PID
    p1 = Process(target=child_1, args=(1,))             # 实例化进程p1
    p2 = Process(target=child_2, name="mrsoft", args=(2,))              # 实例化进程p2
    p1.start()              # 启动进程p1
    p2.start()              # 启动进程p2
    # 同事父进程仍然往下执行，如果p2进程还在执行，将会返回True
    print("p1.is_alive=%s" % p1.is_alive())
    print("p2.is_alive=%s" % p2.is_alive())
    # 输出p1和p2进程的别名和PID
    print("p1.name=%s" % p1.name)
    print("p1.pid=%s" % p1.pid)
    print("p2.name=%s" % p2.name)
    print("p2.pid=%s" % p2.pid)
    print("---等待子进程---")
    p1.join()               # 等待p1进程结束
    p2.join()               # 等待p2进程结束
    print("---父进程执行结束---")

    
    
    
# 使用Process子类创建进程
# 对于一些简单的小任务，通常使用Process(target=test)方式实现多进程。但是如果要处理复杂任务的进程，通常定义一个类，使其继承Process类，每次实例化一个类的时候，就等同于实例化一个进程对象。
# 使用Process子类创建多个进程
# 使用Process子类方式创建2个进程，分别输出父、子进程的PID，以及每个子进程的状态和运行时间。
# 定义了一个SubProcess子类，继承multiprocess.Process子类。SubProcess子类中定义了2个方法：__init__()初始化方法和run()方法。在__init__()初始化方法中，调用multiprocess.Process父类的__init__()
# 初始化方法，否则父类初始化方法会被覆盖，无法开启进程。此外，在SubProcess子类中并没有定义start()方法，但在主进程中却调用了start()方法，此时就会自动执行SubProcess类的run()方法。
  
# -*- coding:utf-8 -*-

from multiprocessing import Process
import time
import os


# 继承Process类
class SubProcess(Process):
    # 由于Process类本身也有__init__初始化方法，这个子类相当于重写了父类的方法
    def __init__(self, interval, name=""):
        Process.__init__(self)  # 调用Process父类的初始化方法
        self.interval = interval  # 接收参数interval
        if name:
            self.name = name  # 如果传递参数name，则为子进程创建name属性，否则使用默认属性

    # 重写Process类的run()方法
    def run(self):
        print("子进程(%s开始执行，父进程为(%s)" % (os.getpid(), os.getpid()))
        t_start = time.time()
        time.sleep(self.interval)
        t_stop = time.time()
        print("子进程(%s)执行结束，耗时%0.2f秒" % (os.getpid(), t_stop - t_start))


if __name__ == '__main__':
    print("---父进程开始执行---")
    print("父进程PID：%s" % os.getpid())
    p1 = SubProcess(interval=1, name='mrsoft')
    p2 = SubProcess(interval=2)
    # 对一个不包含target属性的Process类执行start()方法，就会运行这个类中的run()方法
    # 所以这里会执行p1.run()
    p1.start()
    p2.start()
    # 输出p1和p2进程的执行状态，如果真正进行，返回True，否则返回False
    print("p1.is_alive=%s"%p1.is_alive())
    print("p2.is_alive=%s"%p2.is_alive())
    # 输出p1和p2进程的别名和PID
    print("p1.name=%s"%p1.name)
    print("p1.pid=%s"%p1.pid)
    print("p2.name=%s"%p2.name)
    print("p2.pid=%s"%p2.pid)
    print("---等待子进程---")
    p2.join()  # 等待p1进程结束
    p2.join()  # 等待p2进程结束
    print("---父进程执行结束---")

    
    
    
# 使用processing.Queue实现多进程队列。    
#! /usr/bin/python3
# -*- coding: UTF-8 -*-

from multiprocessing import Queue

if __name__ == '__main__':
    q = Queue(3)  # 初始化一个Queue对象，最多可接收3条put消息
    q.put("消息1")
    q.put("消息2")
    print(q.full())  # 返回false
    q.put("消息3")
    print(q.full())  # 返回True

    # 因为消息队列已满，下面的try会抛出异常
    # 第一个try会等待2秒后再抛出异常，第二个try会立即抛出异常
    try:
        q.put("消息4", True, 2)
    except:
        print("消息队列已满，现有消息数量:%s" % q.qsize())

    try:
        q.put_nowait("消息4")
    except:
        print("消息队列已满，现有消息数量:%s" % q.qsize())

    # 读取消息时，先判断消息队列是否为空，为空时再读取
    if not q.empty():
        print("---从队列中获取消息---")
        for i in range(q.qsize()):
            print(q.get_nowait())
    # 先判断消息队列是否已满，不为满时再写入
    if not q.full():
        q.put_nowait("消息4")
        
    

# 创建2个子进程，一个子进程负责向队列中写入数据，另一个子进程负责从队列中读取数据。为保证能够正确从队列中读取数据，设置读取数据的进程等待时间为2秒。如果2秒后仍然无法读取数据，则抛出异常。    
#! /usr/bin/python3
# -*- coding: UTF-8 -*-

from multiprocessing import Process, Queue
import time


# 向队列中写入数据
def write_task(q):
    if not q.full():
        for i in range(5):
            message = "消息" + str(i)
            q.put(message)
            print("写入:%s" % message)


# 从队列读取数据
def read_task(q):
    time.sleep(1)       # 休眠1秒
    while not q.empty():        # 等待2秒，如果还没读取到任何消息
        print("读取:%s" % q.get(True, 2))     # 则抛出"Queue.Empty"异常


if __name__ == '__main__':
    print("---父进程开始---")
    q = Queue()     # 父进程创建Queue，并传给各个子进程
    pw = Process(target=write_task, args=(q,))      # 实例化写入队列的子进程，并且传递队列
    pr = Process(target=read_task, args=(q,))       # 实例化读取队列的子进程，并且传递队列
    pw.start()      # 启动子进程pw，写入
    pr.start()      # 启动子进程pr，读取
    pw.join()       # 等待pw结束
    pr.join()       # 等待pr结束
    print("---父进程结束---")
   
