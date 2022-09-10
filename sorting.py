"""This code is used to explain the selection sort algorithm."""

def selectionsort(array, size):

	for ind in range(size):
		minimum_index = ind

		"""this for loop works one less than the amount of times the first for loop runs"""

		for k in range(ind + 1, size):
			if array[k] < array[minimum_index]:
				minimum_index = k
		(array[ind], array[minimum_index]) = (array[minimum_index], array[ind])
	print(array)


arr = [8,5,6,2,1,3]
size = len(arr)
selectionsort(arr,size)