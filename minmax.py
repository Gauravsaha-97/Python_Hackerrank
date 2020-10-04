# Problem Statement:Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers. Then print the respective minimum and maximum values as a single line of two space-separated long integers.


def min_maxSum(arr):
    sum = 0
    max = 0
    min = 9999999999999999999
    n = len(arr)
    for i in range(n):
        sum+=arr[i]
        min = min(min, arr[i])
        max = max(max, arr[i])

    print(sum-max, sum-min)

    if __name__ == "__main__":
        arr = list(map(int, input().rstrip().split()))
        min_maxSum(arr)



