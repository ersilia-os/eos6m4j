FROM bentoml/model-server:0.11.0-py37
MAINTAINER ersilia

RUN pip install tmap==1.2.1
RUN pip install rdkit==2023.3.2
RUN wget https://raw.githubusercontent.com/ersilia-os/eos6m4j/main/model/framework/code/bidd-molmap/requirements.txt
RUN pip install -r requirements.txt
RUN conda install -c conda-forge xorg-libxrender xorg-libxtst

WORKDIR /repo
COPY . /repo
