from mpi4py import MPI

# Initialize MPI
comm = MPI.COMM_WORLD
# Get the rank of the current process
rank = comm.Get_rank()

# Print "Hello, World!" from each process
print("Hello, World! from process ", rank)

# Finalize MPI
comm.Barrier()
MPI.Finalize()