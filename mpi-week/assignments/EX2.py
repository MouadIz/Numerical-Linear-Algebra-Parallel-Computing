from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

while True:
    if rank == 0:
        value = int(input("Enter an integer value: "))
    else:
        value = None

    value = comm.bcast(value, root=0)

    if value < 0:
        break

    print(f"Process {rank} got {value}")

MPI.Finalize()
