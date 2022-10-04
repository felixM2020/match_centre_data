# match_centre_data
A project scraping and cleaning data off of the local cricket match centre website.
Whilst this works for all match centre systems, this [link](https://matchcentre.cricketact.com.au/) was used for the data cleaning and analysis part of the repository.

## Single Game Scraper
Used to scrape an individual game off of the match centre system and convert the data to seperate dataframes, specifically divided into match details, individual batting and bowling results.


## Multiple Game Scraper
Use single game scraper and recurse it over all matches in a list of matches.
Includes season scraper.

## Scraper UI
Make user interface to download csv file of scraped data in which you can choose season and grade specifics.
Is executable without python.

## Scraped Data Cleaner
Functions to clean data df for all 4 df types.

## Data Analysis
Analyse last season's act premier cricket season.

