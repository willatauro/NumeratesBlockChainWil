
# to write only 
f = open('demofiles.txt','w')
f.write('Hello from Python!')
f.close()

# to append to the file
f = open('demofiles.txt','a')
f.write('Add this content!')
f.close()

# to Read a file
f = open('demofiles.txt','r')

# read() reads entire line , readlines() -- reads and stores as list, readline() -- reads single line

file_content = f.readline()
f.close()
print(file_content)

## With keyword automatically closes the file