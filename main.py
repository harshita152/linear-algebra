from matrix import(
    add,
    sub,
    scaler_multiple,
    multiplication,
    transpose,
    identity
) 
mat=[[0,0], 
    [0,0] ]
mat[0][0]= int(input('enter a number: '))
mat[0][1]= int(input('enter a number: '))
mat[1][1]= int(input('enter a number: '))
mat[1][0]= int(input('enter a number: '))
mat1=[[0,0], 
    [0,0] ]
mat1[0][0]= int(input('enter a number: '))
mat1[0][1]= int(input('enter a number: '))
mat1[1][1]= int(input('enter a number: '))
mat1[1][0]= int(input('enter a number: '))
print("Addition")
print(add(mat,mat1))

print("Subtraction")
print(sub(mat,mat1))

print("scaler_multiply")
print(scaler_multiple(mat,6))

print("Multiply")
print(multiplication(mat,mat1))

print("Transpose")
print(transpose(mat))

print("Identity")
print(identity(3))
