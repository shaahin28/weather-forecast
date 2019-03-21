import requests #for webscraping

from bs4 import BeautifulSoup #for webscraping

import datetime as dt #for sending email

import smtplib #for sending email

import time #for sending email


page = requests.get('https://globalnews.ca/bc/weather/CAXX1311') #this is the link for Coquitlam,BC Canada,you can change it to the desired city

soup = BeautifulSoup(page.content,'html.parser')

city = soup.find('h3',class_='section-h-new').span.text.split('-')[1] #shows the city name

print('City : ',city)

temp = soup.find('div',class_='weather-column weather-new-temp').span.text

temp = str(temp.replace('°',''))

print('Current Temprature : ',temp)

today_high = soup.find('span',class_='weather-high-low').text

today_high = str(today_high.replace('°',''))

print(today_high)

today_low = soup.find_all('span',class_='weather-high-low')[1].text

today_low = str(today_low.replace('°',''))

print(today_low)

sky = str(soup.find('span',class_='weather-icon-description').text) #sky condition like cloudy,rainy or ...

print('Sky Condition : ',sky)


def send_email():
    user_email = 'youremail@gmail.com'
    recipients = ['recipent1@gmail.com','recipent2@yahoo.com'] #you can add as many as you want
    server = smtplib.SMTP ('smtp.gmail.com', 587)
    server.starttls()
    server.login(user_email, 'your password here')

    message = "Subject : Automatic Weather info\n\nThe weather information for : {}\nThe current temprature is : {}\nToday high : {}\nToday low: {}\nSky condition : {}".format(city,temp,today_high,today_low,sky)
    server.sendmail(user_email, recipients, message)
    server.quit()

#some of time module functions :

# print(time.ctime()) --> will show us the local time

# time.sleep(seconds) --> Suspend execution of the calling thread for the given number of seconds

# time.time() --> Return the time in seconds since the epoch as a floating point number. epoch in linux is Jan 1st 1970 0:0:0

def send_email_at(send_time):
    time.sleep(send_time.timestamp() - time.time())
    send_email()
    print('Email sent')


first_email_time = dt.datetime(2019,3,13,7,0,0) # set your sending time

interval = dt.timedelta(minutes=24*60) # set the interval for sending the email

send_time = first_email_time

while True:
    send_email_at(send_time)
    send_time = send_time + interval

send_email_at(send_time)
