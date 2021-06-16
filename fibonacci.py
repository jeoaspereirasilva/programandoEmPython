x = 1
y = 1
z = x + y
c = 0
n = 1

w = int(input("Informe um número >_"))

while c < w:
	print(n," | ", x , "+" , y , "=" , z )
	y = x
	x = z
	z = x + y
	n+=1
	c+=1
