import heapq

arr = [1,2,3,4,5]

heapq.heapify(arr)

while arr:
    print(heapq.heappop(arr))
