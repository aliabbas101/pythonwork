import re
text="My number is 415-555-2121"
phoneNumber=re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNumber.search(text)
area, country = mo.groups()
print('Area Code: '+ mo.group(1)+'Country code: '+mo.group(2))
