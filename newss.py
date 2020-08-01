import feedparser
def parseRSS(rss_url):
    return feedparser.parse(rss_url)
def getHeadLines(rss_url):
    headlines = []
    feed = parseRSS(rss_url)
    for newitem in feed['items']:
        headlines.append(newitem['title'])
    return headlines
allheadlines = []
newsurls={'googlenews': 'https://news.google.com/news/rss/?h1=ta&amp;ned=us&amp;gl=IN',}# I used IN in this line for indian news instead of that you can use your capital's
for key, url in newsurls.items():
    allheadlines.extend(getHeadLines(url))
for h in allheadlines:
    print(h)
