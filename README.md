# prometheus-examples

### push gateway

1. using `prometheus_client`
    ```python
    from prometheus_client import CollectorRegistry, Gauge, push_to_gateway
    
    
    registry = CollectorRegistry()
    g = Gauge('test_last_success_time', 'Last time a batch job successfully finished', registry=registry)
    g.set_to_current_time()
    push_to_gateway('http://pushgateway:9091', job='test_job_client', registry=registry)
    ```
   
2. using `requests (http)`
    ```python
    url = 'http://pushgateway:9091/metrics/job/{j}/instance/{i}'.format(j=job_name, i=instance_name)
    payload_value = random.random()*100
    response = requests.post(url, data="{k} {v}\n".format(k=payload_key, v=payload_value))
    ```
