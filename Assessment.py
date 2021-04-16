import bs4
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen
import time
start_time= time.time()


my_url = 'https://news.ycombinator.com'

# opening url and grabbing the web page
hacker = urlopen(my_url)
page_html = hacker.read()
hacker.close()

# parsing the web page
page_soup = soup(page_html, 'html.parser')

# grabbing all containers with href
containers = page_soup.findAll(href=True)
print("mumber of times href appears: ", len(containers))

#grabbing all containers with class = storylink
storylink = page_soup.findAll('a', {'class':"storylink"})
print("number of stories: ", len(storylink))

#creating a url list and grabbing the urls from the code and appending it to the list
url_list = []
for item in storylink:
    url_list.append(item['href'])
print(url_list)
#printing the time of execution
print("code executed in: ")
print("--- %s seconds ---" % (time.time() - start_time))












