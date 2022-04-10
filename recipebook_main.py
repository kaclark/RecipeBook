class recipe:
    
    def __init__(self, name=None, equipment=[], ingredients=[], steps=[]):
        self.name = name
        self.equipment = equipment
        self.ingredients = ingredients
        self.steps = steps

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

    def load_from_file(self, rec_name):
        with open("rec/" + rec_name + ".rec", "r") as rec_in:
            raw_rec = [l.split('\n')[0] for l in rec_in.readlines()]
        #mark the zones for recording name, equipment, ingredients, and steps
        n_l = -1; e_l = -1; i_l = -1; s_l = -1
        for l_n, line in enumerate(raw_rec):
            if "&N" in line:
                n_l = l_n
            if "&E" in line:
                e_l = l_n
            if "&I" in line:
                i_l = l_n
            if "&S" in line:
                s_l = l_n
        self.name = raw_rec[n_l + 1]
        for x_e in range(e_l + 1, i_l):
            self.equipment.append(raw_rec[x_e])
        for x_i in range(i_l + 1, s_l):
            self.ingredients.append(raw_rec[x_i])
        for x_s in range(s_l + 1, len(raw_rec)):
            self.steps.append(raw_rec[x_s])
        self.summary()

"""
pan_fry_chicken = recipe(
    "pan fried chicken", 
    ["pan", "stove", "stirring utensil"],
    ["1lb Chicken", "Salt", "Pepper", "Crushed Red Pepper", "Peanut Oil", "Diced Onions"],
    [
        "Pour 3Tbs of Peanut oil into Pan",
        "Turn stove onto medium heat",
        "Add diced onions to Pan",
        "Salt Onions",
        "Cut chicken up into small chunks",
        "Add Chicken to Pan",
        "Season Chicken with Salt, Pepper, and Crushed Red Pepper",
        "Cook for 10-15min. Check temp of a chicken chunk to ensure that 165F has been exceeded"
    ]
    )

pan_fry_chicken.summary()
"""
pan_fried_chicken = recipe()
pan_fried_chicken.load_from_file("pan_fried_chicken")
