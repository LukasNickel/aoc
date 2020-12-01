import numpy as np


def main():
    data = np.genfromtxt('input', dtype='int')
    matrix = np.tile(data, (len(data), 1))
    print(matrix.shape)
    matrix += data[:, np.newaxis]

    position = np.argwhere(matrix == 2020)
    assert (position[0] == position[1][::-1]).all()

    n1 = data[position[0][0]]
    n2 = data[position[0][1]]

    assert (n1 + n2 == 2020)
    solution = n1*n2
    print(solution)

    matrix = np.tile(data, (len(data), len(data), 1))
    matrix += data[:, np.newaxis, np.newaxis]
    matrix += data[np.newaxis, :, np.newaxis]

    position = np.argwhere(matrix == 2020)
    assert position.shape == (6, 3)

    n1 = data[position[0][0]]
    n2 = data[position[0][1]]
    n3 = data[position[0][2]]
    assert n1 + n2 + n3 == 2020
    solution = n1 * n2 * n3
    print(solution)


if __name__ == '__main__':
    main()
