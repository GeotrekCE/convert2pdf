# convert2pdf

## Description

It is a server with a route that allows you to convert **Html** and **Libre Office** documents to **Pdf**.

Supported formats:
* *odt*
* *ott*
* *oth*
* *odm*
* *otm*
* *odg*
* *otg*
* *odp*
* *otp*
* *ods*
* *ots*
* *odc*
* *odf*
* *odi*
* *docx*
* *doc*
* *html*

## How it works

### How to run the server on localhost

You will only need to start a container:

```
docker run -itd -p "127.0.0.1:8000:8000" geotrekce/convert2pdf
```

### How to make a request to the server

This server has only one route. To convert a valid document (**Python** exemple):

```
>>> from requests import post
>>> files = {'file': ('name.ext', open(path, 'rb'), 'mimetype')}
>>> response = post('http://127.0.0.1:8000/', files=files)
```
