import requests
#Necessary imports for webscraping. 

class IMDB():
    def __init__(self):
        """
        Function: 
            Attribute: 
            imdb_url(url): Website that will be eventually be parsed. 
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
        #Creates an empty list for storing found movie years. 
        movie_year=[]  
        #Function to grab all of the years of release on the html document.      
        movie_year_tags=imdb_doc.find_all('span',{'class':"lister-item-year text-muted unbold"})
        #Iterating over the found values. 
        for tag in movie_year_tags:
            #Adding the movie years to the list. 
            movie_year.append(tag.get_text().strip())
        #Returning the list of found movie years. 
        return movie_year

    def get_duration(self, imdb_doc):
        """
        Function: 
            Attribute: 
            imdb_doc(html): Html docmunet that is being parsed. 
            -Gets all of associated movie durations.
            Returns: 
                -List of the movies' durations. 
        """
        #Creates an empty list to store found values 
        movie_duration=[]
        #beautiful soup function to find all duration elemenets in html.
        movie_duration_tags=imdb_doc.find_all('span',{'class':"runtime"})
        #Iterating...
        for tag in movie_duration_tags:
            #Grabs the appropriate amount of text.
            duration = tag.text[:10]
            #Adds the movie durations to the growing list. 
            movie_duration.append(duration)
        #Returnts a list of movie durations. 
        return movie_duration

    def get_rating(self, imdb_doc):
        """
        Function: 
            Attribute: 
            imdb_doc(html): Html docmunet that is being parsed. 
            -Gets all of associated movie ratings.
            Returns: 
                -List of the movies' ratings. 
        """ 
        #Eventual movie rating storage. 
        movie_rating=[]  
        #Searching html for movie ratings.         
        movie_rating_tags=imdb_doc.find_all('div',{'class':"ipl-rating-star small" })
        #Iterating...
        for tag in movie_rating_tags:
            #Adding movie ratings and stripping trailing whitespace. 
            movie_rating.append(tag.get_text().strip())
        #Returns the list of movie ratings. 
        return movie_rating

    def get_meta_score(self, imdb_doc):
        """
        Function: 
            Attribute: 
            imdb_doc(html): Html docmunet that is being parsed. 
            -Gets all of associated movie metacritic ratings.
            Returns: 
                -List of the movies' metacritic ratings. 
        """ 
        #Empty list to store metascores 
        meta_scores=[]  
        #Function to find all metacritic scores in html.         
        meta_score_tags=imdb_doc.find_all('div',{'class':"inline-block ratings-metascore" })
        #Iteraing...
        for tag in meta_score_tags:
            #Adding metacrtic scores to storage. 
            meta_scores.append(tag.get_text().strip())
        #Returning that list. 
        return meta_scores

    def get_movie_genre(self, imdb_doc): 
        """
        Function: 
            Attribute: 
            imdb_doc(html): Html docmunet that is being parsed. 
            -Gets all of associated movie genres.
            Returns: 
                -List of the movies' genres. 
        """ 
        #Genres storage.
        genre_listing=[]    
        #Function to find all genres in html.      
        movie_genre_tags=imdb_doc.find_all('span',{'class': "genre" })
        #Iterating over html.
        for tag in movie_genre_tags:
            #Adding these elements to a list. 
            genre_listing.append(tag.get_text().strip())
        #Return list of genres. 
        return genre_listing

    def get_movie_summary(self, imdb_doc): 
        """
        Function: 
            Attribute: 
            imdb_doc(html): Html document that is being parsed. 
            -Gets all of associated movie metacritic summaries.
            Returns: 
                -List of the movies' summaries. 
        """ 
        #empty list for storage
        summary_listing=[]
        #Finding all elements of summaries in html.
        movie_summary_tags=imdb_doc.find_all('p',{'class':""})
        #Iterating...
        for tag in movie_summary_tags:
            #Adding those summaries to the list.
            summary_listing.append(tag.get_text().strip())
        #Returning the summary listings. 
        return summary_listing

#Necessary imports.
import pandas as pd

#Creating page 6 from found elements.
page6 = IMDB()
#Creating the html page contents to parse. 
page_content = page6.get_html()
#Finding the names...
name = page6.get_movie_title(page_content)
#Finding the movies years...
year = page6.get_movie_year(page_content)
#Finding the movie durations...
duration = page6.get_duration(page_content)
#Finding the movies scores...
movie_score = page6.get_rating(page_content)
#Finding the metascores...
metacritic_score = page6.get_meta_score(page_content)
#Finding the genres...
genre = page6.get_movie_genre(page_content)
#Finding the summaries...
summary = page6.get_movie_summary(page_content)

#Adding these found elements to a dictionary.
movie_catalog={
    'Name':name,
    'Year':year,
    'Duration':duration,
    'Rating':movie_score,
    'Metacritic Score':metacritic_score,
    'Genre':genre,
    'Summary':summary
}

#Making the movie data a dataframe.
movie_data = pd.DataFrame.from_dict(movie_catalog, orient='index')
#Formatting the data for csv columns
movie_data=movie_data.transpose()
#Saving the csv. 
movie_data.to_csv('imdb_web_scraping.csv')
#Print check.
print(movie_data)


#Web Scraping References: 
#https://opensource.com/article/21/9/web-scraping-python-beautiful-soup
#https://medium.com/@philipnirushan25/understanding-the-difference-between-find-and-find-all-in-beautifulsoup-python-76bd0c25cec9
#https://stackoverflow.com/questions/55501111/how-to-go-from-dictionary-to-pandas-dataframe-to-csv-while-making-the-dict-keys
#https://jovian.com/mihirpanchal0072/web-scraping-imdb-database-for-movies-using-python-beautiful-soup#C3
#https://realpython.com/beautiful-soup-web-scraper-python/
#https://www.geeksforgeeks.org/implementing-web-scraping-python-beautiful-soup/
#https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.from_dict.html
#https://numpy.org/doc/stable/reference/generated/numpy.transpose.html
#https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_csv.html

