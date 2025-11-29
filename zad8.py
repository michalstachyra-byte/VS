import requests
import argparse

class Brewery:
    def __init__(self, id: str, name: str, brewery_type: str, street: str,
                 city: str, state: str, country: str, website_url: str):
        self.id = id
        self.name = name
        self.brewery_type = brewery_type
        self.street = street
        self.city = city
        self.state = state
        self.country = country
        self.website_url = website_url

    def __str__(self):
        return f"{self.name} ({self.brewery_type}) – {self.city}, {self.state}, {self.country}"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--city", type=str, help="Nazwa miasta do filtrowania browarów")
    args = parser.parse_args()

    # ---- Budowanie URL w zależności od argumentu ----
    if args.city:
        url = f"https://api.openbrewerydb.org/v1/breweries?by_city={args.city}&per_page=20"
    else:
        url = "https://api.openbrewerydb.org/v1/breweries?per_page=20"

    response = requests.get(url)
    data = response.json()

    browary = []
    for item in data:
        brewery = Brewery(
            id=item.get("id"),
            name=item.get("name"),
            brewery_type=item.get("brewery_type"),
            street=item.get("street"),
            city=item.get("city"),
            state=item.get("state"),
            country=item.get("country"),
            website_url=item.get("website_url")
        )
        browary.append(brewery)

    for b in browary:
        print(b)





if __name__ == "__main__":
    main()
