import numpy as np
import matplotlib.pyplot as plt
import function as func
from statistics import mean

soup = func.crawlData('https://www.bps.go.id/statictable/2019/03/06/2049/rata-rata-upah-gaji-bersih-sebulan-buruh-karyawan-pegawai-menurut-provinsi-dan-lapangan-pekerjaan-utama-di-17-sektor-rupiah-2018.html')
# find results within table
results = soup.find('table',{'class':'xl7325477'})
rows = results.find_all('tr',{'class':'xl7925477'})
pendapatan = []
wilayah = []
for r in rows:
    # find all columns per result
    data = r.find_all('td')
    # check that columns have data
    if len(data) == 0:
        continue
    # write columns to variables
    provinsi = data[0].getText()
    total = data[-1].getText()
    # Remove white space
    total = total.replace(' ','')
    # remove \n (newline)
    provinsi = provinsi.replace('\n ','')
    if provinsi != 'Kalimantan Utara':
        # Cast Data Type Integer
        total = int(total)
        # Cast Uppercase to Wilayah
        provinsi = provinsi.upper()
        wilayah.append(provinsi)
        pendapatan.append(total)

pendapatan_avg = round(mean(pendapatan),2)

pendapatan_tinggi = []
pendapatan_rendah = []
jml_tinggi = []
jml_rendah = []
for i,v in enumerate(pendapatan):
    if(v > pendapatan_avg):
        pendapatan_tinggi.append(wilayah[i])
        jml_tinggi.append([v])
    else:
        pendapatan_rendah.append(wilayah[i])
        jml_rendah.append([v])

print(pendapatan_tinggi)
soup2 = func.crawlData('https://kawalpemilu.org/#0',second=10)
# find results within table
results2 = soup2.find('table',{'class':'table'})
rows2 = results2.find_all('tr',{'class':'row'})
# index 0 = tinggi, index1 = rendah
jokowi_tinggi = []
jokowi_rendah= []
prabowo_tinggi = []
prabowo_rendah= []

# print(rows)
for r in rows2:
    # find all columns per result
    data = r.find_all('td')
    # check that columns have data
    if len(data) == 0:
        continue
    # write columns to variables
    wilayah = data[1].find('a').getText()
    satu = data[2].find('span', attrs={'class':'abs'}).getText()
    dua = data[3].find('span', attrs={'class': 'abs'}).getText()
    # Remove decimal point
    satu = satu.replace('.','')
    dua = dua.replace('.','')
    # Cast Data Type Integer
    satu = int(satu)
    dua = int(dua)
    if wilayah != 'Luar Negeri' and wilayah != 'KALIMANTAN UTARA':
        if wilayah in pendapatan_tinggi:
            print(wilayah)
            jokowi_tinggi.append([satu])
            prabowo_tinggi.append([dua])
        else:
            jokowi_rendah.append([satu])
            prabowo_rendah.append([dua])


# Convert to numpy

np_jokowi= np.array(jokowi_tinggi)
np_jokowi2= np.array(jokowi_rendah)
np_prabowo= np.array(prabowo_tinggi)
np_prabowo2= np.array(prabowo_rendah)
np_tinggi = np.array(jml_tinggi)
np_rendah= np.array(jml_rendah)

func.do_regress(np_tinggi,np_jokowi,xlabel="Tingkat Pendapatan Diatas Rata-Rata Nasional",ylabel="Persentase Suara Jokowi Per Provinsi")
func.do_regress(np_rendah,np_jokowi2,xlabel="Tingkat Pendapatan Dibawah Rata-Rata Nasional",ylabel="Persentase Suara Jokowi Per Provinsi")
func.do_regress(np_tinggi,np_prabowo,xlabel="Tingkat Pendapatan Diatas Rata-Rata Nasional",ylabel="Persentase Suara Prabowo Per Provinsi")
func.do_regress(np_rendah,np_prabowo2,xlabel="Tingkat Pendapatan Dibawah Rata-Rata Nasional",ylabel="Persentase Suara Prabowo Per Provinsi")

# # plot data
# fig,ax = plt.subplots(figsize=(10,5))
# # print(ax)
# pos = list(range(len(np_jokowi)))
# width = 0.25
#
# rects1 = ax.bar(pos,np_jokowi,width,color='red',label='Jokowi 2019')
# rects2 = ax.bar([p + width for p in pos],np_prabowo,width,color='blue',label='Prabowo 2019')
# # ax.set_xticks(ind)
# ax.set_xticks([p + 0.5 * width for p in pos])
# ax.set_xticklabels(['High Income','Low Income'])
# # # Naming label
# plt.xlabel('Income Type')
# plt.ylabel('Vote Percentage')
#
# func.setPlotText(np.round(np_jokowi,2), x=0, y=0.6, val='%', halign='center')
# func.setPlotText(np.round(np_prabowo,2), x=width, y=0.6, val='%', halign='center')
# # # styling x,y value
# plt.yticks(np.arange(np_jokowi.min(),np_jokowi.max(),4000000))
# plt.legend(loc='upper right')
# plt.yscale('linear')
# plt.show()
