import numpy as np
from Node import Node

def euclidean_dist(a,b,arr):
    # Caluculates the distance between the 2 instances a and b.
    rolling_sum = 0
    inst_a = arr[a-1]
    inst_b = arr[b-1]
    # print(f'a: {inst_a}')
    # print(f'b: {inst_b}')
    for i in range(1, len(inst_a)):
        diff = np.power( inst_a[i] - inst_b[i],2)
        rolling_sum = rolling_sum + diff
    return np.sqrt(rolling_sum)


def read_data(filename):
    # Read the file
    with open(filename, 'r') as file:
        # Read lines and split by whitespace
        lines = file.readlines()
        data = [line.strip().split() for line in lines]

    # Convert data to a numpy array
    matrix = np.array(data, dtype=float)
    return matrix



fileName = 'small_test_dataset.txt'
raw_data = read_data(fileName)

nodes = []
for row in raw_data:
    n = Node(row)
    nodes.append(n)










