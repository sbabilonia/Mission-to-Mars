#!/usr/bin/env python
# coding: utf-8

# In[41]:


# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd


# In[21]:


executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# In[17]:


#Visit the Mars Nasa Website
url = 'https://redplanetscience.com'
browser.visit(url)

#delay for page loading
browser.is_element_present_by_css('div.list_text', wait_time=1)


# In[5]:


# set up bs4 object
html = browser.html

#create a html parser
news_soup = soup(html, 'html.parser')

#create parent element, holds all other elements inside
# '.' is used to select classes, pinpoints <div /> with class list_text
slide_elem = news_soup.select_one('div.list_text')


# In[7]:


slide_elem.find('div', class_='content_title')


# In[8]:


#.find() is used when we want only the first class and attribute we've specified.
#.find_all() is used when we want to retrieve all of the tags and attributes

news_title = slide_elem.find('div', class_='content_title').get_text()
news_title


# In[10]:


article_teaser = slide_elem.find('div', class_='article_teaser_body').get_text()

article_teaser


# ### Featured Images

# In[24]:


#visit url
url = 'https://spaceimages-mars.com'
browser.visit(url)


# In[32]:


#find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click


# In[34]:


# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')


# In[38]:


#find the relative image url
img_url_rel = img_soup.find('img', class_='headerimage fade-in').get('src')

img_url_rel


# In[39]:


img_url = f'https://spaceimages-mars.com/{img_url_rel}'

img_url


# In[40]:


#visit url 
url = 'https://galaxyfacts-mars.com/'
browser.visit(url)


# In[48]:


#Scrape the table with pandas; pd.read_html()
#Creates a new df from html table
#pd.read_html() specifically searches for and returns a list of tables found in the html; index = [0] to store 1st list
#inplace = True: updated index will remain in place w/o having to reassign the df to a new variable

df = pd.read_html('https://galaxyfacts-mars.com/')[0]
df.columns = ['Description', 'Mars', 'Earth']
df.set_index('Description', inplace=True)
df


# In[49]:


# return df to html; .to_html()

df.to_html()


# In[50]:


#close the browser
browser.quit()


# In[ ]:




