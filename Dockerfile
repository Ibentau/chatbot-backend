FROM python:3.7

WORKDIR /python-docker

COPY requirements.txt requirements.txt
RUN pip3 install -U pip setuptools wheel
RUN pip3 install spacy==2.3.8
RUN python3 -m spacy download en
RUN pip3 install pyyaml
RUN pip3 install chatterbot
RUN pip3 install chatterbot_corpus
RUN pip3 install -r requirements.txt

COPY . .

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
