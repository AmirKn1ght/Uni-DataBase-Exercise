def Quick(A,Low,High):
    pi = partition(A,Low,High)
    Quick(A,Low,pi-1)
    Quick(A,pi+1,High)
def partition(A,Low,High):
    pi = A[High]
    i = Low-1
    for i in range(Low,High):
        if A[j] < pivot :
            i += 1
            A[i],A[j] = A[j],A[i]
    A[i+1],A[High] = A[High],A[i+1]
    return i+1
