def BFS(graph,start):
    queue[start]
    visited[start]
    while queue :
        vertex=queue.pop(0)
        for ne in graph[vertex]:
            if ne not in visited:
                visited.add(ne)
                queue.append(ne)
        return visited

def DFS(graph,start,visited):
    visited[start]=True
    for ne in graph[start]:
        if not visited[ne]:
            DFS(graph,ne,visited)

def sort1(A):
    B=[]=len(A)
    for i in range(len(A)):
        min=A[0]
        for A in range(1,len(A)):
            if A[1]<min:
                min=A[i]
                k=j
        B[i] = min
        A[k] = flout('inf')
        return B

def bubble(A):
    for i in range(len(A)-1):
        for j in range(len(A)-1):
            if A[j]>A[j+1]:
                A[j],A[j+1]=A[j+1],A[j]
 
def selection(A):
    for i in range(len(A)-1):
        min=A[i]
        k=1
        for i ing range(i+1,len(A)):
            if min > A[j]:
            min=A[j]
            k=j
        A[i],A[k]=A[k],A[i]
