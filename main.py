import csv


def main():
    parts_dict = {}
    with open('productpricelinesellgroup.csv', newline='', encoding='latin-1') as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            parts_dict[row[1]] = set(row[3:])
        for k, v in parts_dict.items():
            print(k, v)
  #  with open('SalesHistory.csv', newline='', encoding='latin-1') as csv_file:



if __name__ == '__main__':
    main()
