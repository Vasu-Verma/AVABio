from os import sys, path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
from Bio.Alphabet import single_letter_alphabet
from Seq import Seq
from SeqRecord import SeqRecord

def parse(File):
	Records = []
	line = File.readline()
	while True:
		if line == "":
			break
		if line[0] == ">":
			id = line[1:].rstrip().split(" ")[0]
			name = line[1:].rstrip().split(" ")[0]
			description = line[1:].rstrip()
			line = File.readline()
			SeqString = ""
			while line[0]!=">":
					SeqString = SeqString + line.rstrip()
					line = File.readline()
					if len(line)==0:
						break
			Records.append(SeqRecord(Seq(SeqString, single_letter_alphabet), id, name, description))
	return Records