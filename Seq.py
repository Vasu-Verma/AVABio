from Bio import Alphabet
from Bio.Data import CodonTable
import string

complementDict = {"A":"T", "G":"C", "T":"A", "C":"G"}
class Seq:
	def __init__(self, sequence, type):
		self.sequence = sequence
		self.type = type

	def __str__(self):
		return self.sequence

	def __len__(self):
		return len(self.sequence)

	def transcribe(self):
		if(isinstance(Alphabet._get_base_alphabet(self.type),Alphabet.DNAAlphabet)):
			return Seq(string.replace(self.sequence,'T','U'),Alphabet.generic_rna)
		else:
			print "Transcibe failed: Sequence not a DNA Sequence"

	def back_transcribe(self):
		if(isinstance(Alphabet._get_base_alphabet(self.type),Alphabet.RNAAlphabet)):
			return Seq(string.replace(self.sequence,'U','T'),Alphabet.generic_dna)
		else:
			print "Back Transcibe failed: Sequence not a RNA Sequence"
	
	def translate(self):
		if isinstance(Alphabet._get_base_alphabet(self.type),Alphabet.DNAAlphabet)==False and isinstance(Alphabet._get_base_alphabet(self.type),Alphabet.RNAAlphabet)==False:
			print "Not a RNA or DNA sequence: Translation to protein failed"
			return
		if(isinstance(Alphabet._get_base_alphabet(self.type),Alphabet.DNAAlphabet)):
			table = CodonTable.ambiguous_dna_by_id[1]
		elif(isinstance(Alphabet._get_base_alphabet(self.type),Alphabet.RNAAlphabet)):
			table = CodonTable.unambiguous_rna_by_id[1]
		length = len(self.sequence)
		if length%3!=0:
			print "Sequence length is not a multiple of 3: Translation to protein failed"
			return
		proteinSeq = ""
		print table.start_codons
		for i in range(0,length,3):
			try:
				proteinSeq = proteinSeq + table.forward_table[self.sequence[i:i+3]]
			except (KeyError, CodonTable.TranslationError):
				if self.sequence[i:i+3] in table.stop_codons:
					proteinSeq = proteinSeq + "*"
		return Seq(proteinSeq,Alphabet.generic_protein)

	def complement(self):
		length = len(self.sequence)
		if(isinstance(Alphabet._get_base_alphabet(self.type),Alphabet.DNAAlphabet)):
			complement = ""
			for i in range(0,length):
				complement = complement + complementDict[self.sequence[i]]
			return Seq(complement,Alphabet.generic_dna)
		if(isinstance(Alphabet._get_base_alphabet(self.type),Alphabet.RNAAlphabet)):
			complement = ""
			for i in range(0,length):
				if self.sequence[i] == "U":
					complement = complement + complementDict["T"]
				elif complementDict[self.sequence[i]]=="T":
					complement = complement + "U"
				else:
					complement = complement + complementDict[self.sequence[i]]
			return Seq(complement,Alphabet.generic_rna)
		else:
			print "Not a DNA or RNA Sequencess"
