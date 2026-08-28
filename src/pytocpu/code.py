import os

class Code:
    def __init__(self):
        self.data = bytearray()

    def emit(self, *bytes_):
        for b in bytes_:
            if not 0 <= b <= 0xFF:
                raise ValueError(f"Byte out of range: {b}")
        self.data.extend(bytes_)

    def save(self, filename):
        filename = os.path.basename(filename)

        with open(filename, "wb") as f:
            f.write(self.data)
        return len(self.data)

    def len(self):
        return len(self.data)

    def hex(self):
        return " ".join(f"{b:02X}" for b in self.data)

    def clear(self):
        self.data.clear()

    def size(self):
        return len(self.data)

    def bytes(self):
        return bytes(self.data)