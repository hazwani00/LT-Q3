import random
import socket
import threading

quotes = ["Spread love everywhere you go. Let no one ever come to you without leaving happier.", 
"Do not go where the path may lead, go instead where there is no path and leave a trail.", 
"Happy Tummy Happy Me", 
"Reduce your expection to feel less dissapoinment"]

def handle_client(client_socket):
    quote = random.choice(quotes)
    client_socket.send(quote.encode())
    client_socket.close()


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("192.168.56.1", 8888))
server.listen(5)
print("[*] Listening on %s:%d for request" % ("192.168.56.1", 8888))



while True:
    client_socket, client_address = server.accept()
    print("[*] Received connection from %s" % str(client_address))
    client_thread = threading.Thread(target=handle_client, args=(client_socket,))
    client_thread.start()

main()
