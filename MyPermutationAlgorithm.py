"""
18th August, 2021.

Description:
This Permutation Algorithm is written by me.
Given a list of integers, the permutation() function returns 
a list of all possible permutations.
"""



def per(list, n, mainlist=[], templist=[]):
	
	for i in range(n):
		
		if i in templist:
			continue
			
		mainlist.append(list[i])
		templist.append(i)
		print(mainlist)
		
		if i==n-1 and len(mainlist) == len(list):
			mainlist.pop()
			templist.pop()
			return
		
		per(list, n, mainlist, templist)
		
		mainlist.pop()
		templist.pop()
		
def permutation(list):
	n=len(list)
	per(list,n)

list = [1,2,3]
permutation(list)


