import socket

HOST = '127.0.0.1'
PORT = 65333

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.bind((HOST, PORT))
    server_socket.listen(1)
    print("client wait....")

    client_socket, addr = server_socket.accept()

    with client_socket:
        print(f'{addr}에서 연결됨')

        while True:
            data = client_socket.recv(1024)
            
            if data:
                print(f'수신된 데이터: {data.decode()}')
                byte_count = len(data)
                print(f'{len(data)}')
                byteSend = bytearray(data)# 파이썬은 bytes 형태를 바로 수정할 수 없어서 수정이 가능한 bytearray 형으로 형변환함.
                for idx in range(len(byteSend)):
                    #print(idx)
                    byteSend[idx] = byteSend[idx] + 1
                client_socket.sendall(byteSend)

        