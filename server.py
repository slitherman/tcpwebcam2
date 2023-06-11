import socket
import threading
import json

IP = socket.gethostbyname(socket.gethostname())
PORT = 6479
ADDR = (IP, PORT)
BUFFER_SIZE = 1024
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


def handle_client(client_socket, client_address):
    print(f"[NEW CONNECTION] {client_address} connected...")
    connected = True
    while connected:
        received_data = client_socket.recv(BUFFER_SIZE).decode("utf-8")
        if not received_data:
            break
        try:
            json_data = json.loads(received_data)
            print(json_data)
            if json_data["width"] / 16 == json_data["height"] / 9:
                feedback = "The webcam format is 16/9"
                feedback = feedback.encode("utf-8")
                #you do not have to specify the clients address when sending messages back

                client_socket.send(feedback)
            else:
                feedback = "The webcam format is not 16/9"
                feedback = feedback.encode("utf-8")
                client_socket.send(feedback)

        except json.JSONDecodeError:
            print("[ERROR] Invalid JSON object received")
            break

    client_socket.close()
    print(f"[CONNECTION CLOSED] {client_address}")


def start_server():
    print(f"[SERVER IS LISTENING ON] {PORT} {IP}")
    server_socket.bind(ADDR)
    server_socket.listen(10)
    while True:
        client_socket, client_address = server_socket.accept()
        thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
        thread.start()


print("[STARTING] The server is starting...")
start_server()
