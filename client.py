import socket
import json

BUFFER_SIZE = 1024
IP = socket.gethostbyname(socket.gethostname())
PORT = 6479
ADDR = (IP, PORT)
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(ADDR)

json_webcams = {
    "brand": None,
    "width": None,
    "height": None,
    "id": None
}

def send_message():
    print(f"[CONNECTED] Client connected to server at {IP}:{PORT}")
    while True:
        try:
            json_webcams["brand"] = input("Enter a brand")
            json_webcams["width"] = int(input("Enter a width"))
            json_webcams["height"] = int(input("Enter a height"))
            json_webcams["id"] = int(input("Enter an id"))
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
            continue

        sent_json_webcam = json.dumps(json_webcams)
        client_socket.send(sent_json_webcam.encode("utf-8"))
        server_response = client_socket.recv(BUFFER_SIZE).decode("utf-8")
        print("Item to be sent:")
        print(sent_json_webcam)
        print("Server response:")
        print(server_response)

        break

    client_socket.close()


send_message()
