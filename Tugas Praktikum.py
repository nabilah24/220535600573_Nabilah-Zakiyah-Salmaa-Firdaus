# Himpunan bilangan asli kurang dari 10 yang merupakan kelipatan 3 atau 5 adalah 3,5,6,9. Jumlah seluruh bilangan tersebut adalah 23. Hitung jumlah seluruh bilangan asli yang merupakan kelipatan 3 atau 5 dan kurang 1100
# Nabilah Zakiyah Salmaa Firdaus
# 220535600573
# Teknik Informatika C

Jumlah_seluruh_bilangan_asli = 0
for i in range(1000):
    if (i%3 == 0 or i%5 == 0):
        Jumlah_seluruh_bilangan_asli = Jumlah_seluruh_bilangan_asli + i

print ("Jumlah seluruh bilangan asli yang merupakan kelipatan 3 atau 5 kurang dari 1000 =", Jumlah_seluruh_bilangan_asli)
