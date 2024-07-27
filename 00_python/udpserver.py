#udp server site

import socket
localIP = "127.0.0.1"
localPort = 20011
bufferSize = 1024
msgFromServer = "Hello UDP Client"
bytesToSend = str.encode(msgFromServer)

# Create a datagram socket
UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

try:
    # Bind to address and port
    UDPServerSocket.bind((localIP, localPort))
    print("UDP server up and listening")

    # Listen for incoming datagrams
    while True:
        bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
        message = bytesAddressPair[0]
        address = bytesAddressPair[1]

        clientMsg = "Message from Client: {}".format(message.decode())
        clientIP = "Client IP Address: {}".format(address)

        print(clientMsg)
        print(clientIP)

        # Sending a reply to client
        UDPServerSocket.sendto(bytesToSend, address)

except socket.error as e:
    print("Error occurred:", e)

finally:
    UDPServerSocket.close()