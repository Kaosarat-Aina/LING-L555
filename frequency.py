import sys

vocab = {}

for line in sys.stdin.readlines():
	line = line.strip('\n')
	if '\t' not in line:
		continue
	row = line.split('\t')
	if len(row) != 10:
		continue
	form = row[1]
	if form not in vocab:
		vocab[form] = 0
	vocab[form] = vocab[form] + 1

#for w in vocab:
	#print('%d\t%s' % (vocab[w], w))

freq = []

for w in vocab:
	freq.append((vocab[w], w))

freq.sort(reverse=True)
	#print('%d\t%s' % (vocab[w], w))
	#freq.sort(reverse=True);;;;;;..

for frequency, w in freq:
	print('%d\t%s' % (frequency, w))

# Open the file freq.txt in write mode
fd = open('freq.txt', 'w+')
# For each of the items in the frequency list 
for (f, w) in freq:
    # Write out the frequency and the word to the file
    # separated by the tab character
    fd.write('%d\t%s\n' % (f, w))
# Close the file
fd.close()  
