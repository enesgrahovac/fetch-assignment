FROM jupyter/datascience-notebook

RUN pip install \
    tensorflow \ 
    numpy \
    pandas \
    matplotlib \
    jupyter \
    scikit-learn \
    keras-tuner \
    ipyfilechooser

ADD ./ml-take-home-assignment $HOME/ml-take-home-assignment

CMD ["jupyter-notebook", "--allow-root"]