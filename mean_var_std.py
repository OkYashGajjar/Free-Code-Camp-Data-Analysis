import numpy as np

def calculate(input_list):
    if len(input_list) != 9 :
        raise ValueError('List must contain 9 numbers')

    unshaped_matrix = np.array(input_list)
    matrix = unshaped_matrix.reshape(3,3)

    #Computing columns axis=0
    axis0 = {
        'mean' : np.mean(matrix, axis=0).tolist(),
        'variance' : np.var(matrix, axis=0).tolist(),
        'standard deviation' : np.std(matrix, axis=0).tolist(),
        'max' : np.max(matrix, axis=0).tolist(),
        'min' : np.min(matrix, axis=0).tolist(),
        'sum' : np.sum(matrix, axis=0).tolist()
    }

    #Computing rows axis =1
    axis1 = {
        'mean' : np.mean(matrix, axis=1).tolist(),
        'variance' : np.var(matrix, axis=1 ).tolist(),
        'standard deviation' : np.std(matrix, axis=1 ).tolist(),
        'max' : np.max(matrix, axis=1).tolist(),
        'min' : np.min(matrix, axis=1).tolist(),
        'sum' : np.sum(matrix, axis=1).tolist()
    }

    #Compute for the flattened(whole) matrix (without axis)
    flattened ={
        'mean' : np.mean(matrix).item(),
        'variance' : np.var(matrix).item(),
        'standard deviation' : np.std(matrix).item(),
        'max' : np.max(matrix).item(),
        'min' : np.min(matrix).item(),
        'sum' : np.sum(matrix).item()
    }

    #Calculations
    calculation = {
        'mean' : [axis0['mean'], axis1['mean'], flattened['mean']],
        'variance' : [axis0['variance'], axis1['variance'], flattened['variance']],
        'standard deviation' : [axis0['standard deviation'], axis1['standard deviation'], flattened['standard deviation']],
        'max' : [axis0['max'], axis1['max'], flattened['max']],
        'min' : [axis0['min'], axis1['min'], flattened['min']],
        'sum' : [axis0['sum'], axis1['sum'], flattened['sum']]
    }

    return calculation