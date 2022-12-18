import computer
import socket


class Client(computer.Computer):
    
    __remoteIP = None
    __remotePort = None
    computer.Specs.powerSupply = "550 Watt be quiet!"
    computer.Specs.getInfo()
    
    def createSocket(self, remoteIP, remotePort):
        csocket = socket.socket()
        self.__remoteIP = remoteIP
        self.__remotePort = remotePort
        csocket.connect((self.__remoteIP, self.__remotePort))
        
        print("You are connected with ", remoteIP , ":" , remotePort )
        self.__c_socket = csocket
    
    
    
    def sendData(self, string):
        
        c_socket = self.__c_socket
        if string == None:
            while True:
                string = input("Befehl eingeben: ")
                if c_socket != None:
                    if string == "exit":
                        print("Connection closed")
                        c_socket.close()
                        break
                    
                    elif string == "shutdown":
                        print("Send remote-command: Server is shutting down")
                        c_socket.send(string.encode())
                        c_socket.close
                        break
                    else:
                        c_socket.send(string.encode())
        else:
            if c_socket != None:
                if string == "exit":
                    print("Connection closed")
                    c_socket.close()
                
                elif string == "shutdown":
                    print("Send remote-command: Server is shutting down")
                    c_socket.send(string.encode())
                    c_socket.close
                else:
                    c_socket.send(string.encode())
                    c_socket.close()
    
    # Create the client socket
MyClient = Client(computer.Specs._cpu,computer.Specs._cpuSpeed," ",computer.Specs._ram,computer.Specs._os,computer.Specs._ip)
MyClient.createSocket("127.0.0.1", 169)
    
    # Start the Client loop
    
MyClient.sendData(None)