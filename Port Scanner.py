import socket

# //Warning// Scanner is slow asf, consider not using it #

first_Port = input('Starting Port: ')
last_Port = input('Final Port: ')
openPort = [] #empty list to be appended with open ports

for port in range (int(first_Port), int(last_Port)): #port range
    try:
        s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.settimeout(1000) #remove if delayed
        if s.connect_ex(('', port)): #public ip
            print('%d:CLOSED' % (port))
        else:
            print('%d:OPEN' % (port))
            openPort.append(port)
            s.close
    except: continue

print ('Open ports are: ', openPort)