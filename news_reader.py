import feedparser
import os
import random
from talker import say_text
from talker import greeting

def get_entries(url):
    return feedparser.parse(url).entries

def format_entry(entry):
    print entry["link"]
    return "[[slnc 700]] %s" % entry["title"]

def read_news(url):
    return [say_text(format_entry(entry)) for entry in get_entries(url)]

def run_reader():
    print "Reading..."
    greeting()
    [read_news(url) for url in random.choice([
        "http://rss.nytimes.com/services/xml/rss/nyt/World.xml",
        "http://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml",
        "http://rss.nytimes.com/services/xml/rss/nyt/Technology.xml",
        "http://rss.nytimes.com/services/xml/rss/nyt/Arts.xml",
        "http://rss.nytimes.com/services/xml/rss/nyt/Travel.xml",
        "http://rss.nytimes.com/services/xml/rss/nyt/Sports.xml",
        "http://rss.nytimes.com/services/xml/rss/nyt/Science.xml",
        "http://rss.nytimes.com/services/xml/rss/nyt/Health.xml"
    ])]

run_reader()