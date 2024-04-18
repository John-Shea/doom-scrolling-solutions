import unittest
from unittest.mock import patch
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from webScraping.pull_1_rt2024_tv import RT_Scraper
from bs4 import BeautifulSoup

mock_html_content = """
<html>
    <div class="article_movie_title"><a>Example Movie Title</a></div>
    <span class="subtle start-year">(2024)</span>
    <span class="tMeterScore">88%</span>
    <div class="info critics-consensus">Consensus example text.</div>
</html>
"""

class MockResponse:
    def __init__(self, text, status_code):
        self.text = text
        self.status_code = status_code
        self.ok = status_code == 200

class TestRTPage5(unittest.TestCase):

    @patch('webScraping.pull_1_rt2024_tv.requests.get')
    def setUp(self, mock_get):
        """Set up mock before each test."""
        mock_get.return_value = MockResponse(mock_html_content, 200)
        self.re_call = RT_Scraper("https://editorial.rottentomatoes.com/guide/best-tv-shows-of-2024/")

    def test_get_html(self):
        """Test the get_html method."""
        html_content = self.re_call.get_html()
        self.assertIsInstance(html_content, BeautifulSoup)

    def test_get_movie_title(self):
        """Test the get_movie_name method."""
        rt_test = self.re_call.get_html()
        movie_names = self.re_call.get_movie_title(rt_test)
        self.assertIn('Example Movie Title', movie_names)

    def test_get_movie_year(self):
        """Test the get_movie_year method."""
        rt_test = self.re_call.get_html()
        movie_years = self.re_call.get_movie_year(rt_test)
        self.assertIn('(2024)', movie_years)
    
    def test_get_rating_and_check_numeric(self):
        """Test the get_rating method and validate the rating format."""
        rt_test = self.re_call.get_html()
        movie_ratings = self.re_call.get_rating(rt_test)
        for rating in movie_ratings:
            numeric_rating = rating.rstrip('%')
            self.assertTrue(numeric_rating.isdigit(), f"Rating '{rating}' is not numeric.")
            rating_value = int(numeric_rating)
            self.assertTrue(0 <= rating_value <= 100, f"Rating '{rating}' is not within the valid range.")

    def test_get_critic_consensus(self):
        """Test the get_critic_consensus method."""
        rt_test = self.re_call.get_html()
        critic = self.re_call.get_critic_consensus(rt_test)
        self.assertIn('Consensus example text.', critic)


if __name__ == '__main__':
    unittest.main
