#barang
mie     = int(input("Jumlah mie instan      : "))
telur   = int(input("Jumlah telur           : "))
minuman = int(input("Jumlah minuman botol   : "))
minyak  = int(input("Jumlah minyak kemasan  : "))
beras   = int(input("Jumlah beras           : "))

#harga
a_mie = 2500*mie
a_telur = 2000*telur
a_minuman = 5500*minuman
a_minyak = 7500*minyak
a_beras = 12000*beras

#perhitungan
belanja = (a_mie+a_telur+a_minuman+a_minyak+a_beras)

#pendiskonan
if belanja > 150000 :
  diskon = belanja*0.2
else:
  diskon = 0

#total harga
Harga = belanja-diskon

#tampilan menu
print ("--------------------------------------------------")
print ("         Toko China Koh AHong             ")
print ("--------------------------------------------------")
print ("No| Nama Produk |   Qty |   Harga   |  Jumlah ")
print ("--------------------------------------------------")
print ("1.| Mie Instan       ",mie,"     Rp2.500 ","","Rp",a_mie)
print ("2.| Telur            ",telur,"     Rp2.000 ","","Rp",a_telur)
print ("3.| Minuman Botol    ",minuman,"     Rp5.500"," ","Rp",a_minuman)
print ("4.| Minyak Kemasan   ",minyak,"     Rp7.500"," ","Rp",a_minyak)
print ("5.| Beras            ",beras,"     Rp12.000","","Rp",a_beras)
print ("")
print ("--------------------------------------------------")
print ("Total Belanja : Rp",belanja)
print ("Diskon        : Rp",diskon)
print ("--------------------------------------------------")
print ("")
print ("Total harga : Rp",Harga)
bayar = int(input("Bayar : Rp"))
while bayar < Harga:
    print("Uang anda kurang'")
    bayar = int(input("Bayar : Rp"))
print (f"Kembalian : Rp{bayar-Harga}")
print ("")
print (" Terima kasih, dan telah belanja di toko kami ")
