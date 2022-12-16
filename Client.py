import computer
import socket


class Client(computer.Computer):
    
    __remoteIP = "127.0.0.1"
    __remotePort = 169
    computer.Specs.powerSupply = "550 Watt be quiet!"
    computer.Specs.getInfo()
    
    def createSocket(remoteIP, remotePort):
        c_socket = socket.socket()
        c_socket.connect((remoteIP, remotePort))
        
        print("You are connected with ", remoteIP , ":" , remotePort )
        return c_socket
    
    
    
    def sendData(c_socket, string):
        
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
    client_socket = createSocket(__remoteIP, __remotePort)
    
    # Start the Client loop
    sendData(client_socket, None)