import feedparser
import os
import random

def get_entries(url):
    return feedparser.parse(url).entries

def read_text(text, voice):
    return os.system("say \"%s\" --voice=%s" % (text.encode('utf-8'), voice))

def read_entry(news):
    return read_text(news, random.choice([
        "Samantha",
        "Alex",
        "Daniel",
        "Karen",
        "Tessa"
    ]))

def get_tag():
    return random.choice([
        "In other news...",
        "Meanwhile..."
    ])

def format_entry(entry):
    return "%s %s. %s." % (get_tag(), entry["title"], entry["description"])

def read_news(url):
    return [read_entry(format_entry(entry)) for entry in get_entries(url)]

print "Reading..."
read_news(random.choice([
    "http://rss.nytimes.com/services/xml/rss/nyt/World.xml",
    "http://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml",
    "http://rss.nytimes.com/services/xml/rss/nyt/Technology.xml",
    "http://rss.nytimes.com/services/xml/rss/nyt/Arts.xml",
    "http://rss.nytimes.com/services/xml/rss/nyt/Travel.xml",
    "http://rss.nytimes.com/services/xml/rss/nyt/Sports.xml",
    "http://rss.nytimes.com/services/xml/rss/nyt/Science.xml",
    "http://rss.nytimes.com/services/xml/rss/nyt/Health.xml"
]))
