#build html files from strings
#quasi component design strategy
from pathlib import Path

def get_recs(file_extension=False):
    recs = []
    for x_path in Path("./rec/").glob("*.rec"):
        if file_extension:
            recs.append(str(x_path).split("/")[1])
        else:
            recs.append(str(x_path).split("/")[1].split(".rec")[0])
    return recs

def construct_index(title, subtitle, img_src):

    def list_recipe(rec):
        return "<a href='./routes/" + rec + ".html'><p>" + rec + "</p></a>\n\t"

    index_output = ""
    index_output += gen_head(title) 
    index_output += gen_header(title, subtitle, img_src)
    for rec in get_recs():
        index_output += list_recipe(rec)
    index_output += gen_tail()
    
    with open("./index.html", "w") as html_out:
        html_out.write(index_output)

def gen_head(title): 
    return f'''<html><head>
    <meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1">
    <title>{title}</title>
    <link href="https://fonts.googleapis.com/css?family=Roboto" rel="stylesheet">
    <link rel="stylesheet" type="text/css" href="./include/main.css"/>
    </head>'''

def gen_header(title, subtitle, img_src):
    return f'''
    <body>
    <div class="content">
        <h1>{title}</h1>
    <div class='teaser-box'>
    <img class='teaser-img' src='{img_src}'></img>
    </div>
    </div>
    <div class="content" id="content">
    <h1>{subtitle}</h1>
    '''

def gen_tail():
    return f'''
    </div>
    </body>
    </html>
    '''
construct_index("Recipebook", "All Recipes", "./include/frying_pan.png")    
