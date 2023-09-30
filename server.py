import socket
import json
import room


class Server:
    def __init__(self, config_file: str):
        self.config_file = config_file
        # AF_INET, Address Family. Specifies the addresses that the socket will comminucate with.
        # AF_INET is typically Internet Protocol 4, IPv4.
        # Also, There's IPv6, AF_INET6
        # See https://stackoverflow.com/questions/1593946/what-is-af-inet-and-why-do-i-need-it#1594039

        # SOCK_STREAM means that it is a TCP socket. (Transmission Control Protocol)
        # SOCK_DGRAM means that it is a UDP socket.  (User Datagram Protocol)

        # A datagram is a basic transfer unit associated with a packet-switched network.
        # Datagrams are typically structured in header and payload sections.
        # Datagrams provide a connectionless communication service across a packet-switched network.
        # The delivery, arrival time, and order of arrival of datagrams need not be guaranteed by the network.
        self.tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.settings = self.load_config()

        self.server_address = (self.settings["IP"], self.settings["PORT"])
        self.tcp_socket.bind(self.server_address)
        self.tcp_socket.listen(self.settings["CONNECTIONS"])

        self.handle()

    def load_config(self):
        with open(self.config_file, "r") as config:
            config = json.load(config)

        return config

    def handle(self):
        code = room.Transcriber().encode_string(self.server_address[0], self.server_address[1])
        while True:
            print(f"Share this code with your friends: {code}")
            connection, client = self.tcp_socket.accept()

            try:
                print(f"Connected to client: {client}")

                # Default
                while True:
                    data = connection.recv(32)
                    print(f"{client} :: {data}")

                    if not data:
                        break
            finally:
                connection.close()


if __name__ == "__main__":
    test_server = Server("config1.json")
