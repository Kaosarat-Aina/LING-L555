# Project

`PROJECT DESCRIPTION HERE`

A program for automatic Part of Speech (POS) tagging of texts for Yoruba 
Kaosarat Aina 
1. Project description 
Natural language Processing (NLP) plays an important role in our society today. It is a means by which we can harness the numerous technologies available for language use, documentation, development, and preservation. A program that automatically tags words with their POS for Yoruba language is a step in the direction of contributing to the NLP tools for Yoruba. The POS used in the language model for this program were chosen in consultation with the Universal Dependency Treebank for Yoruba (Ishola and Zeman, 2020) that is available in udpipe’s collection. This program is beneficial for the purpose of syntactic analysis of Yoruba that is not couched in Universal dependency. 
Apart from the UD work, the other annotated corpora of Yoruba that I know of is the one released just this September 2023 by Ademusire and Ninan (2023) which is for the purpose of arguments, temporal and spatial annotation. It is not for POS tagging or syntactic/grammatical purpose; it is more for information extraction and related tasks purposes. Hence, this project is a worthwhile exercise.  
The program was written with Python and will be discussed more in details. Such a program as this, is important because it will make corpora creation easier since annotation of corpora is a tasking feat and can discourage people. It will not only save time but also encourage more progress in corpora creation for Yoruba. More so, a corpus tagged with a program like this, will be useful for linguistic enquiries about the grammar and structure of Yoruba language, as well as evaluating and developing linguistic theories. It will also enhance the development of more NLP technologies for Yoruba language.  
 
1.1 Types of inputs  
For this project, we have different input and output formats.  
à First, we have the wiki.txt file which is the corpus we annotated with the tagger. It was gotten from Wikipedia à WikiMedia dumps site à and extracted with WikiExtractor.  à Then we have a conllu file called ‘wiki.conllu2’ which is extracted from the wiki.txt corpus for manual POS annotation so as to serve as the language model. It also contains transcriptions. 
à Lastly, we have the model.tsv2 file which contains the result gotten from running the train.py on the wiki.conllu2 file. It contains the tags, counts, and tag probabilities for the forms/words in the wiki.conllu2 file. It is our language model for the tagger.  
All of them are uploaded to my github repository. 
 
1.2 Workflow  à The corpus was a raw collection of plain text so the first thing we did was to write a segmenter. The segmenter divided the corpus into lines by adding a new line after every period.  
à Next, is a tokenizer which breaks each line into its component words followed by some underscores. Basically, each word is in a 10-row line so that information such as lemma, UPOS, transcription, etc. can be entered against each word.  
à After this, we pulled out 50 sentences from the tokenized corpus into a wiki.conllu2 file and manually annotated each word with a POS tag. I increased the sentences from the 10 we initially used for class practical to 50 sentences since this is serving as my project and to make the tagger perform better. 
à Next, the train.py program which generated the language model model.tsv from the conllu file was written. It checked for the tags associated with each form in the conllu file and calculated the number of counts and the tag’s probability given each form, all these were saved in a model.tsv.  
à Finally, we wrote the tagger. It is a unigram POS tagger which tags words in the corpus by assigning to them, the most frequent tag associated to them in the language model. In cases whereby a word isn’t in the language model but exists in the corpus, it falls back to the most frequent tag in general in the language model and assigns it to such words the words.  
 
2.	Results 
Words that are not in the language model are assigned the most frequent tag in the language model which is ‘NOUN’ while those that are in the model.tsv are assigned the tag most frequently assigned to them in the model.tsv. 
3.	How to run the code 
``` 
cat wiki.txt | python3 segementer.py3 | python3 tokeinser.py2 | python3 tagger.py model.tsv2 
``` 
4.	Example output 
Here is an example output for the tagger:  
# sent_id = 47205 
# text = , (November 29, 1908 – April 4, 1972) je oloselu ara Amerika ati Asoju ni Ile Asoju Amerika tele. 
1	, 	_ 	PUNCT _ 	_ 	_ 	_ 	_ 	_ 
2	( 	_ 	PUNCT _ 	_ 	_ 	_ 	_ 	_ 
3	November 	_ 	NOUN _ 	_ 	_ 	_ 	_ 	_ 
4	29 	_ 	NUM 	_ 	_ 	_ 	_ 	_ 	_ 
5	, 	_ 	PUNCT _ 	_ 	_ 	_ 	_ 	_ 
6	1908 	_ 	NUM 	_ 	_ 	_ 	_ 	_ 	_ 
7	– 	_ 	NOUN _ 	_ 	_ 	_ 	_ 	_ 
8	April 	_ 	NOUN _ 	_ 	_ 	_ 	_ 	_ 
9	4 	_ 	NUM 	_ 	_ 	_ 	_ 	_ 	_ 
10	, 	_ 	PUNCT _ 	_ 	_ 	_ 	_ 	_ 
11	1972 	_ 	NUMM _ 	_ 	_ 	_ 	_ 	_ 
12	) 	_ 	PUNCT _ 	_ 	_ 	_ 	_ 	_ 
13	je 	_ 	VERB _ 	_ 	_ 	_ 	_ 	_ 
14	oloselu _ 	NOUN _ 	_ 	_ 	_ 	_ 	_ 
15	ara 	_ 	NOUN _ 	_ 	_ 	_ 	_ 	_ 
16	Amerika _ 	NOUN _ 	_ 	_ 	_ 	_ 	_ 
17	ati 	_ 	CCONJ _ 	_ 	_ 	_ 	_ 	_ 
18	Asoju 	_ 	NOUN _ 	_ 	_ 	_ 	_ 	_ 
19	ni 	_ 	ADP 	_ 	_ 	_ 	_ 	_ 	_ 
20	Ile 	_ 	NOUN _ 	_ 	_ 	_ 	_ 	_ 
21	Asoju 	_ 	NOUN _ 	_ 	_ 	_ 	_ 	_ 
22	Amerika _ 	NOUN _ 	_ 	_ 	_ 	_ 	_ 
23	tele 	_ 	ADV 	_ 	_ 	_ 	_ 	_ 	_ 
24	. 	_ 	PUNCT 	_ 	_ 	_ 	_ 	_ 	_ 
 
 
# sent_id = 127660 
# text = Láti ìgbà tí ó yọbọ́ tí ó sì lọ sí orílẹ̀ èdè Amẹ́ríkà, ó ti ń rìnrìn àjò káàkiri orílẹ̀ èdè láti kọ́ nípa ẹ̀kọ́ àti láti kó lòdì sí Ìsìnrú. 
1	Láti 	_ 	ADP 	_ 	_ 	_ 	_ 	_ 	_ 
2	ìgbà 	_ 	NOUN 	_ 	_ 	_ 	_ 	_ 	_ 
3	tí 	_ 	ADP 	_ 	_ 	_ 	_ 	_ 	_ 
4	ó 	_ 	PRON 	_ 	_ 	_ 	_ 	_ 	_ 
5	yọbọ́ 	_ 	VERB 	_ 	_ 	_ 	_ 	_ 	_ 
6	tí 	_ 	ADP 	_ 	_ 	_ 	_ 	_ 	_ 
7	ó 	_ 	PRON 	_ 	_ 	_ 	_ 	_ 	_ 
8	sì 	_ 	CCONJ 	_ 	_ 	_ 	_ 	_ 	_ 
9	lọ 	_ 	VERB 	_ 	_ 	_ 	_ 	_ 	_ 
10	sí 	_ 	ADP 	_ 	_ 	_ 	_ 	_ 	_ 
11	orílẹ̀ 	_ 	NOUN 	_ 	_ 	_ 	_ 	_ 	_ 
12	èdè 	_ 	NOUN 	_ 	_ 	_ 	_ 	_ 	_ 
13	Amẹ́ríkà 	_ 	NOUN 	_ 	_ 	_ 	_ 	_ 	_ 
14	, 	_ 	PUNCT 	_ 	_ 	_ 	_ 	_ 	_ 
15	ó 	_ 	PRON 	_ 	_ 	_ 	_ 	_ 	_ 
16	ti 	_ 	AUX 	_ 	_ 	_ 	_ 	_ 	_ 
17	ń 	_ 	AUX 	_ 	_ 	_ 	_ 	_ 	_ 
18	rìnrìn 	_ 	VERB 	_ 	_ 	_ 	_ 	_ 	_ 
19	àjò 	_ 	NOUN 	_ 	_ 	_ 	_ 	_ 	_ 
20	káàkiri 	_ 	NOUN 	_ 	_ 	_ 	_ 	_ 	_ 
21	orílẹ̀ 	_ 	NOUN 	_ 	_ 	_ 	_ 	_ 	_ 
22	èdè 	_ 	NOUN 	_ 	_ 	_ 	_ 	_ 	_ 
23	láti 	_ 	ADP 	_ 	_ 	_ 	_ 	_ 	_ 
24	kọ́ 	_ 	VERB 	_ 	_ 	_ 	_ 	_ 	_ 
25	nípa 	_ 	ADP 	_ 	_ 	_ 	_ 	_ 	_ 
26	ẹ̀kọ́ 	_ 	NOUN 	_ 	_ 	_ 	_ 	_ 	_ 
27	àti 	_ 	CCONJ 	_ 	_ 	_ 	_ 	_ 	_ 
28	láti 	_ 	ADP 	_ 	_ 	_ 	_ 	_ 	_ 
29	kó 	_ 	VERB 	_ 	_ 	_ 	_ 	_ 	_ 
30	lòdì 	_ 	ADV 	_ 	_ 	_ 	_ 	_ 	_ 
31	sí 	_ 	ADP 	_ 	_ 	_ 	_ 	_ 	_ 
32	Ìsìnrú 	_ 	NOUN 	_ 	_ 	_ 	_ 	_ 	_ 
33	. 	_ 	PUNCT 	_ 	_ 	_ 	_ 	_ 	_ 
 
 
References 
1.	Ademusire, Adebisi & Ninan, Olufemi. (2023). Development of an annotated Yoruba text corpus for automatic event extraction. 10.21203/rs.3.rs-3327609/v1. 
2.	Olájídé Ishola and Daniel Zeman. (2020). Yorùbá Dependency Treebank (YTB). 
In Proceedings of the Twelfth Language Resources and Evaluation Conference, pages 
5178–5186, Marseille, France. European Language Resources Association 
3.	https://github.com/UniversalDependencies/UD_Yoruba-YTB/blob/master/yo_ytb-udtest.conllu 
