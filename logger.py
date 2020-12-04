log_file = "log.txt"

def log(msg):
    f"""
    Sauvegarde le msg dans un log file {log_file}
    :param msg: le message à ajouter dans le log file
    """
    with open(log_file, 'a') as f:
        f.write(msg + '\n')