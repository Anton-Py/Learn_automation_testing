import random
import string


def random_email():
    domains = ['ru', 'com', 'de']
    names = ['round', 'texas', 'kent']

    def create_random_int():
        return random.randint(100, 999)

    def create_random_words():
        return "".join(random.choice(string.ascii_letters) for _ in range(2))

    def random_domain():
        return random.choice(domains)

    def random_name():
        return random.choice(names)

    return f"{random_name()}{create_random_int()}@{create_random_words()}.{random_domain()}"
