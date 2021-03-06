### Implementation of Quick Sort algorithm

## Worst case complexity: O(N*N) when we choose the smallest or largest element as pivot
## Best case complexity: O(NlogN) when we choose the middle element as pivot
## Average case complexity: O(NlogN)

## Space complexity: O(1)  (in-place sort) --- advantage over Merge Sort

def partition(arr,low,high):
	i = (low)-1
	pivot = arr[high]

	for j in range(low,high):
		if arr[j] <= pivot:
			i = i+1
			arr[i], arr[j] = arr[j], arr[i]

	arr[i+1], arr[high] = arr[high], arr[i+1]
	return i+1


def quicksort(arr,low,high):

	if low<high:

		pi = partition(arr,low,high)
		quicksort(arr,low,pi-1)
		quicksort(arr,pi+1,high)


arr = [3,2,4,1,5,7,8,6,11,30,0]
n = len(arr)-1
quicksort(arr,0,n)

print arr