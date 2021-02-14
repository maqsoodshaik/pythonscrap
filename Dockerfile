FROM python:3.8
RUN mkdir scrapping_email
WORKDIR /scrapping_email
COPY requirements.txt .
COPY scrapping_email.py .
RUN pip install -r requirements.txt

CMD ["python3","./scrapping_email.py"]
