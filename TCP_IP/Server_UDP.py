import socket
import TransData

HOST = '127.0.0.1'
BIND_PORT = 65333
SEND_PORT = 65222

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as bind_socket:
    bind_socket.bind((HOST, BIND_PORT))
    bind_socket.setblocking(False)
    print("UDP server is up and listening")
    
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as send_socket:
        while True:
            try:
                data = bind_socket.recvfrom(1024)
                print(data)
                msg  = data[0]
                addr = data[1]

                #msg_from_client = "Hello Server from client"
                #bytes_to_send = str.encode(msg_from_client)
                print(len(data))
                
                send_socket.sendto(TransData.DataShift(msg), addr)


            except BlockingIOError:#이 구문이 없으면 오류로 팅겨나감.
                continue

