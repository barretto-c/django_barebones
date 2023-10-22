from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <style>
            body {
                font-family: 'Arial', sans-serif;
                background-color: #f0f0f0;
                text-align: center;
                padding: 50px;
            }
            h1 {
                color: #3498db;
            }
        </style>
    </head>
    <body>
        <h1>Simple Django Website</h1>
        <p>Just saying hello</p>
        <a href=" admin/">Admin Site</a>
    </body>
    </html>
    """
    return HttpResponse(html_content)    
