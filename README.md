# RecipeBook

=====================================<br/>
Web Experience<br/>
=====================================<br/>
https://kaclark.github.io/RecipeBook/<br/>
<br />

=====================================<br/>
Introduction<br/>
=====================================<br/>
All html in this repository was generated by a python script written from an android phone running a termux install from f-droid. New recipes are added easily and the website is rebuilt with that script. The entire user experience should be avaiable from just a browser. From my phone to the web, I hope to automate much of my RecipeBook...<br />
<br/>

=====================================<br/>
Project State Milestone Record<br /> 
=====================================<br/>
.rec file convention<br/>
python recipe class<br/>
html generation for index<br/>
github.io site launch<br/>
html generation for arbitrary .rec contents<br/>
<br/>

=====================================<br/>
Vision for Next Steps<br /> 
=====================================<br/>
The home index should be a portfolio of classic dishes I can make with ease and expertise. The Fridge Icon should take one to a page mapped to what's prepped to be fried or baked at will in my kitchen. Ideas should germinate from the index and encounters should dawn from the fridgepage.<br/>

Furthermore, .rec files were imagined to be static. I'm now experimenting with .prep files and recording their relations with other elements. I'm considering having .elt files for purchased items with UPC Bardcode data appended to them.Maybe different garlic powders go into the same .rec. The .elt system will be sensitive to this granularity<br/>

=====================================<br/>
Desired Features/TODO:<br/>
=====================================<br/>
--Functionality<br/>
[ ] Element-relation framework<br/>
[ ] Fridge -> Prep<br/>
[ ] Record Recipe Activation(Card Format)<br/>
Navigation and Organization<br/>
[x] Add more recipes<br/>
[x] Frying Pan img src in routes leads back to home<br/>
[ ] Navigation Bar<br/>
[ ] Collections/Genres of recipies<br/>
[ ] Regex/keyword search<br/>
[ ] list possible recipes given constraints(for fridgestore)<br/>
[ ] Track Recipes(Button for Completion)<br/>
[ ] Main Page with recents, favorites, and reccomendations/predictions<br/>
Fridgestore<br />
[ ] Show recipies avialable for each entry<br/>
[x] Todoist integration (Temporary Database)<br/>
[x] UPC Barcode scanning<br />
--User Experience<br/>
[x] mobile friendly html page generation<br/>
[x] simple html generation for index<br />
[x] github.io page <br/>
[x] .rec to html for links in main index <br/>
[ ] Flash Recipes<br/>
--Aesthetic<br/>
[ ] Flexbox CSS for main index
[ ] 'Card' Component Style
[ ] Add Images to recurring elements(pot, pan, salt and pepper)<br/>
<br/>

=====================================<br/>
Next Milestones:<br/>
=====================================<br/>
Reactpy Refactor<br/>
Text-Capture for Fridgestore<br/>
Grocery Planner<br/>
Quantity Checker<br/>
Pricebot<br/>
Cooking Calender<br/>
Cooking Queue Generation<br/>
<br/>

=====================================<br/>
Recipe file format<br/>
=====================================<br/>
&N<br/>
Name of Recipe<br/>
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
