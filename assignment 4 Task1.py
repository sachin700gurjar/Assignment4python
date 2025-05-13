try:
    file = open("sample.txt","r")
    print("Reading file contents:")
    for i,line in enumerate(file,start=1):
        print(f"Line{i}:{line.strip()}")

except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found.")