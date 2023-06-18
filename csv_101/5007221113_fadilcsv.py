#MUHAMMAD FADHIL NURFAIDZI
#5007221113
import csv

print('------------------------------------------------------------')       
print('        x          y          dydx          ddydxx          ')
print('------------------------------------------------------------')

x = 0
x_div = 40
dx = 0.5


#field = ["x", "y", "dydx", "d2ydx2"]
filecsv='5007221113_kode2222.csv'
with open('/5007221113_kode2222.csv', 'w', newline='') as f:
    name = ["x", "y", "dydx", "d2ydx2"]
    writer = csv.writer(f)
    writer.writerow(name)
    while x <= 20:
        y = 1/4*x**4-2/3*x**3+2*x-5
        dydx = x**3-2*x**2+8*x+2
        d2ydx2 = 3*x**2-4*x+8
        result= [x,y,dydx,d2ydx2] 

        print('%10.1f %10.1f %10.1f %10.1f' %(x, y, dydx, d2ydx2))

        #field= zip(name, result)
        writer.writerows([result])
        #print('data disimpan di',filecsv)
        x = x + dx
      
print('------------------------------------------------------------')