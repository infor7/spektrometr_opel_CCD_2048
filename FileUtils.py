class FileUtils:
    def _read_data(self, filename):
        with open(filename, 'r') as fh:
            return [int(x) for x in fh.readlines()]


if __name__ == "__main__":
    data = FileUtils()
    print(data._read_data("data_from_spec.txt"))
