from google.cloud import pubsub_v1
import datetime
import json
import sensordata
import time

project_id = "<your prject id&gt;"  # enter your project id here
topic_name = "<topic name&gt;"  # enter the name of the topic that you created

publisher = pubsub_v1.PublisherClient()
topic_path = publisher.topic_path(project_id, topic_name)

futures = dict()


def get_callback(f, data):
    def callback(f):
        try:
            # print(f.result())
            futures.pop(data)
        except:
            print("Please handle {} for {}.".format(f.exception(), data))

    return callback


while True:
    time.sleep(3)
    distance = round(float(sensordata.FindDistance()), 2)
    timenow = float(time.time())
    # timenow = datetime.datetime.now()
    data = {"time": timenow, "distance": distance}
    print(data)
    # When you publish a message, the client returns a future.
    future = publisher.publish(
        topic_path, data=(json.dumps(data)).encode("utf-8"))  # data must be a bytestring.
    # Publish failures shall be handled in the callback function.
    future.add_done_callback(get_callback(future, data))
    time.sleep(5)
# Wait for all the publish futures to resolve before exiting.
while futures:
    time.sleep(5)

print("Published message with error handler.")