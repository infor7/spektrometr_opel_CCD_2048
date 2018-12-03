class FileUtils:
    def read_data(self, filename):
        with open(filename, 'r') as fh:
            return [int(x) for x in fh.readlines()]


if __name__ == "__main__":
    data = FileUtils()
    print(data.read_data("data_from_spec.txt"))
