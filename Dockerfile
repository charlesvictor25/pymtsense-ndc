FROM python:3.7

RUN mkdir /app
RUN mkdir /app/templates
WORKDIR /app
ADD . /app/
ADD main.py /app/
ADD /templates/product.html /app/templates/

RUN pip install -r requirements.txt

EXPOSE 5000
CMD ["python", "/app/main.py"]