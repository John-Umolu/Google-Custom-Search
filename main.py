import google_custom_search
from threading import Event

'''
# For single word or sentence search
# perform a new Google search using the text input
links, titles, snippets = google_custom_search.get_data("Chatbot using Deep Learning")
# loop through all the found results
for i in range(len(links)):
    # display all the results
    print('>> Webpage Title: ' + titles[i] + '\n>> Website Link: ' + links[i] + '\n>> Snippets: ' + snippets[i] + '\n')
'''

# for multiple word or sentence in a list search
list_of_searches = ['What is machine learning', 'What is Artificial Intelligence']
for search_item in list_of_searches:
    # perform a new Google search using the text input
    links, titles, snippets = google_custom_search.get_data(search_item)
    while len(links) == 0:
        print("Waiting for result")
        # 60 seconds delay
        Event().wait(60)
        links, titles, snippets = google_custom_search.get_data(search_item)
    else:
        # loop through all the found results
        for i in range(len(links)):
            # display all the results
            print('Searched Item: ' + search_item + '\n>> Webpage Title: ' + titles[i]
                  + '\n>> Website Link: ' + links[i] + '\n>> Snippets: ' + snippets[i] + '\n')