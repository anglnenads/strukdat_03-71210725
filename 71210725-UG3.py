kalimat = input("Masukkan sebuah kalimat : ")
kata = input("Masukkan sebuah kata yang ingin dicari : ")

count = 0
y = kalimat.lower()
cari = y.split()

for i in cari:
    if i == kata:
        count = count + 1

print("Jumlah kata :",  count)