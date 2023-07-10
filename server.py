from socket import *

def createServer():
    serversock = socket(AF_INET, SOCK_STREAM)
    try:
        serversock.bind(('localhost', 9000))
        serversock.listen(5)
        while(1):
            (clientsock, address) = serversock.accept()
            rd = clientsock.recv(5000).decode()
            pieces = rd.split("\n")
            if (len(pieces) > 0): print(pieces[0])

            data = "HTTP/1.1 200 OK\r\n"
            data += "Content-Type: text/xml; charset=utf-8\r\n"
            data += "\r\n"
            data += "<html><body>Hello World</body><html>\r\n\r\n"

            clientsock.sendall(data.encode())
            clientsock.shutdown(SHUT_WR)

    except KeyboardInterrupt:
        print("\nShutting down...\n")
    except Exception as exc:
        print("Error:\n")
        print(exc)

    serversock.close()

print('Access http://localhost:9000')

createServer()