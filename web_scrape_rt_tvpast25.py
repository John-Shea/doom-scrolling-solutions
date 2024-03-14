import requests
from web_scrape_rt2023_movie import RT_main
#Necessary imports for webscraping.

class RT_page2(RT_main):
    def __init__(self):
        self.rt_url = 'https://editorial.rottentomatoes.com/guide/rt25-critics-top-tv-shows-of-the-last-25-years-2/'
        self.access_check = requests.get(self.rt_url)
        self.page_contents = self.access_check.text
#Function to write out html formatting for webscraping. 
    from bs4 import BeautifulSoup
    def get_html(self):
        with open('rt25_tv_webpage.html', 'w') as f:
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
            stars = tag.text[:]
            movie_star_list.append(stars.strip("\n"))
        return movie_star_list

    def get_rating(self, rt_doc):     
        movie_rating=[]    
        movie_rating_tags=rt_doc.find_all('span',{'class': "tMeterScore" })
        for tag in movie_rating_tags:
            movie_rating.append(tag.get_text().strip('%'))
        return movie_rating

    def get_synopsis(self, rt_doc):           
        movie_summary_tags=rt_doc.find_all('div',{'class':"info synopsis"})
        summary_listing=[]
        for tag in movie_summary_tags:
            summary_listing.append(tag.get_text().strip())
        return summary_listing

import pandas as pd

#Driver Code
page2 = RT_page2()
page_content = page2.get_html()
name = page2.get_movie_title(page_content)
year = page2.get_movie_year(page_content)
stars = page2.get_stars(page_content)
movie_score = page2.get_rating(page_content)
summary = page2.get_synopsis(page_content)

movie_catalog={
    'Name':name,
    'Year':year,
    'Starring':stars,
    'Rating':movie_score,
    'Synopis':summary
}

movie_data = pd.DataFrame.from_dict(movie_catalog, orient = 'index')
movie_data=movie_data.transpose()
movie_data.to_csv('page2_rt25_tv_web_scraping.csv')
print(movie_data)