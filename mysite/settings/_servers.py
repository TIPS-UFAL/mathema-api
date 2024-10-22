import socket


def get_server_type():
    host = socket.getfqdn(socket.gethostname()).split('.')
    if len(host) == 6 and host[4] == 'heroku':
        return 'production'
    return 'development'
