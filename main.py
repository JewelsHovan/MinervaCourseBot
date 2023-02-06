from mainwindow import MainWindow
from date_scraper import DateScraper

if __name__ == "__main__":
    # scrape key dates from McGill Site
    date_scraper = DateScraper()
    date_scraper.write_key_dates()
    # run the MainWindow
    main_window = MainWindow()

