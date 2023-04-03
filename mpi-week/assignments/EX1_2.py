from mpi4py import MPI

# Initialize MPI
comm = MPI.COMM_WORLD

# Get the rank of the current process
rank = comm.Get_rank()

# Get the total number of processes
size = comm.Get_size()

# Print the rank and size of each process
print("Hello, World! from process ", rank, "out of", size, "processes")

# Finalize MPI
comm.Barrier()
MPI.Finalize()