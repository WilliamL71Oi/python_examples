
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
   
  
  
  
