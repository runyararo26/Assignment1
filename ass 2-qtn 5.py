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

# example set
t = TextFileHandler("example.txt")
t.write("Hello Sammy")
print(t.read())

b = BinaryFileHandler("example.bin")
b.write(b"0,5,20.25")
print(b.read())