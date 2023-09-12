with open('./oops/3_adv_features/filename.txt') as fh:
    for line in fh:
        line=line.rstrip()
        print(line)
# here we don't have to provide fh.close() as python will close the file as soon as it comes out of with block
