import requests
import openpyxl
from bs4 import BeautifulSoup

excel = openpyxl.Workbook()
print(excel.sheetnames)
sheet = excel.active
sheet.title = 'Books'
print(sheet.title)
sheet.append(['title'])


url = 'https://books.toscrape.com'
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

    # Corrected element selection based on the website's structure
    # For example, let's scrape the titles of the books
    books = soup.find_all('h3')

    for book in books:
        title = book.find('a')['title']
        print(title)
        sheet.append([title])
    excel.save('books.xlsx')
else:
    print("Website not reachable!")
