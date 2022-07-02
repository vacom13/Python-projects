import smtplib
import requests
import bs4


FROM_ADDR = ''
FROM_ADDR_PASSWORD = ''

TO_ADDRS = ''

HEADER = {
    'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
        'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36',
    'Accept-Language': 'en-US,en;q=0.9'
}
link = input("Enter Product Link: ")
threshold_price = float(input("Enter Maximum Price: ₹ "))
response = requests.get(link,headers=HEADER)

content = response.text
soup = bs4.BeautifulSoup(content, 'lxml')
name = soup.find(id='productTitle').text.lstrip().rstrip()
price = float(
    soup.find(name='span', class_='a-size-medium a-color-price priceBlockSalePriceString').text.split()[1].replace(',',
                                                                                                                   ''))
if price <= threshold_price:
    with smtplib.SMTP(host='smtp.gmail.com', port=587) as smt:
        smt.starttls()
        smt.login(user=FROM_ADDR, password=FROM_ADDR_PASSWORD)
        smt.sendmail(msg=f'Subject: Requested Product. \n\n {name} is now available for ₹ {price}.\n'
                         f'Click here to buy now: {link}'.encode('utf-8'),
                     from_addr=FROM_ADDR,
                     to_addrs=TO_ADDRS)
