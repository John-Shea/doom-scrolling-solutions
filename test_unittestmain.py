import unittest
from unittest.mock import patch, mock_open
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from web_scrape_rt2023_movie import RT_main

mock_html_content = """
<html>
    <div class="article_movie_title"><a>Example Movie Title</a></div>
    <span class="subtle start-year">(2023)</span>
    <span class="tMeterScore">88%</span>
    <div class="info critics-consensus">Consensus example text.</div>
</html>
"""
class MockResponse:
    def __init__(self, text, status_code):
        self.text = text
        self.status_code = status_code
        self.ok = status_code == 200

class TestRTMain(unittest.TestCase):

    @patch('web_scrape_rt2023_movie.requests.get')
    def setUp(self, mock_get):
        """Set up mock before each test."""
        mock_get.return_value = MockResponse(mock_html_content, 200)
        self.rt_call = RT_main()

    def test_init(self):
        """Test the __init__ method."""
        self.assertEqual(self.rt_call.rt_url, 'https://editorial.rottentomatoes.com/guide/best-movies-of-2023/')
        self.assertTrue(self.rt_call.access_check.ok)
        self.assertEqual(self.rt_call.page_contents, mock_html_content)

    def test_get_html(self):
        """Test the get_html method."""
        with patch('builtins.open', mock_open(read_data=mock_html_content)) as mocked_file:
            rt_test = self.rt_call.get_html()
            mocked_file.assert_called_once_with('rt2023_movie_webpage.html', 'w', encoding='utf-8')
            self.assertIsNotNone(rt_test)

    def test_get_movie_name(self):
        """Test the get_movie_name method."""
        rt_test = self.rt_call.get_html()
        movie_names = self.rt_call.get_movie_name(rt_test)
        self.assertIn('Example Movie Title', movie_names)

    def test_get_movie_year(self):
        """Test the get_movie_year method."""
        rt_test = self.rt_call.get_html()
        movie_years = self.rt_call.get_movie_year(rt_test)
        self.assertIn('2023', movie_years)

    def test_get_movie_year_is_integer(self):
        """Test that the get_movie_year method returns a year that's an integer."""
        rt_test = self.rt_call.get_html()
        movie_years = self.rt_call.get_movie_year(rt_test)
        for year in movie_years:
            year = int(year.strip('()'))
            self.assertIsInstance(year, int, f"The year '{year}' is not an integer.")


    def test_get_rating(self):
        """Test the get_rating method."""
        rt_test = self.rt_call.get_html()
        movie_ratings = self.rt_call.get_rating(rt_test)
        self.assertIn('88', movie_ratings)

    def test_get_rating_is_numeric(self):
        """Test the get_rating method returns a rating that's an integer."""
        rt_test = self.rt_call.get_html()
        movie_ratings = self.rt_call.get_rating(rt_test)
        for rating in movie_ratings:
            numeric_rating = rating.rstrip('%')
            self.assertTrue(numeric_rating.isdigit(), f"Rating '{rating}' is not numeric.")


    def test_get_critic_consensus(self):
        """Test the get_critic_consensus method."""
        rt_test = self.rt_call.get_html()
        critic_consensus = self.rt_call.get_critic_consensus(rt_test)
        self.assertIn('Consensus example text.', critic_consensus)

if __name__ == '__main__':
    unittest.main()
