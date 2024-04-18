import requests
from web_scrape_rt2023_movie import RT_main
#Necessary imports for webscraping.

import requests
from web_scrape_rt2023_movie import RT_main
#Necessary imports for webscraping.

#Necessary imports for webscraping. 
import requests

#Class representing the first / main page of the application. 
class RT_main():
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
        self.rt_url ='https://editorial.rottentomatoes.com/guide/best-movies-of-2023/'
        self.access_check = requests.get(self.rt_url)
        self.page_contents = self.access_check.text

#Function to write out html formatting for webscraping. 
    def get_html(self):
        """
        Function: 
            Attribute: 
            rt_doc(html): Html docmunet that is being parsed. 
            -Gets an html document page associated with the rotten tomato webiste page. 
            Returns: 
                -An html document to pass through our web scraping class. 
        """
        #While the created html page is open...
        with open('rt2023_movie_webpage.html', 'w') as f:
            #Function to write the page contents of the website into the new html page. 
            f.write(self.page_contents)
            #Necessary library for web scraping. 
            from bs4 import BeautifulSoup
            #Creates a variable that we will parse for the html page. 
            rt_doc = BeautifulSoup(self.page_contents, 'html.parser')
        #Returns this html page to scrape. 
        return rt_doc

    #Functions below are fed the html document to parse for specfic elements. 

    def get_movie_title(self, rt_doc):
        """
        Function: 
            Attribute: 
            rt_doc(html): Html docmunet that is being parsed. 
            -Gets all of the titles of the movies. 
            Returns: 
                -List of all the movie titles. 
        """
        #Empty list to store titles of the movies. 
        movie_name=[]
        #Small function to find and store all movie titles in a variable. 
        movie_name_tags=rt_doc.find_all('div',{'class': "article_movie_title"})
        #Iterating over the elements...
        for tag in movie_name_tags:
            #Further finding tags with associated html text 
            name = tag.find('a').text
            #Adding the name of the movie to the growing list. 
            movie_name.append(name) 
        #Returns the list of movie names. 
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
        #Creating an empty list to store movie year releases. 
        movie_year=[]   
        #Small function to find all the years of release for each movie.     
        movie_year_tags=rt_doc.find_all('span',{'class':"subtle start-year" })
        #Iterating for the movie year releases. 
        for tag in movie_year_tags:
            #Stroing the values in the empty list and stripping trailing empty space. 
            movie_year.append(tag.get_text().strip())
        #Returns the list of movie release years. 
        return movie_year
    
    def get_rating(self, rt_doc): 
        """
        Function: 
            Attribute: 
            rt_doc(html): Html docmunet that is being parsed. 
            -Gets all of the associated movie reviewed score values. 
            Returns: 
                -List of all the movie scores. 
        """
        #Empty list to store ratings for each movie. 
        movie_rating=[]      
        #Function to to find all elements of movie scores and store in a variable.   
        movie_rating_tags=rt_doc.find_all('span',{'class': "tMeterScore"})
        #Iterating over the found movie reviews...
        for tag in movie_rating_tags:
            #Storing them in the list of movie ratings.
                #Getting the appropriate text and stripping the percent sign off value.
                #Note: Percent sign was causing type error later in application sorting. 
            movie_rating.append(tag.get_text().strip('%'))
        #Returns the list of movie reviews. 
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
        #Creating an empty list to store critic reviews. 
        summary_listing=[]     
        #Parsing html function to find and store all critc reviews into movie_summary_tags.      
        movie_summary_tags=rt_doc.find_all('div',{'class': "info critics-consensus"})
        #Iterates over the html rt_doc for all of the critic review elements presented on the website page. 
        for tag in movie_summary_tags:
            #Stores the found elements into the empty summary_list list.
                #Then...
                #Grabs the readable text and strips trailing blank space at end of elements.
            summary_listing.append(tag.get_text().strip())
        #Returns list of critic consensus reviews. 
        return summary_listing

#Necessary library for data list conversion to csv format.
import pandas as pd


##
#Driver code to collect page information. 
##

#Intializes class for this particular page. 
page1 = RT_main()
#Creates the html format for web scraping.
page_content = page1.get_html()
#Places collected movie names into variable name.
name = page1.get_movie_title(page_content)
#Places collected movies movie into a variable year.
year = page1.get_movie_year(page_content)
#Places movie ratings into a movie rating variable.
movie_score = page1.get_rating(page_content)
#Collects critic reviews into a summary variable. 
summary = page1.get_critic_consensus(page_content)

##
#Dictionary to collect list information for each category.
##

movie_catalog={'Name':name,'Year':year,'Rating':movie_score,'Critic Consensus':summary}
#Converts to a dataframe and helps orient for csv format. 
movie_data = pd.DataFrame.from_dict(movie_catalog, orient='index')
#Coverts 1D array into a 2D column format. Handles column formatting into csv. 
movie_data=movie_data.transpose()
#Saves collected movie data into a csv format. 
movie_data.to_csv('page_1_rt2023_web_scraping.csv')

#Test print to make sure elements are formatted correctly. 
print(movie_data)

class RT_page2(RT_main):
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
        self.rt_url = 'https://editorial.rottentomatoes.com/guide/rt25-critics-top-tv-shows-of-the-last-25-years-2/'
        self.access_check = requests.get(self.rt_url)
        self.page_contents = self.access_check.text
#Function to write out html formatting for webscraping. 
        

    def get_html(self):
        """
        Function: 
            Attribute: 
            rt_doc(html): Html docmunet that is being parsed. 
            -Gets an html document page associated with the rotten tomato webiste page. 
            Returns: 
                -An html document to pass through our web scraping class. 
        """
        with open('rt25_tv_webpage.html', 'w') as f:
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
            -Gets all of the titles of the tv shows. 
            Returns: 
                -List of all the tv show titles. 
        """

        movie_name=[]
        movie_name_tags=rt_doc.find_all('div',{'class': "article_movie_title"})
        for tag in movie_name_tags:
            name = tag.find('a').text
            movie_name.append(name) 
        return movie_name

    def get_movie_year(self, rt_doc):
        """
        Function: 
            Attribute: 
            rt_doc(html): Html docmunet that is being parsed. 
            -Gets all of associated tv show release years. 
            Returns: 
                -List of the tv shows' associated release years. 
        """
        movie_year=[]
        movie_year_tags=rt_doc.find_all('span',{'class':"subtle start-year" })
        for tag in movie_year_tags:
            movie_year.append(tag.get_text().strip())
        return movie_year

    def get_stars(self, rt_doc):
        """
        Function: 
            Attribute: 
            rt_doc(html): Html docmunet that is being parsed. 
            -Gets all of cast members of the tv shows. 
            Returns: 
                -List of all the tv show scores. 
        """
        movie_star_list=[]
        movie_star_tags=rt_doc.find_all('div',{'class':"info cast"})
        for tag in movie_star_tags:
            stars = tag.text[:]
            movie_star_list.append(stars.strip("\n"))
        return movie_star_list

    def get_rating(self, rt_doc): 
        """
        Function: 
            Attribute: 
            rt_doc(html): Html docmunet that is being parsed. 
            -Gets all of the associated tv show reviewed score values. 
            Returns: 
                -List of all the tv show scores. 
        """    
        movie_rating=[]    
        movie_rating_tags=rt_doc.find_all('span',{'class': "tMeterScore" })
        for tag in movie_rating_tags:
            movie_rating.append(tag.get_text().strip('%'))
        return movie_rating

    def get_synopsis(self, rt_doc):   
        """
        Function: 
            Attribute: 
            rt_doc(html): Html docmunet that is being parsed. 
            -Gets all of the summaries of tv shows.
            Returns: 
                -List of tv show summaries. 
        """        
        movie_summary_tags=rt_doc.find_all('div',{'class':"info synopsis"})
        summary_listing=[]
        for tag in movie_summary_tags:
            summary_listing.append(tag.get_text().strip())
        return summary_listing

import pandas as pd

#Driver code to collect data. 
page2 = RT_page2()
page_content = page2.get_html()
name = page2.get_movie_title(page_content)
year = page2.get_movie_year(page_content)
stars = page2.get_stars(page_content)
movie_score = page2.get_rating(page_content)
summary = page2.get_synopsis(page_content)

#further storing data in dictionary. 
movie_catalog={
    'Name':name,
    'Year':year,
    'Starring':stars,
    'Rating':movie_score,
    'Synopis':summary
}

#Formatting dictionary into a csv table. 
movie_data = pd.DataFrame.from_dict(movie_catalog, orient = 'index')
movie_data=movie_data.transpose()
movie_data.to_csv('page2_rt25_tv_web_scraping.csv')
print(movie_data)
class RT_page3(RT_main):
    def __init__(self):
        self.rotten_tomato_url25 = 'https://editorial.rottentomatoes.com/guide/rt25-critics-top-movies-of-the-last-25-years/'
        self.access_check = requests.get(self.rotten_tomato_url25)
        self.page_contents = self.access_check.text

#Function to write out html formatting for webscraping. from bs4 import BeautifulSoup
    def get_html(self):
        """
        Function: 
            Attribute: 
            rt_doc(html): Html docmunet that is being parsed. 
            -Gets an html document page associated with the rotten tomato webiste page. 
            Returns: 
                -An html document to pass through our web scraping class. 
        """
        with open('rt25_movie_webpage.html', 'w') as f:
            f.write(self.page_contents)
            from bs4 import BeautifulSoup
            rt_doc= BeautifulSoup(self.page_contents, 'html.parser')
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
        movie_summary_tags=rt_doc.find_all('div',{'class':"info critics-consensus" })
        for tag in movie_summary_tags:
            critic_listing.append(tag.get_text().strip())
        return critic_listing
    
    def get_synopsis(self, rt_doc):
        """
        Function: 
            Attribute: 
            rt_doc(html): Html docmunet that is being parsed. 
            -Gets all of the movie summaries of the listed movies of last 25 years.
            Returns: 
                -List of all summaries. 
        """
        summary_listing=[]           
        movie_summary_tags=rt_doc.find_all('div',{'class':"info synopsis"})
        for tag in movie_summary_tags:
            summary_listing.append(tag.get_text().strip())
        return summary_listing
    
import pandas as pd

#Driver code to get all elements 
page3 = RT_page3()
page_content = page3.get_html()
name = page3.get_movie_title(page_content)
year = page3.get_movie_year(page_content)
consensus = page3.get_critic_consensus(page_content)
movie_score = page3.get_rating(page_content)
summary = page3.get_synopsis(page_content)
    
#Storing elements in dictionary.
movie_catalog={
    'Name':name,
    'Year':year,
    'Rating':movie_score,
    'Critic Consensus':consensus,
    'Summary': summary
}

#Converting dictionary to csv table.

movie_data = pd.DataFrame.from_dict(movie_catalog, orient='index')
movie_data=movie_data.transpose()
movie_data.to_csv('page3_movie_web_scraping25.csv')
print(movie_data)

import requests
#Necessary imports for webscraping.
from web_scrape_rt2023_movie import RT_main 

class RT_page4(RT_main):
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
        self.rotten_tomato_url23 ='https://editorial.rottentomatoes.com/guide/best-tv-shows-of-2023/'
        self.access_check = requests.get(self.rotten_tomato_url23)
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
        with open('rt2023_webpage.html', 'w') as f:
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
            -Gets all of the titles of the tv shows of 2023. 
            Returns: 
                -List of all tv shows. 
        """
        movie_name=[]
        movie_name_tags=rt_doc.find_all('div',{'class': "article_movie_title"})
        for tag in movie_name_tags:
            name = tag.find('a').text
            movie_name.append(name) 
        return movie_name

    def get_movie_year(self, rt_doc): 
        """
        Function: 
            Attribute: 
            rt_doc(html): Html docmunet that is being parsed. 
            -Gets all of associated tv show release years. 
            Returns: 
                -List of the tv shows' associated release years. 
        """
        movie_year=[]         
        movie_year_tags=rt_doc.find_all('span',{'class':"subtle start-year" })
        for tag in movie_year_tags:
            movie_year.append(tag.get_text().strip())
        return movie_year
    
    def get_stars(self, rt_doc):
        """
        Function: 
            Attribute: 
            rt_doc(html): Html docmunet that is being parsed. 
            -Gets all cast members of the tv shows. 
            Returns: 
                -List of cast. 
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
            -Gets all of the associated tv show reviewed score values. 
            Returns: 
                -List of all the tv show scores. 
        """     
        movie_rating=[]      
        movie_rating_tags=rt_doc.find_all('span',{'class': "tMeterScore" })
        for tag in movie_rating_tags:
            movie_rating.append(tag.get_text().strip('%'))
        return movie_rating

    def get_critic_consensus(self, rt_doc):
        """
        Function: 
            Attribute: 
            rt_doc(html): Html docmunet that is being parsed. 
            -Gets all of the critic reviews of the listed tv shows of 2023.
            Returns: 
                -List of all critic consensus reviews. 
        """
        critic_listing=[]           
        movie_summary_tags=rt_doc.find_all('div',{'class':"info critics-consensus" })
        for tag in movie_summary_tags:
            critic_listing.append(tag.get_text().strip())
        return critic_listing
    
import pandas as pd

#Driver code to collect data. 
page4 = RT_page4()
page_content = page4.get_html()
name = page4.get_movie_title(page_content)
year = page4.get_movie_year(page_content)
stars = page4.get_stars(page_content)
movie_score = page4.get_rating(page_content)
consensus = page4.get_critic_consensus(page_content)

#Storing found data in dictionary. 
movie_catalog={
        'Name':name,
        'Year':year,
        'Starring':stars,
        'Rating':movie_score,
        'Critc Consensus':consensus
    }

#Transferring dictionary data into a csv table format. 
movie_data = pd.DataFrame.from_dict(movie_catalog, orient='index')
movie_data=movie_data.transpose()
movie_data.to_csv('page4_rttv2023_web_scraping.csv')
print(movie_data)

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
