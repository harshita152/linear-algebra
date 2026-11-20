def add(A,B):
  result = []

  for i in range(len(A)):
    row = []

    for j in range(len(A[0])):
      row.append(A[i][j] + B[i][j])

    result.append(row)

  return result


def sub(A,B):
  result = []

  for i in range(len(A)):
    row = []

    for j in range(len(A[0])):
      row.append(A[i][j] - B[i][j])

    result.append(row)

  return result

def scaler_multiple(A,Number):
  result = []

  for i in range(len(A)):
    row = []

    for j in range(len(A[0])):
      row.append(A[i][j] * Number)

    result.append(row)

  return result

def multiplication(A,B):
  result = []

  for i in range(len(A)):
    row = []

    for j in range(len(B[0])):
      total = 0

      for k in range(len(B)):
        total = A[i][k]* B[k][j]

      row.append(total)

    result.append(row)

  return result

def transpose(A):
  result = []

  for j in range(len(A)):
    row = []

    for i in range(len(A)):
      row.append(A[i][j])

    result.append(row)

  return result

def identity(n):
  result = []

  for i in range(n):
    row = []

    for j in range(n):

      if i == j:
        row.append(1)
      else:
        row.append(0)

    result.append(row)

  return result