import sys, os

def load(f, file_directory=None):
	s = f.read()
	lib = []

	record = []
	for record in s.split('@'):
		lines = [line[:min(len(line),line.find('%'))] for line in record.split('\n')]
		lines = [line for line in lines if line.strip() != '']
		if lines == []:
			continue
		parts = record.split('{', 1)
		assert len(parts) == 2, parts
		type, body = parts
		parts = body.split(',\n')
		id = parts[0]
		bodydict = dict(type=type, id=id)
		for part in parts[1:]:
			kv = part.split('   = ', 1)
			assert len(kv) == 2, (id, kv, parts)
			k, v = kv
			bodydict[k.strip().lower()] = v.strip().lstrip('{').rstrip('}')
		if 'file' in bodydict:
			filerecords = bodydict['file'].split(';')
			files = []
			for fr in filerecords:
				ftype, fname, fformat = fr.split(':')
				files.append((ftype, fname if file_directory is None else os.path.join(file_directory, fname), fformat))
			bodydict['files'] = files
		lib.append(bodydict)
	return lib



