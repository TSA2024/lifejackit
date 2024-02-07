from yaml import load, FullLoader

aspirations = []
faq: dict
quotes: list
appointment_people = (
    "Dr. Darcy",
    "Dr. Haber",
    "Dr. Orr",
    "Dr. Lelache",
)

for i in range(6):
    aspirations.append("")

with open("content.yml") as f:
    data = load(f, Loader=FullLoader)
    faq = data["faq"]
    quotes = data["quotes"]
    f.close()

