import unittest
from unittest.mock import patch
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from web_scrape_rt_tvpast25 import RT_page2
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

    @patch('web_scrape_rt_tvpast25.requests.get')
    def setUp(self, mock_get):
        """Set up mock before each test."""
        mock_get.return_value = MockResponse(mock_html_content, 200)
        self.re_call = RT_page2()

    def test_get_html(self):
        """Test the get_html method."""
        html_content = self.re_call.get_html()
        self.assertIsInstance(html_content, BeautifulSoup)


    def test_get_movie_name(self):
        """Test the get_movie_name method."""
        rt_tset = self.re_call.get_html()
        movie_names = self.re_call.get_movie_name(rt_tset)
        self.assertIn('Example Movie Title', movie_names)

    def test_get_movie_year(self):
        """Test the get_movie_year method."""
        rt_tset = self.re_call.get_html()
        movie_years = self.re_call.get_movie_year(rt_tset)
        self.assertIn('2024', movie_years)

    def test_get_rating(self):
        """Test the get_rating method."""
        rt_tset = self.re_call.get_html()
        movie_ratings = self.re_call.get_rating(rt_tset)
        self.assertIn('88', movie_ratings)


if __name__ == '__main__':
    unittest.main()