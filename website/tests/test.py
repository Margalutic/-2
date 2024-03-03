import requests

s = requests.Session()

username = 'Default'
key='jlIQvCua01B8kjBwZYY2z4soNut5T8kwaYfBc6uIPHmxKQq5emh8DoWpCqbXMRoaiVQ41BzCIUk5U65bx5IZulFR2fOQYC1SzGDiht8DwLALlQvVwjtyuaVpRZU23e2TuO2Vh7YRTCIbBEhgHenQKqvnxoTPuUhC2LZiT61muvFwWou3IHWsnjmtY5EfCLP2haWHa82M2KcdCcGQrbimeO6eUeCrG1AMZQf5vj6qXTy74vO8I4UjBQgi1xDB5Q82'
# Actually, key is 256 character-long

s.post(
    'http://myopencart.localhost/index.php?route=api/login',
    data={'username':username, 'key':key}
).text