import feedparser
def rss_scrappy(url):
    f = feedparser.parse(url)
    rss = {}

    for entry in f.entries:
        rss[entry.title] = [entry.summary, entry.link]

    return rss