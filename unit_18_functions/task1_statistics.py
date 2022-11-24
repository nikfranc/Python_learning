def mean(arr):
    return sum(arr)/len(arr)


def median(arr):
    arr.sort()
    if len(arr) % 2 == 0:
        return (arr[int(len(arr)/2)] + arr[int(len(arr)/2 - 1)])/2
    else:
        return arr[int(len(arr)/2)]


def print_statistics(arr):
    if arr:
        print(len(arr))
        print(mean(arr))
        print(max(arr))
        print(min(arr))
        print(median(arr))
    else:
        for _ in range(6):
            print('0')


print_statistics([])
