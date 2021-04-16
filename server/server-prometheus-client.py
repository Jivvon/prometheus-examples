import time

from prometheus_client import CollectorRegistry, Gauge, push_to_gateway


registry = CollectorRegistry()
g = Gauge('test_last_success_time', 'Last time a batch job successfully finished', registry=registry)

if __name__ == '__main__':
    while True:
        g.set_to_current_time()
        push_to_gateway('http://pushgateway:9091', job='test_job_client', registry=registry)
        print("push metric: test_last_success_time")
        time.sleep(1)
