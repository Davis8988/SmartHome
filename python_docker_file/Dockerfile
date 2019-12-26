# you need to mount the /smart-home to the folder that have all smart-home relevant files
FROM python:3
RUN cat /etc/*release
RUN apt-get update
RUN apt-get install -y mpg321
RUN pip3 install paho-mqtt
RUN pip3 install python-telegram-bot
RUN pip3 install python-miio
RUN pip3 install gtts


CMD [ "python", "/smart-home/main-script.py" ]