#Python Tutorial: Automate Parsing and Renaming of Multiple Files

import os

os.chdir('home/atual/')


for f in os.listdir():
    
    if f == 'atual':
        continue

    file_name, file_ext = os.path.splitext(f)

    f_title, f_course, f_number = file_name.split('-')

    print('{}-{}-{}{}'.format(f_number, f_course, f_title, file_ext))

    
    f_title = f_title.strip()
    f_course = f_course.strip()
    f_number = f_number.strip()


    f_number = f_number.strip()[1:].zfill(2)

    print('{}-{}{}'.format(f_number, f_title.strip(), file_ext.strip()))

    new_name = '{}-{}{}'.format(file_num, file_title, file_ext)

    os.rename(fn, new_name)