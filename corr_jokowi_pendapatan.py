import numpy as np
import matplotlib.pyplot as plt
import function as func
from sklearn.linear_model import LinearRegression

soup = func.crawlData('https://kawalpemilu.org/#0')
# find results within table
results = soup.find('table',{'class':'table'})
rows = results.find_all('tr',{'class':'row'})
array = []
jokowi = []
prabowo = []
total = []
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
    if wilayah!= 'KALIMANTAN UTARA' and wilayah!= 'Luar Negeri':
        satu = data[2].find('span', attrs={'class':'abs'}).getText()
        dua = data[3].find('span', attrs={'class': 'abs'}).getText()
        # Remove decimal point
        satu = satu.replace('.','')
        dua = dua.replace('.','')
        # Cast Data Type Integer
        satu = int(satu)
        dua = int(dua)
        array.append(wilayah)
        sum = satu + dua
        total.append([sum])
        persen_satu = round(satu*100 / sum,2)
        persen_dua= round(dua*100 / sum,2)
        prabowo.append([persen_dua])
        jokowi.append([persen_satu])

# Convert to numpy
np_array = np.array(array)
np_jokowi= np.array(jokowi)
np_prabowo= np.array(prabowo)
np_total= np.array(total)
print(len(jokowi))
soup = func.crawlData('https://www.bps.go.id/statictable/2019/03/06/2049/rata-rata-upah-gaji-bersih-sebulan-buruh-karyawan-pegawai-menurut-provinsi-dan-lapangan-pekerjaan-utama-di-17-sektor-rupiah-2018.html')
# find results within table
results = soup.find('table',{'class':'xl7325477'})
rows = results.find_all('tr',{'class':'xl7925477'})
wilayah2 = []
pendapatan = []
for r in rows:
    # find all columns per result
    data = r.find_all('td')
    # check that columns have data
    if len(data) == 0:
        continue
    provinsi = data[0].getText()
    provinsi = provinsi.replace('\n', '')
    if provinsi != 'Kalimantan  Utara':
        # write columns to variables
        total = data[-1].getText()
        # Remove white space
        total = total.replace(' ','')
        # Cast Data Type Integer
        total = int(total)
        wilayah2.append([provinsi])
        # Cast Uppercase to Wilayah
        pendapatan.append([total])

np_pendapatan = np.array(pendapatan)
# analisis regresi linier
func.do_regress(np_pendapatan,np_jokowi,xlabel="Tingkat Pendapatan",ylabel="Persentase Suara Jokowi Per Provinsi")
func.do_regress(np_pendapatan,np_prabowo,xlabel="Tingkat Pendapatan",ylabel="Persentase Suara Prabowo Per Provinsi")