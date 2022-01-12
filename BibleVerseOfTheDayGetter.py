import requests
import re
import html

def getVerseOfTheDay():
    link = "https://www.biblegateway.com/votd/get/?format=html&version=NIV"
    f = requests.get(link) #This downloads the HTML for the verse of the day

    
    verse_body = re.search(r'&ldquo;(.*?)&rdquo;',f.text).group(1) #This regexes for text between quotation marks
    verse_index = re.search(r'>(.*?)</a>',f.text).group(1) #This searches for the index

    output = html.unescape(verse_index + ' "' + verse_body+'"') #This adds some quotes in a structes it a little bit
    return output
