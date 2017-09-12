import tarfile
with tarfile.open('tarfile_add.tar', mode='w') as out:
    out.add('README.txt')
