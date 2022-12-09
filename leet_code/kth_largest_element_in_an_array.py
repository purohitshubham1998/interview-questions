import heapq
def kth_largest_element(k, array):
    heapq.heapify(array)
    result = heapq.nlargest(k, array)
    return result[k-1]

array = [3,2,1,5,6,4]
k = 2
kth_largest_element(k, array)
