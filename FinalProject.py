import os



print("Ivan Figueroa final project\n\n")

while True:
    print("\n\nEnter E to open file. ")
    print("Enter C to create a new file. ")
    print("Enter W to write to an existing file. ")
    print("Enter X to delete file. Must restart program if recently created. ")
    print("Enter D to create new directory/folder. ")
    print("Enter P to print the files and folders in a directory")
    print("Enter Z to delete a folder/directory")
    print("Enter Q to quit. ")
    

    option = str(input("\nEnter an option. \n"))
    
    if option == "q" or option ==  "Q":
        quit()

    elif option == "z" or option == 'Z':
        currDir = "E:\\"
        os.chdir(currDir)
        selectionC = str(input("Default directory is ({}), change directory? Y(yes) or N(no). CANNOT BE ROOT DIRECTORY.\n".format(currDir)))
        if selectionC == 'Y' or selectionC == 'y':
            newDir = str(input("Enter new directory. "))
            os.chdir(newDir)
            print("New directory is {}. ".format(newDir))
        elif selectionC == "n" or selectionC == "N":
            pass
        else:
            print("invalid entry: returning to menu. \n")
            continue
        folderName = str(input("Enter folder name to delete. \n"))
        if os.path.exists(folderName):
            if len(os.listdir(folderName)) == 0:
                os.rmdir(folderName)
                print("You have deleted folder {} in directory {}.\n".format(folderName, currDir))
            else:
                print("Folder must be empty before deleting\n")
        else:
            print("Folder not found. \n")


    elif option == "p" or option == "P":
        currDir = "E:\\"
        os.chdir(currDir)
        selectionC = str(input("Default directory is ({}), change directory? Y(yes) or N(no). CANNOT BE ROOT DIRECTORY.\n".format(currDir)))
        if selectionC == 'Y' or selectionC == 'y':
            newDir = str(input("Enter new directory. "))
            os.chdir(newDir)
            print("New directory is {}. ".format(newDir))
        elif selectionC == "n" or selectionC == "N":
            pass
        else:
            print("invalid entry: returning to menu. \n")
            continue #Ivan Figueroa
            
        cwd = os.getcwd()
        files = os.listdir(cwd)

        selection = str(input("Print text files only? Enter Y or N"))
        if selection == "y" or selection == "Y":
            for f in files:
                if ".txt" in f:
                    print(f)
        elif selection == 'n' or selection == 'N':
            for f in files:
                print(f)
        else:
            print("Invalid entry: returning to menu. \n")
            continue


    elif option == "x" or option == "X":
        currDir = "E:\\"
        os.chdir(currDir)
        selectionC = str(input("Default directory is ({}), change directory? Y(yes) or N(no). CANNOT BE ROOT DIRECTORY.\n".format(currDir)))
        if selectionC == 'Y' or selectionC == 'y':
            newDir = str(input("Enter new directory. "))
            os.chdir(newDir)
            print("New directory is {}. ".format(newDir))
        elif selectionC == "n" or selectionC == "N":
            pass
        else:
            print("invalid entry: returning to menu. \n")
            continue
        fileName = str(input("Type the file name to delete. \n")) + ".txt"
        if os.path.exists(fileName):
            os.remove(fileName)
            print("file {} has been deleted. \n".format(fileName))
        else:
            print("The file does not exist.")
    
    
    elif option == "w" or option ==  "W":
        currDir = "E:\\"
        os.chdir(currDir)
        
        selection = str(input("Default directory is ({}), change directory? Y(yes) or N(no). \n".format(currDir)))
        if selection == 'Y' or selection == 'y':
            newDir = str(input("Enter new directory. "))
            os.chdir(newDir)
            print("New directory is {}. ".format(newDir))
        elif selection == "n" or selection == "N":
            pass
        else:
            print("invalid entry: returning to menu. \n")
            continue
        
        selectionW = str(input("Append content to file or overwrite file? Press a(append) or w(overwrite). \n"))

        if selectionW == 'w' or selectionW == 'W':
            fileName = str(input("Enter the file name: ")) + ".txt"
            f = open(fileName, "w")
            overWrite = str(input("Type content to overwrite to file. \n"))
            f.write(overWrite)
            f.close()
            print("Your entry has overwritten the file {}.".format(fileName))
            
        elif selectionW == 'a' or selectionW == 'A':
            fileName = str(input("Enter the file name: ")) + ".txt"
            f = open(fileName, "a")
            append = str(input("Type content to append to file. \n"))
            f.write(append)
            f.close()
            print("Your entry has been appended to the file {}.\n".format(fileName))


    elif option == "c" or option ==  "C":
        currDir = "E:\\"
        os.chdir(currDir)
        selectionC = str(input("Default directory is ({}), change directory? Y(yes) or N(no). CANNOT BE ROOT DIRECTORY\n".format(currDir)))
        if selectionC == 'Y' or selectionC == 'y':
            newDir = str(input("Enter new directory. "))
            os.chdir(newDir)
            print("New directory is {}. ".format(newDir))
        elif selectionC == "n" or selectionC == "N":
            pass
        else:
            print("invalid entry: returning to menu. \n")
            continue
            
        fileName = str(input("Please type the new file name: \n")) + ".txt"
        open(fileName, 'x')
        cwd = os.getcwd()  #Ivan Figueroa's project
        print("You have created a new file named {} in {}. ".format(fileName, cwd))


    elif option == "e" or option ==  "E":
        currDir = "E:\\"
        os.chdir(currDir)
        
        selectionE = str(input("Default directory is ({}), change directory? Y(yes) or N(no). \n".format(currDir)))
        if selectionE == 'Y' or selectionE == 'y':
            newDir = str(input("Enter new directory. "))
            os.chdir(newDir)
            print("New directory is {}. ".format(newDir))

        elif selectionE == "n" or selectionE == "N":
            pass
        else:
            print("invalid entry: returning to menu. \n")
            continue

        fileName = str(input("Type the file name to open\n\n")) + ".txt"
        f = open(fileName, "r")
        print(f.read())
        print(" \n")


    elif option == "d" or option ==  "D":
        currDir = "E:\\"
        os.chdir(currDir)
        
        selectionD = str(input("Default directory is ({}), change directory? Y(yes) or N(no). \n".format(currDir)))
        if selectionD == 'Y' or selectionD == 'y':
            newDir = str(input("Enter new directory. "))
            os.chdir(newDir)
            print("New directory is {}. \n".format(newDir))

        elif selectionD == "n" or selectionD == "N":
            pass
        else:
            print("invalid entry: returning to menu. \n")
            continue
            
        folderName = str(input("Enter a name for new folder. \n"))
        cwd = os.getcwd()
        os.mkdir(folderName)
        print("You have created a new folder named {} in {} \n".format(folderName, cwd))
    else:
        print("invalid entry: returning to menu. \n")
        continue
        



    


    
    
