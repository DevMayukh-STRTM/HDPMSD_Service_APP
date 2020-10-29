import os
import sys

import pickle
import json

class HDPMSD():
    def writeFile(self, filename, data, mode):
        try:
            if mode == 0:
                ax = open(filename, 'w')
                ax.write(str(data))
                ax.close
                return 200 #success
            elif mode == 1:
                ax = open(filename, 'wb')
                ax.write(str(data))
                ax.close()
                return 200 #success
            else:
                return 203 #Mode error
        except:
            return 404 #FileWriteError
    
    def readFile(self, filename, mode):
        try:
            if mode == 0:
                ax = open(filename, 'r')
                return ax.read()
            elif mode == 1:
                ax = open(filename, 'rb')
                return ax.read()
        except:
            return "105" #BAD read
    
    def deleteFile(self, filename):
        try:
            if os.path.isfile(filename):
                os.remove(filename)
                return 200 #success
            else:
                return 404 #FileDeleteError
        
        except:
            return 103 #BAD delete

    def filesize(self, filename):
        try:
            return os.path.getsize(filename)
        except:
            return 105 #BAD read

    #all file system is over. Now move on to list

    def readList(self, list_data, index):
        xn = eval(list_data)
        try:
            return f'{xn[index]}'
        except:
            return 99 #Index_Error
        
    def writeList(self, list_data, data):
        xn = eval(list_data)
        if type(data) == type([]) or type(data) == type({}):
            try:
                xn.append(eval(data))
                return f'{xn}'
            except:
                return 105 #BAD READ

        else:
            try:
                xn.append(data)
                return f'{xn}'
            except:
                return 105 #BAD READ
    
    def deleteListItem(self, list_index, index):
        xn = eval(list_index)
        try:
            xn.pop(index)
            return f'{xn}'
        except:
            return 103 # Bad delete

    def listSize(self, listdata):
        xn = eval(listdata)
        return len(xn)

    #all list items. Now move over to JSON

    def writeNode(self, json_data, new_data):
        xn = eval(json_data)
        if type(new_data) == type({}):
            try:
                xn.update(new_data)
                return f'{xn}'
            except:
                return 105 #bad read
        else:
            return 59 #Invalid Update Format

    def readNode(self, json_data, node):
        xn = eval(json_data)
        try:
            return f'{xn[node]}'
        except:
            return 105 #bad read

        
    def deleteNode(self, json_data, node):
        xn = eval(json_data)
        try:
            xn.pop(node)
            return f'{xn}'
        except:
            return 59 #Invalid Update format

    def json_size(self, json_data):
        xn = eval(json_data)
        return len(xn)