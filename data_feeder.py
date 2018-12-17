import serial


class DataFeeder:
    def __init__(self):
        serial_input = serial.Serial('/dev/ttyUSB0', 115200)
        serial_input.write(b'T')
        serial_input.write((100).to_bytes(3, byteorder='big'))
        serial_input.write((10).to_bytes(3, byteorder='big'))
        serial_input.write(b'R')
        self.data = serial_input.read(4096)

    def get_measurements(self):
        even, odd = self.data[0::2], self.data[1::2]
        data = ""
        for i in range(len(even)):
            int16 = int.from_bytes([even[i], odd[i]], byteorder='big')
            data += str(int16) + "\n"

        return(data)

# 200-700 nm
# 400-500 get_blue
# 500 600 green
# 600 700 red

    def get_rgb(self):
        data = self.get_measurement()
        start_red = 0
        start_green = 0
        start_blue = 0
        red = data[start_red:]
        green = data[start_green:start_red-1]
        blue = data[start_blue:start_green-1]
        return (red, green, blue)


if __name__ == "__main__":
    print(DataFeeder().get_measurements())
