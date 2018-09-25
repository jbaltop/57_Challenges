def get_info():
    info_list = []
    while True:
        stop = input("Do you want to stop? [Y/n] ")
        if stop.lower() == "y":
            break
        item = input("item: ")
        serial_num = input("serial number: ")
        while True:
            price = input("price($): ")
            try:
                price_float = float(price)
                break
            except ValueError:
                print("\nprice must be float")
        info_list.append([item, serial_num, price])
    return info_list


def make_json_file(info_list):
    n = len(info_list)
    with open("56.json", "wt", encoding="utf-8") as fout:
        fout.write('{"products": [')
        i = 0
        while i < n - 1:
            fout.write(
                '{"name": "'
                + info_list[i][0]
                + '", "serial_num": "'
                + info_list[i][1]
                + '", "price": "'
                + info_list[i][2]
                + '"}, '
            )
            i += 1
        fout.write(
            '{"name": "'
            + info_list[i][0]
            + '", "serial_num": "'
            + info_list[i][1]
            + '", "price": "'
            + info_list[i][2]
            + '"}'
        )
        fout.write("]}")


def make_html_file(product_list):
    with open("56.html", "wt", encoding="utf-8") as fout:
        fout.write("<html>\n  <body>\n    <table border>\n")
        fout.write(
            "      <tr>\n        <th>Name</th>\n        <th>Serial Number</th>\n        <th>Price($)</th>\n      </tr>\n"
        )
        for product in product_list:
            fout.write("      <tr>\n")
            for value in product:
                fout.write("        <td>{}</td>\n".format(value))
            fout.write("      </tr>\n")
        fout.write("    </table>\n  </body>\n</html>")


def main():
    info_list = get_info()
    make_json_file(info_list)
    make_html_file(info_list)


main()
