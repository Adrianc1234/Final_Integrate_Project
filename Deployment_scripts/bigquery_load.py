from datetime import datetime
def loading_data(client, table, original_tweet, app_label, sentiment_result):
    e = datetime.now()
    row = [{
        "Date":e,
        "Text":original_tweet,
        "App":app_label,
        "Sentiment":sentiment_result,
        "Location":"",
        "Available":"F"
        }]

    errors = client.insert_rows(table, row)

    if errors == []:
        print("New rows have been added")
    else:
        print("Error: Couldn't insert error")
    

#loading_data(client, table, "")
