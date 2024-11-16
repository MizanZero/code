from bs4 import BeautifulSoup

tags = {} # 'tagName' : soup.find_all('tagName') ----> format 

with open("C:/Users/Mizan/Documents/Code/PyPrjct/Projects/Legal/Web/home.html",'r') as scrape_file:
    content=scrape_file.read()
    #print(content)
    soup = BeautifulSoup(content,'lxml')
    #print(soup)
    print('\n'*10)
    #print(soup.prettify())
    tags['p']=soup.find_all('p') 
    tags['h1'] = soup.find_all('h5') 

    def printTags(tag):
        tagName=tag
        tag = tags[tag]
        for x in list(tag):
            print(x)
            print()
        print("Number of",tagName,'tags is',len(tag))

    printTags('h1')

    tags()