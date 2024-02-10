# Fast Port Scanner [Python]

## Purpose

A reliable port scanner with custom inputable start and finish port numbers to a public IP. This was to be faster than most port scanners out there while remaining simple so as to be easily adaptable.

## Skills Learned

- Utilise the socket library to interact with and list open ports
- Implement the threading library to speed up the scanning process
- Converting IPv6 addresses to IPv4 addresses in the command line terminal during pings

## Tools

- VS Code

## Process

Import modules and establish variables

```

import socket
import threading
from queue import Queue #queues elements in a list and takes them out after interacted with

ip = input('IP Address: ') #remember to ping a website address to grab its IP
first_Port = input('Starting Port: ')
last_Port = input('Final Port: ')
queue = Queue()
open_Port = [] #empty list to be appended with open ports

```

Create the main port scanning function with socket

```

def port_Scan(port):
    try:
        s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip, port)) #public ip only
        return True
    except:   
        return False

```

Create a queueing function to queue up ports to be readily scanned

```

def fill_queue(port_List):
    for port in port_List:
        queue.put(port)

```

Create a function that runs through the queue. If the port_Scan function identifies an open port, print it out

```

def display():
    while not queue.empty():
        port = queue.get()
        if port_Scan(port):
            print('{}:OPEN'.format(port))
            open_Port.append(port)

```

Establish a variable port list and pass it into the queue function

```

port_List = range(int(first_Port), int(last_Port))
fill_queue(port_List)

```

Establish a threading list variable which will be used to ensure ports are counted in order and once only rather than being sporadically re-counted over and over

```

for t in range(1000): #at a threading rate of 1000...
    thread = threading.Thread(target=display) #the display function is to be run with threading
    thread_List.append(thread) #the list ensures the thread function can count the ports in order as it runs rather than running through the same ports multiple times

```

Create a for loop to run through all of the display functions so that ports can be printed

```

for thread in thread_List:
    thread.start() #runs all display() functions in the list

```

Create a for loop to allow cohesive threading and then print the open_Port list at the end

```

for thread in thread_List:
    thread.join() #this waits for a thread to be done before continuing

print ('Open ports are: ', open_Port)

```







