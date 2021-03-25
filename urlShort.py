import pyshorteners

def shortner(link):
    # creating object ..
    short = pyshorteners.Shortener()
    short_link = short.tinyurl.short(link)
    return short_link

url = input("Enter url : ")
final = shortner(url)
print(f"Shortened Link is {final}")
