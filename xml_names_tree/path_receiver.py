# создает полное дерево со всеми названиями тестов
import xml.etree.ElementTree as ET

collection_branch1 = ''
collection_branch2 = ''
collection_branch3 = ''
collection_branch4 = ''
collection_branch5 = ''
tree1 = ''

tree = ET.parse(r'C:\avs\Utilities\Template_generator\For DWNT From XML\Main_Buf_v0.1_Report[11 47 43][19.05.2023].xml')
root = tree.getroot()
branch0 = root.tag + '\n'
in_branch = root.attrib

#print(111, root.tag,111, root.attrib)
for branch1 in root:
    # i = 0
    # word = branch1.tag
    # for a in word:
    #     if word[i] != '}':
    #         c = branch1.tag[i]
    #         name_branch1 = word.replace(c, "")
    #     i = i + 1
    #     print(i)
    # print(word)
    # print(name_branch1, 11111111111111111111)

    # fullstring = collection_branch1
    # substring = branch1.tag
    # if substring in fullstring:
    #     a = 1
    # else:

    collection_branch1 = collection_branch1 + ('}'.join(branch1.tag.split('}')[-1:])) + '\n'

    print(type(branch1.tag))
    print(type(collection_branch1))
    print(type('112dfcd'), 1111, collection_branch1+branch1.tag+'112dfcd')
    # collection_branch1 = branch1.tag.split('}')[:-1]
    print(branch1.tag)
    print('}'.join(branch1.tag.split('}')[-1:])) #ОХРЕНЕЕЕЕЕЕЕЕЕЕТЬ, ЭТА ШТУКА УДАЛЯЕТ ТО ДЕРЬМО!!!!!!!!!!!
    for branch2 in branch1:
        # fullstring = collection_branch2
        # substring = branch2.tag
        # if substring in fullstring:
        #     a = 1
        # else:

        collection_branch2 = collection_branch2 + ('}'.join(branch2.tag.split('}')[-1:])) + '\n'

        for branch3 in branch2:
            in_branch3 = branch3.attrib
            if 'name' in in_branch3:
                if '}'.join(branch3.tag.split('}')[-1:]) == 'SystemOperator':
                    a = 1
                else:
                    tree1 = tree1 + ('}'.join(branch1.tag.split('}')[-1:])) + ' -> ' + ('}'.join(branch2.tag.split('}')[-1:])) \
                        +' -> ' + ('}'.join(branch3.tag.split('}')[-1:])) +' -> ' + in_branch3['name'] + '\n'
            # fullstring = collection_branch3
            # substring = branch3.tag
            # if substring in fullstring:
            #     a = 1
            # else:
            #collection_branch3 = collection_branch3 + branch3.tag + '\n'

            # for branch4 in branch3:
            #     collection_branch4 = collection_branch4 + branch4.tag + '\n'
            #
            #     for branch5 in branch4:
            #         collection_branch5 = collection_branch5 + branch5.tag + '\n'

# collection_branch1 = collection_branch1 + '\n'
# collection_branch2 = collection_branch2 + '\n'
# collection_branch3 = collection_branch3 + '\n'
# collection_branch4 = collection_branch4 + '\n'
# collection_branch5 = collection_branch5 + '\n'
# type(branch2.tag)
# print(collection_branch1,11111111111111111111111111111111111111111)
my_file = open("appletree1.txt", "w+")
my_file.write(tree1)

my_file.close()