from abc import ABC, abstractmethod
from pathlib import Path

class FileHandler(ABC):
    @abstractmethod
    def read(self):
        pass

    @abstractmethod
    def write(self, data):
        pass

class TextFileHandler(FileHandler):
    def __init__(self, path: Path):
        self.path = Path(path)

    def read(self):
        return self.path.read_text(encoding="utf-8")

    def write(self, data: str):
        self.path.write_text(data, encoding="utf-8")

class BinaryFileHandler(FileHandler):
    def __init__(self, path: Path):
        self.path = Path(path)

    def read(self):
        return self.path.read_bytes()

    def write(self, data: bytes):
        self.path.write_bytes(data)

# Demo
t = TextFileHandler("example.txt")
t.write("Hello text")
print(t.read())

b = BinaryFileHandler("example.bin")
b.write(b"\x00\x01\x02")
print(b.read())