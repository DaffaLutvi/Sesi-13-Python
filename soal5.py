import pandas as pd 

file_path = "sesi_13/5_baris_dengan_total.xlsx"
xls = pd.ExcelFile(file_path)
df = xls.parse('Sheet1')

df_sorted = df.sort_values(by='Total Harga', ascending=False)

output_path = "sesi_13/penjualan_terurut.xlsx"
df_sorted.to_excel(output_path, index= False)

print(f"File berhasil disimpan sebagai: {output_path}")