from sys import stderr

from panflute import *

headers = set()


def action(elem, doc):
    if type(elem) == Header:
        temp = stringify(elem)
        if temp in headers:
            stderr.write("Repeated headers!")
        else:
            headers.add(temp)

        if elem.level >= 3:
            return elem.walk(upper)

    if type(elem) == Str:
        if elem.text == "BOLD":
            bold_text = [Str(elem.text)]
            return Strong(*bold_text)


def upper(elem, doc):
    if type(elem) == Str:
        elem.text = elem.text.upper()


if __name__ == "__main__":
    run_filter(action)
