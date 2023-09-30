class Transcriber:
    def __init__(self):
        self._encode_map = {
            '1': 'a',
            '2': 'b',
            '3': 'c',
            '4': 'd',
            '5': 'e',
            '6': 'f',
            '7': 'g',
            '8': 'h',
            '9': 'i',
            '0': 'j'
        }

        self._decode_map = {
            'a': '1',
            'b': '2',
            'c': '3',
            'd': '4',
            'e': '5',
            'f': '6',
            'g': '7',
            'h': '8',
            'i': '9',
            'j': '0'
        }

    def encode_string(self, ip: str, port: int):
        parts = ip.split('.')
        ip = ""
        code = ""

        for part in parts:
            if len(part) == 3:
                ip += part
                continue

            part = "0" * (3 - len(part)) + part
            ip += part

        code = ''.join([self._encode_map[char] for char in ip])

        code += '.'
        code += ''.join([self._encode_map[char] for char in str(port)])

        return code

    def decode_string(self, code: str):
        original_ip, port = code.split('.')

        final_ip = ''.join([self._decode_map[char] for char in original_ip])
        final_ip = '.'.join(final_ip[i:i + 3] for i in range(0, len(final_ip), 3))

        final_port = ''.join([self._decode_map[char] for char in port])

        return final_ip, int(final_port)


if __name__ == "__main__":
    t = Transcriber()
    ip = '127.0.0.1'
    port = 8080

    code = t.encode_string(ip, port)
    print(code)
    decoded = t.decode_string(code)
    print(decoded)
