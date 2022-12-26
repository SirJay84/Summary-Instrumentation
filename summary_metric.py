from prometheus_client import start_http_server, Summary 
import random
import time

# Create a metric to track time spent and requests made.
REQUEST_TIME = Summary(
    'request_processing_seconds',
    'Time spent processing a request',
  )

# Decorate function with metric.
@REQUEST_TIME.time()
def render_user_page(self):
    time.sleep(1)
    
    
if  __name__ == '__main__':
  # Start up the server to expose the metrics.
  start_http_server(8000)
  # Generate some requests.
  while True:
    render_user_page(random.random())
