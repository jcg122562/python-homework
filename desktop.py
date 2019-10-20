import os
# change directory to desktop
os.chdir('C:/Users/jcgalindez/Desktop')

# make a list of the files in the current directory
my_desktop = os.listdir('C:/Users/jcgalindez/Desktop')  # I think this can be just os.listdir()  since I have the path changed but it says parameter path unfilled so I put the path

for my_file in my_desktop:
    is_file = os.path.isfile(my_file)
    if os.path.isfile(my_file):
        print(f'This is a file: ', my_file)
    elif os.path.isdir(my_file):
        print(f'This is a directory: ', my_file)
    else:
        print('unknown file')

# Note: I can just use the isfile i think and if not isfile then it is assumed a directory.  However, I used the isdir too to make sure


