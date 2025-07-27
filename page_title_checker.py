import requests

def get_all_article_titles(limit=500, max_pages=250):
    S = requests.Session()

    URL = "https://ta.wikipedia.org/w/api.php"
    titles = []
    params = {
        "action": "query",
        "format": "json",
        "list": "allpages",
        "aplimit": limit,
    }

    apcontinue = ""
    count = 0

    while count < max_pages:
        if apcontinue:
            params["apcontinue"] = apcontinue

        response = S.get(url=URL, params=params)
        data = response.json()

        pages = data["query"]["allpages"]
        for page in pages:
            titles.append(page["title"])

        count += 1
        print(f"Fetched {len(titles)} titles so far...")

        if "continue" in data:
            apcontinue = data["continue"]["apcontinue"]
        else:
            break

    return titles

possibly_misspelt_titles = [
"௫", "௧", "௨", "௭", "௮" # these are numbers but look similar to letters
]

# ஜீ -> ஜு  (juice written as jees)
# ju mistakenly written as juu (arjun -> arjuun)
# கௌ  (kau) written as  கெள  (keLa )
######### to check from
# ko written as ke + thunaikkaal (applies to nedil kO, also kou)
# ha written as ura உ ற ->  ஹா 
#  துணைக்கால் / ரகரம் குழப்பம் 
# scha  kuzhappam
# னை written as னன 

# check all ன்த combo for ந்த (similarly, nk, nch, nT, nth, mp)
# ஞ் ஜ -> ஞ் ச , ன் ட ->  ண் டா 
# க்க் -> க்க

# Example usage
article_titles = get_all_article_titles(limit=500, max_pages=370)
found_titles = []
for title in article_titles:
        found_titles.append(title)

for title in found_titles:
    #if "" in title or "" in title and "" in title:
         print(title)

