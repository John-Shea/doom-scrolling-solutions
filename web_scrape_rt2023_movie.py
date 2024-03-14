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
#Coverts 1D array into a 2D column format.
movie_data=movie_data.transpose()
#Saves collected movie data into a csv format. 
movie_data.to_csv('page_1_rt2023_web_scraping.csv')

#Test print to make sure elements are formatted correctly. 
print(movie_data)