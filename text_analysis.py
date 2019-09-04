from csv import DictReader
from textblob import TextBlob
from itertools import combinations

import csv




'''
def tagger(names, character_mapping):
    character_mapping = [('Frodo', 'Samyise Gangee'), ('Frodo', 'Gandalf'), ('Frodo','Sauron'), ('Frodo','Bilbo'),('Samyise Gangee','Gandalf'),('Samyise Gangee','Sauron'),('Samyise Gangee','Bilbo'),('Gandalf','Sauron'),('Gandalf', 'Bilbo'),('Sauron', 'Bilbo')]
    names = {
        'Frodo': ['Frodo','Master','Ring-bearer','Mr. Underhill', 'The Halfling', "Iorhael"],
        'Samvise Gangee': ['Samvise Gangee','Sam', 'Samvise'],
        'Gandalf': ['Gandalf',"Mithrandir","Olórin","Greyhame","Stormcrow"],
        'Sauron': ['Sauron',"Gorthaur","Necromancer","the Abhorred Dread","Nameless Enemy","Lord of Mordor"],
        'Bilbo': ['Bilbo','Burglar']
    }
    final_result = {}
    with open("file.txt", 'r') as f:
        lines = f.read()

    texts = lines.split("\n\n")
    first_name = list()
    second_name = list()
    all_alt_names = dict()
    all_names = list()
    name_paragph = dict()
    for x in character_mapping:
        for key, value in names.items():
            if(x[0] == key):
                if names[x[0]] not in first_name:
                    all_names.append(names[x[0]])
            if(x[1] == key):
                if names[x[1]] not in second_name:
                    all_names.append(names[x[1]])
    for y in range(len(all_names)-1):
        all_alt_names[all_names[y].split()[0]] = all_names[y].split(',')
    for y in second_name:
        if(j< len(second_name)-1):
            all_alt_names[j] = y[j].split()
            j = j + 1
    for para in texts:
        for x in character_mapping:
            if x[0] in names and x[1] in names:
                first_name.extend(names[x[0]])
                second_name.extend(names[x[1]])
            if(x[0] == key):
                if names[x[0]] not in first_name:
                    first_name.append(names[x[0]])
            if(x[1] == key):
                if names[x[1]] not in second_name:
                    second_name.append(names[x[1]])
            for name in first_name:
                for sname in second_name:
                    if name in para and sname in para:
                        if x not in name_paragph:
                            name_paragph[x] = para
                        else:
                            name_paragph[x]= str(name_paragph[x]) + para
            first_name.clear()
            second_name.clear()
            final_result[key] = paragraph.sentiment.polarity
    print(final_result)
def mapping():
    all_names = list()
    character_mapping = list()
    with open('names.csv', 'r', encoding='utf-8') as csvfile:
        reader = DictReader(csvfile)
        data = [dict(x) for x in reader]

    for row in data:
        all_names.append((row['Name']))
    character_mapping.extend(list(combinations(all_names, 2)))
    return character_mapping

def name_meaning():
    name_mean = dict()
    with open('names.csv', 'r', encoding='utf-8') as csvfile:
        reader = DictReader(csvfile)
        data = [dict(x) for x in reader]
    for row in data:
        name_mean[row['Name']] = row['Alternative name']
    return name_mean

def get_name_paragraph(names, character_mapping):
    first_name = list()
    second_name = list()
    for x in names:
        for key, value in character_mapping.items():
            if(x[0] == key):
                first_name.append(character_mapping[x[0]])
            if(x[1] == key):
                second_name.append(character_mapping[x[1]])
    print(first_name)

character_mapping = mapping()
names = name_meaning()

tagger(names, character_mapping)
'''
def name_meaning():
    name_mean = dict()
    with open('names.csv', 'r', encoding='utf-8') as csvfile:
        reader = DictReader(csvfile)
        data = [dict(x) for x in reader]
    for row in data:
        name_mean[row['Name']] = row['Alternative name'].split(',')
    return name_mean

def mapping():
    all_names = list()
    character_mapping = list()
    with open('names.csv', 'r', encoding='utf-8') as csvfile:
        reader = DictReader(csvfile)
        data = [dict(x) for x in reader]

    for row in data:
        all_names.append((row['Name']))
    character_mapping.extend(list(combinations(all_names, 2)))
    return character_mapping
def senti(mapping, name_meaning):
    list1 = list()
    list2 = list()
    all_names_para = dict()
    names_sentiment = dict()
    count_name= dict();
    with open("tfile.txt", 'r') as f:
        lines = f.read()
    text = lines.split("\n\n")

    for name in mapping:
        if name[0] and name[1] in name_meaning:
            list1.append(name_meaning[name[0]])
            list2.append(name_meaning[name[1]])
            for name1 in list1:
                for one in name1:
                    for name2 in list2:
                        for two in name2:
                            for para in text:
                                if two in para and one in para:
                                    if (name1[0], name2[0]) in all_names_para or (name2[0], name1[0]) in all_names_para:
                                        all_names_para[(name1[0], name2[0])] = str(all_names_para[(name1[0], name2[0])]) +'\n\n'+ para
                                    else:
                                        all_names_para[(name[0], name2[0])] = para
                                    if (name1[0], name2[0]) in count_name or (name2[0], name1[0]) in count_name :
                                        count_name[(name1[0], name2[0])] = count_name[(name1[0], name2[0])] + 1
                                    else:
                                        count_name[(name1[0], name2[0])] = 1
            list1.clear()
            list2.clear()
    for key, value in all_names_para.items():
        paragraph = TextBlob(value)
        names_sentiment[key] = paragraph.sentiment.polarity 

    for key, value in all_names_para.items():
        row = [key, value]
        with open('paragraph_name.csv', 'a') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow(row)
            csvFile.close()


    for key,value in  names_sentiment.items():
        row = [key, value]
        with open('result.csv', 'a') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow(row)
            csvFile.close()






    for key, value in count_name.items():
        row = [key, value]
        with open('results.csv', 'a') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow(row)
            csvFile.close()








    '''for para in text:'''
def count_name(name_meaning):

    count = dict()
    list1 = list()
    with open('names.csv', 'r', encoding='utf-8') as csvfile:
        reader = DictReader(csvfile)
        data = [dict(x) for x in reader]
    with open("tfile.txt", 'r') as f:
        lines = f.read()
    text = lines.split("\n\n")
    for row in data:
        list1.append(row['Alternative name'].split(','))
    for name in list1:
        for nm in name:
            for para in text:
                if nm in para:
                    if name[0] not in count:
                        count[name[0]] = 1
                    else:
                        count[name[0]] = count[name[0]] + 1
    for key, value in count.items():
        row = [key, value]
        with open('character count.csv', 'a') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow(row)
            csvFile.close()
name_meaning = name_meaning()
mapping = mapping()
senti(mapping, name_meaning)

'''count_name(name_meaning)'''


