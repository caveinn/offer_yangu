import os

# default values
defaults = {
    "DB_USERNANE": "root",
    "DB_PASSWORD": "root",
    "DB_HOST": "localhost",
    "DB_PORT": "5432"
}


def config(var):
    val = os.getenv(var)
    if not val:
        val = defaults.get(var)
    if not val:
        raise Exception("Env Value does not exist")
    return val
