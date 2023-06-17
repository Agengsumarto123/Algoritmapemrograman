#setting variabel nilai 

 a = p = int(input("Masukkan nilai a/p: ")) 

 b = l = int(input("Masukkan nilai b/l: ")) 

 c = t = int(input("Masukkan nilai c/t: ")) 

  

 #perhitungan 1 

 hitung1 = ((a+b)*(b*c))/(a+b+c) 

 hitung2 = a*b*c 

 hitung3 = 1/2*a*t 

 hitung4 = ((a+b)**2+(b*c)**2)/(a*b) 

  

 #menampilkan 

 print ("-------------------------") 

 print ("Nilai a/p :",a) 

 print ("Nilai b/l :",b) 

 print ("Nilai c/t :",t) 

 print ("-------------------------") 

 print ("") 

 print ("A. ((a+b)x(b.c))/(a+b+c) = ...") 

 print(f"   = ((({a}+{b})*({b}*{c}))/({a}+{b}+{c}))") 

 print(f"   = ({a+b})*({b*c}) / ({a+b+c})") 

 print("   =", hitung1) 

 print("") 

 print ("B. P x L x T = ...") 

 print (f"  = {p}*{l}*{t}") 

 print ("  = ",hitung2) 

 print ("") 

 print ("C. 1/2 x a.t= ...") 

 print (f"  = 1/2*{a}*{t}") 

 print ("  = ",hitung3) 

 print ("") 

 print("D. ((a+b)^2+(b.c)^2)/(a.b) = ...") 

 print(f"  = (({a}+{b})**2+({b}*{c})**2)/({a}*{b})") 

 print(f"  = (({(a+b)**2})+({(b*c)**2})/({a*b})") 

 print("  = ", hitung4)
