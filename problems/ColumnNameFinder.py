""" This problem was recently asked by Apple:

In many spreadsheet applications, the columns are marked with letters. From the 1st to the 26th column the letters are A to Z. Then starting from the 27th column it uses AA, AB, ..., ZZ, AAA, etc.

Given a number n, find the n-th column name.  """



n=104 # n is the column number that we need to find
count=0
i=0
if(n<=26):
	count=1
while(n>=27):
	count+=1
	n=n-26

dictionary={
	1:"A",
	2:"B",
	3:"C",
	4:"D",
	5:"E",
	6:"F",
	7:"G",
	8:"H",
	9:"I",
	10:"J",
	11:"K",
	12:"L",
	13:"M",
	14:"N",
	15:"O",
	16:"P",
	17:"Q",
	18:"R",
	19:"S",
	20:"T",
	21:"U",
	22:"V",
	23:"W",
	24:"X",
	25:"Y",
	26:"Z"
}

print(dictionary[n]*count)


