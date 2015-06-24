import bibtexparser
import sys
import os

filename = sys.argv[1]
outfilename = filename.replace('.bib', '.rst')

with open(filename) as bibtex_file:
	bib_database = bibtexparser.load(bibtex_file, os.environ.get('BIBDIR'))

with open(outfilename, 'w') as out:
	title = 'Bibliography file: %s' % filename.replace('.bib', '')
	out.write('%s\n%s\n\n' % (title, '='*len(title)))
	out.write('.. contents:: Table of Contents\n   :depth: 2\n\n')
	for entry in bib_database:
		if 'review' not in entry:
			continue
		out.write('%s\n' % entry['id'])
		out.write('%s\n' % ('-'*len(entry['id'])))
		out.write('\n')
		out.write('Title: *%s*\n\n' % entry['title'])
		if 'files' in entry:
			out.write('Files:\n')
			for ftype, fname, fformat in entry['files']:
				if fformat != 'PDF':
					continue
				out.write('`%s <%s>`__ ' % (ftype, fname))
		out.write('\n\n')
		if True or entry['review'].startswith('rst'):
			out.write(entry['review'])
		else:
			out.write('::\n\n')
			for line in entry['review'].split('\n'):
				out.write('  %s\n' % line)
			out.write('\n\n')
		out.write('\n\n')
	


