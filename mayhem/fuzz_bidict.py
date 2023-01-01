#! /usr/bin/python3

import atheris
import sys

with atheris.instrument_imports():
    from bidict import bidict


@atheris.instrument_func
def test_input(input_bytes):
    fdp = atheris.FuzzedDataProvider(input_bytes)
    input_string = fdp.ConsumeUnicodeNoSurrogates(sys.maxsize)
    # input_str_w_surrogates = fdp.ConsumeUnicode(sys.maxsize)
    # input_int = fdp.ConsumeInt(sys.maxsize)
    bidict({input_string: input_string})
    # return input_bytes

def main():
    atheris.Setup(sys.argv, test_input)
    atheris.Fuzz()

if __name__ == "__main__":
    main()
