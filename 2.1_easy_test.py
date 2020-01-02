import torch

# print(torch.__version__)

N, D = 3, 4
x = torch.tensor(torch.rand(N, D))
y = torch.tensor(torch.rand(N, D))
z = torch.tensor(torch.rand(N, D))

a = x*y
b = a+z
c = torch.sum(b)

print(c)
