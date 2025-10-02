from prometheus_flask_exporter.multiprocess import GunicornPrometheusMetrics

bind = "0.0.0.0:5000"  # Your main Flask app port
workers = 2
#threads = 2

def when_ready(server):
    # start the separate metrics HTTP server on 9090 (host optional)
    GunicornPrometheusMetrics.start_http_server_when_ready(port=9090, host="0.0.0.0")
    server.log.info("Requested Prometheus metrics HTTP server to start on port 9090")

def child_exit(server, worker):
    # ensure multiprocess files from the worker are marked dead on exit
    GunicornPrometheusMetrics.mark_process_dead_on_child_exit(worker.pid)


