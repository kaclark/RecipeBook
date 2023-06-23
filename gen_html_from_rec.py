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

def construct_index():
    html_top = ""
    with open("./include/boiler_html_elements/html_top.txt", "r") as h_top:
        lines = h_top.readlines()
        for line in lines:
            html_top += line

    def list_recipe(rec):
        return "<a href='./routes/" + rec + ".html'><p>" + rec + "</p></a>\n\t"

    html_bottom = ""
    with open("./include/boiler_html_elements/html_bottom.txt", "r") as h_bottom:
        blines = h_bottom.readlines()
        for bline in blines:
            html_bottom += bline

    index_output = ""
    index_output += html_top 
    for rec in get_recs():
        index_output += list_recipe(rec)
    index_output += html_bottom
    
    with open("./index.html", "w") as html_out:
        html_out.write(index_output)

construct_index()    
