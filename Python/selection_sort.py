#selection sort in python
A = [102,6,74,50,64,98,47,63,112]
for i in range(len(A)):
	min_idx = i
	for j in range(i+1, len(A)):
		if A[min_idx] > A[j]:
			min_idx = j

	A[i], A[min_idx] = A[min_idx], A[i]


print ("Sorted array")
for i in range(len(A)):
	print("%d" %A[i],end=" ")
