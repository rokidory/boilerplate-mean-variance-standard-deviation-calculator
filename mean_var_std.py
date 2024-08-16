import numpy as np

def calculate(list):
    if len(list) < 9:
        raise ValueError("List must contain nine numbers.")
    data = np.array(list)
    data.shape = (3, 3)

    mean_0 = data.mean(axis=0).tolist()
    mean_1 = data.mean(axis=1).tolist()
    mean_all = data.mean().tolist()

    var_0 = data.var(axis=0).tolist()
    var_1 = data.var(axis=1).tolist()
    var_all = data.var().tolist()

    std_0 = data.std(axis=0).tolist()
    std_1 = data.std(axis=1).tolist()
    std_all = data.std().tolist()

    max_0 = data.max(axis=0).tolist()
    max_1 = data.max(axis=1).tolist()
    max_all = data.max().tolist()

    min_0 = data.min(axis=0).tolist()
    min_1 = data.min(axis=1).tolist()
    min_all = data.min().tolist()

    sum_0 = data.sum(axis=0).tolist()
    sum_1 = data.sum(axis=1).tolist()
    sum_all = data.sum().tolist()

    calculations = {
        'mean': [mean_0, mean_1, mean_all],
        'variance': [var_0, var_1, var_all],
        'standard deviation': [std_0, std_1, std_all],
        'max': [max_0, max_1, max_all],
        'min': [min_0, min_1, min_all],
        'sum': [sum_0, sum_1, sum_all]
    }

    return calculations
