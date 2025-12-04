import smtplib
import requests
from bs4 import BeautifulSoup


def scrape_book_info():
    try: 
        url = "https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"
        html = requests.get(url).text

        soup = BeautifulSoup(html, "html.parser")#Parese the HTML content#

        name = soup.find("h1").get_text(strip=True) #Get the book title#
        price = soup.find("p", class_="price_color").get_text(strip=True) #Get the book price#
        real_price = price[2:] #Remove the currency symbol#

        print(name, real_price)
        if float(real_price) < 60.00:
            send_mail()
    except Exception as e:
        print("Error during scraping:", e)        

def send_mail():
    print("Preparing to send email...")
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login("raaghulk04@gmail.com", "iwsc lbby juid lcfs")
        msg = "Subject: Book Price Alert!\n\nThe price of the book you wanted has dropped!"
        server.sendmail(
            "raaghulk04@gmail.com", "raaghulk04@gmail.com", msg)
        print("Mail Sent")
    except Exception as e:
        print("Failed to send email:", e)
    finally:
        server.quit()        

scrape_book_info();    