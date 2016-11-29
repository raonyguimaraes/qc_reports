from Bio import SeqIO


import argparse
parser = argparse.ArgumentParser()
parser.add_argument('-i', help='input')
args = parser.parse_args()
print(args)

handle1 = open(args.i, "rU")

fastq_reader = SeqIO.parse(handle1, "fastq")
for record in fastq_reader :
	print(record)
	die()
    #Calculate GC on record 1 and record 2
handle1.close()
