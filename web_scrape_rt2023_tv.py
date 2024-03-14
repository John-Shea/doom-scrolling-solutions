import requests
#Necessary imports for webscraping.
from web_scrape_rt2023_movie import RT_main 

class RT_page4(RT_main):
    def __init__(self):
        self.rotten_tomato_url23 ='https://editorial.rottentomatoes.com/guide/best-tv-shows-of-2023/'
        self.access_check = requests.get(self.rotten_tomato_url23)
        self.page_contents = self.access_check.text
#Function to write out html formatting for webscraping. 
    def get_html(self):
        with open('rt2023_webpage.html', 'w') as f:
            f.write(self.page_contents)
    #Using BeautifulSoup Library to grab html parsing. 
            from bs4 import BeautifulSoup
            rt_doc = BeautifulSoup(self.page_contents, 'html.parser')
        return rt_doc

    def get_movie_title(self, rt_doc):
        movie_name=[]
        movie_name_tags=rt_doc.find_all('div',{'class': "article_movie_title"})
        for tag in movie_name_tags:
            name = tag.find('a').text
            movie_name.append(name) 
        return movie_name

    def get_movie_year(self, rt_doc): 
        movie_year=[]         
        movie_year_tags=rt_doc.find_all('span',{'class':"subtle start-year" })
        for tag in movie_year_tags:
            movie_year.append(tag.get_text().strip())
        return movie_year
    
    def get_stars(self, rt_doc):
        movie_star_list=[]
        movie_star_tags=rt_doc.find_all('div',{'class':"info cast"})
        for tag in movie_star_tags:
            duration = tag.text[:]
            movie_star_list.append(duration.strip('\n'))
        return movie_star_list

    def get_rating(self, rt_doc):     
        movie_rating=[]      
        movie_rating_tags=rt_doc.find_all('span',{'class': "tMeterScore" })
        for tag in movie_rating_tags:
            movie_rating.append(tag.get_text().strip('%'))
        return movie_rating

    def get_critic_consensus(self, rt_doc):
        critic_listing=[]           
        movie_summary_tags=rt_doc.find_all('div',{'class':"info critics-consensus" })
        for tag in movie_summary_tags:
            critic_listing.append(tag.get_text().strip())
        return critic_listing
    
import pandas as pd

page4 = RT_page4()
page_content = page4.get_html()
name = page4.get_movie_title(page_content)
year = page4.get_movie_year(page_content)
stars = page4.get_stars(page_content)
movie_score = page4.get_rating(page_content)
consensus = page4.get_critic_consensus(page_content)

movie_catalog={
        'Name':name,
        'Year':year,
        'Starring':stars,
        'Rating':movie_score,
        'Critc Consensus':consensus
    }

movie_data = pd.DataFrame.from_dict(movie_catalog, orient='index')
movie_data=movie_data.transpose()
movie_data.to_csv('page4_rttv2023_web_scraping.csv')
print(movie_data)
