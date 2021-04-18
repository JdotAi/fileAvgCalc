def averager(valList):
    if valList==0:
        return 0
    # Here we say if the there was 0 data we return 0
    else:
        total = 0
        divisor=len(valList)
        for i in valList:
            total +=float(i)
            # since the data was a string and we want floats
            # I did the convertion of string to float here
            # and then stored the total of the data in total

        final = total/divisor
        return final
    # here we the average calculation

def data2listMaker(filename):
    fm = open(filename)
    # Here I took the FILE NAMES that were given to me and
    # I now opened up the file with all of the data to fine the average

    rows = fm.readlines()[1:]
    # The reason why I did [1:] is BECAUSE in all of the files the FIRST
    # line had information that was not needed so you can change that to
    # whatever line all of the information. If there is no unnessary information
    # than you can REMOVE [1:]
    if len(rows)==0:
        return 0
    # Some of the files that I got did not have any data in it so if
    # there is no data in the bach of files than we are going to skip over it
    else:
        newInfo= rows[0]
        # I had all of my data on the second line of the origal file
        # since I had already started to read from the second line and we
        # only had one line of all of all of the data so I just took the first
        # row to interpert the data.

        intInfo= newInfo.split(' ')
        # In the file I was working on with it
        # it was one long string with all of the data and was sperated by space
        # so that is why I did .split(' ') that way that string can split
        # up by spaces between the data and and can be stored into the list

        changer= intInfo.pop()
        # In the files that I got the original file had a new line at the end of the data

        changer=changer.split('\n')
        # As a result since the author had a new line at the end of the file I added
        # a split by new line : split('\n') so that it removes the new line at the
        # at the end of the file

        intInfo.append(changer[0])
        # And then we put that new data that we striped the new /n line from back into
        # the origial list

        return intInfo



def mainFile():
    textFiles = open("files_names.txt").read().split('\n')
    # splits at each line since the name of the next file is
    # put after each line. Here it already stores all of the
    # file names in a list

    for files in textFiles:
        final=averager(data2listMaker(files))
        print(final, "File name:",files)
    # Here we go through the list of file and perform the
    # action we want to it


    #for i in fileNames:
        #print(averager('S14002_tcksample_r_vta_alic_fa.txt'))
        # print(i)


mainFile()

# fm = open('S14002_tcksample_r_vta_alic_fa.txt')
# rows = fm.readlines()[1:]
# new_items = []
# stor = 0
# final = 0
# for item in rows:
#     new_items.extend(item.split())
# for i in range(len(new_items)):
#     stor+=float(new_items[i-1])
# final = stor/len(new_items)
# print (final)


# stor = 0
# length= len(filename)
# for item in rows:
#     new_items.extend(item.split())
#     for i in range(len(new_items)):
#         stor+=float(new_items[i-1])
#     averager(stor , length)
#
# return final, length
