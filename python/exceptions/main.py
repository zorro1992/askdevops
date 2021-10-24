# try:
# 	fo=open("nari.txt")
# 	print(fo.read())
# 	fo.close()
# except Exception as e:
# 	print(e)


# Custom Expections 

# try:
# 	fo=open("nari.txt")
# 	print(fo.read())
# 	fo.close()
# except Exception as e:
# 	print(e)




my_list=[3,4,5]

try:
	print(my_list[4])
except Exception as e:
	print("Check your list index call: ",e)
