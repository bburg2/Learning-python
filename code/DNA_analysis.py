# import bioinfokit.analys
from bioinfokit.analys import fastq

# load some data generated with the minION
fastq_iter = fastq.fastq_reader(file='data/AIR589_pass_dbebcefe_1.fastq')
# read fastq file

# get sequence length
sequence_len = len(sequence)

# count bases
a_base = sequence.count('A')
c_base = sequence.count('C')
t_base = sequence.count('T')
g_base = sequence.count('G')

# make a dictionary for the DNA data
DNA = {}
DNA["sequence length"] = sequence_len 
DNA["A count"] = a_base  
DNA["C count"] = c_base  
DNA["T count"] = t_base  
DNA["G count"] = g_base  

# print the dictionary
print(DNA)
