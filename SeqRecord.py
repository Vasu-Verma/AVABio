import Seq
from Bio._py3k import basestring

class SeqRecord:
	def __init__(self, sequence, id="unknown", name="unknown", description="unknown", features=None, dbxrefs=None, annotations=None, letter_annotations=None):
		self.seq = sequence
		self.id = id
		self.name = name
		self.description = description

		if features is None:
			features = []
		elif not isinstance(features, list):
			print "Not a valid feature list: Initializing empty feature list"
			features = []
		self.features =  features

		if dbxrefs is None:
			dbxrefs = []
		elif not isinstance(dbxrefs, list):
			print "Not a valid database reference list: Initializing empty database reference list"
			dbxrefs = []
		self.dbxrefs =  dbxrefs

		if annotations is None:
			annotations = {}
		elif not isinstance(annotations, dict):
			print "Not a valid annotations dictionary: Initializing empty annotations dictionary"
			annotations = {}
		self.annotations = annotations

	def __str__(self):
		value = "Id: " + self.id + "\n"
		value = value + "name: " + self.id + "\n"
		value = value + "description: " + self.description + "\n"
		value = value + "features: " + str(self.features) + "\n" 
		value = value + "Sequence: " + str(self.seq) + "\n"
		return value