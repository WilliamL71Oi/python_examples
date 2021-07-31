
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
