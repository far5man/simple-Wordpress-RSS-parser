#!/usr/bin/python
#for rss
import feedparser

d = feedparser.parse('/Users/joanhealy1/Downloads/altv.wordpress.2015-07-01-2.xml')
# Access links
print d['feed']['link']
# Access the feed's titles
print d.entries['title']
# Access the items' subtitle
print d.feed.subtitle
# Access first item's title
print d['entries'][0]['title'] 
# Find how many items in file
print len(d['entries'])

# Loop through items/posts in list 
for post in d.entries:
	# get links and titles and encode to utf8
    l = post.link.encode('utf8')
    t = post.title.encode('utf8')
	# Append to a new data file
    with open('/Applications/MAMP/htdocs/social_test/twitter/altv-wp-video-4.data', 'a+') as g:
        print post.title + "\t" + post.link + "\n"
        # Write titles and links to the file separated by tabs and newlines
        g.write("%s \t %s \n" % (t,l))



