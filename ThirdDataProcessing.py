
# Projekt Michał

import numpy as np
from FileUtils import FileUtils

file_name = 'data_from_spec_with_light.txt'

data = FileUtils().read_data(file_name)
data_max = max(data)
print(data_max)
print(data.index(data_max))
tmp = np.linspace(200, 700, 2048)

wave_lenghts = []
wave_lenghts = tmp.tolist()
# 400nm indx = print(wave_lenghts[819])

light_temperature = []

for i in range(len(wave_lenghts)):
    light_temperature.append(2897768.5/wave_lenghts[i])

print(wave_lenghts[data.index(data_max)])
print(light_temperature[data.index(data_max)])
# print(light_temperature)
