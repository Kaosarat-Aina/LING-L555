import sys

IPA = {}

fd = open('IPA.txv', 'r')
for line in fd.readlines(): 

	line = line.strip('\n')
	#if '\t' not in line:
		#continue
	(w, i) = line.split('\t')
	IPA[w] = i

for line in sys.stdin.readlines():
	line = line.strip('\n')
	if '\t' not in line:
		print(line)
	if '\t' in line:
		row = line.split('\t')
		form = row[1]
		transcription = form
		for character in IPA:
			transcription = transcription.replace(character, IPA[character])
		row[9] = 'IPA=' + transcription
		print('\t'.join(row))
