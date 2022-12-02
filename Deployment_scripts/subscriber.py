#!/usr/bin/env python

# Copyright 2019 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import argparse
from typing import Optional
import json
import base64
import classifier
import bigquery_load
import sentiment
from google.cloud import pubsub_v1
from google.cloud import bigquery
from datetime import datetime

client = bigquery.Client()
table = client.get_table("places-api-364005.nlp_deep.tweet_results")

def sub(project_id: str, subscription_id: str, timeout: Optional[float] = None) -> None:
    """Receives messages from a Pub/Sub subscription."""
    # Initialize a Subscriber client
    subscriber_client = pubsub_v1.SubscriberClient()
    # Create a fully qualified identifier in the form of
    # `projects/{project_id}/subscriptions/{subscription_id}`
    subscription_path = subscriber_client.subscription_path(project_id, subscription_id)

    def callback(message: pubsub_v1.subscriber.message.Message) -> None:
        dictionary = json.loads(json.loads((message.data)))
        data = dictionary['data']
        text = data['text']

        # TRANSFORM
        
        app_name = classifier.prediction(text)
        sentiment_result = sentiment.sentiment(text)

        global client
        global table
        # LOAD
        bigquery_load.loading_data(client, table, text, app_name, sentiment_result)



    streaming_pull_future = subscriber_client.subscribe(
        subscription_path, callback=callback
    )
    print(f"Listening for messages on {subscription_path}..\n")

    try:
        # Calling result() on StreamingPullFuture keeps the main thread from
        # exiting while messages get processed in the callbacks.
        streaming_pull_future.result(timeout=timeout)
    except:  # noqa
        streaming_pull_future.cancel()  # Trigger the shutdown.
        streaming_pull_future.result()  # Block until the shutdown is complete.

    subscriber_client.close()


if __name__ == "__main__":
    sub("places-api-364005", "sub_one")
