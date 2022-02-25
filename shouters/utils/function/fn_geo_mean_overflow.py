import numpy as np


def cal(iterable):
  a = np.log(iterable)
  return np.exp(a.mean())