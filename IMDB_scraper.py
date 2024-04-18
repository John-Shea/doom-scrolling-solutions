import requests
from bs4 import BeautifulSoup
import pandas as pd

class IMDB_Scraper():
    def __init__(self, url):
        self.url = url
        self.access_check = requests.get(self.url)
        self.page_contents = self.access_check.text

    def get_html(self):
        with open(f'{self.url.replace("/", "_").replace(":", "")}_webpage.html', 'w') as f:
            f.write(self.page_contents)
        return BeautifulSoup(self.page_contents, 'html.parser')

    def get_movie_title(self, imdb_doc):
        movie_name = []
        movie_name_tags = imdb_doc.find_all('h3', {'class': "lister-item-header"})
        for tag in movie_name_tags:
            name = tag.find('a').text
            movie_name.append(name)
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
            meta_scores.append(tag.get_text().strip("Metascore"))
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
        summary_listing = []
    # Finding all elements of summaries in html.
        movie_summary_tags = imdb_doc.find_all('p', {'class': ""})
        for tag in movie_summary_tags:
            movie_sum = tag.text.strip()  # Extract text directly from <p> tag
        # Check if the text contains the unwanted string
            if "KEEP FOLLOW! To be continued..." not in movie_sum:
                summary_listing.append(movie_sum)
    # Returning the summary listings. 
        return summary_listing
    

    # def get_movie_summary(self, imdb_doc): 
    #     """
    #     Function: 
    #         Attribute: 
    #         imdb_doc(html): Html document that is being parsed. 
    #         -Gets all of associated movie metacritic summaries.
    #         Returns: 
    #             -List of the movies' summaries. 
    #     """ 
    #     #empty list for storage
    #     summary_listing=[]
    #     #Finding all elements of summaries in html.
    #     movie_summary_tags=imdb_doc.find_all('p',{'class':''})
    #     #Iterating...
    #     for tag in movie_summary_tags:
    #         #Adding those summaries to the list.
    #         #Adds the movie durations to the growing list. 
    #         summary_listing.append(tag.get_text().strip())
    #     #Returning the summary listings. 
    #     return summary_listing

# Define URLs for each page
urls = {
    "page6": "https://www.imdb.com/list/ls000199717/?sort=release_date,desc&st_dt=&mode=detail&page=1",
    "page7": "https://www.imdb.com/list/ls524708103/"
}

# Scrape data for each page
for page, url in urls.items():
    scraper = IMDB_Scraper(url)
    page_content = scraper.get_html()
    name = scraper.get_movie_title(page_content)
    #Finding the movies years...
    year = scraper.get_movie_year(page_content)
    #Finding the movie durations...
    duration = scraper.get_duration(page_content)
    #Finding the movies scores...
    movie_score = scraper.get_rating(page_content)
    #Finding the metascores...
    metacritic_score = scraper.get_meta_score(page_content)
    #Finding the genres...
    genre = scraper.get_movie_genre(page_content)
    #Finding the summaries...
    summary = scraper.get_movie_summary(page_content)
    # Store data in dictionary
    
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

    # Convert dictionary to DataFrame and save as CSV
    movie_data = pd.DataFrame.from_dict(movie_catalog, orient='index').transpose()
    movie_data.to_csv(f'{page}_web_scrapingIMDB.csv')
    print(f"Data saved for {page}.")
