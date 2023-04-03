from mpi4py import MPI

# Initialize MPI
comm = MPI.COMM_WORLD

# Get the rank of the current process
rank = comm.Get_rank()

# Get the total number of processes
size = comm.Get_size()

# Print the message only from process 0
if rank == 0:
    print(f"Hello, World! I'm {rank} the  controller process.")

# Finalize MPI
comm.Barrier()
MPI.Finalize()
