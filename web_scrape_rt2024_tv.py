import requests
#Necessary imports for webscraping. 
from web_scrape_rt2023_movie import RT_main

class RT_page5(RT_main):
#Function to write out html formatting for webscraping. 
    def __init__(self):
        """
        Function: 
            Attribute: 
            rt_url(url): Html docmunet that is being parsed. 
            access_check(int): Checks if a page is accessible. 
            page_contents(): Page related information that gets fed into BeautifulSoup for our custom parsing. 
            -Intializes the associated elements of the web page. 
            Returns: 
                -List of all critic consensus reviews. 
        """ 
        self.rotten_tomato_url24 ='https://editorial.rottentomatoes.com/guide/best-tv-shows-of-2024/'
        self.access_check = requests.get(self.rotten_tomato_url24)
        self.page_contents = self.access_check.text

    def get_html(self):
        """
        Function: 
            Attribute: 
            rt_doc(html): Html docmunet that is being parsed. 
            -Gets an html document page associated with the rotten tomato webiste page. 
            Returns: 
                -An html document to pass through our web scraping class. 
        """
        with open('rt2024_tv_webpage.html', 'w') as f:
            f.write(self.page_contents)
    #Using BeautifulSoup Library to grab html parsing. 
            from bs4 import BeautifulSoup
            rt_doc = BeautifulSoup(self.page_contents, 'html.parser')
        return rt_doc

    def get_movie_title(self, rt_doc):
        """
        Function: 
            Attribute: 
            rt_doc(html): Html docmunet that is being parsed. 
            -Gets all of the titles of the movies. 
            Returns: 
                -List of all the movie titles. 
        """
        movie_name=[]
        movie_name_tags=rt_doc.find_all('div',{'class':"article_movie_title"})
        for tag in movie_name_tags:
            name = tag.find('a').text
            movie_name.append(name) 
        return movie_name
    
    def get_movie_year(self, rt_doc): 
        """
        Function: 
            Attribute: 
            rt_doc(html): Html docmunet that is being parsed. 
            -Gets all of associated movie release years. 
            Returns: 
                -List of the movies' associated release years. 
        """ 
        movie_year=[]      
        movie_year_tags=rt_doc.find_all('span',{'class':"subtle start-year"})
        for tag in movie_year_tags:
            movie_year.append(tag.get_text().strip())
        return movie_year
    
    def get_stars(self, rt_doc):
        """
        Function: 
            Attribute: 
            rt_doc(html): Html docmunet that is being parsed. 
            -Gets all of the associated cast members . 
            Returns: 
                -List of all cast. 
        """
        movie_star_list=[]
        movie_star_tags=rt_doc.find_all('div',{'class':"info cast"})
        for tag in movie_star_tags:
            duration = tag.text[:]
            movie_star_list.append(duration.strip('\n'))
        return movie_star_list
    
    def get_rating(self, rt_doc):
        """
        Function: 
            Attribute: 
            rt_doc(html): Html docmunet that is being parsed. 
            -Gets all of the associated movie reviewed score values. 
            Returns: 
                -List of all the movie scores. 
        """
        movie_rating=[]           
        movie_rating_tags=rt_doc.find_all('span',{'class':"tMeterScore" })
        for tag in movie_rating_tags:
            movie_rating.append(tag.get_text().strip('%'))
        return movie_rating

    def get_critic_consensus(self, rt_doc): 
        """
        Function: 
            Attribute: 
            rt_doc(html): Html docmunet that is being parsed. 
            -Gets all of the critic reviews of the listed movies of 2023.
            Returns: 
                -List of all critic consensus reviews. 
        """ 
        critic_listing=[]          
        movie_summary_tags=rt_doc.find_all('div',{'class':"info critics-consensus"})
        for tag in movie_summary_tags:
            critic_listing.append(tag.get_text().strip())
        return critic_listing

import pandas as pd

#Driver code to collect data for database.
page5 = RT_page5()
page_content = page5.get_html()
name = page5.get_movie_title(page_content)
year = page5.get_movie_year(page_content)
stars = page5.get_stars(page_content)
movie_score = page5.get_rating(page_content)
consensus = page5.get_critic_consensus(page_content)       
    
#Storing data in a dictionary. 
movie_catalog={
    'Name':name,
    'Year':year,
    'Starring':stars,
    'Rating':movie_score,
    'Critic Consensus':consensus
}

#Transposing dictionary to a csv table. 
movie_data = pd.DataFrame.from_dict(movie_catalog, orient='index')
movie_data=movie_data.transpose()
movie_data.to_csv('page5_RT_2024_tvscraping.csv')