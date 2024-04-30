from time import asctime
from avito_parser import Get_A_Page, GetData
from os import listdir
def write_to_json(finally_search):
    data=finally_search
    time=str(asctime()).lower()
    list_main_info=['rooms', 'floor', 'size']
    other_info=[None,'price', 'link']
    value =len(data[0])
    w=dict({x:{'rooms':None, 'floor':None, 'size':None, 'price':None, 'link':None} for x in range(value)})
    for x in range(len(w)):
        for main in range(len(list_main_info)):
            w[x][list_main_info[main]]=data[0][x][main]
        for other in range(1, len(other_info)):
            w[x][other_info[other]]=data[other][x]
    w['Time']=time
    del value, list_main_info, other_info, data, time
    with open('result.json', 'w', encoding='utf-8') as json_file:
        json_file.write('"')
        json_file.write(str(w))
        json_file.write('"')
#a little clarification: this code was written in Python 3.5.3 on Windows 7, and for some reason absolutely incomprehensible to me, and I had enough time to figure it out to figure it out, which is what I did, json had a problem with the encoding and so I had to  to resort to such a crutch, this is the first time lol 




        
