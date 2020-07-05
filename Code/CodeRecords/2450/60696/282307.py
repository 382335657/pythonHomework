res = [-1, -1]


def find(l, r):
    global res
    if l == r:
        if nums[l] == target:
            res[0] = l
    mid = int((l+r)/2)
    if target <= nums[mid]:
        find(l, mid)
    else:
        find(mid+1, r)


def rfind(l, r):
    global res
    if l == r:
        if nums[l] == target:
            res[1] = l
    mid = int((l+r)/2)
    if target < nums[mid]:
        find(l, mid-1)
    else:
        find(mid, r)


if __name__ == '__main__':
    nums = [int(i) for i in input().split(',')]
    target = int(input())
    find(0, len(nums)-1)
    rfind(0, len(nums)-1)
    print(res)