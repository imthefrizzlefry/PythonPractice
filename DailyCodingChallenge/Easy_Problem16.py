import logging

''' This problem was asked by Twitter.

You run an e-commerce website and want to record the last N order ids in a log. Implement a data structure to accomplish this, with the following API:

record(order_id): adds the order_id to the log
get_last(i): gets the ith last element from the log. i is guaranteed to be smaller than or equal to N.

You should be as efficient with time and space as possible.
'''

class orderRecorder:
    def __init__(self, max_size = 5):
        self.orderList = []
        self.max_size = max_size

    def record(self, order_id):
        self.orderList.append(order_id)
        if len(self.orderList) > self.max_size:
            self.orderList.pop(0)

    def get_last(self, i=5):
        return self.orderList[i-1]



if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)

    n=50
    order_log = orderRecorder(n)

    for order in range(1,n+1):
        order_log.record(order)

    logging.debug(order_log.get_last(1))
    logging.debug(order_log.get_last(n))

