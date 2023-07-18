FROM ubuntu:18.04
WORKDIR /app/webapp

RUN apt update -y
RUN apt install -y python3-pip python3-dev build-essential
RUN apt install -y net-tools procps
RUN python3 -m pip install flask PyMySQL
RUN groupadd -g 999 user
RUN useradd -r -u 999 -g user user
USER user
ENTRYPOINT /app/entrypoint.sh && /bin/bash
CMD ["true"]
