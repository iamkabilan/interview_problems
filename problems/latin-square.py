t=int(input())

diagonal=[]
row=[]
column=[]

for i in range(t):
	n=int(input())

	mat=[]
	for j in range(n):
		temp=[]
		for k in range(n):
			a=int(input())
			print('\t')
			temp.append(a)
		mat.append(temp)


	dia=[]
	for j in range(n):
		k=mat[j][j]
		dia.append(k)
	#print(sum(dia))

	r=0
	for j in range(len(mat)):
		count=0

		my_list=mat[j]
		for i in my_list:
			
			for k in my_list:
				
				if(i==k):
					count=count+1
					
				else:
					pass
		if(count>=5):
			r=r+1
		else:
			pass
	#print(r)

	c=0
	#print(mat)
	for j in range(n):
		count=0

		my_list=[]
		for f in range(n):
			temp=mat[f][j]
			my_list.append(temp)
		#print(my_list)


	c=0
	for j in range(len(mat)):
		new_c=[]

		for i in range(len(mat)):
			temp=[]
			for k in range(len(mat)):
				p=mat[k][i]
				temp.append(p)
			new_c.append(temp)
	#print(new_c)

	for j in range(len(new_c)):
		count=0

		my_list=new_c[j]
		for i in my_list:
			
			for k in my_list:
				
				if(i==k):
					count=count+1
					
				else:
					pass
		if(count>=5):
			c=c+1
		else:
			pass

	diagonal.append(sum(dia))
	row.append(r)
	column.append(c)


#Display

for i in range(t):
	print("Case #{}: ".format(i),str(diagonal[i])+' '+str(row[i])+' '+str(column[i]))