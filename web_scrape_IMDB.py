import requests
#Necessary imports for webscraping. 

class IMDB():
    def __init__(self):
        """
        Function: 
            Attribute: 
            imdb_url(url): Html docmunet that is being parsed. 
            access_check(int): Checks if a page is accessible. 
            page_contents(): Page related information that gets fed into BeautifulSoup for our custom parsing. 
            -Intializes the associated elements of the web page. 
            Returns: 
                -List of all critic consensus reviews. 
        """ 
        self.imdb_url ='https://www.imdb.com/list/ls000199717/?sort=release_date,desc&st_dt=&mode=detail&page=1'
        self.access_check = requests.get(self.imdb_url)
        self.page_contents = self.access_check.text

#Function to write out html formatting for webscraping. 
    def get_html(self):
        """
        Function: 
            Attribute: 
            imdb_doc(html): Html docmunet that is being parsed. 
            -Gets an html document page associated with the rotten tomato webiste page. 
            Returns: 
                -An html document to pass through our web scraping class. 
        """
        #While the create html page is open...
        with open('imdb_webpage.html', 'w') as f:
            #Function to write the page contents of the website.
            f.write(self.page_contents)
            #Necessary library for web scraping an html.
            from bs4 import BeautifulSoup
            #Creates a variable that we will parse.
            imdb_doc = BeautifulSoup(self.page_contents, 'html.parser')
        #Returns the html document to scrape.
        return imdb_doc


    def get_movie_title(self, imdb_doc):
        """
        Function: 
            Attribute: 
            imdb_doc(html): Html docmunet that is being parsed. 
            -Gets all of the titles of the movies. 
            Returns: 
                -List of all the movie titles. 
        """
        #Empty list to store titles of the movies.
        movie_name=[]
        #Small function to find and store all movie titles. 
        movie_name_tags=imdb_doc.find_all('h3',{'class':"lister-item-header"})
        #Iterating over the elements...
        for tag in movie_name_tags:
            #Further finding tags associated with html text.
            name = tag.find('a').text
            #Adding the name of the movie to the list. 
            movie_name.append(name) 
        #Returning the list of movie names. 
        return movie_name

    def get_movie_year(self, imdb_doc):
        """
        Function: 
            Attribute: 
            rt_doc(html): Html docmunet that is being parsed. 
            -Gets all of associated movie release years. 
            Returns: 
                -List of the movies' associated release years. 
        """ 
        movie_year=[]       
        movie_year_tags=imdb_doc.find_all('span',{'class':"lister-item-year text-muted unbold"})
        for tag in movie_year_tags:
            movie_year.append(tag.get_text().strip())
        return movie_year

    def get_duration(self, imdb_doc):
        movie_duration=[]
        movie_duration_tags=imdb_doc.find_all('span',{'class':"runtime"})
        for tag in movie_duration_tags:
            duration = tag.text[:10]
            movie_duration.append(duration)
        return movie_duration

    def get_rating(self, imdb_doc): 
        movie_rating=[]          
        movie_rating_tags=imdb_doc.find_all('div',{'class':"ipl-rating-star small" })
        for tag in movie_rating_tags:
            movie_rating.append(tag.get_text().strip())
        return movie_rating

    def get_meta_score(self, imdb_doc):
        meta_scores=[]           
        meta_score_tags=imdb_doc.find_all('div',{'class':"inline-block ratings-metascore" })
        for tag in meta_score_tags:
            meta_scores.append(tag.get_text().strip())
        return meta_scores

    def get_movie_genre(self, imdb_doc): 
        genre_listing=[]          
        movie_genre_tags=imdb_doc.find_all('span',{'class': "genre" })
        for tag in movie_genre_tags:
            genre_listing.append(tag.get_text().strip())
        return genre_listing

    def get_movie_summary(self, imdb_doc):     
        movie_summary_tags=imdb_doc.find_all('p',{'class':""})
        summary_listing=[]
        for tag in movie_summary_tags:
            summary_listing.append(tag.get_text().strip())
        return summary_listing

import pandas as pd

page6 = IMDB()
page_content = page6.get_html()
name = page6.get_movie_title(page_content)
year = page6.get_movie_year(page_content)
duration = page6.get_duration(page_content)
movie_score = page6.get_rating(page_content)
metacritic_score = page6.get_meta_score(page_content)
genre = page6.get_movie_genre(page_content)
summary = page6.get_movie_summary(page_content)
    
movie_catalog={
    'Name':name,
    'Year':year,
    'Duration':duration,
    'Rating':movie_score,
    'Metacritic Score':metacritic_score,
    'Genre':genre,
    'Summary':summary
}

movie_data = pd.DataFrame.from_dict(movie_catalog, orient='index')
movie_data=movie_data.transpose()
movie_data.to_csv('imdb_web_scraping.csv')
print(movie_data)


#Web Scraping References: 
#https://opensource.com/article/21/9/web-scraping-python-beautiful-soup
#https://medium.com/@philipnirushan25/understanding-the-difference-between-find-and-find-all-in-beautifulsoup-python-76bd0c25cec9
#https://realpython.com/beautiful-soup-web-scraper-python/
#https://www.geeksforgeeks.org/implementing-web-scraping-python-beautiful-soup/
#https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.from_dict.html
#https://numpy.org/doc/stable/reference/generated/numpy.transpose.html
#https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_csv.html

#Streamlit References: 


