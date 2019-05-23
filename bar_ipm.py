import numpy as np
import matplotlib.pyplot as plt
import function as func


soup = func.crawlData('https://www.bps.go.id/dynamictable/2019/04/16/1615/peringkat-indeks-pembangunan-manusia-menurut-provinsi-2010-2018-metode-baru-.html')
# find results within table
results_left = soup.find('table',{'id':'tableLeftBottom'})
rows_left = results_left.find_all('tr');
wilayah_tabel = []
for r in rows_left:
    # find all columns per result
    data = r.find_all('td')
    # check that columns have data
    if len(data) == 0:
        continue
    provinsi = data[0].find('b').getText()
    provinsi = provinsi.replace('\n', '')
    wilayah_tabel.append(provinsi)

results_right = soup.find('table',{'id':'tableRightBottom'})
rows_right = results_right.find_all('tr')
wilayah_tinggi = []
wilayah_rendah = []

for i,r in enumerate(rows_right):
    # find all columns per result
    data = r.find_all('td')
    # check that columns have data
    if len(data) == 0:
        continue
    # write columns to variables
    rank = data[-1].getText()
    # remove \n (newline)
    provinsi = provinsi.replace('\n','')
    # Cast Data Type Integer
    rank = int(rank)
    if(rank < 17):
        wilayah_tinggi.append(wilayah_tabel[i])
    else:
        wilayah_rendah.append(wilayah_tabel[i])

soup2 = func.crawlData('https://kawalpemilu.org/#0',second=10)
# find results within table
results2 = soup2.find('table',{'class':'table'})
rows2 = results2.find_all('tr',{'class':'row'})
# index 0 = tinggi, index1 = rendah
jokowi = [0,0]
prabowo = [0,0]

# print(rows)
for r in rows2:
    # find all columns per result
    data = r.find_all('td')
    # check that columns have data
    if len(data) == 0:
        continue
    # write columns to variables
    provinsi = data[1].find('a').getText()
    satu = data[2].find('span', attrs={'class':'abs'}).getText()
    dua = data[3].find('span', attrs={'class': 'abs'}).getText()
    # Remove decimal point
    satu = satu.replace('.','')
    dua = dua.replace('.','')
    # Cast Data Type Integer
    satu = int(satu)
    dua = int(dua)
    if provinsi in wilayah_tinggi:
        jokowi[0] +=satu
        prabowo[0] +=dua
    else:
        jokowi[1]+=satu
        prabowo[1]+=dua

# math percentage
total = sum(jokowi) + sum (prabowo)
satu_tinggi = jokowi[0] / total * 100
jokowi[0] = satu_tinggi
satu_rendah = jokowi[1] / total *100
jokowi[1] = satu_rendah
dua_tinggi= prabowo[0] / total * 100
prabowo[0] = dua_tinggi
dua_rendah = prabowo[1] / total * 100
prabowo[1] = dua_rendah

# Convert to numpy

np_jokowi= np.array(jokowi)
np_prabowo= np.array(prabowo)
# plot data
fig,ax = plt.subplots(figsize=(10,5))
# print(ax)
pos = list(range(len(np_jokowi)))
width = 0.25

rects1 = ax.bar(pos,np_jokowi,width,color='red',label='Jokowi 2019')
rects2 = ax.bar([p + width for p in pos],np_prabowo,width,color='blue',label='Prabowo 2019')
# ax.set_xticks(ind)
ax.set_xticks([p + 0.5 * width for p in pos])
ax.set_xticklabels(['High IPM','Low IPM'])
# # Naming label
plt.xlabel('Index IPM')
plt.ylabel('Vote Percentage')

func.setPlotText(np.round(np_jokowi,2), x=0, y=0.6, val='%', halign='center')
func.setPlotText(np.round(np_prabowo,2), x=width, y=0.6, val='%', halign='center')
# # styling x,y value
plt.yticks(np.arange(np_jokowi.min(),np_jokowi.max(),4000000))
plt.legend(loc='upper right')
plt.yscale('linear')
plt.show()