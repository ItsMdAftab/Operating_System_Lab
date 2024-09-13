class PatientRecord:
    def __init__(self, name, age, medical_id, address):
        self.name = name
        self.age = age
        self.medical_id = medical_id
        self.address = address
        self.size = 1
        
    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Medical ID: {self.medical_id}, Address: {self.address}"

class IndexBlock:
    def __init__(self):
        self.blocks = [] 
class IndexedFileAllocation:
    def __init__(self, total_blocks):
        self.total_blocks = total_blocks
        self.disk = [None] * total_blocks  
        self.index_table = {}  
        self.free_blocks = set(range(total_blocks)) 

    def allocate_blocks(self, num_blocks):
        """Allocate 'num_blocks' from free blocks and return their indices."""
        if len(self.free_blocks) < num_blocks:
            return None  
        
        allocated = set()
        while len(allocated) < num_blocks:
            block = self.free_blocks.pop()
            allocated.add(block)
        
        return allocated

    def add_record(self, patient_record):
        if patient_record.medical_id in self.index_table:
            print(f"Record for Medical ID {patient_record.medical_id} already exists.")
            return False
        
        index_block = IndexBlock()
        allocated_blocks = self.allocate_blocks(patient_record.size)
        if not allocated_blocks:
            print("Not enough disk space to add record for patient:", patient_record.name)
            return False
        
        index_block.blocks.extend(allocated_blocks)
        
        for block in allocated_blocks:
            self.disk[block] = patient_record
        
        self.index_table[patient_record.medical_id] = index_block
        return True

    def delete_record(self, medical_id):
        if medical_id not in self.index_table:
            print(f"Record not found for Medical ID: {medical_id}")
            return False
        
        index_block = self.index_table.pop(medical_id)
        for block in index_block.blocks:
            self.disk[block] = None
            self.free_blocks.add(block)
        return True

    def update_record(self, medical_id, name=None, age=None, address=None):
        if medical_id not in self.index_table:
            print(f"Record not found for Medical ID: {medical_id}")
            return False
        
        index_block = self.index_table[medical_id]
        patient_record = self.disk[index_block.blocks[0]]
        if name:
            patient_record.name = name
        if age:
            patient_record.age = age
        if address:
            patient_record.address = address
        return True

    def retrieve_record(self, medical_id):
        if medical_id not in self.index_table:
            print(f"Record not found for Medical ID: {medical_id}")
            return None
        
        index_block = self.index_table[medical_id]
        patient_record = self.disk[index_block.blocks[0]]
        return patient_record

    def display_records(self):
        print("Index Table:")
        for medical_id, index_block in self.index_table.items():
            patient = self.disk[index_block.blocks[0]]
            print(f"Medical ID: {patient.medical_id}, Name: {patient.name}, Age: {patient.age}, Address: {patient.address}")
        
        print("\nDisk Blocks:")
        for i, block in enumerate(self.disk):
            if block:
                print(f"Block {i}: {block}")
            else:
                print(f"Block {i}: Free")

indexed_file_allocation = IndexedFileAllocation(total_blocks=10)

indexed_file_allocation.add_record(PatientRecord("John Smith", 45, 1001, "123 Hospital Road"))
indexed_file_allocation.add_record(PatientRecord("Jane Doe", 32, 1002, "456 Clinic Avenue"))
indexed_file_allocation.add_record(PatientRecord("Michael Johnson", 58, 1003, "789 Medical Plaza"))

indexed_file_allocation.display_records()

indexed_file_allocation.update_record(1002, age=33)

indexed_file_allocation.display_records()

indexed_file_allocation.delete_record(1001)

indexed_file_allocation.display_records()
