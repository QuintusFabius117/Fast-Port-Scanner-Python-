import socket
import threading
from queue import Queue #queues elements in a list and takes them out after interacted with

ip = input('IP Address: ') #remember to ping a website address to grab its IP
first_Port = input('Starting Port: ')
last_Port = input('Final Port: ')
queue = Queue()
open_Port = [] #empty list to be appended with open ports


def port_Scan(port):
    try:
        s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip, port)) #public ip only
        return True
    except:   
        return False

def fill_queue(port_List):
    for port in port_List:
        queue.put(port)

def display():
    while not queue.empty():
        port = queue.get()
        if port_Scan(port):
            print('{}:OPEN'.format(port))
            open_Port.append(port)

port_List = range(int(first_Port), int(last_Port))
fill_queue(port_List)

thread_List = []

for t in range(1000): #at a threading rate of 1000...
    thread = threading.Thread(target=display) #the display function is to be run with threading
    thread_List.append(thread) #the list ensures the thread function can count the ports in order as it runs rather than running through the same ports multiple times

for thread in thread_List:
    thread.start() #runs all display() functions in the list

for thread in thread_List:
    thread.join() #this waits for a thread to be done before continuing

print ('Open ports are: ', open_Port)