import multiprocessing
import threading

## 클래스 선언 부분 ##
class MyThread:
    threadName = ''
    def __init__(self,name):
        self.threadName = name

    def plus1000(self):
        count1 = 0
        for i in range(1,1001):
            count1 += i
            print(i ,end = ' ')
        print('=', count1)

    def plus100000(self):
        count2 = 0
        for i in range(1,100001):
            count2 += i
            print(i ,end = ' ')
        print('=', count2)


    def plus10000000(self):
        count3 = 0
        for i in range(1,10000001):
            count3 += i
            print(i,end=' ')
        print(count3)


## 메인함수 부분 ##
thread1 = MyThread('첫번째')
thread2 = MyThread('두번째')
thread3 = MyThread('세번째')

th1 = threading.Thread(target = thread1.plus1000)
th2 = threading.Thread(target = thread2.plus100000)
th3 = threading.Thread(target = thread3.plus10000000)

th1.start()
th2.start()
th3.start()