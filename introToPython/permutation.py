def permute(nums):
    if(len(nums) == 1):
        return [nums]
    perm = []
    for i in nums:
        sub_perm = permute([j for j in nums if j != i])
        for j in sub_perm:
            perm.append([i] + j)
    return perm