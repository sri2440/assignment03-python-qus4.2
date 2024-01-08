import re

text = """
Sample text with email addresses:
john.doe@example.com
alice_smith123@example.co.uk
support@company.com
"""

email_pattern = re.compile(r'(\b[A-Za-z0-9._%+-]+)@([A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b)')

matches = email_pattern.findall(text)

for match in matches:
    username, domain = match
    print(f"Username: {username}, Domain: {domain}")
