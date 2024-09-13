class StudentRecord:
    def __init__(self, name, student_id, grade, address):
        self.name = name
        self.student_id = student_id
        self.grade = grade
        self.address = address

    def __str__(self):
        return f"Name: {self.name}, ID: {self.student_id}, Grade: {self.grade}, Address: {self.address}"

class SequentialFileAllocation:
    def __init__(self, block_size):
        self.disk_blocks = []  
        self.fat = {}
        self.block_size = block_size
        self.next_free_block = 0 

    def add_record(self, student_record):
        record_size = self.calculate_record_size(student_record)
        
        if self.next_free_block + record_size > len(self.disk_blocks):
            for _ in range(self.next_free_block + record_size - len(self.disk_blocks)):
                self.disk_blocks.append([None] * self.block_size)
        
        start_block = self.next_free_block
        for i in range(record_size):
            block = self.disk_blocks[start_block + i]
            block_data = [student_record.name, student_record.student_id, student_record.grade, student_record.address]
            for j in range(len(block_data)):
                if j + i * self.block_size < self.block_size:
                    block[j + i * self.block_size] = block_data[j]
        
        self.fat[student_record.student_id] = (start_block, record_size)
        
        self.next_free_block += record_size
        
        return True

    def get_record(self, student_id):
        if student_id not in self.fat:
            return None
        
        start_block, record_size = self.fat[student_id]
        record_data = []
        
        for i in range(record_size):
            block = self.disk_blocks[start_block + i]
            record_data.extend(block)
        
        name, student_id, grade, address = record_data[:4]
        return StudentRecord(name, student_id, grade, address)

    def calculate_record_size(self, student_record):
        return 1

    def print_disk_status(self):
        print("Disk Blocks:")
        for index, block in enumerate(self.disk_blocks):
            print(f"Block {index}: {block}")
        
        print("File Allocation Table (FAT):")
        for student_id, (start_block, length) in self.fat.items():
            print(f"Student ID {student_id}: Start Block {start_block}, Length {length}")

block_size = 4
allocator = SequentialFileAllocation(block_size)

students = [
    StudentRecord("John Doe", 101, 10, "123 Main Street"),
    StudentRecord("Jane Smith", 102, 11, "456 Elm Street"),
    StudentRecord("Michael Brown", 103, 9, "789 Oak Avenue")
]

for student in students:
    allocator.add_record(student)

for student in students:
    retrieved = allocator.get_record(student.student_id)
    print(f"Retrieved: {retrieved}")

allocator.print_disk_status()
