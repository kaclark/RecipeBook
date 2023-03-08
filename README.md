# RecipeBook
Possible App Name: Tummy-ome<br/>
Goal: Simple collection of recipie file formats that can be processed into minimal html files that are mobile-friendly. Individual recipies can be sent as links branching from github.io page for this project.<br/>
Current State of Project: Minimal Command Line functionality. Presently just a repository of recipies. Django experimentation upcoming. html-generation may be done by user then html files are simply linked to bare-bones html?<br/>

Recipes are saved in files<br/>
Recipes are loaded from that<br/>

random recipe can be loaded by typing in:<br/>
python recipebook.py -r 1<br/>
OR<br/>
python recipebook.py -r True<br/>

a specific recipe can be loaded with:<br/>
python recipebook.py -l RECIPE_NAME<br/>

Recipe file format<br/>
&N<br/>
Name of Dish<br/>
&E<br/>
Equipment #1<br/>
...<br/>
Equipment #N<br/>
&I<br/>
Ingredient #1<br/>
...<br/>
Ingredient #M<br/>
&S<br/>
Step #1<br/>
...<br/>
Step #K<br/>

other recipies can be asserted prior to a .rec by adding the following as a header before &N <br/>
&P<br/>
assert first_rec_name.rec = first_prepped_ingredient_name<br/>
...<br/>
assert last_rec_name.rec = last_prepped_ingredient_name<br/>

Desired Features/TODO:<br/>
[ ] Add more recipes<br/>
[ ] Collections/Genres of recipies<br/>
[ ] Regex/keyword search<br/>
[ ] list possible recipes given constraints<br/>
[ ] Look into mobile friendly html page generation for each rec<br/>
[ ] > https://docs.djangoproject.com/en/4.1/intro/tutorial02/ <br/>
[ ] Add Images to link with recurring elements<br/>
