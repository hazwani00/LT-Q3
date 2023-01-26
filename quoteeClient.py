import socket

def main():
    
    server_ip = "192.168.56.1"
    server_port = 8888

    
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    
    client_socket.connect((server_ip, server_port))

    
    quote = client_socket.recv(1024)
    print("Quotes Of The Day! : \n %s" % quote.decode())

    
    client_socket.close()


main()
