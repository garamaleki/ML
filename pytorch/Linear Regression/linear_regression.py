# -*- coding: utf-8 -*-
"""Linear Regression.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Dj7vq39UrcVDL8cgXjAF3Vo92v5ZsrGQ
"""

import torch
import torch.nn as nn
import numpy as np
import matplotlib.pyplot as plt

X = torch.randn(100, 1) * 2
Y = X + torch.randn(100, 1) * 3
plt.plot(X.numpy(), Y.numpy(), 'o')

class Regression(nn.Module):
  def __init__(self):
    super(Regression, self).__init__()
    self.linear = nn.Linear(in_features=1, out_features=1)
    
  def forward(self, input):
    y = self.linear(input)
    return y

model = Regression()
criterion = nn.MSELoss()
optimizer = torch.optim.SGD(model.parameters(), lr=0.02)
epochs = 100
for i in range(epochs):
  y = model.forward(X)
  loss = criterion(y, Y)
  print(i, loss.item())
  optimizer.zero_grad()
  loss.backward()
  optimizer.step()

a, b = map(float, list(model.parameters())) 
plt.plot(X.numpy(), Y.numpy(), 'o')
def plot_line(a, b):
  x = np.array([min(X) - 1, max(X) + 1])
  y = a * x + b
  plt.plot(x, y, 'r')
plot_line(a, b)
print("{}x + {}".format(a, b))