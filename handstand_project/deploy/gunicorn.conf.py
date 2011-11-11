bind = "127.0.0.1:29000"
logfile = "/sites/{{ site_url }}/logs/gunicorn.log"
workers = 3
working_dir = '/sites/{{ site_url }}/'
