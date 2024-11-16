from bs4 import BeautifulSoup

with open("C:/Users/Mizan/Documents/Code/PyPrjct/Projects/Legal/Web/home.html",'r') as scrape_file:
    content=scrape_file.read()
    #print(content)
    soup = BeautifulSoup(content,'lxml')
    #print(soup)
    print('\n'*10)
    #print(soup.prettify())
    p_tags=soup.find_all('p') 
    print (x for x in list(p_tags)) 