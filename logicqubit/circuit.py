#!/usr/bin/python
# encoding: utf-8

# Author Cleoner S. Pietralonga
# e-mail: cleonerp@gmail.com
# Apache License

class Circuit():

    def __init__(self):
        Circuit.__operations = []

    def addOp(self, operation, values):  # add the new type of operation
        op = str(operation)+"("+str(values[0])
        for value in values[1:]:
            op += ","+str(value)
        op += ")"
        Circuit.__operations.append(op)

    def getOp(self):  # get all operations
        return Circuit.__operations

    def PrintOperations(self):  # print all operations
        print(self.__operations)
