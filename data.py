from yaml import load, FullLoader

faq: dict

with open("content.yml") as f:
    data = load(f, Loader=FullLoader)["faq"]
    faq = data
    f.close()
