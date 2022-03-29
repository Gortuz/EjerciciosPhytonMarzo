A = ["hola","gato","perro","gato","palabra","hola"]
print(A)
for i in range(len(A)-1,-1,i-1):
    if A[i] in A[:i]:
        del A[i]
print(A)
