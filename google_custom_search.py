from googleapiclient.discovery import build

# define key
api_key = "Enter API Key Here"
cse_key = "Enter CSE Key Here"

# function to call custom Google api search
def google_search(search_term, cse_id, **kwargs):
    service = build("customsearch", "v1", developerKey=api_key)
    res = service.cse().list(q=search_term, cx=cse_id, **kwargs).execute()
    return res['items']


# function insert new search keyword and return found results
def get_data(keyword, all_link = [], all_title = [], all_snippet = []):
    # perform custom search
    results = google_search(keyword, cse_key, num=10, cr="countryUK", lr="lang_en")
    # loop through all returned results and get data
    for result in results:
        all_link.append(result.get('link'))
        all_title.append(result.get('title'))
        all_snippet.append(result.get('snippet'))
    # returns searched results
    return all_link, all_title, all_snippet



