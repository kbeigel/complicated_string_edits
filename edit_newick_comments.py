#!/bin/python


# import
import re
import numpy as np

# Function to find the tree block of the NEXUS file
def FindStartLine(infile):
	line_num = 0
	begin_line = []
	search_string = 'begin tree'
	with open(infile, 'r') as file:
		for line in file:
			line_num += 1
			if search_string in line:
				begin_line.append((line_num, line.rstrip()))
	return begin_line

# Get the string of the tree
def GetTreeString(infile):
	begin_line_num = FindStartLine(infile)
	tree_line_num = begin_line_num[0][0] + 1
	with open(infile, 'r') as file:
		tree = file.readlines()[begin_line:(begin_line + 1)]
	return tree

# Edit the statistics / info in the comments
def EditStatComments(infile):
	tree_text = "".join(GetTreeString(infile))

	comment_pattern = re.compile('(?<=)\[.+?\](?=)')
	comment_list = comment_pattern.findall(tree_text)


	leading_pattern = r'\&(.*?)nt\)\=\"'
	leading_replacement = '&label='

	following_pattern = r'\"(.*?)\}\]'
	following_replacement = ''

	edited_comment_list = []
	for element in comment_list:
		preceding_sub = re.sub(leading_pattern, leading_replacement, element)
		following_sub = re.sub(following_pattern, following_replacement, preceding_sub)
		edited_comment_list.append(following_sub)
	
	return edited_comment_list


def GetPositionRanges(infile):
	# get string of the tree
	tree_text = "".join(GetTreeString(infile))

	# get edited stat blocks
	new_stats = EditStatComments(infile)
	
	# start counter
	count = 0

	# declare a list for the "start" of insert position
	pos_start_list = []

	# declare a list for the "end" of insert position
	pos_end_list = []

	# for each character in the tree string
	for char in range(len(tree_text)):
		# if the character is a specified character
		if tree_text[char] == "[":
			# add +1 to the counter
			count += 1

	# Make list of start positions
	# for characters at position in tree string
	for pos_start, char in enumerate(tree_text):
		# if the character is a specified character
		if(char == "["):
			# add the position of that character to list
			pos_start_list.append(pos_start)

	# Make list of end positions
	# for characters at position in tree string
	for pos_start, char in enumerate(tree_text):
		# if the character is a specified character
		if(char == "]"):
			# add the position of that character to list
			pos_end_list.append(pos_start)

	# Make a list of (pos_start, pos_end) tuples
	# declare list of tuples for position ranges
	pos_range_list = []

	# for index position in the range of index positions in start list
	for index in range(len(pos_start_list)):
		# make a tuple of pos_start and pos_end at this index in each list
		pos_range = (pos_start_list[index],pos_end_list[index])
		# append tuple to pos_range_list
		pos_range_list.append(pos_range)

	#print((pos_range_list))
	return pos_range_list


def InsertAtRange(infile):
	
	mystring = "".join(GetTreeString(infile))
	replacements = EditStatComments(infile)
	pos_range_list = GetPositionRanges(infile)
	new_string = []

	for coord in range(len(replacements)-1):
		
		length = int(len(replacements))

		if coord == 0:
			begin = mystring[0:(pos_range_list[0][0])]
			first = replacements[coord]
			following = mystring[(pos_range_list[0][1]):pos_range_list[1][0]]
			## INITIAL PART OF STRING
			new_string.append(begin+first+following)
			
		elif coord == 1:
			second = replacements[coord-1]
			new_string.append(second)
			
		elif 1 < coord < length:
			add = replacements[coord]
			begin = mystring[pos_range_list[coord][1]:pos_range_list[(coord+1)][0]]
			new_string.append(add+begin)

	add = replacements[coord+1]
	begin = mystring[pos_range_list[coord+1][1]:pos_range_list[-1][0]]
	new_string.append(add+begin)
	end = mystring[pos_range_list[-1][1]:int(len(mystring))]

	new_string.append(end)

	FINAL = "".join(new_string)
	return FINAL


############# MAIN ##################

if __name__ == '__main__':

    ## the infile name goes here, as a string
	file_name = '20180920_ITSTrachyFungi_aligned_trim_oneoutgroup_JLAMJS_mb.nexus.con.tre'

	RESULT = InsertAtRange(file_name)

	print(RESULT)

	with open('EDITEDSTATS.txt', 'w') as f:
		f.write(RESULT)