import os
from sqlalchemy import create_engine
engine = create_engine('mysql+mysqldb://root:damos02@host:3306/blackjack')

# To generate a new secret key:
# >>> import random, string
# >>> "".join([random.choice(string.printable) for _ in range(24)])
SECRET_KEY = "#d#JCqTTW\nilK\\7m\x0bp#\tj~#H"

FB_APP_ID = 1200420960103822





