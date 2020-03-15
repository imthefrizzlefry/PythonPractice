from time import sleep
from datetime import datetime

'''This problem was asked by Apple.

Implement a job scheduler which takes in a function f and an integer n, and calls f after n milliseconds.
'''

def job_scheduler(f, n):
    print("original function call")
    print(datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3])
    
    sleep(n/1000)
    f()

if __name__ == '__main__':
    def func():
        print("Delayed Function")
        print(datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3])

    job_scheduler(func, 1000)