import sys

tag_counts = {}
word_to_tag = {}

fd = open('model.tsv2', 'r')
for line in fd.readlines():
	row = line.strip().split('\t')
	form = row[3]
	tag = row[2]
	count = row [1]
#	count = int(row [1])
	P = row[0]
	if form not in word_to_tag or word_to_tag[form][1] < count:
		word_to_tag[form] = (tag, count)

	if tag not in tag_counts:
		tag_counts[tag] = 0
	tag_counts[tag] += 1
most_frequent_tag = max(tag_counts, key=tag_counts.get)
#print(word_to_tag)

for line in sys.stdin.readlines():
	line = line.strip('\n')
	if '\t' not in line:
		print(line)
	if '\t' in line:
		row = line.split('\t')
		form = row[1]
		tag = form
		if form in word_to_tag: 
			tag = word_to_tag[form][0] 
		else: 
			tag = most_frequent_tag
		row[3] = tag
		print('\t'.join(row))
