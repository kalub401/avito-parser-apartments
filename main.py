from json_writer import *
CITY='penza'
PAGES=2         #no 1, cause pages going from 1
HEADERS={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; rv:109.0) Gecko/20100101 Firefox/115.0'}


def main():
    for x in range(1, PAGES):
        Get_A_Page(CITY, HEADERS).get_html(x)
path=Get_A_Page(CITY).html_path
html_files=listdir(path)
for data in html_files:
    write_to_json(GetData(CITY).search(path+'\\'+data))

if __name__=="__main__":
	main()
