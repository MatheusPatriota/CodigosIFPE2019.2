
x = float(input("Digite o valor de x: "))
y = float(input("Digite o valor de y: "))
temp1 = 2
temp2 = 3
s = round(x*y,2)

if (x > 0 and x < 1) and (y > 0 and y < 1):
  while True:
    if round(s,3) < 0.001:
      break
    else:
      a = (x**temp1 *  y**temp2)/(x+y)**temp1*temp2
      temp1 += 1
      temp2 += 2
      b = (x**temp1 *  y**temp2)/(x+y)**temp1*temp2
      s -= a
      s += b
      temp1 += 1
      temp2 += 2

    print ("o resultado de S é {:}".format(s))

