from matplotlib import pyplot
from FileUtils import FileUtils
from scipy.interpolate import spline


class Chart:
    def display(self):
        data = FileUtils().read_data('data_from_spec_with_light.txt')
        x = [200 + x * 500/2048 for x in range(2048)]
        pyplot.plot(x, data)
        pyplot.show()


if __name__ == "__main__":
    chart = Chart()
    chart.display()
