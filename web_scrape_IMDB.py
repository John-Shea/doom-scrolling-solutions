
import requests
#Necessary imports for webscraping. 

class IMDB():
    def __init__(self):
        self.imdb_url ='https://www.imdb.com/list/ls000199717/?sort=release_date,desc&st_dt=&mode=detail&page=1'
        self.access_check = requests.get(self.imdb_url)
        self.page_contents = self.access_check.text

#Function to write out html formatting for webscraping. 
    def get_html(self):
        with open('imdb_webpage.html', 'w') as f:
            f.write(self.page_contents)
            from bs4 import BeautifulSoup
            imdb_doc = BeautifulSoup(self.page_contents, 'html.parser')
        return imdb_doc


    def get_movie_name(self, imdb_doc):
        movie_name=[]
        movie_name_tags=imdb_doc.find_all('h3',{'class':"lister-item-header"})
        for tag in movie_name_tags:
            name = tag.find('a').text
            movie_name.append(name) 
        return movie_name

    def get_movie_year(self, imdb_doc):  
        movie_year=[]       
        movie_year_tags=imdb_doc.find_all('span',{'class':"lister-item-year text-muted unbold"})
        for tag in movie_year_tags:
            movie_year.append(tag.get_text().strip())
        return movie_year

    def get_certificate(self, imdb_doc):
        maturity_rating=[]
        movie_rating_tags=imdb_doc.find_all('span',{'class':"certificate"})

        for tag in movie_rating_tags:
            certificate = tag.text[:10]
            maturity_rating.append(certificate)
    
        return maturity_rating

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
name = page6.get_movie_name(page_content)
year = page6.get_movie_year(page_content)
maturity_rating = page6.get_certificate(page_content)
duration = page6.get_duration(page_content)
movie_score = page6.get_rating(page_content)
metacritic_score = page6.get_meta_score(page_content)
genre = page6.get_movie_genre(page_content)
summary = page6.get_movie_summary(page_content)
    
movie_catalog={
    'Name':name,
    'Year':year,
    'Maturity Rating':maturity_rating,
    'Duration':duration,
    'Rating':movie_score,
    'Metacritic Score':metacritic_score,
    'Genre':genre,
    'Summary':summary
}

movie_data = pd.DataFrame.from_dict(movie_catalog, orient='index')
movie_data=movie_data.transpose()
movie_data.to_csv('page5_imdb_web_scraping.csv')
print(movie_data)