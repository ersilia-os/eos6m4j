FROM bentoml/model-server:0.11.0-py37
MAINTAINER ersilia

RUN conda install -c tmap tmap -y
RUN python -m pip install rdkit
RUN wget https://raw.githubusercontent.com/ersilia-os/eos6m4j/main/model/framework/code/bidd-molmap/requirements.txt
RUN python -m pip install -r requirements.txt
RUN python -m pip install h5py==2.10.0

WORKDIR /repo
COPY . /repo
