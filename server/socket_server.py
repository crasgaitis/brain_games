import socket

def run_socket_server():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('0.0.0.0', 6000))
    s.listen(5)
    print("Socket server listening...")

    while True:
        conn, addr = s.accept()
        data = conn.recv(1024)
        if not data:
            break
        print(f"Received data: {data.decode('utf-8')}")
        conn.close()

run_socket_server()
