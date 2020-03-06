import unittest
import webScraper

class webScraperTests(unittest.TestCase):
     def test_webScraperGetsCorrectLength(self):
         expectedLength = 65620
         raw_html = webScraper.simple_get('https://www.imthefrizzlefry.blog/p/test-example.html')
         self.assertGreaterEqual(len(raw_html), expectedLength)

     def test_webScraperThrowsExceptionOnInvalidPage(self):        
         self.assertRaises(webScraper.RequestException, webScraper.simple_get('https://invalid.stevenfarnell.net/'))

     def test_webScraperReturnNonForInvalidPage(self):        
         raw_html = webScraper.simple_get('https://invalid.stevenfarnell.net')
         self.assertTrue(raw_html is None)

