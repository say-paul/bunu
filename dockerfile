FROM tiangolo/uwsgi-nginx-flask:python3.8
# RUN git config --global http.sslVerify false
# RUN git clone -b flask_prime  https://github.com/say-paul/bunu.git testing
# # RUN cd bunu/app/
# RUN cp -r testing/app/ /app
# RUN cd test
# RUN python /test/app
COPY ./testing/app /app