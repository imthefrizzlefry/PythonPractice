import sys

class Flight:
    def __init__(self, number, seat=''):
        
        self.setnumber(number)
        
        if seat:
            self.addseat(seat)
        else:
            self._seat = 'unassigned'

    def setnumber(self, number):
        if not number[:2].isalpha():
            raise ValueError("No airline Code in '{}'".format(number))

        if not number[:2].isupper():
            raise ValueError("Invalid airline code '{}'".format(number))

        if not (number[2:].isdigit() and int(number[2:]) <= 9999):
            raise ValueError("Invalid route number '{}'".format(number))

        self._number = number

    def addseat(self, seat):

        if not seat[2:].isalpha():
            raise ValueError("No airline Code in '{}'".format(seat))

        if not seat[2:].isupper():
            raise ValueError("Invalid airline code '{}'".format(seat))

        if not (seat[:2].isdigit() and int(seat[:2]) <= 99):
            raise ValueError("Invalid route number '{}'".format(seat))

        self._seat = seat

    def number(self):
        return self._number

    def seat(self):
        return self._seat

    def display(self):
        print('You are in seat {0} on flight {1}'.format(self._seat, self._number))

    def saveFile(self, filename='temp.csv'):
        f = open(filename, mode='wt', encoding='utf-8')
        f.write('{0},{1}'.format(self.number(), self.seat()))
        f.close()

    def loadFile(self, filename='temp.csv'):
        f = open(filename, mode='rt', encoding='utf-8')
        self._number, self._seat = f.read().split(',')
        #self._number = temp[0]
        #self._seat = temp[1]
        f.close()
        
