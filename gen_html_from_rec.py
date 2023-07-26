#build html files from strings
#quasi component design strategy
from pathlib import Path
import random
from todoist_api_python.api import TodoistAPI
import requests
from PIL import Image
import os


def get_tasks(p_id, xapi):
	tasks=xapi.get_tasks()
	tasks_out = []
	for task in tasks:
		imgname = task.content
		if int(task.project_id) == p_id and task.is_completed == False:
			tasks_out.append((task.content, get_attachment_from_comment(get_comments(task.id), imgname)))
	return tasks_out

def get_comments(t_id):
	try:
		comments=api.get_comments(task_id=t_id)
		return comments[0]
	except Exception as error:
		pass

def get_attachment_from_comment(comment, imgname):
	try:
		iurl = comment.attachment.image
		fattach = iurl.split(".")[-1]
		ifp = "include/" + imgname + "." + fattach
		if not os.path.isfile(ifp):
			with open(ifp, "wb") as img_out:
				img_out.write(requests.get(iurl).content)
		return ifp

	except Exception as error:
		print(error)
		pass

def gen_fridgestore_head(title): 
    return f'''<html><head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    <title>{title}</title>
    <link href="https://fonts.googleapis.com/css?family=Roboto" rel="stylesheet">
    <link rel="stylesheet" type="text/css" href="../include/fridge.css"/>
    </head>
    <body>
    <div class="content" id="content"><p>{title}</p></div>'''


def gen_fridgestore_p(text, img_src):
    img_src_mod = "../" + img_src
    return f'''<div class="content" id="content"><p id="entry">{text}</p><img class="teaser-img" src={img_src_mod}></div>
    '''

#recipe class that will be handling all the information for a single recipie
class Recipe:

    #There is a default, empty form that this can be initialized into for loading recipe from file
    #This is how this class is expected to be used for the most part
    def __init__(self, name=None, equipment=[], ingredients=[], steps=[]):
        self.name = name
        self.equipment = equipment
        self.ingredients = ingredients
        self.steps = steps

    #The summary prints everything that makes up the recipie
    def summary(self):
        print(self.name.upper())
        print("Equipment")
        for eq in self.equipment:
            print(" ", eq)
        print("Ingredients")
        for ing in self.ingredients:
            print(" ", ing)
        print("Instructions")
        for ind, step in enumerate(self.steps):
            print(" ", str(ind + 1) + ")", step)
    
    def clear(self):
        self.name = None
        self.equipment = []
        self.ingredients  = []
        self.steps = []

    def load_from_file(self, rec_name):
        #recipies should all be stored in rec dir
        with open("rec/" + rec_name + ".rec", "r") as rec_in:
            #list comp: remove newline character from each line
            raw_rec = [l.split('\n')[0] for l in rec_in.readlines()]
        #mark the zones for recording name, equipment, ingredients, and steps
        n_l = -1 
        e_l = -1 
        i_l = -1 
        s_l = -1
        for l_n, line in enumerate(raw_rec):
            if "&N" in line:
                n_l = l_n
            if "&E" in line:
                e_l = l_n
            if "&I" in line:
                i_l = l_n
            if "&S" in line:
                s_l = l_n
        #name is on row after name tag
        self.name = raw_rec[n_l + 1]
        #rows after equipment tag and up to ingredients tag are equipment entries
        for x_e in range(e_l + 1, i_l):
            self.equipment.append(raw_rec[x_e])
        #rows after ingredients tag up to the steps tag are ingredient entries
        for x_i in range(i_l + 1, s_l):
            self.ingredients.append(raw_rec[x_i])
        #all rows after steps tag are step entries
        for x_s in range(s_l + 1, len(raw_rec)):
            self.steps.append(raw_rec[x_s])
        #After loading the file in, the present desired behavior is to just give a summary
        self.summary()

    def to_h1(self, content):
        return "<h1>" + content + "</h1><br/>"

    def to_p(self, content, stepb=False, stepn=0):
        if not stepb:
            return "<p>" + content + "</p>"
        if stepb:
            return "<p>" + str(stepn) + ".) " + content + "</p>"

    def to_html(self):
        html_stream = ""
        html_stream += self.to_h1("Equipment")
        for eq in self.equipment:
            html_stream += self.to_p(eq)
        html_stream += self.to_h1("Ingredients")
        for ing in self.ingredients:
            html_stream += self.to_p(ing)
        html_stream += self.to_h1("Instructions")
        for ind, step in enumerate(self.steps):
            html_stream += self.to_p(step, stepb=True, stepn=str(ind + 1))
        return html_stream


def get_recs(file_extension=False):
    recs = []
    for x_path in Path("./rec/").glob("*.rec"):
        if file_extension:
            recs.append(str(x_path).split("/")[1])
        else:
            recs.append(str(x_path).split("/")[1].split(".rec")[0])
    return recs


def gen_head(title, main=False): 
    if main:
        return f'''<html><head>
        <meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1">
        <title>{title}</title>
        <link href="https://fonts.googleapis.com/css?family=Roboto" rel="stylesheet">
        <link rel="stylesheet" type="text/css" href="./include/main.css"/>
        >
        
        <link rel="stylesheet" href="https://pyscript.net/latest/pyscript.css" />
        <script defer src="https://pyscript.net/latest/pyscript.js"></script>
        </head>'''
    else:
        return f'''<html><head>
        <meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1">
        <title>{title}</title>
        <link href="https://fonts.googleapis.com/css?family=Roboto" rel="stylesheet">
        <link rel="stylesheet" type="text/css" href="../include/main.css"/>
        </head>'''

def gen_main_header(title, subtitle, img_src='./include/fridge.jpeg', redirect="./routes/fridgestore_collect.html"):
    return f'''
    <body>
    <div class="content">
        <h1>{title}</h1>
    <div class='teaser-box'>
    <a href="{redirect}">
    <img class='teaser-img' src='{img_src}'></img>
    </a>
    </div>
    </div>
    <div class="content" id="content">
    <h1 id="xsub">{subtitle}</h1>
    <py-script>display("Cook it up", target="xsub")</py-script>
    '''
def gen_header(title, home_img=False, home_img_src="../include/frying_pan.png", redirect="../index.html"):
    mtitle = strip_underscores(title)
    if not home_img:
        return f'''
        <body>
        <div class="content">
            <h1>{mtitle}</h1>
        </div>
        <div class="content" id="content">
        '''
    else:
        return f'''
        <body>
        <div class="content">
            <h1>{mtitle}</h1>
        <div class='teaser-box'>
        <a href="{redirect}">
        <img class='teaser-img' src='{home_img_src}'></img>
        </a>
        </div>
        </div>
        <div class="content" id="content">

        '''


def gen_tail():
    return f'''
    </div>
    </body>
    </html>
    '''

def strip_underscores(string):
    return " ".join([f.capitalize() for f in string.split("_")])

def construct_main_index(title, subtitle, img_src, recs):

    def list_recipe(rec):
        return "<a href='./routes/" + rec + ".html'><p>" + strip_underscores(rec) + "</p></a>\n\t"

    index_output = ""
    index_output += gen_head(title, main=True) 
    #img_src should be provided here, but
    #default vals are being used fior now
    #TODO Refactor
    index_output += gen_main_header(title, subtitle)
    for rec in recs:
        index_output += list_recipe(rec)
    index_output += gen_tail()
    
    with open("./index.html", "w") as html_out:
        html_out.write(index_output)

def construct_rec_index(rec):

    index_output = ""
    index_output += gen_head(rec) 
    index_output += gen_header(rec, home_img=True)
    #TODO: FIll with rec info
    #load rec class from .rec file here
    xrec = Recipe()
    xrec.clear()
    xrec.load_from_file(rec)
    #print(rec)
    #xrec.summary()
    
    index_output += xrec.to_html()
    index_output += gen_tail() 
    with open("./routes/" + rec + ".html", "w") as html_out:
        html_out.write(index_output)

def construct_fridgestore():
    ###Fridgestore
    with open("api.token", "r") as key_in:
        api = TodoistAPI(str(key_in.readlines()[0].split("\n")[0]))
    project_id = 2294556610
    task_data = get_tasks(project_id, xapi)
    html_stream = ""
    html_stream += gen_fridgestore_head("peek into our fluffy fridge!")
    for t_data in task_data:
        html_stream += gen_fridgestore_p(t_data[0], t_data[1])
    html_stream += gen_tail()
    with open("./routes/fridgestore_collect.html", "w") as out_html:
        out_html.write(html_stream)

rec_names = get_recs()
construct_main_index("Recipebook", "All Recipes", "./include/frying_pan.png", rec_names)    
for rec in rec_names:
    construct_rec_index(rec)
#construct_fridgestore()
