"""
Given an array with positive number the task to find the largest subsequence from array that contain elements which are Fibonacci numbers.

Input:
The first line of input contains an integer T denoting the no of test cases. Then T test cases follow. Each test case contains an integer N denoting the size of the array. Then in the next line are N space separated values of the array.

Output:
For each test case in a new line print the space separated elements of the  longest fibonacci subsequence.

Constraints:
1<=T<=100
1<=N<=100
1<=A[]<=1000

Example:
Input:
2
7
1 4 3 9 10 13 7
9
0 2 8 5 2 1 4 13 23

Output:
1 3 13
0 2 8 5 2 1 13 
"""
for _ in range(int(input())):
    n = int(input())
    lst = [int(x) for x in input().split()]
    
    fibo = [0, 1]
    temp = max(lst)
    for i in range(2, temp + 1):
        fibo.append(fibo[i - 1] + fibo[i - 2])
    for i in range(n):
        if lst[i] in fibo:
            print(lst[i], end=' ')
    print()
