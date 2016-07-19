FROM ubuntu:12.04

RUN apt-get update
RUN apt-get install -y python-pip

RUN mkdir /code/
WORKDIR /code/
COPY apt-packages.txt apt-packages.txt

RUN xargs -a apt-packages.txt apt-get install -qq --fix-missing

RUN add-apt-repository -y ppa:chris-lea/node.js  \
	&& apt-get update -qq  \
	&& apt-get install -qq nodejs

RUN gem install sass

RUN mkdir requirements/

# COPY requirements/wheels.txt requirements/wheels.txt
# RUN pip install -r requirements/wheels.txt
RUN pip install lxml==3.4.4
RUN pip install numpy==1.6.2
RUN pip install scipy==0.14.0
RUN pip install scikit-learn==0.12.1

COPY requirements/base.txt requirements/base.txt
RUN pip install -r requirements/base.txt

RUN python -m nltk.downloader stopwords maxent_treebank_pos_tagger wordnet

RUN apt-get install libjpeg-dev -y
COPY requirements/test-acceptance.txt requirements/test-acceptance.txt
RUN pip install -r requirements/test-acceptance.txt

COPY requirements/test.txt requirements/test.txt
RUN pip install -r requirements/test.txt

COPY requirements/dev.txt requirements/dev.txt
RUN pip install -r requirements/dev.txt

RUN pip install Django==1.8

ADD . /code/

RUN pip install -q -e .


