for i in range(3):
	print('Start of outer #%s' % (i))
	
	for j in range(3):
		print('Hello!')
		continue
		print('Goodbye!')
	
	print('End of outer #%s' % (i))
