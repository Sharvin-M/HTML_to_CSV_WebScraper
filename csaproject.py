import csv
import requests
from bs4 import BeautifulSoup
import pandas
import random

#By: Sai Kolla, Sharvin Manjrekar, Anirudh Nagasamudra, Joshua Chon

def scrape_data(url):

    #getting a request to search a website
    response = requests.get(url, timeout=10)

    soup = BeautifulSoup(response.content, 'html.parser')

    #finding the first table
    table = soup.find_all('table')[0]
    
    #making all the columns
    rows = table.select('tbody > tr')
   
    #making all the column headers
    header = [th.text.rstrip() for th in rows[0].find_all('th')]

    #writing a csv file with all of the rows and columns 
    with open('output.csv', 'w') as csv_file:

        writer = csv.writer(csv_file)
        writer.writerow(header)
        for row in rows[1:]:
            data = [th.text.rstrip() for th in row.find_all('td')]
            writer.writerow(data)

#finds the population of the country that you said 
def askQuestion(csv_name, country):
    countries = pandas.read_csv(csv_name)
    name = countries.Rank.to_list()
    population = countries.Population.to_list()

#loops through the countries to find the one you sent and writes the population percentage of it
    for i in range(len(name)):
        countryname = name[i].lower()
        if (countryname.find(country.lower()) != -1):
            print(country + "'s population percentage is: " + str(population[i]))

#displays the entire csv
def showCSV():
    countries = pandas.read_csv("output.csv")
    name = countries.Rank.to_list()
    population = countries.Population.to_list()
    for i in range(len(name)):
        print(name[i] + ": " + population[i])


if __name__ == "__main__" :
    
   url = "https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population"
   scrape_data(url)

    #input a choice to either stop, display entire csv, and ask a question 
   answer = " "

   #loops asking question until user enters stop
   while (answer != "stop"):
    answer = input("If you want to know the total population type 'P'. If you want to see the list of all the countries and their population percentage press 'C'. If you want to stop running, type 'stop'. ")
   
   # if p, gets the population of desired country
    if (answer.lower() == "p"):
        countryAnswer = input('What country do you want to know the population percent of?: ')
        askQuestion('output.csv', countryAnswer)
        
    #if C, gets population of all of them
    if (answer.lower() == "c"):
        showCSV()



