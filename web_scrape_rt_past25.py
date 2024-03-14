import requests
from web_scrape_rt2023_movie import RT_main
#Necessary imports for webscraping.
class RT_page3(RT_main):
    def __init__(self):
        self.rotten_tomato_url25 = 'https://editorial.rottentomatoes.com/guide/rt25-critics-top-movies-of-the-last-25-years/'
        self.access_check = requests.get(self.rotten_tomato_url25)
        self.page_contents = self.access_check.text

#Function to write out html formatting for webscraping. from bs4 import BeautifulSoup
    def get_html(self):
        with open('rt25_movie_webpage.html', 'w') as f:
            f.write(self.page_contents)
            from bs4 import BeautifulSoup
            rt_doc= BeautifulSoup(self.page_contents, 'html.parser')
        return rt_doc

    def get_movie_title(self, rt_doc):
        movie_name=[]
        movie_name_tags=rt_doc.find_all('div',{'class':"article_movie_title"})
        for tag in movie_name_tags:
            name = tag.find('a').text
            movie_name.append(name) 
        return movie_name

    def get_movie_year(self, rt_doc):  
        movie_year=[]      
        movie_year_tags=rt_doc.find_all('span',{'class':"subtle start-year"})
        for tag in movie_year_tags:
                movie_year.append(tag.get_text().strip())
        return movie_year
    
    def get_rating(self, rt_doc): 
        movie_rating=[]         
        movie_rating_tags=rt_doc.find_all('span',{'class':"tMeterScore" })
        for tag in movie_rating_tags:
            movie_rating.append(tag.get_text().strip('%'))
        return movie_rating

    def get_critic_consensus(self, rt_doc):  
        critic_listing=[]       
        movie_summary_tags=rt_doc.find_all('div',{'class':"info critics-consensus" })
        for tag in movie_summary_tags:
            critic_listing.append(tag.get_text().strip())
        return critic_listing
    
    def get_synopsis(self, rt_doc):
        summary_listing=[]           
        movie_summary_tags=rt_doc.find_all('div',{'class':"info synopsis"})
        for tag in movie_summary_tags:
            summary_listing.append(tag.get_text().strip())
        return summary_listing
    
import pandas as pd

page3 = RT_page3()
page_content = page3.get_html()
name = page3.get_movie_title(page_content)
year = page3.get_movie_year(page_content)
consensus = page3.get_critic_consensus(page_content)
movie_score = page3.get_rating(page_content)
summary = page3.get_synopsis(page_content)
    
movie_catalog={
    'Name':name,
    'Year':year,
    'Rating':movie_score,
    'Critic Consensus':consensus,
    'Summary': summary
}

movie_data = pd.DataFrame.from_dict(movie_catalog, orient='index')
movie_data=movie_data.transpose()
movie_data.to_csv('page3_movie_web_scraping25.csv')
print(movie_data)