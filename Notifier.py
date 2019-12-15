# Kalr 2019 - Limited Notifer Edited.
# This actually doesn't notify it prints.
import requests, time

def lims():
    req = requests.get('https://www.roblox.com/catalog/json?Category=2&Subcategory=2&SortType=3&Direction=2&PageHash" \
          "=0e4ba52b8fb2ab17f924d1fdc696e22d').json()

    limiteds = []
    for x in req:
        if x["Remaining"] == "":
            continue
        remaining = int(x["Remaining"])
        if remaining > 0:
            limiteds.append(x)
    return limiteds

def main():
    items = lims()
    for x in items:
        print(x["Name"])
    return

while True:
    time.sleep(1000)
    main()
