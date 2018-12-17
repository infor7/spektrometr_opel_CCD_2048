from data_feeder import DataFeeder


class FileUtils:
    def read_data(self, filename):
        dataFeeder = DataFeeder()
        measurements = dataFeeder.get_measurements()

        with open('data_from_spec_with_light.txt', 'w') as fh:
            for measrement in measurements:
                fh.write(measrement)

        with open(filename, 'r') as fh:
            return [int(x.replace('\n\n', '\n')) for x in fh.readlines()]


if __name__ == "__main__":
    data = FileUtils()
    print(data.read_data("data_from_spec_with_light.txt"))
