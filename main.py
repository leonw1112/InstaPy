import instaloader
from instapy_cli import client

# Instagram credentials
username = 'YOUR_USERNAME'
password = 'YOUR_PASSWORD'
print('Logging in with Username:' + username + 'password:' + password)

# Login to Instagram with instaloader
try :
    L = instaloader.Instaloader()
    L.login(username, password)
except:
    print('Login failed, please check your credentials.')
    exit()

# Search for users
keyword = 'test'
users = L.get_profiles_by_username_generator(keyword)

# Login to Instagram with instapy-cli
with client(username, password) as cli:
    # Send a message to each user
    for user in users:
        cli.direct_message(user.username, 'Hello, this is a test message.')