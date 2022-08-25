FROM bentoml/model-server:0.11.0-py36
MAINTAINER ersilia

RUN conda install -c tmap tmap -y
RUN conda install -c conda-forge rdkit=2020.03 -y
RUN python -m pip install -r requirements.txt
RUN python -m pip install h5py==2.10.0

WORKDIR /repo
COPY . /repo
