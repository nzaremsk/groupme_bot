import re

link_pattern = r'\w+\.\w+'

		
print(re.match(link_pattern, "link.com"))
print(re.match(link_pattern, "link."))
print(re.match(link_pattern, "linkcom"))
print(re.match(link_pattern, ".com"))
print(re.match(link_pattern, "http://bit.ly/asdf"))