def averager(valList):
    if valList==0:
        return 0
    else:
        total = 0
        length=len(valList)
        for i in valList:
            total +=float(i)
        final = total/length
        return final

def listMaker(filename):
    fm = open(filename)
    rows = fm.readlines()[1:]
    if len(rows)==0:
        return 0
    else:
        newInfo= rows[0]

        intInfo= newInfo.split(' ')
        changer= intInfo.pop()
        changer=changer.split('\n')
        intInfo.append(changer[0])
        new_items=[]
        for item in intInfo:
            new_items.append(item)
        return new_items



def main():
    textFiles = open("files_names.txt").read().split('\n')
    fileNames=[]

    for files in textFiles:
        fileNames.append(files)
    print(textFiles)
    for i in textFiles:
        final=averager(listMaker(i))
        print(final)

    #for i in fileNames:
        #print(averager('S14002_tcksample_r_vta_alic_fa.txt'))
        # print(i)


main()

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
