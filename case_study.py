def simple_sort(arr):
    n = len(arr) #Sets n to length of the given array
    for i in range(n): #itterates through the arary a total of n times (n = length of array)
        for j in range(0, n-i-1): # each itteration compares each number to its neighbors 
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j] #switch the two number if one is larger than the other (moves biggest number to the end of the array)
    print(arr)

#this algorithm has a time complexiy of O(n^2) {The best case scenerio is O(n) if the array is already sorted}
#this is not the best way nor the most efficient way to sort an array because itteratting through the array multiple times is not efficient

simple_sort([1,5,3,7,2,6,3])
