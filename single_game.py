from lib2to3.pgen2 import driver
from bs4 import BeautifulSoup
import requests
import match_info_scraper as mi
import batting_scraper as bt
import bowling_scraper as bw

from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
import time




# Match information

match_columns = ['result_string', 'left_team', 'right_team', 'location', 'toss_won_by', 'batted_first', 'competition_string', 'datetime']

# Batting stats

bat_columns = ['unclean_name', 'bat_id', 'team', 'runs', 'balls', 'wicket_string']

# Bowling stats

bowl_columns = ['unclean_name', 'bowl_id', 'team', 'wicket_string', 'over_string']

test_link = 'https://matchcentre.cricketact.com.au/match/2807-3885253/scorecard/?period=3630138'

def create_list_dict_with_keys(keys):
    output = {}
    for key in keys:
        output[key] = []

def create_soup(link):
    
    options = Options()
    options.page_load_strategy = 'normal'
    driver = webdriver.Chrome(options=options)
    driver.get(link)
    time.sleep(2)
    html = driver.page_source

    
    return BeautifulSoup(html, 'html.parser')

class match_centre_page:

    def __init__(self, link):
        self.soup = create_soup(link)
        print(self.soup.prettify())
        self.match_info_dic = create_list_dict_with_keys(match_columns)
        self.batting_dic = create_list_dict_with_keys(bat_columns)
        self.bowling_dic = create_list_dict_with_keys(bowl_columns)


    def fill_dic(self, fill_function):
        soup = self.soup
        dic = self.match_info_dic
        fill_function(soup, dic)

    def fill_match_data_dic(self):
        self.fill_dic(mi.fill_match_data_dic_from_soup)
    
    def fill_batting_dic(self):
        self.fill_dic(bt.fill_batting_dic_from_soup)
    
    def fill_bowling_dic(self):
        self.fill_dic(bw.fill_bowling_dic_from_soup)



    def scrape_page(self):
        self.fill_match_data_dic()
        self.fill_batting_dic()
        self.fill_bowling_dic()
        
    
page = match_centre_page(test_link)

page.fill_match_data_dic()

print(page.match_info_dic)
