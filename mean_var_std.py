import numpy as np

def calculate(list):

  if len(list) != 9:
    raise ValueError("List must contain nine numbers.")

  list2 = np.reshape(list,(3,3))
  mean = [np.mean(list2,axis = 0).tolist(), np.mean(list2,axis = 1).tolist(), np.mean(list2).tolist()]
  
  variance = [np.var(list2,axis = 0).tolist(), np.var(list2,axis = 1).tolist(), np.var(list2)]
  
  standard_deviation = [np.std(list2,axis = 0).tolist(), np.std(list2,axis = 1).tolist(), np.std(list2)]
  
  max = [np.max(list2,axis = 0).tolist(), np.max(list2,axis = 1).tolist(), np.max(list2)]
  
  min = [np.min(list2,axis = 0).tolist(), np.min(list2,axis = 1).tolist(), np.min(list2)]
  
  sum = [np.sum(list2,axis = 0).tolist(), np.sum(list2,axis = 1).tolist(), np.sum(list2)]
  
  dict = {
    'mean': mean,
    'variance': variance,
    'standard deviation': standard_deviation,
    'max': max,
    'min': min,
    'sum': sum
  }

  return dict