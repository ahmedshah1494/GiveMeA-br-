
def parse_pdf(name):
	with open(name) as f:
		raw = f.readlines();
		
	# raw = filter(lambda x: x[0] != '@' and ord(x[0]) != 12, raw);
	for i in range(len(raw)):
		line = raw[i].strip();
		if len(line) < 4 and len(line) > 0 and len(filter(lambda x: ord(x) < 58 and ord(x) > 47, list(line))) == len(line) and raw[i - 1] == '\n' and raw[i + 1] == '\n' and int(line) <= 260:
			raw[i] = 'LINEBREAK';

	raw = ''.join(raw).split('LINEBREAK')
	for i in range(len(raw)):
		with open("pages/%s_page_%.3d.txt" % (name.split('/')[-1], i), "w") as f:
			f.write(raw[i]);


pdfs = ["../pdf_texts/eua_2014_full_0.txt", "../pdf_texts/eua_2010_full_0.txt", "../pdf_texts/eua_2007_full_0.txt"]

for pdf in pdfs:
	parse_pdf(pdf)
