import numpy as np
from FileUtils import FileUtils
import matplotlib.pyplot as plt


file_name = 'data_from_spec_with_light.txt'

data = FileUtils().read_data(file_name)
data_max = max(data)
# print(data_max)
# print(data.index(data_max))

# generate
tmp = np.linspace(200, 700, 2048)

wave_lenghts = []
wave_lenghts = tmp.tolist()
# 400nm indx = print(wave_lenghts[819])

# Lists for visible light
visible_wave_length = wave_lenghts[819:]
visible_wave_length_intensity = data[819:]
percent_wave_length_intensity = []


# red
fun_x = []
# green
fun_y = []
# blue
fun_z = []

# color matching functions
for i in range(len(visible_wave_length_intensity)):
    percent_wave_length_intensity.append(visible_wave_length_intensity[i]/data_max)
    fun_x.append(1.065 * np.exp((-1/2) * ((visible_wave_length[i]-595.8)/33.33) ** 2) + 0.366 * np.exp((-1/2) * ((visible_wave_length[i] - 446.8)/19.44) ** 2))
    fun_y.append(1.014 * np.exp((-1/2) * ((np.log(visible_wave_length[i]) - np.log(556.3))/0.075) ** 2))
    fun_z.append(1.839 * np.exp((-1/2) * ((np.log(visible_wave_length[i]) - np.log(449.3))/0.051) ** 2))

# print(visible_wave_length)
# print(percent_wave_length_intensity)

X = 0
Y = 0
Z = 0

for i in range(len(visible_wave_length_intensity)):
    X = X + (percent_wave_length_intensity[i] * fun_x[i])
    Y = Y + (percent_wave_length_intensity[i] * fun_y[i])
    Z = Z + (percent_wave_length_intensity[i] * fun_z[i])


xc = X/(X + Y + Z)
yc = Y/(X + Y + Z)

# CIE 1931 chromaticity coordinates
print("Coordinate x:", xc)
print("Coordinate y:", yc)

# CIE 1960 chromaticity coordinates
u = 4 * xc / (-2 * xc + 12 * yc + 3)
v = 6 * yc / (-2 * xc + 12 * yc + 3)

print("\nCoordinate u:", u)
print("Coordinate v:", v)

# Calvin McCamy method
n = (xc - 0.332)/(yc - 0.1858)
cct = 449 * n ** 3 + 3525 * n ** 2 - 6823.3 * n + 5520.33

print("\nColor temperature:", cct)

plt.plot(visible_wave_length, visible_wave_length_intensity)
plt.show()

#plt.plot(visible_wave_length, percent_wave_length_intensity, '.')
#plt.show()
