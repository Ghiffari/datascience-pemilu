import numpy as np
import matplotlib.pyplot as plt
import function as func

soup = func.crawlData('https://kawalpemilu.org/#0')
# find results within table
results = soup.find('table',{'class':'table'})
rows = results.find_all('tr',{'class':'row'})
array = []
jokowi = [0,0]
prabowo = [0,0]
jawa = ['DKI JAKARTA','JAWA BARAT','JAWA TENGAH','DAERAH ISTIMEWA YOGYAKARTA','JAWA TIMUR','BANTEN']

# print(rows)
for r in rows:
    # find all columns per result
    data = r.find_all('td')
    # check that columns have data
    if len(data) == 0:
        continue
    # write columns to variables
    wilayah = data[1].find('a').getText()
    if wilayah != 'KALIMANTAN UTARA' :
        satu = data[2].find('span', attrs={'class':'abs'}).getText()
        dua = data[3].find('span', attrs={'class': 'abs'}).getText()
        # Remove decimal point
        satu = satu.replace('.','')
        dua = dua.replace('.','')
        # Cast Data Type Integer
        satu = int(satu)
        dua = int(dua)
        array.append(wilayah)
        if wilayah in jawa:
            jokowi[0] +=satu
            prabowo[0] +=dua
        else:
            jokowi[1]+=satu
            prabowo[1]+=dua

# math percentage
total = sum(jokowi) + sum (prabowo)
satu_jawa = jokowi[0] / total * 100
jokowi[0] = satu_jawa
satu_nonjawa = jokowi[1] / total *100
jokowi[1] = satu_nonjawa
dua_jawa = prabowo[0] / total * 100
prabowo[0] = dua_jawa
dua_nonjawa = prabowo[1] / total * 100
prabowo[1] = dua_nonjawa

# Convert to numpy
np_array = np.array(array)
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
ax.set_xticklabels(['Jawa','Non Jawa'])
# # Naming label
plt.xlabel('provinsi')
plt.ylabel('perolehan suara')

func.setPlotText(np.round(np_jokowi,2), x=0, y=0.6, val='%', halign='center')
func.setPlotText(np.round(np_prabowo,2), x=width, y=0.6, val='%', halign='center')
# # styling x,y value
plt.yticks(np.arange(np_jokowi.min(),np_jokowi.max(),4000000))
plt.legend(loc='upper right')
plt.yscale('linear')
plt.show()

