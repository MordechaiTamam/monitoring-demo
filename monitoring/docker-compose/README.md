## Example on how to use Prometheus and Grafana to monitor a Flask API application

Example deployment of a Flask API using Prometheus and Grafana for metrics and monitoring. All tied together using docker-compose.

### Install dependencies

```
pip install -r api/requirements.txt
```

### Set up and run everything using docker-compose

```
docker-compose up
```

### Access

* API: http://localhost:5000/flask-prometheus-grafana-example/
* Prometheus: http://localhost:9090/
* Grafana: http://localhost:3000 `[username: admin, password: pass@123]`
### Requests per second

Number of successful Flask requests per second. Shown per path.

```
rate(
  flask_http_request_duration_seconds_count{status="200"}[30s]
)
```

### Errors per second

Number of failed (non HTTP 200) responses per second.

```
sum(
  rate(
    flask_http_request_duration_seconds_count{status!="200"}[30s]
  )
)
```

### Total requests per minute

The total number of requests measured over one minute intervals. Shown per HTTP response status code.

```
increase(
  flask_http_request_total[1m]
)
```

### Average response time [30s]

The average response time measured over 30 seconds intervals for successful requests. Shown per path.

```
rate(
  flask_http_request_duration_seconds_sum{status="200"}[30s]
)
 /
rate(
  flask_http_request_duration_seconds_count{status="200"}[30s]
)
```

### Requests under 250ms

The percentage of successful requests finished within 1/4 second. Shown per path.

```
increase(
  flask_http_request_duration_seconds_bucket{status="200",le="0.25"}[30s]
)
 / ignoring (le)
increase(
  flask_http_request_duration_seconds_count{status="200"}[30s]
)
```

### Request duration [s] - p50

The 50th percentile of request durations over the last 30 seconds. In other words, half of the requests finish in (min/max/avg) these times. Shown per path.

```
histogram_quantile(
  0.5,
  rate(
    flask_http_request_duration_seconds_bucket{status="200"}[30s]
  )
)
```

### Request duration [s] - p90

The 90th percentile of request durations over the last 30 seconds. In other words, 90 percent of the requests finish in (min/max/avg) these times. Shown per path.

```
histogram_quantile(
  0.9,
  rate(
    flask_http_request_duration_seconds_bucket{status="200"}[30s]
  )
)
```

### Memory usage

The memory usage of the Flask app. Based on data from the underlying Prometheus client library, not Flask specific.

```
process_resident_memory_bytes{ job="flask-api"}
```

### CPU usage

The CPU usage of the Flask app as measured over 30 seconds intervals. Based on data from the underlying Prometheus client library, not Flask specific.

```
rate(
  process_cpu_seconds_total{ job="flask-api"}[30s]
)
```

