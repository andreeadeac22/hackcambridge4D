import csv, json, sys
import pandas as pd
import png
import matplotlib.pyplot as plt
import numpy as np
import os

LIMIT = 175

input_file = sys.argv[1]
data = pd.read_csv(input_file)

labels = data['Label']
pixels = data.iloc[:, :-1]


print(labels[0])
print(pixels.values.shape)


df = pixels.values.reshape(27455, 28,28)
print(df.shape)


path = "sign-language-mnist/"


for i in range(26):
    letter = chr(i + 65)
    #cnt_letter = 0

    if not os.path.exists(path+letter):
        os.makedirs(path+letter)

    for j in range(labels.shape[0]):
        if(labels[j] == i):
            el = df[j,:,:]
            image = np.array(el, dtype=np.uint8)
            plt.imsave(path+letter+'/sample'+str(j)+'.png', image, cmap='gray')
            #cnt_letter += 1
            #if cnt_letter > LIMIT:
            #    break



"""
f = open('ramp.png', 'wb')      # binary mode is important
w = png.Writer(28, 28, greyscale=True)
w.write(f, el)
f.close()
"""
