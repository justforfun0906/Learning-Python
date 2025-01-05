def reverse(L):
    rL = L[::-1]
    for i , subL in enumerate(rL):
        if(type(subL) == list):
            rL[i] = reverse(subL)
    return rL