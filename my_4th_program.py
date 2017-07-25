import csv
with open("2.csv","rb") as f:
   data=csv.reader(f)
   for i in data:
       print i
       for j in i:
           print j

    

   
