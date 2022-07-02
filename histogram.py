# program of : hergonomy of three given softwares
# author      ZERGAOUI MOHAMED EL AMINE
# version     1.0
# date         29/03/2022



import matplotlib.pyplot as plt

def hergonomie(s):

 print("******  "+s+"  *******")
 print("interface[1-10]:")
 i = int(input())
 print("facilite d'utulisation[1-10]:")
 c = int (input())
 print("facilité de comprehension[1-10]:")
 f = int(input())

 if (i > 6):
    a = 0.5
 else : a = 0.2
 

 if (c > 5):
    cc = 0.3
 else:
    cc = 0.1

 
 if (f > 6):
    b = 0.4
 else :
    b = 0.2

 e = a * i + b * f + c * cc
 
 print("Hergonomie of : "+s+" is")
 print(e)
 print("\n")
 return e


#call the hergonomie function

php = hergonomie("phpmyadmin");
mg = hergonomie("mongodb");
sql = hergonomie("sqldevlopper");

print("------------------------------")


if (php > mg and php > sql) :print(" PhpMyAdmin is the Best" )
else :
    if (mg > php and mg > sql): print("MongoDb is the Best  ")
    else :
        if (sql > php and sql > mg): print("Sql_Developer is the Best ")


# take the value of hergonomy of each software and print
# it into the Histogram


x=['Phpmyadmin','mongodb','sqldev']
y=[int(php),int(mg),int(sql)]

# plt.hist([x,y],color=['blue','orange'],
#         label=['php','sql'],ec="green",rwidth=0.8)
plt.barh(x,y)

for index,value in enumerate (y):
     plt.text(value,index,str(value))


plt.ylabel("softwares")
plt.title("Hergonomie value")
#plt.xticks(y)

plt.legend(loc='upper right')
plt.show()
