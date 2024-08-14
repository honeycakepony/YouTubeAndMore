import PyPDF2
from fontTools.misc.cython import returns

if __name__ == '__main__':
    with open('state_union.pdf', 'rb') as pdf:
        reader = PyPDF2.PdfReader(pdf, strict=False)
        pdf_text = list()

        for page in reader.pages:
            content = page.extract_text()
            pdf_text.append(content)

    print(len(pdf_text), pdf_text[19].count('PIP'))

    for page in pdf_text:
        print(page)
        print()
        print()