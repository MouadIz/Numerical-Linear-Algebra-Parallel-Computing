from mpi4py import MPI
import numpy as np

N = 840

# initialize MPI
comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

# compute range of i for this process
start = rank * N // size
end = (rank + 1) * N // size

# compute local sum
sum_local = 0.0
for i in range(start, end):
    x = (i + 0.5) / N
    sum_local += 4.0 / (1.0 + x**2)

# reduce local sum to get global sum
sum_global = comm.reduce(sum_local, op=MPI.SUM, root=0)

# compute and print pi on root process
if rank == 0:
    pi = sum_global / N
    print(f"pi = {pi}")
