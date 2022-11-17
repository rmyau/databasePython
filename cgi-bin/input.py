import cgi
form = cgi.FieldStorage()
text1=form.getfirst("instrument", "не задано")
text2=form.getfirst("class", "не задано")
print(text1,text2)
print('''<!DOCTYPE HTML>
    <html lang="en-US">>
    <head>
     <meta charset = "cp1251">
     <title>Обработка </title>
     </head>
     <body>
     <h1>Добро пожаловать!</h1>
     </body>
     </html>''')