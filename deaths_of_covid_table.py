import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
df = pd.read_csv("datasets/covid_19_data_tr.csv") 

first_wave = df['Deaths'].iloc[:32]
second_wave = df['Deaths'].iloc[32:63]
third_wave = df['Deaths'].iloc[63:95]
fourth_wave = df['Deaths'].iloc[95:126]
fig,axs = plt.subplots(2,2)

yil1 = df['Last_Update'].iloc[:32]
yil2 = df['Last_Update'].iloc[32:63]
yil3 = df['Last_Update'].iloc[63:95]
yil4 = df['Last_Update'].iloc[95:126]

axs[0,0].grid() # tabloyu kareli yapıyor
axs[0,1].grid()
axs[1,0].grid() 
axs[1,1].grid()
axs[0,0].set_title("İLK AY") # 1. ye title atadık
axs[0,1].set_title("İKİNCİ AY") # 2. ye title atadık
axs[1,0].set_title("ÜÇÜNCÜ AY") # 3. ye title atadık
axs[1,1].set_title("DÖRDÜNCÜ AY") # 4. ye title atadık
axs[0,0].plot(yil1,first_wave, 'o--r')
axs[0,0].set_xticklabels(yil1, rotation=70) # yazıları 70 derece döndürtüyor

axs[0,1].plot(yil2,second_wave, 'o--r')
axs[0,1].set_xticklabels(yil2, rotation=70)

axs[1,0].plot(yil3,third_wave, 'o--r')
axs[1,0].set_xticklabels(yil3, rotation=70)

axs[1,1].plot(yil4,fourth_wave, 'o--r')
axs[1,1].set_xticklabels(yil4, rotation=70)
plt.tight_layout()
fig.suptitle("COVID-19 DEATHS IN TURKEY")
plt.savefig('datasets/covid.pdf') # pdf olarak pc ye kaydettik
plt.legend() # tabloların arasını açıp görüntüyü düzelltik
plt.show() # tabloyu açar


