import random

class DataStream:
    def __init__(self):
        self.data_store = {}
        self.current_pos = 1

    def receive(self, chunk_num, bytes_data):
        self.data_store[chunk_num] = bytes_data

    def read(self, empty_byte_array):
        buffer_fill_size = 0

        for i in range(len(empty_byte_array)):
            if self.current_pos in self.data_store:
                for byte in self.data_store[self.current_pos]:
                    if buffer_fill_size == len(empty_byte_array):
                        break
                    empty_byte_array[buffer_fill_size] = byte
                    buffer_fill_size += 1
                
                del self.data_store[self.current_pos]
                self.current_pos += 1
            else:
                break

        return buffer_fill_size


def generate_random_order_string(string):
    chunks = [(i+1, c) for i, c in enumerate(string)]
    random.shuffle(chunks)
    return chunks

class DataStream:
    def __init__(self):
        self.data_store = {}
        self.current_pos = 1

    def receive(self, chunk_num, bytes_data):
        self.data_store[chunk_num] = bytes_data

    def read(self, empty_byte_array):
        buffer_fill_size = 0

        for i in range(len(empty_byte_array)):
            if self.current_pos in self.data_store:
                byte = self.data_store[self.current_pos]
                empty_byte_array[buffer_fill_size] = ord(byte)
                buffer_fill_size += 1
                
                del self.data_store[self.current_pos]
                self.current_pos += 1
            else:
                break

        return buffer_fill_size


data_stream = DataStream()
chunks = generate_random_order_string("I am a programmer")

for chunk in chunks:
    data_stream.receive(*chunk)


empty_byte_array = bytearray(10)  # bytearray of size 10
bytes_read = data_stream.read(empty_byte_array)
print("Bytes read:", bytes_read)
print("Data:", empty_byte_array[:bytes_read].decode())

