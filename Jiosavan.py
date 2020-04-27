import requests,pprint
from bs4 import BeautifulSoup
import webbrowser
print("\n \n \t \t \t \t \033[1;31m* *  \033[1;m'+'%s}    JIOSAVAN.com      \U0001F3B5 '+'\033[1;31m  * *\033[1;m'+")
responce=requests.get('https://www.jiosaavn.com/').text
soup=BeautifulSoup(responce,'html.parser')
ul=soup.find('ul')
new_list=[]
all_li=ul.find_all('li')
def languages():
    num=1
    for i in all_li:
        i_=i.text
        print(num,".",i_)
        new_list.append("https://www.jiosaavn.com/"+"new-releases/"+i_.lower())
        num+=1  
languages()

ask_for_lang=int(input("\n \t \t \033[1;34mWhich language do you like :) \033[1;m"))

neded_lang=new_list[ask_for_lang-1]
responce2=requests.get(neded_lang).text
soup4=BeautifulSoup(responce2,'lxml')
albums_link=[]
divs=soup4.findAll('div',class_='art-wrap')
# print(soup4.prettify())
para=soup4.findAll("p")
def newrelese():
    count_para=0
    for p in para:
        if count_para==0 or len(para)-1==count_para:
            pass
        else:
            print(count_para,".", p.text)
        count_para+=1
    for A in  divs:
        albums_link.append(A.a['href'])

newrelese()

ask_for_song=int(input("\n \t \t \033[1;35mWhich song do you want to play ? >\033[1;m"))
neded_song=albums_link[ask_for_song-1]

play=webbrowser.open(neded_song)
print(play)
print("\033[1;31m* *  \033[1;m'+'%s} enjoy the music \U0001F3B5 '+'\033[1;31m  * *\033[1;m'+")