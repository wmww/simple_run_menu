#! /bin/python3
# simple run menu

import os
import stat

def is_file_executable(path):
	executable = stat.S_IEXEC | stat.S_IXGRP | stat.S_IXOTH
	if not os.path.isfile(filename):
		return False
	st = os.stat(filename)
	mode = st.st_mode
	if not mode & executable:
		return False
	return True
