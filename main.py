from api.amsterdam_api import AmsterdamApi


def main():
    amsterdam_api = AmsterdamApi()
    list_trash_bins = amsterdam_api.get_trash_bins()
    list_monuments = amsterdam_api.get_monuments()

    print("Overview of trash bins in Amsterdam \n")

    for trash_bin in list_trash_bins:
        print(
            str(trash_bin['id']) + "\t" +
            trash_bin['name'] + "\t" +
            trash_bin['type'] + "\t" +
            trash_bin['address']
        )

    print("Overview of monuments in Amsterdam \n")

    for monument in list_monuments:
        print(
            str(monument['id']) + "\t" +
            monument['address'] + "\t"
        )


if __name__ == "__main__":
    main()
