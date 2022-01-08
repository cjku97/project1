from seqparser import (
        FastaParser,
        FastqParser,
        transcribe,
        reverse_transcribe)

def main():
	"""
	The main function
	"""
	# Create instance of FastaParser
	fastaparse = FastaParser("./data/small_test.fa")
	# Create instance of FastqParser
	fastqparse = FastqParser("./data/small_test.fq")

	# For each record of FastaParser, Transcribe the sequence 
	# and print it to console	
	print("FASTA TRANSCRIBE")
	for record in fastaparse:
		print(record[0])
		print(transcribe(record[1]))   
	print()
	# For each record of FastqParser, Transcribe the sequence
	# and print it to console
	print("FASTQ TRANSCRIBE")
	for record in fastqparse:
		print(record[0])
		print(transcribe(record[1]))
	print()				
	# For each record of FastaParser, Reverse Transcribe the sequence
	# and print it to console
	print("FASTA REVERSE-TRANSCRIBE")
	for record in fastaparse:
		print(record[0])
		print(reverse_transcribe(record[1]))
	print()
	# For each record of FastqParser, Reverse Transcribe the sequence
	# and print it to console
	print("FASTQ REVERSE-TRANSCRIBE")
	for record in fastqparse:
		print(record[0])
		print(reverse_transcribe(record[1]))

"""
When executing a python script from the command line there will
always be a hidden variable `__name__` set to the value `__main__`.

Since this is guaranteed you can execute your `main` function with
the following if statement
"""
if __name__ == "__main__":
    main()
