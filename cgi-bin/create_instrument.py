import cgi
import sys
import os
import inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)
import BD as bd
from lxml import etree as ET
msg = ''
form = cgi.FieldStorage()
instr = form.getfirst("instrum")
class_id = form.getfirst("class_id")
if (class_id is not None) and (instr is not None):
    bd.addInstrum(class_id, instr)
    msg = '''
            <br>
            <div class="card">
                <div class="card-body">
                    Класс добавлен
                </div>
            </div>
        '''

instrum_xml = form.getfirst("xml_file")

if instrum_xml is not None:
    root = ET.fromstring(instrum_xml.decode("utf-8"))
    success_cnt = 0
    for child in root:
        instrument = {}
        for a_ch in child:
            if a_ch.tag == 'name_instrum':
                instrument['name_instrum'] = a_ch.text
            if a_ch.tag == 'name_class':
                instrument['name_class'] = a_ch.text
        if ('name_instrum' in instrument) and ('name_class' in instrument):
            bd.addInstrum(bd.getIndexClass(instrument['name_class']), instrument['name_instrum'])
            success_cnt += 1

    msg = f'''
        <br>
        <div class="card">
            <div class="card-body">
                Успешно загружено {success_cnt} инструментов
            </div>
        </div>
    '''


classes = bd.getAllClass()
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
            <h1>Добавление инструмента</h1>
            <a class="h3 link-primary" href="/">На главную</a>
            <div class="ps-4 pe-4">
                <form method="GET">
                <label class="form-label" for="class_id">Класс</label>
                    <select class="form-select" aria-label="Default select example" name="class_id" required>
                        {class_options}
                    </select>
                    <br>
                    <label class="form-label" for="instrum">Инструмент</label>
                    <input class="form-control" type="text" name="instrum" required>
                    <br>
                    <input type="submit" class="btn btn-primary">
                </form>
                {msg}
            </div>
            
            <h1>Загрузить из XML</h1>
             <div class="ps-4 pe-4">
                <form method="post" enctype="multipart/form-data">
                    <label class="form-label" for="xml_file">XML Файл</label>
                    <input class="form-control" name="xml_file" type="file" accept=".xml">
                    <br>
                    <input type="submit" class="btn btn-primary">
                </form>
             </div>
        </body>
    </html>
'''
class_options=''
for cl in classes:
    class_options += f'<option value="{cl[0]}">{cl[1]}</option>'

print("Content-Type: text/html\n")
print(template.format(msg=msg, class_options=class_options))

