import serial


class DataFeeder:
    def __init__(self):
        serial_input = serial.Serial('/dev/ttyUSB0', 115200)
        serial_input.write(b'R')
        self.data = serial_input.read(4096)

    def get_measurements(self):
        even, odd = self.data[0::2], self.data[1::2]
        data = ""
        for i in range(len(even)):
            int16 = int.from_bytes([even[i], odd[i]], byteorder='big')
            data += str(int16) + "\n"

        return(int16)


if __name__ == "__main__":
    DataFeeder().get_measurements()
