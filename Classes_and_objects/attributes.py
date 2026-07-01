
# Concept: Attributes in Object-Oriented Programming
# Attributes represent the data, properties, or state of a class and its objects.


class NumberSequence:
    subject_category="Maths and Statistics"

    def __init__(self,seq_name,seq_data):
        self.seq_name=seq_name
        self.seq_data=seq_data
        self.is_analysed=False


seq1=NumberSequence("Test Scores",[10,7,8,9])
seq2=NumberSequence("puzzle ",[2,4,6,1,6])
    
print(f"Sequence 1 Name:{seq1.seq_name}")
print(f"Sequence 1 Data:{seq1.seq_data}")

print(f"Sequence 2 Name:{seq2.seq_name}")
print(f"Sequence 2 Data:{seq2.seq_data}")

print(f"Subject category of sequence 1: {seq1.subject_category}")
print(f"Subject category of sequence 2: {seq2.subject_category}")

seq1.is_analysed=True
print(f"Sequence 1 is Analysed? :{seq1.is_analysed}")



