# !/bin/bash
app="docker.test"
git clone -b flask_prime  https://github.com/say-paul/bunu.git testing
docker build -t ${app} . -f dockerfile
docker run -d -p 80:80 \
    --name=${app} ${app}
    # -v $PWD/app:/app ${app}
    