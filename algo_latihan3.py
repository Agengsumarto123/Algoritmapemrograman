#setting variabel
nim     =input("Masukkan NIM        :")
nama    =input("Masukkan Nama       :")
kelas   =input("Masukkan Kelas      :")
prodi   =input("Masukkan Nama Prodi :")

#setting variabel nilai

bhs_ind = int(input("Nilai Bahasa Indonesia         :"))
bhs_ing = int(input("Nilai Bahasa Inggris           :"))
pd      = int(input("Nilai Bahasa Pemrograman Dasar :"))
mtk     = int(input("Nilai Matematika               :"))
kal1    = int(input("Nilai Kalkulus 1               :"))
os      = int(input("Nilai Operasi sistem           :"))

#perhitungan
rata = (bhs_ind+bhs_ing+pd+mtk+kal1+os)/6

if (bhs_ing > 0 and bhs_ing <=60):
    grade_ing = ("C")
elif (bhs_ing > 60  and bhs_ing <=75):
    grade_ing =("B")
elif (bhs_ing > 75 and bhs_ing <=85):
    grade_ing =("AB")
elif (bhs_ing > 85 and bhs_ing <=100):
    grade_ing =("A")
else:
    grade_ing =(" Grade Anda tidak ditemukan!")
    

if (bhs_ind > 0 and bhs_ind <=60):
    grade_ind = ("C")
elif (bhs_ind > 60  and bhs_ind <=75):
    grade_ind =("B")
elif (bhs_ind > 75 and bhs_ind <=85):
    grade_ind =("AB")
elif (bhs_ind > 85 and bhs_ind <=100):
    grade_ind =("A")
else:
    grade_ind =(" Grade Anda tidak ditemukan!")
    
if (pd > 0 and pd <=60):
    grade_pd = ("C")
elif (pd > 60  and pd <=75):
    grade_pd =("B")
elif (pd > 75 and pd <=85):
    grade_pd =("AB")
elif (pd > 85 and pd <=100):
    grade_pd =("A")
else:
    grade_pd =(" Grade Anda tidak ditemukan!")
    
if (mtk > 0 and mtk <=60):
    grade_mtk = ("C")
elif (mtk > 60  and mtk <=75):
    grade_mtk =("B")
elif (mtk > 75 and mtk <=85):
    grade_mtk =("AB")
elif (rata > 85 and mtk <=100):
    grade_mtk =("A")
else:
    grade_mtk =(" Grade Anda tidak ditemukan!")
    
if (kal1 > 0 and kal1 <=60):
    grade_kal1 = ("C")
elif (kal1 > 60  and kal1 <=75):
    grade_kal1 =("B")
elif (kal1 > 75 and kal1 <=85):
    grade_kal1 =("AB")
elif (kal1 > 85 and kal1 <=100):
    grade_kal1 =("A")
else:
    grade_kal1 =(" Grade Anda tidak ditemukan!")   
    
if (os >0 and os <=60):
    grade_os = ("C")
elif (os > 60  and os <=75):
    grade_os =("B")
elif (os > 75 and os <=85):
    grade_os =("AB")
elif (os > 85 and os <=100):
    grade_os =("A")
else:
    grade_kal1 =(" Grade Anda tidak ditemukan!")   
    
if (rata >0 and rata <=60):
    grade_rata = ("C")
elif (rata > 60  and rata <=75):
    grade_rata =("B")
elif (rata > 75 and rata <=85):
    grade_rata =("AB")
elif (rata > 85 and rata <=100):
    grade_rata =("A")
else:
    grade_rata =(" Grade Anda tidak ditemukan!")
    
    
    
#menampilkan

print ("============================================================")
print ("    Hasil Kartu Hasil Studi ")
print ("============================================================")
print ("NIM anda          :",nim)
print ("nama lengkap anda :",nama)
print ("kelas anda        :",kelas)
print ("progam studi anda :",prodi)

print ("------------------------------------------------------------")
print ("Hasil Kartu Hasil Studi")
print ("------------------------------------------------------------")
print ("1. Bahasa Indonesia  =",bhs_ind,"",grade_ind)
print ("2. Bahasa Inggris    =",bhs_ing,"",grade_ing)
print ("3. Pemrograman Dasar =",pd,"",grade_pd)
print ("4. Matematika        =",mtk,"",grade_mtk)
print ("5. Kalkulus 1        =",kal1,"",grade_kal1)
print ("6. Sistem Operasi    =",os,"",grade_os)
print ("------------------------------------------------------------")
print ("Rata-Rata",rata)
print ("------------------------------------------------------------"
