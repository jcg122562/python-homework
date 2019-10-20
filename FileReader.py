from os.path import isfile

file_path = 'housing.data'

if isfile(file_path):

    # To read a file using python we'll use the method `open`
    my_file = open(file_path)

    for line in my_file.readlines():
        strip_split_line = line.strip().split()
        print(strip_split_line)
    # must close the file
    my_file.close()

else:
    print('Please provide a valid file!')

