#for loops
#for i in range(1,10):
   #print (i)
list_hari = ("senin","selasa","rabu","kamis")
list_bulan = ("januari","februari","maret","april")

for i in (list_hari):
  for k in (list_bulan):
    print(i, " _ ",k)

#fibonanci
n=10
fib = [0,1]

for i in range(n-2):
  fib_lanjut = fib[i+1] + fib[i]
  print(fib[i+1]," + ",fib[i]," = ",fib_lanjut)
  fib.append(fib_lanjut)
print(fib)
