# DNA -> RNA Transcription


def transcribe(seq: str) -> str:
    """
    transcribes DNA to RNA by generating
    the complement sequence with T -> U replacement
    """
    s = list(seq)
    for i in range(0,len(s)):
    	base = s[i]
    	if base == 'A':
    		s[i] = 'U'
    	elif base == 'T':
    		s[i] = 'A'
    	elif base == 'G':
    		s[i] = 'C'
    	elif base == 'C':
    		s[i] = 'G'
    	else:
    		raise ValueError("Incorrect DNA sequence input")
    return("".join(s))


def reverse_transcribe(seq: str) -> str:
    """
    transcribes DNA to RNA
	then reverses the sequence
    """
    t = transcribe(seq)
    return(t[::-1])


"""
test1 = "CATCATCAT"
print("input:   " + test1)
print("output:  " + transcribe(test1))
print("reverse: " + reverse_transcribe(test1))

#test2 = "CATKATCAT"
#print("input:   " + test2)
#print("output:  " + transcribe(test2))
#print("reverse: " + reverse_transcribe(test2))

test3 = "GATACATAGATA"
print("input:   " + test3)
print("output:  " + transcribe(test3))
print("reverse: " + reverse_transcribe(test3))
"""