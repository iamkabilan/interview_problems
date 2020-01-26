"""
Given a list of numbers, for each element find the next element that is larger
 than the current element.
Return the answer as a list of indices. 
If there are no elements larger than the current element, then use -1 instead.
"""
def nearest(n):
	new=[]
	temp=[]
	for i in range(0,len(n)):
		temp=[]
		for j in range(i+1,len(n)):
			if(n[j]>n[i]):
				temp.append(j)
				break
		if(len(temp)==0):
			new.append(-1)
		else:
			new.append(min(temp))
	return new



print(nearest([3,2,5,6,9,8]))
#[2,2,3,4,-1,-1]

