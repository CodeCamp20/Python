import socket

hostname = socket.gethostname()
IPAddress = socket.gethostbyname(hostname)

print("Computer Name :\n", hostname)

print("Your ip address :\n", IPAddress)
