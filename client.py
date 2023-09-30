import socket
import room


class Client:
    def __init__(self):
        self.username = None
        self.tcp_socket = None
        self.transcoder = room.Transcriber()
        self.setup()

    def setup(self):
        self.username = input("Username >> ")
        code = input("Server Code >> ")
        self.connect(code)

    def connect(self, code: str):
        print(f"Attempting to find server with code: {code}")
        ip, port = self.transcoder.decode_string(code)

        ip = (ip, port)

        self.tcp_socket = socket.create_connection(ip)

        try:
            while True:
                message = input(f"[{self.username}]  ")
                message = str.encode(message)
                self.tcp_socket.sendall(message)
        except KeyboardInterrupt:
            print(f"Closing Connection to {code}.")
            self.tcp_socket.close()


if __name__ == "__main__":
    client = Client()
