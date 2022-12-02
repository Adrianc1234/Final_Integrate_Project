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

from google.api_core import retry
from google.cloud import pubsub_v1

# TODO(developer)
project_id = "places-api-364005"
subscription_id = "sub_one"

subscriber = pubsub_v1.SubscriberClient()
subscription_path = subscriber.subscription_path(project_id, subscription_id)

NUM_MESSAGES = 20000
counter=0
# Wrap the subscriber in a 'with' block to automatically call close() to
# close the underlying gRPC channel when done.
with subscriber:
    # The subscriber pulls a specific number of messages. The actual
    # number of messages pulled may be smaller than max_messages.
    response = subscriber.pull(
        request={"subscription": subscription_path, "max_messages": NUM_MESSAGES},
        retry=retry.Retry(deadline=300),
    )

    if len(response.received_messages) == 0:
        quit()

    ack_ids = []
    for received_message in response.received_messages:
        #print(f"Received: {received_message.message.data}.")
        counter=counter+1
        print(counter)
        ack_ids.append(received_message.ack_id)

    # Acknowledges the received messages so they will not be sent again.
    subscriber.acknowledge(
        request={"subscription": subscription_path, "ack_ids": ack_ids}
    )

    print(
        f"Received and acknowledged {len(response.received_messages)} messages from {subscription_path}."
    )



