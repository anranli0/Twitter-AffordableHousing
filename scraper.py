import time
import re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from datetime import date, timedelta, datetime
import json
import csv

def get_num(str):
    return int(re.search(r'\d+', str).group(0))

def get_date_range(start, end):
    days = []
    delta = end - start
    for i in range(delta.days + 1):
        day = start + timedelta(days=i)
        days.append(str(day))
    return days

def single_tweet(tweet):

    info = tweet.find_element(by=By.CSS_SELECTOR, value="a.r-bcqeeo.r-3s2u2q.r-qvutc0")
    info_lst = info.get_attribute("href").split("/")
    username = info_lst[3]
    tweetid = info_lst[-1]

    content = tweet.find_element(by=By.CSS_SELECTOR, value='div[lang]').text

    reply = tweet.find_element(by=By.CSS_SELECTOR, value='[data-testid="reply"]')
    reply_str = reply.get_attribute("aria-label")
    reply_count = get_num(reply_str)

    retweet = tweet.find_element(by=By.CSS_SELECTOR, value='[data-testid="retweet"]')
    retweet_str = retweet.get_attribute("aria-label")
    retweet_count = get_num(retweet_str)

    timestamp = tweet.find_element(by=By.TAG_NAME, value="time").get_attribute("datetime")
    timestamp_lst = timestamp.replace('T', '.').split('.')
    date_ = timestamp_lst[0]
    hms = timestamp_lst[1]

    likes = tweet.find_element(by=By.CSS_SELECTOR, value='[data-testid="like"]')
    likes_str = likes.get_attribute("aria-label")
    likes_count = get_num(likes_str)

    hashtags = re.findall(r"#(\w+)", content)
    mentions = re.findall(r"@(\w+)", content)

    single = {
            'tweetid': tweetid,
            'username': username,
            'content': content,
            'reply': reply_count,
            'retweet': retweet_count,
            'likes': likes_count,
            'date': date_,
            'time': hms,
            'hashtags': hashtags,
            'mentions': mentions
        }
    return tweetid, single

def scrape(start_date, end_date, ndowns=20, hashtag='affordablehousing'):
    # count = 0
    days = get_date_range(start_date, end_date)
    t = {}
    for since, until in zip(days[:-1], days[1:]):
        url = f'https://mobile.twitter.com/search?f=live&q=(%23{hashtag})%20until%3A{until}%20since%3A{since}%20-filter%3Areplies&src=typed_query'
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get(url)
        time.sleep(6)

        for _ in range(ndowns):
            body = driver.find_element(by=By.CSS_SELECTOR, value='body')
            for _ in range(6):
                body.send_keys(Keys.PAGE_DOWN)
                time.sleep(0.5)
            
            tweets = driver.find_elements(by=By.CSS_SELECTOR, value='[data-testid="tweet"]')
            for tweet in tweets:
                try:
                    tweetid, single = single_tweet(tweet)
                except:
                    continue
                if tweetid in t: 
                    # count += 1
                    continue
                t[tweetid] = single

        driver.close()
        driver.quit()
    
    outname = './data/2.csv'
    data = list(t.values()) 
    headers = list(data[0].keys())
    with open(outname,'w',newline='') as data_file:
        writer = csv.DictWriter(data_file,fieldnames=headers)
        writer.writerows(data)

