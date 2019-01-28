import os
import re


def file_selector(dir_path):
	file_list = os.listdir(dir_path)
	md_list = [file for file in file_list if re.search('.md', file)]
	for i, file_name in enumerate(md_list):
		print('{} : {}'.format(i, file_name))
	print('Select number you want to see.')
	file_number = int(input())
	file_name = dir_path + '/' + md_list[file_number]
	return file_name
	
	
def ls_md_files(dir_path):
	file_list = os.listdir(dir_path)
	return [file for file in file_list if re.search('.md', file)]
