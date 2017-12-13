def matAdd(*args): ## Funcion para sumar matrices
    list = [args[x] for x in range(0,len(args))]
    zipped_list = zip(*list)
    result = [sum(item) for item in zipped_list]
    return result

mat1 = [1,2,3]
mat2 = [4,5,6]
mat3 = [7,8,9]

print(matAdd(mat1,mat2,mat3))