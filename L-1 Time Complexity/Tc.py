""" 
1. Constant Time — O(1)
Takes the same time no matter input size

arr = [10, 20, 30, 40, 50]
print(arr[2])  # Always one step

Even if list has 5 or 5 lakh elements still fast

2. Linear Time — O(n)
Time increases with number of elements

arr = [10, 20, 30, 40, 50]

for x in arr:
    print(x)

If elements double time also doubles

3. Quadratic Time — O(n²)

Loop inside loop (nested loop)

arr = [1, 2, 3]

for i in arr:
    for j in arr:
        print(i, j)

If n = 3 then, 9 operations
If n = 100 then, 10,000 operations  


4. Cubic Time — O(n³)

Three nested loops

arr = [1, 2, 3]

for i in arr:
    for j in arr:
        for k in arr:
            print(i, j, k)


5. Logarithmic Time — O(log n)

Problem size is reduced by half each step or vice - versa

n = 16

while n > 1:
    print(n)
    n = n // 2   # divide by 2 each time

o/p 16 -> 8 -> 4 -> 2 -> 1
Steps are very few even if number is big
"""