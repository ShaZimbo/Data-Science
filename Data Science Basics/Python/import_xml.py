"""Importing xml data"""
import xml.etree.ElementTree as ET

tree = ET.parse('movie.xml')
root = tree.getroot()

unique_tags = set()
print(f"{'Unique child tags'}\n{'-'*20}\n")

for movie in root.iter('movie'):
    for child in movie.iter():
        unique_tags.add(child.tag)

for tag in unique_tags:
    print(f"{tag}\n")
print(f"{'-'*20}\n")

print(f"{'Descriptions:'}\n{'\u2500'*100}")

for description in root.iter('description'):
    for d in description.itertext():
        print(f"\n{d}\n{'-'*100}\n")

COUNT_TRUE = 0
COUNT_FALSE = 0

for movie in root.iter('movie'):
    favorite = movie.get('favorite')
    if favorite is not None:
        favorite = favorite.lower()
        if favorite == "true":
            COUNT_TRUE += 1
        elif favorite == "false":
            COUNT_FALSE += 1

print(f"{'\u2500'*60}\n"
      f"{'Number of movies that are favorites:':<50}{COUNT_TRUE}\n"
      f"{'Number of moview that are not favorites:':<50}{COUNT_FALSE}\n"
      f"{'\u2500'*60}\n"
      )
