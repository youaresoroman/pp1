def checkFile(filename):
    try:
        file = open(filename, "r")
        output = []
        for line in file:
            output += line
        file.close()
        return output
    except FileNotFoundError:
        print('Not exist.')
    except IOError:
        print('Reading error.')
        
            
print(checkFile("NoEducation.txt"))