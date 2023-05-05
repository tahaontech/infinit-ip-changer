FROM ubuntu:22.04
RUN apt-get update
# install python
RUN apt install python3 python3-pip -y
RUN pip3 install Flask waitress
# install tor and config tor
RUN apt-get install tor -y
RUN /etc/init.d/tor restart
RUN tor --hash-password my_password
COPY torrc .
RUN cat torrc > /etc/tor/torrc
RUN /etc/init.d/tor restart
RUN apt-get install python3-stem -y
# install and config forward proxy
RUN apt-get install privoxy -y
COPY config .
RUN cat config > /etc/privoxy/config
RUN /etc/init.d/privoxy restart
# copy app
COPY app.py .
# expose proxy port
EXPOSE 8118
# expose api ports
EXPOSE 5000
# run the app
CMD [ "python3", "app.py"]