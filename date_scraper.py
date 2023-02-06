import requests
from bs4 import BeautifulSoup
from datetime import datetime

# get data from mcgill website
# the keydates of each semester such as:
# - add/drop
# - start of classes
# - end of classes
class DateScraper:
    def __init__(self):
        self.url = "https://www.mcgill.ca/importantdates/key-dates"
        self.response = requests.get("https://www.mcgill.ca/importantdates/key-dates")
        self.soup = BeautifulSoup(self.response.text, "html.parser")
        self.key_dates = {} # stores key dates

    def write_website_html(self, file_name):
        with open(file_name, 'w') as wf:
            wf.write(self.soup.prettify())
    
    def extract_key_dates(self):
        '''
        Extracts the key dates from the beautifulsoup object and 
        stores the key dates in a dictionary -> self.key_dates
        '''
        self.data = self.soup.find_all("li")
        important_elements = []
        for element in self.data:
            if "Classes" in element.text or "Add/Drop" in element.text:
                important_elements.append(element.text)
        for e in important_elements:
            e = e.strip('\\')
            e = e.split('(')[0]
            e_split = e.split(":")
            self.key_dates[e_split[1]] = e_split[0]

        # find the years
        self.data2 = self.soup.find_all("h2")
        for e in self.data2:
            if "Fall" in e.text:
                self.fall_year = e.text.split(" ")[-1]
            if "Winter" in e.text:
                self.winter_year = e.text.split(" ")[-1]


    def write_key_dates(self):
        if self.key_dates == {}: # if haven't extracted
            self.extract_key_dates()
        # write to file
        with open('key_dates.txt', 'w') as wf:
            counter = 0
            for key, value in self.key_dates.items():
                if counter == 0:
                    wf.write(f"Key Dates for Fall {self.fall_year}:\n")
                if counter == 3:
                    wf.write(f"Key Dates for Winter {self.winter_year}:\n")
                if counter < 3:
                    wf.write(str(value) + ": " + str(key) + " " + str(self.fall_year) +"\n")
                elif counter >= 3: 
                    wf.write(str(value) + ": " + str(key) + " " + str(self.winter_year) + "\n")
                counter += 1


if __name__ == "__main__":
    test_date_str = "Wednesday, August 31 2022"
    date_format = "%A, %B %d %Y"
    aDate = datetime.strptime(test_date_str, date_format)


