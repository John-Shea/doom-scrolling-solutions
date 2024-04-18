import requests
from bs4 import BeautifulSoup
import pandas as pd

class RT_Scraper():
    def __init__(self, url):
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
        self.url = url
        self.access_check = requests.get(self.url)
        self.page_contents = self.access_check.text

    def get_html(self):
        with open(f'{self.url.replace("/", "_").replace(":", "")}_webpage.html', 'w') as f:
            f.write(self.page_contents)
            rt_doc = BeautifulSoup(self.page_contents, 'html.parser')
        return rt_doc

    def get_movie_title(self, rt_doc):
        movie_name = []
        movie_name_tags = rt_doc.find_all('div', {'class': "article_movie_title"})
        for tag in movie_name_tags:
            name = tag.find('a').text
            movie_name.append(name)
        return movie_name

    def get_movie_year(self, rt_doc):
        movie_year = []
        movie_year_tags = rt_doc.find_all('span', {'class': "subtle start-year"})
        for tag in movie_year_tags:
            movie_year.append(tag.get_text().strip(""))
        return movie_year

    def get_rating(self, rt_doc):
        movie_rating = []
        movie_rating_tags = rt_doc.find_all('span', {'class': "tMeterScore"})
        for tag in movie_rating_tags:
            movie_rating.append(tag.get_text().strip('%'))
        return movie_rating

    def get_critic_consensus(self, rt_doc):
        critic_listing = []
        movie_summary_tags = rt_doc.find_all('div', {'class': "info critics-consensus"})
        for tag in movie_summary_tags:
            critic_listing.append(tag.get_text().strip("Critics Consensus:"))
        return critic_listing

    def get_synopsis(self, rt_doc):
        summary_listing = []
        movie_summary_tags = rt_doc.find_all('div', {'class': "info synopsis"})
        for tag in movie_summary_tags:
            summary_listing.append(tag.get_text().strip("Synopsis:"))
        return summary_listing

# Define URLs for each page
urls = {
    "page1": "https://editorial.rottentomatoes.com/guide/best-movies-of-2023/",
    "page2": "https://editorial.rottentomatoes.com/guide/rt25-critics-top-tv-shows-of-the-last-25-years-2/",
    "page3": "https://editorial.rottentomatoes.com/guide/rt25-critics-top-movies-of-the-last-25-years/",
    "page4": "https://editorial.rottentomatoes.com/guide/best-tv-shows-of-2023/",
    "page5": "https://editorial.rottentomatoes.com/guide/best-tv-shows-of-2024/"
}

# Scrape data for each page
for page, url in urls.items():
    scraper = RT_Scraper(url)
    page_content = scraper.get_html()
    name = scraper.get_movie_title(page_content)
    year = scraper.get_movie_year(page_content)
    consensus = scraper.get_critic_consensus(page_content)
    movie_score = scraper.get_rating(page_content)
    summary = scraper.get_synopsis(page_content)

    # Store data in dictionary
    movie_catalog = {
        'Name': name,
        'Year': year,
        'Rating': movie_score,
        'Critic Consensus': consensus,
        'Summary': summary
    }

    # Convert dictionary to DataFrame and save as CSV
    movie_data = pd.DataFrame.from_dict(movie_catalog, orient='index').transpose()
    movie_data.to_csv(f'{page}_web_scraping.csv')
    print(f"Data saved for {page}.")
