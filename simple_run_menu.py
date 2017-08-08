#! /bin/python3
# simple run menu

import os
import stat

def is_file_executable(path):
	executable = stat.S_IEXEC | stat.S_IXGRP | stat.S_IXOTH
	if not os.path.isfile(path):
		return False
	st = os.stat(path)
	mode = st.st_mode
	if not mode & executable:
		return False
	return True

def get_files_in_dir(directory):
	if directory == '':
		directory = '.'
	if directory[-1] != '/':
		directory += '/'
	return [directory + i for i in os.listdir(directory)]

def command_to_name(command):
	filename_with_ext = os.path.basename(command)
	filename = filename_with_ext.rsplit('.', 1)[0]
	name = filename.replace('_', ' ')
	capitalized = ' '.join([i[0].upper() + i[1:] for i in name.split()])
	return capitalized
	
class Option:
	
	options = {}
	
	@staticmethod
	def add(command):
		options['a'] = Option(command, command, 'a')
	
	def __init__(self, name, command, trigger):
		self.name = name
		self.command = command
		self.trigger = trigger
	
if __name__ == "__main__":
	print([command_to_name(i) for i in get_files_in_dir('') if is_file_executable(i)])
	
