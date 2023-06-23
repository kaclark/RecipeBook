#build html files from strings
#quasi component design strategy

def construct_index(rec_pages):
    html_top = """
    <html>

    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1">
        <title>Recipebook</title>

        <link href="https://fonts.googleapis.com/css?family=Roboto" rel="stylesheet">
        <link rel="stylesheet" type="text/css" href="./include/main.css"/>

    </head>

    <body>
        <div class="content">
            <h1>Recipebook</h1>
        <div class='teaser-box'>
        <img class='teaser-img' src='./include/fyring_pan.png'></img>
        </div>
        <h2>All Recipies<h2>
        </div>
        <div class="content" id="content">
    """
    #TODO:print rec as one would in terminal for cli version
    def list_recipe(rec):
    return "<a href='./routes/" + rec + ".html'><p>" + rec + "</p></a>"

    html_bottom = """
       </div>

    </body>

    </html>
    """
    index_output = ""
    index_output += html_top 
    for rec in rec_pages:
        index_output += list_recipies(rec)
    index_output += html_bottom
    
print(html_top)
print(html_bottom)
