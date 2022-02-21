a = input('a ni kiriting:')
b = input('b ni kiriting:')
c = input('c  ni kiriting:')
a = float(a)
b = float(b)
c = float(c)
discriminant = b**2 - 4*a*c
print('Diskerminant= ' + str(discriminant))
if discriminant < 0:
   print('Ildizda manfiy son yuzaga keldi')
elif discriminant == 0:
   x = -b / (2 * a)
   print('x = ' + str(x))
else:
   x1 = (-b + discriminant ** 0.5) / (2 * a)
   x2 = (-b - discriminant ** 0.5) / (2 * a)
   print('x₁ = ' + str(x1))
   print('x₂ = ' + str(x2))
	
	