from bs4 import BeautifulSoup

def find_div_contains(soup, string):
    return soup.select('div[class*="'+string+'"]')[0]

def find_all_div_contains(soup, string):
    return soup.select('div[class*="'+string+'"]')

def find_all_container_class_contains(soup, container, string):
    return soup.select(container + '[class*="'+string+'"]')


def find_value_in_bottom_details(soup, detail_string):
    text = find_all_container_class_contains(soup, 'span', 'OtherMatchDetails__InlineNormalText')
    titles = find_all_container_class_contains(soup, 'span', 'OtherMatchDetails__InlineBoldText')
    titles = [item.text for item in titles]
    index = titles.index(detail_string)
    output = text[index]
    return output.text


def fill_match_data_dic_from_soup(soup, dic):
    add_teams(soup, dic)
    add_result(soup, dic)
    add_location(soup, dic)
    add_toss(soup, dic)
    add_batted_first(soup, dic)
    add_comp_string(soup, dic)
    add_date_time(soup, dic)

def find_teams(soup):
    containers = find_all_container_class_contains(soup,'span', 'BoxStyle_TeamName-')
    print(containers)
    teams = []
    for c in containers:
        teams.append(c.text)
    return teams

def add_teams(soup, dic):
    teams = find_teams(soup)
    dic['left_team'] = teams[0]
    dic['right_team'] = teams[-1]

def find_result(soup):
    text = find_div_contains(soup, 'MatchSummaryText').text
    print(text)
    return text

def add_result(soup, dic):
    result_string = find_result(soup)
    dic['result_string'] = result_string


def find_location(soup):
    text = find_div_contains(soup, 'MatchAddress').text
    return text



def add_location(soup, dic):
    loc_string = find_location(soup)
    dic['location'] = loc_string

def find_toss(soup):
    return find_value_in_bottom_details(soup, 'Toss won by: ')

def add_toss(soup, dic):
    toss = find_toss(soup)
    dic['toss_won_by'] = toss


def find_batted_first(soup):
    return find_value_in_bottom_details(soup, 'Batted first: ')


def add_batted_first(soup, dic):
    batted_first = find_batted_first(soup)
    dic['batted_first'] = batted_first

def find_comp_string(soup):
    text = find_div_contains(soup, 'BoxStyle__MatchGradeName-').text
    return text

def add_comp_string(soup, dic):
    comp_string = find_comp_string(soup)
    dic['competition_string'] = comp_string

def find_datetime(soup):
    header_details = find_all_div_contains(soup, 'OtherMatchDetails__HeaderNormalText')
    return header_details[-1].text

def add_date_time(soup, dic):
    datetime = find_datetime(soup)
    dic['datetime'] = datetime







