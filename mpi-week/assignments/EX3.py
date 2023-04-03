from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

data = None

if rank == 0:
    data = int(input("Enter an integer value: "))
    print(f"Process {rank} sending data {data}")
    comm.send(data, dest=(rank + 1) % size)
else:
    data = comm.recv(source=(rank - 1) % size)
    print(f"Process {rank} received data {data}")
    data += rank
    if rank == size - 1:
        print(f"Final result: {data}")
    else:
        print(f"Process {rank} sending data {data}")
        comm.send(data, dest=(rank + 1) % size)
