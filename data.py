from yaml import load, FullLoader

aspirations = []
faq: dict

for i in range(6):
    aspirations.append("")

with open("content.yml") as f:
    data = load(f, Loader=FullLoader)["faq"]
    faq = data
    f.close()

