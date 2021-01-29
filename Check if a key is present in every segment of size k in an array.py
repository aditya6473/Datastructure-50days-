#!/usr/bin/env python
# coding: utf-8

# In[1]:


def findxinkindowSize(arr, x, k, n) : 

	i = 0
	while i < n : 

		j = 0
		

		while j < k : 
			
			if arr[i + j] == x : 
				break
			
			j += 1

		 
		if j == k : 
			return False

		i += k 

	if i == n : 
		return True

	j = i - k 
	

	while j < n : 
		if arr[j] == x : 
			break

		j += 1

	if j == n : 
		return False

	return True

if __name__ == "__main__" : 

	arr = [ 3, 5, 2, 4, 9, 3, 
			1, 7, 3, 11, 12, 3 ] 
	x, k = 3, 3
	n = len(arr) 
	
	if (findxinkindowSize(arr, x, k, n)) : 
		print("Yes") 
	else : 
		print("No") 
		


# In[ ]:




