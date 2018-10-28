from urllib.request import urlopen


def download_name_list():
    url = "https://projecteuler.net/project/resources/p022_names.txt"
    data = urlopen(url).read()
    decoded = data.decode('utf-8').replace('"', '')
    return sorted(decoded.split(','))


def calculate_name_score():
    names = download_name_list()

    for x in range(0, len(names)):
        name = names[x]
        for char in name:
            yield (x + 1) * (ord(char) - 64)


print(sum(calculate_name_score()))