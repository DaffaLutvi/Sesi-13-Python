import pandas as pd

data = pd.read_excel('sesi_13/data_penjualan.xlsx')
data_elekronik = data[data['Kategori'] == 'Elektronik'].head()

data_elekronik.to_excel("sesi_13/elektronik_5_baris.xlsx", index= False)

print('File "elektronik_5_baris.xlsx" berhasil dibuat.' )