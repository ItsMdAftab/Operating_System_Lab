import random

class DiskBlock:
    def __init__(self, block_id):
        self.block_id = block_id
        self.next_block = None

class MediaFile:
    def __init__(self, file_name, file_type, size):
        self.file_name = file_name
        self.file_type = file_type
        self.size = size
        self.start_block = None  # Points to the first block in the chain

    def __str__(self):
        return f"{self.file_name} ({self.file_type}), Size: {self.size} MB"

class FileAllocationTable:
    def __init__(self):
        self.fat = {}  # Maps file name to its starting block

    def allocate_blocks(self, media_file, disk_blocks, block_size):
        num_blocks = (media_file.size + block_size - 1) // block_size  # Calculate the number of blocks needed
        allocated_blocks = []

        for _ in range(num_blocks):
            block = random.choice(disk_blocks)
            if block.next_block is None:  # Find a block that is not yet allocated
                allocated_blocks.append(block)
                disk_blocks.remove(block)
            if len(allocated_blocks) > 0:
                allocated_blocks[-1].next_block = block if len(allocated_blocks) < num_blocks - 1 else None

        if allocated_blocks:
            media_file.start_block = allocated_blocks[0]  # Set the start block of the media file
            self.fat[media_file.file_name] = media_file.start_block

    def delete_file(self, media_file, disk_blocks):
        start_block = media_file.start_block
        while start_block:
            next_block = start_block.next_block
            start_block.next_block = None  # Disconnect the block
            disk_blocks.append(start_block)  # Add the block back to the free list
            start_block = next_block
        del self.fat[media_file.file_name]  # Remove the file from the FAT

def simulate_linked_file_allocation():
    block_size = 1  # Assume each block is 1 MB for simplicity
    total_blocks = 60
    disk_blocks = [DiskBlock(i) for i in range(total_blocks)]  # Initialize disk with blocks

    file_a = MediaFile("Landscape.jpg", "Image", 5)
    file_b = MediaFile("Concert.mp4", "Video", 50)
    file_c = MediaFile("Song.mp3", "Audio", 8)

    fat = FileAllocationTable()

    # Allocate blocks for files
    fat.allocate_blocks(file_a, disk_blocks, block_size)
    fat.allocate_blocks(file_b, disk_blocks, block_size)
    fat.allocate_blocks(file_c, disk_blocks, block_size)

    # Print FAT
    print("File Allocation Table:")
    for file_name, block in fat.fat.items():
        blocks = []
        while block:
            blocks.append(block.block_id)
            block = block.next_block
        print(f"{file_name}: {blocks}")

    # Simulate deletion of a file
    fat.delete_file(file_c, disk_blocks)
    print("\nAfter deleting 'Song.mp3':")
    print("File Allocation Table:")
    for file_name, block in fat.fat.items():
        blocks = []
        while block:
            blocks.append(block.block_id)
            block = block.next_block
        print(f"{file_name}: {blocks}")

simulate_linked_file_allocation()
