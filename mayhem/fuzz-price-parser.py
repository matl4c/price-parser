#! /usr/bin/python3

import atheris
import sys
import io

with atheris.instrument_imports():
    import price_parser

def TestOneInput(input_bytes):
    fdp = atheris.FuzzedDataProvider(input_bytes)
    data = fdp.ConsumeUnicode(sys.maxsize)
    price_parser.Price.fromstring(data)

def main():
    atheris.Setup(sys.argv, TestOneInput)
    atheris.Fuzz()


if __name__ == "__main__":
    main()
