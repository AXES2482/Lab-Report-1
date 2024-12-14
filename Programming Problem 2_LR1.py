
FileName = input('Enter the input file name: ')

fin = open(FileName, "r")

fileList = list()

for line in fin:

	line = line.strip('\n')

	fileList.append(line)

