tuple_1 = ("Faqih", "Niko", "Ageng", "Ikhsan", "adin")
tuple_2 = (23, 42, 12, 53, 64)
tuple_3 = "puri", "putri", "syifa", "anggun"

print(tuple_1)
print(tuple_2)
print(tuple_3)

#membuat tuple yang bernilai kosong
empty_tuple = ()
print("tuple kosong: ", empty_tuple)

#tuple bernilai integer
int_tuple = (4, 6, 8, 10, 12, 14,)
print("Tuple bernilai Integer: ", int_tuple)

#tuple dengan kombinasi tipe data
mixed_tuple = (4, "python", 9.3)
print("Tuple dengan type data yang berbeda: ",mixed_tuple)

#tuple bersarang
nested_tuple = ("python", {4: 5, 6: 2, 8:2}, (5, 3, 5, 6))
print("Tuple bersarang: ", nested_tuple)

print()
print()
print()

#membuat List

identitas = ["Ageng", 19, "Indonesia"]
prodi_1 = ["Informatika",19]
prodi_2 = ["Sistem Operasi",20]
dosen_1 = [32,"Ageng Sumarto"]
dosen_2 = [23,"bae"]

print("Cetak semua data...")
print("--------------------------------------------------")
print("Nama : %s, Usia: %d, Negara: %s" %(identitas[0], identitas[1],identitas[2]))
print("--------------------------------------------------")
print("Cetak Program Studi...")
print("--------------------------------------------------")
print("Program studi 1:\nNama Prodi Pertama:%s,ID:%d\nProgram Studi Kedua:\nNama Prodi Kedua: %s,ID:%s:"%(prodi_1[0],prodi_1[1],prodi_2[0],prodi_2[1]))
print("--------------------------------------------------")
print("Dosen Pengampu...")
print("--------------------------------------------------")
print("Dosen Informatika: %s, ID: %d" % (dosen_1[1], dosen_1[0]))
print("Dosen Sistem Informasi: %s, ID: %d"%(dosen_2[1],dosen_2[0]))
print(type(identitas), type(prodi_1), type(prodi_2),type(dosen_1),type(dosen_2))

print()
print()
print()

list =[1,2,3,4,5]

#forward
print("--------------------------------------------------")
print("firmansyah")
print("--------------------------------------------------")
print(list[1])
print(list[3:1])
print(list[:1])
print(list[1:3])

#backward
print("---------------------------------------------------")
print("firmansyah")
print("---------------------------------------------------")

print(list[-1])
print(list[-3:])
print(list[:-1])
print(list[-3:-1])
