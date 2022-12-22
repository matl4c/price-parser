FROM fuzzers/atheris:2.0.7-python3.9

RUN apt-get update

ADD . /src
WORKDIR /src

RUN python3 -m pip install price-parser
RUN chmod +x /src/mayhem/fuzz-price-parser.py

CMD ["/src/mayhem/fuzz-price-parser.py"]
