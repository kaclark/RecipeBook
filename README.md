# RecipeBook

https://kaclark.github.io/RecipeBook/<br/>

Desired Features/TODO:<br/>
--Functionality<br/>
[ ] Add more recipes<br/>
[ ] Collections/Genres of recipies<br/>
[ ] Regex/keyword search<br/>
[ ] list possible recipes given constraints(for fridgestore)<br/>
[ ] Barcode scanner(from browser?)<br />
[x] UPC Barcode scanning<br />
[ ] Fridgestore<br />
--User Experience<br/>
[x] mobile friendly html page generation<br/>
[x] simple html generation for index<br />
[x] github.io page <br/>
[x] .rec to html for links in main index <br/>
--Aesthetic<br/>
[ ] Add Images to recurring elements(pot, pan, salt and pepper)<br/>

Goal: Simple collection of recipie file formats that can be processed into minimal html files that are mobile-friendly. Individual recipies can be sent as links branching from github.io page for this project. Fridgestore, Recipebook integration with a recipe search function(webscraping on-masse)<br/><br/>
Current State of Project: html-generation of page from .rec file format in works! Github.io page launched! Barcode scanning from browser in works!<br/><br/>
Far Future: User accounts that allow for the forking of recipies, comments, ratings of satiety, flavor, ease of production, price? sharing platform?<br/><br/>

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

