from yaml import load, FullLoader

faq: dict
quotes: list

with open("content.yml") as f:
    data = load(f, Loader=FullLoader)
    faq = data["faq"]
    quotes = data["quotes"]
    f.close()
