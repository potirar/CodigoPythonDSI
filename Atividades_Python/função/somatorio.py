def somatorio(x):
   soma = 0
   for i in range(1, x+1):
      soma +=i
   
      if i == x:

         print(f"{i}={soma}")
      else:
      
         print(f"{i}", end="+")

while True:
   num = int(input("Informe uma valor inteiro positivo: "))
   if num > 0:
      somatorio(num)
   else:
      print("Informe um valor positivo")

   op = str(input("Deseja continuar s/n: ")).lower()

   if op == "n":
      break

  


