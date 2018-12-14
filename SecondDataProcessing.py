
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
# red
funx = []
# green
funy = []
# blue
funz = []
# funx = 1.065 * np.e((-1/2) * (((visible_wave_length)-595.8)/33.33) ^ 2)+0.366 * np.e((-1/2) * (((visible_wave_length)-446.8)/19.44) ^ 2)
# funy(i) = 1.014.*exp((-1/2).*((log(i+399)-log(556.3))/0.075).^2);
# funz(i) =  1.839.*exp((-1/2).*((log(i+399)-log(449.3))/0.051).^2);

for i in range(len(visible_wave_length_intensity)):
    percent_wave_length_intensity.append(visible_wave_length_intensity[i]/16383)
    funx.append(1.065 * np.exp((-1/2) * ((visible_wave_length[i]-595.8)/33.33) ** 2)+0.366 * np.exp((-1/2) * ((visible_wave_length[i]-446.8)/19.44) ** 2))
    funy.append(1.014*np.exp((-1/2)*((np.log(visible_wave_length[i])-np.log(556.3))/0.075)**2))
    funz.append(1.839*np.exp((-1/2)*((np.log(visible_wave_length[i])-np.log(449.3))/0.051)**2))

# print(visible_wave_length)
# print(percent_wave_length_intensity)
# print(funz)
x = 0
y = 0
z = 0

for i in range(len(visible_wave_length_intensity)):
    x = x + (percent_wave_length_intensity[i]*visible_wave_length[i]*10**(-9)*funx[i])
    y = y + (percent_wave_length_intensity[i]*visible_wave_length[i]*10**(-9)*funy[i])
    z = z + (percent_wave_length_intensity[i]*visible_wave_length[i]*10**(-9)*funz[i])

print(x)
print(y)
print(z)

xt = x/(x+y+z)
yt = y/(x+y+z)


print(xt)
print(yt)

n = (xt-0.332)/(yt-0.1858)
cct = 449*n**3+3525*n**2-6823.3*n+5520.33

print(cct)
