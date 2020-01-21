import zipfile

z_file = zipfile.ZipFile('g:\\new.zip')
z_file.extract('a.pdf', 'g:\\')
z_file.close()
