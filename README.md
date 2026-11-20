# 🧮 Pure Python Linear Algebra

[![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Zero Dependencies](https://img.shields.io/badge/dependencies-none-brightgreen.svg)](#)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-orange.svg)](https://github.com/harshita152/linear-algebra/pulls)

A lightweight, zero-dependency Python implementation of foundational matrix operations and linear algebra algorithms built entirely from scratch without external libraries like NumPy.

Designed for educational purposes, algorithm study, and understanding fundamental matrix arithmetic from first principles.

---

## 📌 Features

- **Zero External Dependencies**: Implemented using pure native Python 2D lists (`list[list]`).
- **Matrix Addition & Subtraction**: Element-wise addition and subtraction of matrices.
- **Scalar Multiplication**: Uniform scaling of matrix elements by a constant factor.
- **Matrix Multiplication**: Classic dot-product matrix multiplication ($O(n^3)$ algorithm).
- **Matrix Transpose**: Swapping rows and columns ($A \to A^T$).
- **Identity Matrix Generator**: Dynamic construction of an $n \times n$ identity matrix ($I_n$).
- **Interactive CLI Demo**: Terminal-based test interface for live experimentation.

---

## 📂 Repository Structure

```text
linear-algebra/
├── matrix.py       # Core matrix arithmetic functions
├── main.py         # Interactive command-line test runner
└── README.md       # Project documentation
```

---

## 🚀 Getting Started

### Prerequisites

* Python 3.8 or later (no third-party packages required).

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/harshita152/linear-algebra.git
   cd linear-algebra
   ```

2. **Run the interactive test script:**
   ```bash
   python main.py
   ```

---

## 📖 API Reference & Usage

Import the functions directly into your own Python scripts:

```python
from matrix import add, sub, scaler_multiple, multiplication, transpose, identity
```

### 1. Matrix Addition (`add`)
Performs element-wise addition between two matrices of identical dimensions:
$$C_{i,j} = A_{i,j} + B_{i,j}$$

```python
A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]

result = add(A, B)
# Output: [[6, 8], [10, 12]]
```

### 2. Matrix Subtraction (`sub`)
Computes the difference between two matrices:
$$C_{i,j} = A_{i,j} - B_{i,j}$$

```python
result = sub(B, A)
# Output: [[4, 4], [4, 4]]
```

### 3. Scalar Multiplication (`scaler_multiple`)
Multiplies every element of matrix $A$ by scalar factor $k$:
$$C_{i,j} = k \cdot A_{i,j}$$

```python
A = [[1, 2], [3, 4]]
result = scaler_multiple(A, 3)
# Output: [[3, 6], [9, 12]]
```

### 4. Matrix Multiplication (`multiplication`)
Calculates the matrix product $C = A \times B$ where columns of $A$ equal rows of $B$:
$$C_{i,j} = \sum_{k} A_{i,k} \cdot B_{k,j}$$

```python
A = [[1, 2], [3, 4]]
B = [[2, 0], [1, 2]]

result = multiplication(A, B)
# Output: [[4, 4], [10, 8]]
```

### 5. Matrix Transpose (`transpose`)
Reflects the matrix across its main diagonal, converting rows into columns:
$$(A^T)_{i,j} = A_{j,i}$$

```python
A = [[1, 2], [3, 4]]
result = transpose(A)
# Output: [[1, 3], [2, 4]]
```

### 6. Identity Matrix (`identity`)
Generates an $n \times n$ identity matrix with ones on the main diagonal and zeros elsewhere:

```python
result = identity(3)
# Output:
# [
#   [1, 0, 0],
#   [0, 1, 0],
#   [0, 0, 1]
# ]
```

---

## 🛠️ Interactive Example

Running `python main.py` prompts you to populate two $2 \times 2$ matrices and displays all computations in sequence:

```text
enter a number: 1
enter a number: 2
enter a number: 3
enter a number: 4
enter a number: 5
enter a number: 6
enter a number: 7
enter a number: 8

Addition
[[6, 8], [10, 12]]

Subtraction
[[-4, -4], [-4, -4]]

scaler_multiply
[[6, 12], [18, 24]]

Multiply
[[19, 22], [43, 50]]

Transpose
[[1, 3], [2, 4]]

Identity
[[1, 0, 0], [0, 1, 0], [0, 0, 1]]
```

---

## 🗺️ Roadmap & Planned Enhancements

- [ ] **Dimension & Type Validation**: Gracefully raise `ValueError` on incompatible dimensions.
- [ ] **Determinant Calculation**: Support for $2 \times 2$, $3 \times 3$, and recursive $N \times N$ determinants.
- [ ] **Matrix Inversion**: Inverse calculation via Gauss-Jordan elimination or Adjugate formula.
- [ ] **Object-Oriented API**: Wrap functions in a reusable `Matrix` class with operator overloading (`+`, `-`, `*`).
- [ ] **Unit Tests**: Automated test suite using `unittest` or `pytest`.

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!
1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/MatrixDeterminant`)
3. Commit your Changes (`git commit -m 'feat: add matrix determinant'`)
4. Push to the Branch (`git push origin feature/MatrixDeterminant`)
5. Open a Pull Request

---

## 📄 License

Distributed under the **MIT License**. See `LICENSE` for more information.
