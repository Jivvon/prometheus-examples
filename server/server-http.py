import time
import random
import requests


job_name='test_job_http'
instance_name='instance_name'
payload_key='test_metric_http'


def _post():
    url = 'http://pushgateway:9091/metrics/job/{j}/instance/{i}'.format(j=job_name, i=instance_name)
    payload_value = random.random()*100
    response = requests.post(url, data="{k} {v}\n".format(k=payload_key, v=payload_value))

    print('status: {status}'.format(status=response.status_code))


if __name__ == '__main__':
    while True:
        _post()
        time.sleep(1)

# PROMQL: avg(rate(test_metric_http[1m]))
