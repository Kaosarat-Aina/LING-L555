import sys

s = sys.stdin.readlines()

total_number_of_tokens = 0

tag_frequency = {}
word_tag = {}

fd = open('wiki.conllu', 'r')

for line in fd.readlines():

	line = line.strip('\n')
	if '\t' not in line:
		continue
	row = line.split('\t')
	form = row[1]
	tag = row[3]
	if form not in word_tag:
		word_tag[form]= {}
	if tag not in word_tag[form]:
		word_tag[form][tag] = 0
	word_tag[form][tag] += 1

#for w in word_tag:
	#print('%d\t%s' % (word_tag[tag], w))
#for w1 in word_tag:
	#if w1 not in word_tag:
		#word_tag[w1] = {}
	#for w2 in word_tag:
		#word_tag[w1][w2] = 0
	
print('\t' + '\t'.join(word_tag))
for form in word_tag:
	print('%s\t' % (form), end='')
	for tag in word_tag[form]:
		print('%d\t%s\t' % (word_tag[form][tag], tag), end='')
	print('')

