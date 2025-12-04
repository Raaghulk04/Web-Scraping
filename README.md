# Book Price Tracker — Web Scraping & Email Alert System

This project is a simple web-scraping price tracker built using Python, requests, and BeautifulSoup.
It monitors a product page on BooksToScrape.com, extracts the book title and price, and automatically sends an email notification when the price drops below a chosen threshold.

# What the script does

* Fetches HTML from a book page

* Parses the page using BeautifulSoup

* Extracts:

  - Book name

  - Current price

* Compares the scraped price against a target value

* Sends an email alert through Gmail’s SMTP server if the price is low enough

# This makes it useful as a beginner-friendly demonstration of:

* Basic web scraping

* HTML parsing

* Automating tasks with Python

* Using SMTP to send emails

* Simple data monitoring logic

# Technologies Used

* Python 3

* requests

* BeautifulSoup4

* smtplib for email

* Gmail App Password for secure authentication

# Notes

* Gmail now requires an App Password instead of a normal email password.

* The scraper includes a User-Agent header to avoid blocked requests.

* BooksToScrape is a public demo website specifically built for practicing scraping — safe and legal to use.


