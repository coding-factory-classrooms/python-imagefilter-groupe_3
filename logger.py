log_file = "log.txt"

def log(msg):
    with open(log_file, 'a') as f:
        f.write(msg + '\n')