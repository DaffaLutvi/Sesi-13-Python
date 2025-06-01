import pandas as pd

data = pd.read_excel("sesi_13/data_penjualan.xlsx").head()

data['Total Harga'] = data['Jumlah'] * data['Harga Satuan']

data.to_excel('sesi_13/5_baris_dengan_total.xlsx', index=False)

print('file 5_baris_dengan_total.xlsx berhasil dibuat')