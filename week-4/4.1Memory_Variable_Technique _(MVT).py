class MemoryVariableTechnique:
    def __init__(self, partitions):
        self.partitions = partitions  # Dictionary of partition sizes
        self.memory_map = {key: [False] * size for key, size in partitions.items()}
        self.processes = {}  # Dictionary to track allocated processes and their sizes

    def allocate_memory(self, process_id, size):
        # Find the smallest partition that can fit the process
        suitable_partition = None
        min_waste = float('inf')
        
        for partition_id, partition_size in self.partitions.items():
            if size <= partition_size:
                # Check if the partition can fit the process
                free_space = self.memory_map[partition_id]
                # Find the smallest contiguous block of free space that fits the size
                start = -1
                for i in range(len(free_space) - size + 1):
                    if all(not free_space[j] for j in range(i, i + size)):
                        waste = partition_size - (i + size)
                        if waste < min_waste:
                            min_waste = waste
                            suitable_partition = partition_id
                            start = i

        if suitable_partition is not None:
            # Allocate the memory
            for i in range(start, start + size):
                self.memory_map[suitable_partition][i] = True
            self.processes[process_id] = (suitable_partition, size)
            print(f"Process {process_id} allocated {size} KB to Partition {suitable_partition}")
        else:
            print(f"Failed to allocate memory for Process {process_id}: Not enough space available")

    def deallocate_memory(self, process_id):
        if process_id in self.processes:
            partition_id, size = self.processes[process_id]
            free_space = self.memory_map[partition_id]
            
            # Deallocate the memory
            for i in range(len(free_space)):
                if all(free_space[j] for j in range(i, i + size)):
                    for j in range(i, i + size):
                        free_space[j] = False
                    break
            
            del self.processes[process_id]
            print(f"Process {process_id} deallocated from Partition {partition_id}")
        else:
            print(f"Process {process_id} not found")

    def display_memory_status(self):
        for partition_id, partition_size in self.partitions.items():
            used_space = sum(self.memory_map[partition_id])
            free_space = partition_size - used_space
            print(f"Partition {partition_id}: {used_space} KB used, {free_space} KB free")
            print(f"Memory map: {self.memory_map[partition_id]}")
        print(f"Currently allocated processes: {self.processes}")

# Driver Code
mvt = MemoryVariableTechnique({1: 300, 2: 500, 3: 200})

mvt.allocate_memory(1, 150) 
mvt.allocate_memory(2, 400) 
mvt.allocate_memory(3, 100) 
mvt.display_memory_status()

mvt.deallocate_memory(2) 
print("\nAfter deallocating Process 2:")
mvt.display_memory_status()
