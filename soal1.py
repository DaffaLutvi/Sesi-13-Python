import pandas as pd

data = pd.read_excel("sesi_13/data_penjualan.xlsx")

first_five_rows = data.head(5)

output_file = 'sesi_13/5_baris_pertama.xlsx'
first_five_rows.to_excel(output_file, index=False)

print(f"Data Berhasil disimpan ke dalam file {output_file}")