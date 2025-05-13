from builtins import PythonFinalizationError

user_input = input("Enter text to write to the file:")

file = open("file.txt","w")


file.write(user_input+"\n")
print("Data successfully written to output.txt.")
text2 = input("Enter additional text to append:")
file = open("file.txt","a")
file.write(text2+"\n")
print("Data successfully appended.\n")
print("Final content of output.txt:")
file = open("file.txt","r")
for line in file:
    print(line.strip())



