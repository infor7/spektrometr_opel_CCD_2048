import numpy as np
from FileUtils import FileUtils
import matplotlib.pyplot as plt
import scipy as sp
from scipy import signal



file_name = 'data_from_spec_with_light.txt'

data = FileUtils().read_data(file_name)
data_max = max(data)
# print(data_max)
# print(data.index(data_max))

# generate
tmp = np.linspace(200, 700, 2048)

wave_lengths = []
wave_lengths = tmp.tolist()
# 400nm indx = print(wave_lenghts[819])

# Lists for visible light
visible_wave_length = wave_lengths[737:]
# visible_wave_length_intensity = data[737:]
visible_wave_length_intensity_all = data[737:]
visible_wave_length_intensity = []
percent_wave_length_intensity = []

# red
fun_x = []
# green
fun_y = []
# blue
fun_z = []

# noise reduction
for i in range(len(visible_wave_length_intensity_all)):
    if visible_wave_length_intensity_all[i] > 6000:
        visible_wave_length_intensity.append(visible_wave_length_intensity_all[i]-6000)
    else:
        visible_wave_length_intensity.append(0)

# median filter        
visible_wave_length_intensity = sp.signal.medfilt(visible_wave_length_intensity, 9)

# correction
# for i in reversed(range(len(visible_wave_length_intensity))):
#    visible_wave_length_intensity[i] = visible_wave_length_intensity[i - 300]
    
# color matching functions
for i in range(len(visible_wave_length)):
    percent_wave_length_intensity.append(visible_wave_length_intensity[i]/(data_max-6000))
    fun_x.append(1.065 * np.exp((-1/2) * ((visible_wave_length[i]-595.8)/33.33) ** 2) + 0.366 * np.exp((-1/2) * ((visible_wave_length[i] - 446.8)/19.44) ** 2))
    fun_y.append(1.014 * np.exp((-1/2) * ((np.log(visible_wave_length[i]) - np.log(556.3))/0.075) ** 2))
    fun_z.append(1.839 * np.exp((-1/2) * ((np.log(visible_wave_length[i]) - np.log(449.3))/0.051) ** 2))

X = 0
Y = 0
Z = 0

for i in range(len(visible_wave_length)):
    if percent_wave_length_intensity[i] > 0:
        X = X + (percent_wave_length_intensity[i] * fun_x[i])
        Y = Y + (percent_wave_length_intensity[i] * fun_y[i])
        Z = Z + (percent_wave_length_intensity[i] * fun_z[i])

# CIE 1931 chromaticity coordinates
xc = X/(X + Y + Z)
yc = Y/(X + Y + Z)
print("CIE 1931")
print("Coordinate x:", xc)
print("Coordinate y:", yc)

# CIE 1960 chromaticity coordinates
u = 4 * xc / (-2 * xc + 12 * yc + 3)
v = 6 * yc / (-2 * xc + 12 * yc + 3)
print("\nCIE 1960")
print("Coordinate u:", u)
print("Coordinate v:", v)

# Calvin McCamy method
n = (xc - 0.332)/(yc - 0.1858)
cct = 449 * n ** 3 + 3525 * n ** 2 - 6823.3 * n + 5520.33

print("\nColor temperature:", cct)

plt.plot(wave_lengths, data)
plt.show()

mysignals = [{'name': 'red', 'x': visible_wave_length,
             'y': fun_x, 'color':'r', 'linewidth':2},
            {'name': 'green', 'x': visible_wave_length,
             'y': fun_y, 'color':'g', 'linewidth':2},
            {'name': 'blue', 'x': visible_wave_length,
             'y': fun_z, 'color':'b', 'linewidth':2},
            {'name': 'light source', 'x': visible_wave_length,
             'y': percent_wave_length_intensity, 'color':'k', 'linewidth':1}]

fig, ax = plt.subplots()
for signal in mysignals:
    ax.plot(signal['x'], signal['y'], 
            color=signal['color'], 
            linewidth=signal['linewidth'],
            label=signal['name'])

ax.legend()
plt.show()
