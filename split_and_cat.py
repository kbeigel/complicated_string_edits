#!/bin/python

#if "name" == '__main__':

# mystring = "tree tree_1 = [&R] (('name1':1.0E-6,('name2':0.001787,('name3',((('name4':0.006545,'name5':0.009508)[&label=93]:0.006261,'name6':0.007287)[&label=57]:0.005223,(('name7':0.006607,'name7':0.008204)[&label=36]:0.004148,('name8':0.009306,(('name9':0.010862,('name10':0.010024,'name11':0.046175)[&label=91]:0.01465)[&label=100]:0.029529,('name12':0.005558,'name13':0.006982)[&label=42]:0.00672)[&label=24]:0.00594)[&label=36]:0.006402)[&label=100]:0.011681)[&label=55]:0.008229)[&label=100]:0.025243)[&label=100]:0.023593):0.172252,'name14':0.172252);"

mystring = "tree tree_1 = [&R] (('name1':1,('name2':0.001,('name3',((('name4':0.006,'name5':0.009)[&label=93]:0.006,'name6':0.007)[&label=57]:0.00,(('name7':0.006,'name7':0.008)[&label=36]:0.004,('name8':0.009,(('name9':0.01,('name10':0.01,'name11':0.04)[&label=91]:0.01)[&label=100]:0.02,('name12':0.005,'name13':0.006)[&label=42]:0.006)[&label=24]:0.005)[&label=36]:0.006)[&label=100]:0.01)[&label=55]:0.008)[&label=100]:0.02)[&label=100]:0.02):0.1,'name14':0.1);"

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

# first_piece = mystring[(int(pos_range_list[0][0])):(int(pos_range_list[0][1]))]

# third_piece = mystring[(int(pos_range_list[0][1])):(int(pos_range_list[1][0]))]

# final_string = first_piece + str(replacements[2]) + third_piece


new_string = []

# x=1
# y=0

# #print(x)


# begin = mystring[pos_range_list[2][1]:pos_range_list[3][0]]

# add = '[&NEWER_LABEL'
# new_string.append(begin + add)
# print(new_string)

# begin = mystring[pos_range_list[3][1]:pos_range_list[4][0]]

# add = '[&NEWEST_LABEL'
# new_string.append(begin + add)
# print(new_string)


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




# update begin to start new
# follow = mystring[(pos_range_list[1][1]):pos_range_list[2][0]]
# x =x + 1
# begin = mystring[pos_range_list[1][0]:(pos_range_list[(x)][0])]
# print(begin)

# #new_string.append(follow)
# print(begin)



end = (pos_range_list[0][1]) # - (pos_range_list[0][1])

 # - (pos_range_list[x][0])
# for tup in pos_range_list:
	
# 	before = mystring[begin:end]
# 	after = mystring[end:tup[1]]
	
# 	#print(begin)
# 	#print(begin)
# 	#print(x)
# 	while x < (len(pos_range_list)-1):
# 		x += 1
# 		print(x)
# 		begin = (pos_range_list[x][0])
# 		end = (pos_range_list[x][1])
# 		print(begin)

	
#print(x)
#print(pos_range_list[12])
#print(type(x))

#print(''.join(new_string))
#print(first_piece)
#print(next_piece)



# print(range(len(pos_range_list)))
# print(range(len(replacements)))

# print(mystring)
