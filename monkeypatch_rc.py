from selenium.webdriver.remote.remote_connection import RemoteConnection

old_init = RemoteConnection.__init__

def new_init(self, *args, **kwargs):
    kwargs['resolve_ip'] = False
    return old_init(self, *args, **kwargs)

RemoteConnection.__init__ = new_init
