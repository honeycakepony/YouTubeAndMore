from collections import Counter

if __name__ == '__main__':
    with open('references.bib', 'r') as doc:
        file = doc.read().split('\n')
        # print(file[:10], sep='\n')
        count = 0
        list_year: list[int] = list()
        for elem in file:
            if 'year' in elem:
                elem = elem.strip()
                start, end = elem.find('{') + 1, elem.find('}')
                elem = elem[start:end]
                if elem.find('.') != -1:
                    elem = elem[-4:]
                list_year.append(int(elem))
                count += 1

    c = Counter(list_year)
    print(sorted(c.items(), key=lambda pair: pair[0], reverse=True))

