from lib2to3.pgen2.tokenize import tokenize
from selenium import webdriver
import re
from html.parser import HTMLParser
from collections import defaultdict

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

class Heuristics:
    def url_tokenize(self, url):
        tokenized_word = re.split('\W+', url)
        num_element, sum_of_element, largest = 0, 0, 0
        for element in tokenized_word:
            l = len(element)
            sum_of_element += l
            if l > 0:
                num_element += l
                if largest < l:
                    largest = l
        
        try:
            return ([float(sum_of_element)/num_element, num_element, largest])
        
        except:
            return ([0, num_element, largest])

    def url_has_exe(self, url):
        try:
            if url.find('.exe/') != -1:
                return [url, 1]
        except:
            pass
    
    def phishing_word_count(self, url):
        tokenized_word = re.split('\W+', url)
        phishing_words = ['confirm', 'account', 'banking', 'secure', 'software', 'config', 'login', 'signin', 'delete', 'lucky', 'free', 'adult', 'pics', 'xx', 'archive', 'save']
        words = []
        count = 0
        for element in phishing_words:
            if element in tokenized_word:
                count += 1
                words.append(element)
        if count > 0:
            return count, words
    
    def scan_pg_src(self, url):
        class MyHTMLParser(HTMLParser):
            def __init__(self):
                self.count = defaultdict(int)
                super().__init__()
            
            def handle_starttag(self, tag, attrs):
                self.count[tag] += 1

            def handle_startendtag(self, tag, attrs):
                self.count[tag] += 1
        
        def count_tags(html):
            parser = MyHTMLParser()
            parser.feed(html)
            return parser.count
        
        wd = webdriver.Chrome('chromedriver', options=chrome_options)
        wd.get(url)
        return count_tags(wd.page_source)

obj = Heuristics()

print(obj.phishing_word_count("http://www.software-secure.com/asp/"))
print(obj.url_has_exe("http://food.hubcom.com/recipe/cgi-win/recipe.exe/1"))
print(obj.url_tokenize("http://food.hubcom.com/recipe/cgi-win/recipe.exe/1"))
print(obj.scan_pg_src("http://www.liquidgeneration.com/"))