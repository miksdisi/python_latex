# создает полное дерево со всеми названиями тестов
import xml.etree.ElementTree as ET
a = 1
collection_branch1 = ''
collection_branch2 = ''
collection_branch3 = ''
collection_branch4 = ''
collection_branch5 = ''
tree = ET.parse(r'C:\avs\Utilities\Template_generator\For DWNT From XML\Main_Buf_v0.1_Report[11 47 43][19.05.2023].xml')
root = tree.getroot()
branch0 = root.tag + '\n'
#print(111, root.tag,111, root.attrib)
for branch1 in root:
    # fullstring = collection_branch1
    # substring = branch1.tag
    # if substring in fullstring:
    #     a = 1
    # else:
    #     collection_branch1 = collection_branch1 + branch1.tag + '\n'
    for branch2 in branch1:
        # fullstring = collection_branch2
        # substring = branch2.tag
        # if substring in fullstring:
        #     a = 1
        # else:
        collection_branch2 = collection_branch2 + branch2.tag + '\n'
        for branch3 in branch2:
            # fullstring = collection_branch3
            # substring = branch3.tag
            # if substring in fullstring:
            #     a = 1
            # else:
            collection_branch3 = collection_branch3 + branch3.tag + '\n'
            for branch4 in branch3:
                collection_branch4 = collection_branch4 + branch4.tag + '\n'

                for branch5 in branch4:
                    collection_branch5 = collection_branch5 + branch5.tag + '\n'

collection_branch1 = collection_branch1 + '\n'
collection_branch2 = collection_branch2 + '\n'
collection_branch3 = collection_branch3 + '\n'
collection_branch4 = collection_branch4 + '\n'
collection_branch5 = collection_branch5 + '\n'
print(branch1.tag)
my_file = open("appletree.txt", "w+")
my_file.write(branch0)
my_file.write(collection_branch1)
my_file.write(collection_branch2)
my_file.write(collection_branch3)
my_file.write(collection_branch4)
my_file.write(collection_branch5)
my_file.close()


#len(root.tag))