import socket

#Main Function Start
if __name__=="__main__":

    port=80
    mainsoc=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    mainsoc.connect(("www.example.com",80))
    mainsoc.send(b"GET / HTTP/1.1\r\nHost:www.example.com\r\n\r\n")
    response=mainsoc.recv(4096)
    mainsoc.close()
    print(response.decode())

#Main Function End