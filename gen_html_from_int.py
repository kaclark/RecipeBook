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

    def load_from_file(self, int_name):
        #recipies should all be stored in int dir
        with open("int/" + int_name + ".int", "r") as int_in:
            #list comp: remove newline character from each line
            raw_int = [l.split('\n')[0] for l in int_in.readlines()]
        #mark the zones for recording name, equipment, ingredients, and steps
        n_l = -1 
        e_l = -1 
        i_l = -1 
        s_l = -1
        for l_n, line in enumerate(raw_int):
            if "&N" in line:
                n_l = l_n
            if "&E" in line:
                e_l = l_n
            if "&I" in line:
                i_l = l_n
            if "&S" in line:
                s_l = l_n
        #name is on row after name tag
        self.name = raw_int[n_l + 1]
        #rows after equipment tag and up to ingredients tag are equipment entries
        for x_e in range(e_l + 1, i_l):
            self.equipment.append(raw_int[x_e])
        #rows after ingredients tag up to the steps tag are ingredient entries
        for x_i in range(i_l + 1, s_l):
            self.ingredients.append(raw_int[x_i])
        #all rows after steps tag are step entries
        for x_s in range(s_l + 1, len(raw_int)):
            self.steps.append(raw_int[x_s])
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
            if "*" in ing:
                print("TODO: Pages for elements(.elt); link from ing listings")
            html_stream += self.to_p(ing)
        html_stream += self.to_h1("Instructions")
        for ind, step in enumerate(self.steps):
            html_stream += self.to_p(step, stepb=True, stepn=str(ind + 1))
        return html_stream


def get_ints(file_extension=False):
    ints = []
    for x_path in Path("./int/").glob("*.int"):
        if file_extension:
            ints.append(str(x_path).split("/")[1])
        else:
            ints.append(str(x_path).split("/")[1].split(".int")[0])
    return ints


def gen_head(title, main=False): 
    if main:
        return f'''<html><head>
        <meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1">
        <title>{title}</title>
        <link href="https://fonts.googleapis.com/css?family=Roboto" rel="stylesheet">
        <link rel="stylesheet" type="text/css" href="./include/main.css"/>
        </head>'''
    else:
        return f'''<html><head>
        <meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1">
        <title>{title}</title>
        <link href="https://fonts.googleapis.com/css?family=Roboto" rel="stylesheet">
        <link rel="stylesheet" type="text/css" href="../include/main.css"/>
        </head>'''

def gen_intfetch_head(title, intslist):
        return f'''<html><head>
        <meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1">
        <title>{title}</title>
        <link href="https://fonts.googleapis.com/css?family=Roboto" rel="stylesheet">
        <link rel="stylesheet" type="text/css" href="./include/main.css"/>
        </head>'''

def gen_intsubmit_head(title):
        return f'''<html><head>
        <meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1">
        <title>{title}</title>
        <link href="https://fonts.googleapis.com/css?family=Roboto" rel="stylesheet">
        <link rel="stylesheet" type="text/css" href="./include/main.css"/>
        </head>'''

def gen_main_header(title):
    return f'''
    <body>
    <div class="content">
        <h1>{title}</h1>
    </div>
    <div class="content" id="content">
    '''
def gen_header(title, home_img=False, redirect="../index.html"):
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
        [Return to Integrations Hub]
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

def javascript_inject():
    with open("./include/javascript_inject.js", "r") as js_in:
        injection = [l.split("\n")[0] for l in js_in.readlines()]
    injection = "\n".join(injection)
    return f'''
    {injection}
    '''

def test_button():
    return f'''
    <div class="outer-wrap">
      <h1 id="title"></h1>
      <div class="button-container">
        <a id="btn" class="btn btn-1">
          <svg>
            <rect x="0" y="0" fill="none" width="100%" height="100%"/>
          </svg>
          Create New Account
        </a>
      </div>
    </div>

    <div class="outer-wrap">
      <h1 id="title"></h1>
      <div class="button-container">
        <a id="btn2" class="btn btn-1">
          <svg>
            <rect x="0" y="0" fill="none" width="100%" height="100%"/>
          </svg>
          Log In
        </a>
      </div>
    </div>

    <div class="outer-wrap">
      <h1 id="title"></h1>
      <div class="button-container">
        <a id="btn3" class="btn btn-1">
          <svg>
            <rect x="0" y="0" fill="none" width="100%" height="100%"/>
          </svg>
          Push Data
        </a>
      </div>
    </div>

    <div class="outer-wrap">
    <p id="post"></p>
    <div class="button-container">
        <a id="btn4" class="btn btn-1">
          <svg>
            <rect x="0" y="0" fill="none" width="100%" height="100%"/>
          </svg>
          [Post]
        </a>
      </div>
    </div>
            
    '''

def test_login():
    return f'''
    <div class="container">
        <form action="" id="loginForm">
            <h1>Login</h1>
            <input type="text" id="username" class="form-control" placeholder="Enter your Username...">
            <input type="password" id="password" class="form-control" placeholder="Enter your Password...">
            <button type="submit">Submit</button>
            <p id="load_bar"></p>
        </form>
    </div>

    <div class="outer-wrap">
      <p id="db_item1"></p>
      <p id="db_item2"></p>
      <div class="button-container">
        <button type="submit", id="get_user_data">Get User Data</button>
      </div>
    </div>
    '''

def f_login():
    return f'''
    <div class="container">
        <form action="" id="loginForm">
            <h1>Login</h1>
            <input type="text" id="username" class="form-control" placeholder="Enter your Username...">
            <input type="password" id="password" class="form-control" placeholder="Enter your Password...">
            <button type="submit">Submit</button>
            <p id="load_bar_1"></p>
        </form>
    </div>
    '''

def test_int_capture():
    return f'''
    <div class="container">
        <form action="" id="int_form">
            <h1>Integration</h1>
            <input type="text" id="int_name" class="form-control" placeholder="Enter your Username...">
            <button type="submit">Submit</button>
            <p id="load_bar_2"></p>
        </form>
    </div>
    '''

def strip_underscores(string):
    return " ".join([f.capitalize() for f in string.split("_")])

def construct_main_index(title, img_src, ints):

    def list_recipe(xint):
        return "<a href='./routes/" + xint + ".html'><p>" + strip_underscores(xint) + "</p></a>\n\t"

    index_output = ""
    index_output += gen_head(title, main=True) 
    #img_src should be provided here, but
    #default vals are being used fior now
    #TODO Refactor
    index_output += javascript_inject()
    index_output += gen_main_header(title)
    #index_output += test_login()
    index_output += f_login()
    index_output += test_int_capture()
    for xint in ints:
        index_output += list_recipe(xint)
    index_output += gen_tail()
    
    with open("./index.html", "w") as html_out:
        html_out.write(index_output)

def construct_int_index(xxint):

    index_output = ""
    index_output += gen_head(xxint) 
    index_output += gen_header(xxint, home_img=True)
    #TODO: FIll with rec info
    #load rec class from .rec file here
    xint = Recipe()
    xint.clear()
    xint.load_from_file(xxint)
    #print(rec)
    #xrec.summary()
    
    index_output += xint.to_html()
    index_output += gen_tail() 
    with open("./routes/" + xxint + ".html", "w") as html_out:
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

def construct_intsubmit(all_recs):

    #all_recs_mod = ["./rec/" + rec + ".rec" for rec in all_recs]
    intsubmit = ""
    intsubmit += gen_intsubmit_head("Submit Recipe")
    intsubmit += "<p id='termout'>Nothing to See<p>"
    intsubmit += gen_tail()

    with open("./intsubmit.html", "w") as out_html:
        out_html.write(intsubmit)

#with open("/mnt/test.txt", "w") as test_out:
#test_out.write("testingtesting")

def refresh():
    int_names = get_ints()
    construct_main_index("Integrations Hub", "./include/frying_pan.png", int_names) 
    for xint in int_names:
        construct_int_index(xint)
    #construct_fridgestore()

refresh()
