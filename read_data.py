#open file
data = open("data.txt", "r")
print("Nama File", data.name)

#read
file_konten = data.read(100)
print("Isi data :", file_konten[17:39])

#closed
data.close()
