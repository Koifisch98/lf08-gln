import computer
import socket
import time


class Server(computer.Computer):
    
    _service = ""
    __sockIP = None
    __sockPort = None
    sock = None
    
    
    computer.Specs.powerSupply = "500 Watt Inter-Tech ASPower"
    computer.Specs.getInfo()

    def create_Socket(self, ip, port):
        try:
            # Create the server socket
            server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

            self.__sockIP = ip
            self.__sockPort = port
            # Bind the socket to the IP and port
            server_socket.bind((ip, port))
            self.sock = server_socket
            
            
        except Exception as e:
            #Using f in print to use python expressions then writing printing the error with {e}
            print(f"Failed to create server: {e}")
            #Exit if creation fails
            exit()
            
    # Start the Socket creation function

    
    def runningServer(self):
        try:
            server_socket = self.sock
            # Start listening for incoming connections
            server_socket.listen(5)

            print("Server listening on " + self.__sockIP + ":" + str(self.__sockPort))
            
            # Accept incoming connections
            client_socket, address = server_socket.accept()

            #Print the IP of the connecting Client
            print(f"Received connection from {address[0]}:{address[1]}")

            # Send a message to the client to confirm the connection
            client_socket.send("Connection established".encode())

            while True:
                # Receive data from the client
                data = client_socket.recv(1024).decode()

                # If the received data is "shutdown", close the client and server sockets and exit the function
                if data == "shutdown":
                    print("Shutting down")
                    
                    server_socket.close()
                    break

                # Print the received data with a timestamp and the client's IP address
                print(f"[{time.ctime()}] {address[0]}: {data}")
                
        except Exception as e:
            print(f"Error in runningServer(): {e}")
            # Get back into the running Loop after printing Exception
            self.runningServer()
            

    
    
    


    
# Initialize Server Object
MyServer = Server(computer.Specs._cpu,computer.Specs._cpuSpeed," ",computer.Specs._ram,computer.Specs._os,computer.Specs._ip)
# Start the server loop
MyServer.create_Socket("127.0.0.1", 169)
MyServer.runningServer()
