from request_app import GetMenuItem


class KeywordsMenuItem(GetMenuItem):

    def __init__(self):
        super(GetMenuItem, self).__init__()

        self.keywords = [{"All": []},
                         {"Acai": ["acai", "açaí", "berry", "bowl", "Brazilian", "fruit", "smoothie", "superfood"]},
                         {"Afghani": ["kebab", "naan", "pilaf", "spices", "lamb", "chickpeas", "yogurt", "tea"]},
                         {"African": ["yam", "plantain", "jollof", "fufu", "egusi", "suya", "akara", "pepper soup"]},
                         {"American": ["burger", "hot dog", "apple pie", "fried chicken", "BBQ ribs", "mac and cheese", "chili", "donut"]},
                         {"Arabic": ["hummus", "falafel", "shawarma", "tabbouleh", "baklava", "tagine", "kibbeh", "baba ghanoush"]},
                         {"Arabic sweets": ["qatayef", "baklava", "knafa", "ma'amoul", "basbousa", "halva", "awamat", "balah el sham"]},
                         {"Argentinian": ["asado", "empanadas", "mate", "milanesa", "chimichurri", "dulce de leche", "facturas", "mate cocido"]},
                         {"Asian": ["sushi", "ramen", "pho", "curry", "dim sum", "szechuan", "bao", "kimchi"]},
                         {"Bagel": ["bagel", "lox", "cream cheese", "smoked salmon", "red onion", "capers", "dill", "beets"]},
                         {"Bahraini": ["kebab", "machboos", "ghoozi", "thareed", "biriyani", "hummus", "halwa", "qahwa"]},
                         {"Baked potatoes": ["baked potato", "sour cream", "bacon bits", "chives", "cheddar cheese", "broccoli", "butter", "garlic"]},
                         {"Bakery": ["croissant", "pain au chocolat", "baguette", "macaron", "éclair", "tarte tatin", "quiche", "madeleines"]},
                         {"Beverages": ["coffee", "tea", "juice", "soda", "beer", "wine", "cocktail"]},
                         {"Biryani": ["rice", "spices", "chicken", "vegetables", "raita"]},
                         {"Bowls": ["grain", "vegetables", "protein", "sauce", "bowl"]},
                         {"Brazilian": ["feijoada", "moqueca", "coxinha", "brigadeiro", "caipirinha"]},
                         {"Breakfast": ["eggs", "bacon", "toast", "pancakes", "waffles", "coffee", "juice"]},
                         {"British": ["fish and chips", "shepherd's pie", "bangers and mash", "cream tea"]},
                         {"Bubble tea": ["tapioca", "milk tea", "fruit", "straw", "boba"]},
                         {"Burgers": ["beef", "cheese", "lettuce", "tomato", "bun", "fries"]},
                         {"Burrito": ["tortilla", "rice", "beans", "meat", "guacamole", "salsa"]},
                         {"Cafe": ["coffee", "tea", "pastry", "sandwich", "soup"]},
                         {"Cafeteria": ["school", "lunch", "tray", "mystery meat"]},
                         {"Cakes": ["chocolate", "vanilla", "frosting", "birthday", "wedding"]},
                         {"Calzone": ["pizza", "folded", "filling", "sauce"]},
                         {"Candy": ["chocolate", "gummy", "sour", "sweet", "jelly beans"]},
                         {"Charity": ["donation", "nonprofit", "volunteer", "fundraiser"]},
                         {"Chicken": ["fried", "roasted", "grilled", "sandwich", "nuggets"]},
                         {"Chinese": ["stir-fry", "noodles", "dumplings", "baozi", "hot pot", "tea"]},
                         {"Chocolate": ["dark", "milk", "white", "cocoa", "truffle"],},
                         {"Churros": ["doughnut", "cinnamon", "sugar", "dipping sauce"]},
                         {"Coffee":  ["latte", "cappuccino", "espresso", "cold brew", "mug"]},
                         {"Continental": ["European", "bread", "cheese", "meat", "wine"]},
                         {"Crepes": ["French", "thin", "filling", "sweet", "savory"]},
                         {"Curry": ["spices", "sauce", "rice", "naan", "chicken", "vegetables"]},
                         {"Desserts": ["cake", "pie", "ice cream", "cookies", "pudding", "fruit"]},
                         {"Dim sum": ["steamed", "dumplings", "shumai", "buns", "tea"]},
                         {"Doner": ["meat", "pita", "lettuce", "tomato", "tzatziki"]},
                         {"Donuts": ["donut", "doughnut", "glazed", "sprinkles", "baked goods", "pastry", "coffee"]},
                         {"Dumplings": ["dumpling", "potsticker", "gyoza", "dim sum", "soup", "noodles", "pork", "vegetables"]},
                         {"Egyptian": ["ful", "tahini", "koshari", "fava beans", "spices", "grilled meat", "flatbread", "tea"]},
                         {"Emirati": ["shawarma", "machboos", "salona", "thareed", "sambousek", "hummus", "balaleet", "chamomile tea"]},
                         {"European": ["paella", "schnitzel", "pierogi", "lasagna", "fish and chips", "raclette", "cheese fondue", "sausages"]},
                         {"Falafel": ["falafel", "hummus", "pita", "shawarma", "tahini", "tabbouleh", "sumac", "pickles"]},
                         {"Fast Food": ["hamburger", "fries", "pizza", "hot dog", "taco", "burrito", "soda", "milkshake"]},
                         {"Filipino": ["adobo", "sinigang", "pancit", "lechon", "ube", "halo-halo", "kakanin", "champorado"]},
                         {"Fish & chips": ["fish and chips", "mushy peas", "tartar sauce", "vinegar", "lemon wedge", "ketchup", "salt"]},
                         {"Foul": ["foul", "taameya", "shakshuka", "ful medames", "za'atar", "olives", "labneh", "mint tea"]},
                         {"French": ["croissant", "baguette", "ratatouille", "escargot", "quiche", "coq au vin", "crème brûlée", "champagne"]},
                         {"Fried Chicken": ["fried chicken", "mashed potatoes", "biscuits", "coleslaw", "gravy", "hot sauce", "buttermilk"]},
                         {"Frozen Yogurt": ["frozen yogurt", "toppings", "fruits", "granola", "chocolate chips", "honey", "sprinkles", "whipped cream"]},
                         {"Fruits": ["apple", "banana", "strawberry", "mango", "pineapple", "watermelon", "kiwi", "papaya"]},
                         {"Gelato": ["gelato", "sorbetto", "affogato", "pistachio", "stracciatella", "amarena", "crema", "cioccolato"]},
                         {"German": ["bratwurst", "sauerkraut", "pretzel", "schnitzel", "spätzle", "mustard", "beer", "cider"]},
                         {"Gluten free": ["gluten free", "celiac", "rice", "quinoa", "almond flour", "coconut flour", "potatoes", "vegetables"]},
                         {"Greek": ["feta", "olives", "tzatziki", "gyro", "souvlaki", "baklava", "dolmades", "spanakopita"]},
                          {"Grills": ["steak", "chicken", "ribs", "pork chops", "grilled vegetables", "kebabs", "shishito peppers", "corn on the cob"]},
                           {"Healthy": ["salad", "quinoa", "brown rice", "tofu", "grilled fish", "avocado", "sweet potato", "chia seeds"]},
                            {"Hot Dogs": ["mustard", "ketchup", "relish", "onions", "sauerkraut", "chili", "cheese", "bacon bits"]},
                             {"Ice cream": ["vanilla", "chocolate", "strawberry", "mint chip", "cookies and cream", "rocky road", "caramel", "fudge"]},
                              {"Indian": ["naan", "curry", "masala", "tandoori", "saag", "paneer", "samosas", "chutney"]},
                            {"Indonesian": ["nasi goreng", "sate", "rendang", "gado-gado", "tempeh", "sambal", "krupuk", "coconut milk"]},
                          {"International": ["fusion", "global", "world cuisine", "multicultural", "cosmopolitan", "diverse", "eclectic", "mix"]},
                          {"Iranian": ["kebab", "rice pilaf", "stews", "kuku", "dolma", "fesenjan", "shawarma", "lavash"]},
                          {"Iraqi": ["tikka", "biriyani", "masgouf", "khoubiz", "dolma", "pacha", "maglooba", "samoon"]},
                          {"Italian": ["pasta", "pizza", "lasagna", "risotto", "gnocchi", "bruschetta", "caprese salad", "tiramisu"]},
                          {"Jamaican": ["jerk chicken", "curry goat", "ackee and saltfish", "plantains", "rice and peas", "coconut water", "bammy", "rum cake"]},
                          {"Japanese": ["sushi", "ramen", "udon", "tempura", "yakitori", "okonomiyaki", "matcha", "mochi"]},
                          {"Jordanian": ["mansaf", "makloubeh", "zarb", "muhammara", "ful medames", "knafeh", "arabic sweets", "sahlab"]},
                          {"Juices": ["fresh", "cold-pressed", "green", "fruity", "smoothies", "vegetable", "detox", "boost"]},
                          {"Kebab": ["shish kebab", "doner kebab", "lamb kebab", "chicken kebab", "vegetable kebab", "shawarma", "kofta", "tikka"]},
                          {"Keto": ["low-carb", "high-fat", "avocado", "zucchini noodles", "cauliflower rice", "almond flour", "coconut oil", "berries"]},
                         {"Korean": ["kimchi", "bibimbap", "bulgogi", "galbi", "tteokbokki", "japchae", "samgyeopsal", "mandu"]},
                         {"Koshary": ["lentils", "rice", "pasta", "chickpeas", "tomato sauce", "caramelized onions", "garlic"]},
                         {"Kurdish": ["kebab", "dolma", "pita bread", "baklava", "kubba", "kawap"]},
                         {"Kuwaiti": ["machboos", "ghoozi", "thareed", "biriyani", "hummus", "halwa", "qahwa"]},
                         {"Latin american": ["tacos", "empanadas", "ceviche", "arepas", "chorizo", "guacamole", "quesadillas"]},
                         {"Lebanese": ["hummus", "tabbouleh", "shawarma", "kibbeh", "baklava", "manakish", "labneh"]},
                         {"Machbouss": ["rice", "chicken", "onion", "saffron", "tomatoes", "cardamom"]},
                         {"Malaysian": ["nasi lemak", "laksa", "roti canai", "satay", "char kway teow", "rendang"]},
                         {"Manaqeesh": ["za'atar", "labneh", "manoushe", "cheese", "za'atar w zeit"]},
                         {"Mandi": ["rice", "chicken", "lamb", "spices", "tomatoes", "onion"]},
                         {"Mediterranean": ["falafel", "hummus", "tzatziki", "spanakopita", "kibbeh", "tabbouleh"]},
                         { "Mexican": ["tacos", "burritos", "enchiladas", "quesadillas", "guacamole", "salsa", "mole"]},
                         {"Mezze": ["hummus", "tabbouleh", "baba ghanoush", "kibbeh", "falafel", "manakish", "labneh"]},
                         {"Middle eastern": ["hummus", "shawarma", "kibbeh", "falafel", "baklava", "manakish", "labneh"]},
                         {"Milkshakes": ["vanilla", "chocolate", "strawberry", "oreo", "peanut butter", "banana", "caramel"]},
                         {"Mongolian": ["khuushuur", "bansh", "khorkhog", "boodog", "budaatai", "huushuur"]},
                         {"Moroccan": ["couscous", "tagine", "pastilla", "harira", "baklava", "zaalouk"]},
                         {"Nepalese": ["momos", "dal bhat", "chow mein", "curry", "sel roti", "yomari"]},
                         {"Noodles": ["ramen", "pho", "udon", "soba", "lo mein", "pad thai", "chow mein"]},
                         {"North indian": ["tandoori", "biryani", "naan", "saag", "paneer", "dal", "gulab jamun", "lassi"]},
                         {"Nuts": ["almond", "walnut", "cashew", "hazelnut", "pistachio", "macadamia", "pecan", "peanut"]},
        {"Omani": ["shuwa", "harees", "salona", "kabuli", "khubz", "halwa", "kahwa", "dried lemon"]},
         {"Organic": ["kale", "quinoa", "chia", "goji", "acai", "spirulina", "kombucha", "tempeh"]},
          {"Pakistani": ["seekh kebab", "nihari", "haleem", "samosa", "chapli kebab", "biryani", "lassi", "chai"]},
           {"Paleo": ["meat", "fish", "vegetables", "fruit", "nuts", "seeds", "eggs", "coconut oil"]},
            {"Palestinian": ["falafel", "hummus", "musakhan", "shawarma", "maqluba", "taboon bread", "za'atar", "tahini"]},
        {"Pancakes": ["pancake", "maple syrup", "blueberry", "chocolate chips", "whipped cream", "banana", "honey", "buttermilk"]},
        {"Pasta": ["spaghetti", "lasagna", "fettuccine alfredo", "penne arrabiata", "linguine carbonara", "ravioli", "gnocchi", "pesto"]},
        {"Pastries": ["croissant", "danish", "pain au chocolat", "apple turnover", "cinnamon roll", "strudel", "palmier", "scone"]},
        {"Peruvian": ["ceviche", "aji de gallina", "lomo saltado", "arroz con pollo", "papa a la huancaína", "anticuchos", "causa", "pisco sour"]},
        {"Pies": ["apple pie", "pumpkin pie", "blueberry pie", "pecan pie", "lemon meringue pie", "cherry pie", "shepherd's pie", "meat pie"]},
        {"Pizza": ["pepperoni", "margherita", "hawaiian", "meat lovers", "vegetarian", "calzone", "deep dish", "stuffed crust"]},
        {"Poke": ["tuna", "salmon", "avocado", "edamame", "sesame oil", "soy sauce", "rice vinegar", "wasabi"]},
        {"Portuguese": ["bacalhau", "cozido", "pastel de nata", "francesinha", "caldo verde", "arroz doce", "vinho verde", "porto"]},
        {"Pretzels": ["soft pretzel", "mustard", "cheese sauce", "cinnamon sugar", "jalapeno", "everything seasoning", "pretzel bites", "pretzel dogs"]},
                         {"Ramen": ["noodles", "broth", "chashu", "egg", "bamboo shoots", "seaweed", "green onion", "pork"]},
                         {"Russian": ["blini", "borscht", "pelmeni", "beef stroganoff", "syrniki", "pirozhki", "caviar", "kvass"]},
                         {"Saj": ["pita bread", "shawarma", "kebab", "hummus", "tabbouleh", "sumac", "za'atar",  "falafel"]},
                         {"Salad": ["lettuce", "tomatoes", "cucumbers", "olives", "feta cheese", "red onion", "vinaigrette", "croutons"]},
                         {"Sandwiches": ["bread", "meat", "cheese", "lettuce", "tomato", "mayonnaise", "mustard", "pickles"]},
                         {"Saudi": ["kabsa", "shawarma", "mutabbaq", "thareed", "haneeth", "saleeg", "balaleet", "arabic coffee"]},
                         {"Seafood": ["fish", "shrimp", "crab", "lobster", "clams", "oysters", "mussels", "squid"]},
                         {"Seyami": ["lamb", "beef", "chicken", "fish", "dates", "honey", "coffee", "herbs"]},
                         {"Shawarma": ["pita bread", "chicken", "beef", "lamb", "garlic sauce", "tzatziki", "tomatoes", "onions"]},
                         {"Singaporean": ["chilli crab", "hainanese chicken rice", "char kway teow", "satay", "roti prata", "bak kut teh", "laksa", "kaya toast"]},
                         {"Sliders": ["mini burgers", "beef", "cheese", "lettuce", "tomato", "pickle", "ketchup", "mayonnaise"]},
                         {"Smoothies": ["fruit", "yogurt", "milk", "honey", "spinach", "kale", "protein powder", "chia seeds"]},
                         {"Snacks": ["chips", "nuts", "crackers", "popcorn", "jerky", "dried fruit", "granola bars", "trail mix"]},
                         {"Soup": ["chicken noodle", "tomato", "minestrone", "clam chowder", "miso", "pho", "gazpacho", "pumpkin"]},
                         {"South indian": ["dosa", "idli", "sambhar", "rasam", "vada", "thali", "biriyani", "coconut chutney"]},
                         {"Spanish": ["paella", "tortilla española", "gazpacho", "patatas bravas", "pan con tomate", "chorizo", "croquetas", "flan"]},
                         {"Steaks": ["beef", "ribeye", "filet mignon", "sirloin", "porterhouse", "strip steak", "marinade", "grill"]},
                         {"Street food": ["tacos", "gyro", "hot dog", "pretzel", "crepes", "empanadas", "kebab", "arepa"]},
                         {"Sudanese": ["ful medames", "kisra", "shakshuka", "mahshi", "mulukhiyah", "asida", "basbousa", "karkadeh"]},
                         {"Sushi": ["nigiri", "maki", "sashimi", "tempura", "wasabi", "soy sauce", "pickled ginger", "ramen"]},
                         {"Swedish": ["meatballs", "gravlax", "knäckebröd", "cinnamon buns", "smörgåsbord", "prinsesstårta", "janssons frestelse", "surströmming", "rolls"]},
                         {"Syrian": ["hummus", "shawarma", "tabbouleh", "baba ghanoush", "manakeesh", "kibbeh", "ful medames", "za'atar"]},
                         {"Tacos": ["carne asada", "carnitas", "al pastor", "fish", "shrimp", "barbacoa", "pollo", "tortilla"]},
                         {"Tea": ["chai", "oolong", "green tea", "black tea", "matcha", "herbal tea", "bubble tea", "iced tea"]},
                         {"Thai": ["pad thai", "tom yum", "green curry", "massaman curry", "papaya salad", "som tam", "mango sticky rice", "khao soi"]},
                         {"Tunisian": ["brik", "tagine", "couscous", "merguez", "shakshuka", "lablabi", "kaak warka", "harissa"]},
                         {"Turkish": ["kebab", "pide", "börek", "dolma", "baklava", "simit", "kumpir", "çay"]},
                         {"Uzbek": ["plov", "samsa", "lagman", "shurpa", "chuchvara", "manti", "shashlik", "tandoori naan"]},
                         {"Vegan": ["tofu", "tempeh", "quinoa", "chickpeas", "nutritional yeast", "soy milk", "seitan", "plant-based meat"]},
                         {"Vegetarian": ["vegetable stir-fry", "quiche", "falafel", "caprese salad", "ratatouille", "spinach lasagna", "vegetable curry", "hummus"]},
                         {"Vietnamese": ["pho", "banh mi", "spring rolls", "banh xeo", "com tam", "bun cha", "cha gio", "ca phe sua da"]},
                         {"Waffles": ["Belgian waffles", "chicken and waffles", "waffle cones", "waffle fries", "waffle sandwiches", "blueberry waffles", "waffle sundaes", "waffle croutons"]},
                         {"Wings": ["buffalo wings", "BBQ wings", "garlic parmesan wings", "teriyaki wings", "honey mustard wings", "lemon pepper wings", "sweet chili wings", "sriracha wings"]},
                         {"Wraps": ["chicken Caesar wrap", "falafel wrap", "veggie wrap", "tuna salad wrap", "steak fajita wrap", "BLT wrap", "Greek wrap", "turkey club wrap"]}]

        print(f"keywords: {self.keywords[1].values()}")

if __name__ == "__main__":
    K = KeywordsMenuItem()