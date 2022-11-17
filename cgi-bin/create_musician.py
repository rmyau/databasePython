import cgi
import sys
import os
import inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)
import BD as bd

msg = ''
form = cgi.FieldStorage()
instr = form.getfirst("instrum")
music = form.getfirst("musician")
if (music is not None) and (instr is not None):
    bd.addMusician(instr, music)
    msg = '''
            <br>
            <div class="card">
                <div class="card-body">
                    Музыкант добавлен
                </div>
            </div>
        '''
instruments = bd.getAllInstrument()
template = '''
    <!DOCTYPE html>
    <html lang="en-US">
        <head>
            <meta charset="UTF-8">
            <!-- CSS only -->
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-Zenh87qX5JnK2Jl0vWa8Ck2rdkQ2Bzep5IDxbcnCeuOxjzrPF/et3URy9Bv1WTRi" crossorigin="anonymous">
            <!-- JavaScript Bundle with Popper -->
            <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-OERcA2EqjJCMA+/3y+gxIOqMEjwtxJY7qPCqsdltbNJuaOe923+mo//f6V8Qbsw3" crossorigin="anonymous"></script>
        </head>
        <body>
            <h1>Добавление музыканта</h1>
            <a class="h3 link-primary" href="/">На главную</a>
            <div class="ps-4 pe-4">
                <form method="GET">
                <label class="form-label" for="instrum">Название инструмента</label>
                    <select class="form-select" aria-label="Default select example" name="instrum" required>
                        {instrum_options}
                    </select>
                    <br>
                    <label class="form-label" for="musician">Имя музыканта</label>
                    <input class="form-control" type="text" name="musician" required>
                    <br>
                    <input type="submit" class="btn btn-primary">
                </form>
                {msg}
            </div>
        </body>
    </html>
'''
instrum_options=''
for instrument in instruments:
    instrum_options += f'<option value="{instrument[0]}">{instrument[1]}</option>'

print("Content-Type: text/html\n")
print(template.format(msg=msg, instrum_options = instrum_options))
