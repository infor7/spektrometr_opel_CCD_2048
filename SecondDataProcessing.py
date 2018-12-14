
# Projekt Marcina

import numpy as np
from FileUtils import FileUtils

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
funx = []
funy = []
# funx = 1.065 * np.e((-1/2) * (((visible_wave_length)-595.8)/33.33) ^ 2)+0.366 * np.e((-1/2) * (((visible_wave_length)-446.8)/19.44) ^ 2)
# funy(i) = 1.014.*exp((-1/2).*((log(i+399)-log(556.3))/0.075).^2);

for i in range(len(visible_wave_length_intensity)):
    percent_wave_length_intensity.append(visible_wave_length_intensity[i]/16383)
    funx.append(1.065 * np.e*(((-1)/2) * ((visible_wave_length[i]-595.8)/33.33) ** 2)+0.366 * np.e*(((-1)/2) * ((visible_wave_length[i]-446.8)/19.44) ** 2))
    funy.append(1.014*np.e*((-1/2)*((np.log(visible_wave_length[i])-np.log(556.3))/0.075)**2))

# print(visible_wave_length)
# print(percent_wave_length_intensity)
print(funy)
