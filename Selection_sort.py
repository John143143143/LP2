def selection_sort(a):

    for i in range(len(a)-1):
        min_index=i
        for j in range(i,len(a)):
            if a[min_index] > a[j]:
                min_index = j
        #tuple unboxing
        a[min_index],a[i]=a[i],a[min_index]
        # print(a)

a=[7,5,4,9,2,10,3]
print('Unsorted array',a)
selection_sort(a)
print('Sorted array',a)