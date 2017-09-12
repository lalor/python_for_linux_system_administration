import tarfile
with tarfile.open('tarfile_add.tar') as t:
    for member_info in t.getmembers():
        print(member_info.name)
