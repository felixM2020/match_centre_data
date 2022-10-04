from bs4 import BeautifulSoup


def fill_match_data_dic_from_soup(soup, dic):
    add_teams(soup, dic)
    add_result(soup, dic)
    add_location(soup, dic)
    add_toss(soup, dic)
    add_batted_first(soup, dic)
    add_comp_string(soup, dic)
    add_date_time(soup, dic)


def add_teams(soup, dic):
    teams = find_teams(soup)
    dic['left_team'] = teams[0]
    dic['right_team'] = teams[-1]

def add_result(soup, dic):
    result_string = find_result(soup)
    dic['result_string'] = result_string

def add_location(soup, dic):
    loc_string = find_location(soup)
    dic['location'] = loc_string


def add_toss(soup, dic):
    toss = find_toss(soup)
    dic['toss_won_by'] = toss

def add_batted_first(soup, dic):
    batted_first = find_batted_first(soup)
    dic['batted_first'] = batted_first

def add_comp_string(soup, dic):
    comp_string = find_comp_string(soup)
    dic['competition_string'] = comp_string


def add_date_time(soup, dic):
    datetime = find_datetime(soup)
    dic['datetime'] = datetime





