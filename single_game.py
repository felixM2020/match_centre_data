from bs4 import BeautifulSoup
import requests
import match_info_scraper as mi
import batting_scraper as bt
import bowling_scraper as bw


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
    page = requests.get(link)
    return BeautifulSoup(page.text, 'html.parser')

class match_centre_page:

    def __init__(self, link):
        self.soup = create_soup(link)

    match_info_dic = create_list_dict_with_keys(match_columns)

    batting_dic = create_list_dict_with_keys(bat_columns)

    bowling_dic = create_list_dict_with_keys(bowl_columns)


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
        
    

    
