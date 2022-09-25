#!/bin/python

if "name" == '__main__':


# Newick formatted tree from a NEXUS file that that has additional information stored in [&]
mystring = "name tree_1 = [&R] (('taxa1':1,('taxa2':0.001,('taxa3',((('taxa4':0.006,'taxa5':0.009)[&label=93]:0.006,'taxa6':0.007)[&label=57]:0.00,(('taxa7':0.006,'taxa7':0.008)[&label=36]:0.004,('taxa8':0.009,(('taxa9':0.01,('taxa10':0.01,'taxa11':0.04)[&label=91]:0.01)[&label=100]:0.02,('taxa12':0.005,'taxa13':0.006)[&label=42]:0.006)[&label=24]:0.005)[&label=36]:0.006)[&label=100]:0.01)[&label=55]:0.008)[&label=100]:0.02)[&label=100]:0.02):0.1,'taxa14':0.1);"


pos_start_list =[]
for pos_start, char in enumerate(mystring):
	# if the character is a specified character
	if(char == "["):
		# add the position of that character to list
		pos_start_list.append(pos_start)

pos_end_list = []
for pos_start, char in enumerate(mystring):
	# if the character is a specified character
	if(char == "]"):
		# add the position of that character to list
		pos_end_list.append(pos_start)

pos_range_list = []
# for index position in the range of index positions in start list
for index in range(len(pos_start_list)):
	# make a tuple of pos_start and pos_end at this index in each list
	pos_range = (pos_start_list[index],pos_end_list[index])
	# append tuple to pos_range_list
	pos_range_list.append(pos_range)


replacement = 'POS0'
replacements = ['[POS0', '[POS1', '[POS2', '[POS3', '[POS4', '[POS5', '[POS6', '[POS7', '[POS8', '[POS9', '[POS10', '[POS11', '[POS12']

new_string = []

begin = mystring[0:(pos_range_list[(0)][0])]
print(begin)

first = "[&NEW_label"

## INITIAL PART OF STRING
new_string.append(begin + first)
print(new_string)


for coord in range(len(replacements)-1):
	begin = mystring[pos_range_list[coord][1]:pos_range_list[(coord+1)][0]]
	add = replacements[coord]
	new_string.append(begin + add)
print(type(new_string))

end = mystring[pos_range_list[coord][1]:len(mystring)]

# print(type(new_string))

new_string.append(end)


# print(new_string)

print("".join(new_string))
