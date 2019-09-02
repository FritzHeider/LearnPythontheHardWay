

file_name = raw_input("Type the file name > ")

txt = open(file_name)
#txt.write('i am a test line')
print txt.readlines()

print "Here's your file %r:" % file_name
print txt.fileno()
txt.close()


txt1 = open(file_name)
print txt1.readline(10)
txt1.close()

print "Type the filename again:"
file_again = raw_input("> ")

txt_again = open(file_again)
#txt_again.write('test test test')

print txt_again.read() 

txt_again.close()