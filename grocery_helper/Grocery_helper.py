from constants import *


def num_hours() -> float:
    """
    Returns the number of hours spent on this project as a float
    """
    return float(25)


def get_recipe_name(recipe: tuple[str, str]) -> str:
    """
    Returns the str name of recipe given a recipe in the form tuple[str, str]
    Example:
    >>> get_recipe_name(('chocolate peanut butter banana shake',
    '1 large banana,240 ml almond milk'))
    'chocolate peanut butter banana shake'
    """
    return recipe[0]


def parse_ingredient(raw_ingredient_detail: str) -> tuple[float, str, str]:
    """
    Returns the amount, measure and ingredient as strings in a tuple given
    the raw ingredient details in a single string.
    Example:
    >>> parse_ingredient('0.5 tsp coffee granules')
    (0.5, 'tsp', 'coffee granules')
    """
    # generate a list containing the ingredient details
    ingredient_list = raw_ingredient_detail.split(" ")

    # define each element within the list as its corresponding variable
    amt = float(ingredient_list[0])
    meas = ingredient_list[1]
    ingr = " ".join(ingredient_list[2:])

    # return the variables in a tuple
    return (amt, meas, ingr)


def create_recipe() -> tuple[str, str]:
    """
    Returns a recipe in the tuple[str, str] format after a series of prompting. The recipe name
    is prompted first followed by continuous ingredient prompting until an empty string is entered
    (enter or return key press with no text).
    Example:
    >>> create_recipe()
    Please enter the recipe name: peanut butter
    Please enter an ingredient: 300 g peanuts
    Please enter an ingredient: 0.5 tsp salt
    Please enter an ingredient: 2 tsp oil
    Please enter an ingredient:
    ('peanut butter', '300 g peanuts,0.5 tsp salt,2 tsp oil')
    """
    # prompt the user for a recipe name and store it in a variable
    recipe_name = input("Please enter the recipe name: ")

    # create an empty list of ingredients to append to later
    ingredient_list = []

    # while loop taking the ingredient inputs to append to the ingredient list
    while True:
        ingredients = input("Please enter an ingredient: ")
        if ingredients == "":
            break
        ingredient_list.append(ingredients)

    # take the ingredient list and turn it into a string
    str_ingredient_list = str(",".join(ingredient_list))

    # return the name and ingredients of the new recipe in a tuple
    return (recipe_name, str_ingredient_list)


def recipe_ingredients(recipe: tuple[str, str]) -> tuple[tuple[float, str, str]]:
    """
    Given a recipe in the tuple[str, str] form,
    Returns a tuple which contains ingredients in the tuple form
    containing amount, measure and ingredient name strings.
    Example:
    >>> recipe_ingredients(('peanut butter',
    '300 g peanuts,0.5 tsp salt,2 tsp oil'))
    ((300.0, 'g', 'peanuts'), (0.5, 'tsp', 'salt'), (2.0, 'tsp', 'oil'))
    """
    # generate a list containing the ingredients
    ingr_list = str(recipe[1]).split(",")

    # prepare a final ingredient list to append ingredient tuples to later
    final_ingr_list = []

    for ingr_str in ingr_list:
        # generate smaller lists containing the details of each ingredient
        ingr_details = ingr_str.split()

        # store ingredient details as corresponding variables
        amt = float(ingr_details[0])
        meas = ingr_details[1]
        ingr = " ".join(ingr_details[2:])

        # store variables in an ingredient tuple
        ingr_tuple = (amt, meas, ingr)

        # append ingredient tuples to the final list
        final_ingr_list.append(ingr_tuple)

    # return the list as a tuple
    return tuple(final_ingr_list)


def add_recipe(new_recipe: tuple[str, str], recipes: list[tuple[str, str]]) -> None:
    """
    Given a new recipe in the tuple[str,str] format, adds the given recipe to a list of recipes.
    Example:
    >>> recipes = []
    >>> recipe = ('peanut butter', '300 g peanuts,0.5 tsp salt,2 tsp oil')
    >>> add_recipe(recipe, recipes)
    >>> recipes
    [('peanut butter', '300 g peanuts,0.5 tsp salt,2 tsp oil')]
    """
    recipes.append(new_recipe)


def find_recipe(
    recipe_name: str, recipes: list[tuple[str, str]]
) -> tuple[str, str] | None:
    """
    Given a recipe name in a string, this function attempts to find the recipe
    within a list of recipes. Returns the recipe as tuple[str, str] if found.
    If the recipe can not be found then this function should return None.
    >>> recipes = [('peanut butter', '300 g peanuts,0.5 tsp salt,2 tsp oil')]
    >>> find_recipe('peanut butter', recipes)
    ('peanut butter', '300 g peanuts,0.5 tsp salt,2 tsp oil')
    """
    # check if the given recipe name matches the name of any recipes in the list and return if True
    for recipe in recipes:
        if recipe_name == recipe[0]:
            return recipe


def remove_recipe(name: str, recipes: list[tuple[str, str]]) -> None:
    """
    Removes a recipe from the list of recipes given the name of a recipe as a string.
    If the recipe name does not match any of the recipes within the list then nothing happens.
    Example:
    >>> recipes = [('peanut butter', '300 g peanuts,0.5 tsp salt,2 tsp oil'),
    ('cinnamon rolls', '480 ml almond milk,115 g Nuttelex,50 g sugar,7 g
    active dry yeast,5.5 cup flour,1 tsp salt,170 g Nuttelex,165 g brown
    sugar,2 tbsp cinnamon,160 g powdered sugar,30 ml almond milk,0.5 tsp
    vanilla extract')]
    >>> remove_recipe('brownie', recipes)
    >>> recipes
    [('peanut butter', '300 g peanuts,0.5 tsp salt,2 tsp oil'), ('cinnamon
    rolls', '480 ml almond milk,115 g Nuttelex,50 g sugar,7 g active dry
    yeast,5.5 cup flour,1 tsp salt,170 g Nuttelex,165 g brown sugar,2 tbsp
    cinnamon,160 g powdered sugar,30 ml almond milk,0.5 tsp vanilla
    extract')]
    """
    # check if the recipe name matches any recipes in the list and remove it from the list if True
    for recipe in recipes:
        if name == recipe[0]:
            recipes.remove(recipe)


def get_ingredient_amount(
    ingredient: str, recipe: tuple[str, str]
) -> tuple[float, str] | None:
    """
    Return the amount and measure as a tuple[float, str] of a certain ingredient,
    given the ingredient str and a recipe in tuple[str, str] format.
    If the ingredient doesn’t exist within the recipe then nothing happens.
    Example:
    >>> recipe = ('peanut butter', '300 g peanuts,0.5 tsp salt,2 tsp oil')
    >>> get_ingredient_amount('peanuts', recipe)
    (300.0, 'g')
    >>> get_ingredient_amount('soy beans', recipe)
    """
    # generate a list from the ingredient str
    ingr_list = recipe[1].split(",")

    for ingr in ingr_list:
        # generate lists containing the details of each ingredient
        ingr_details = ingr.split(" ")

        # store relevant details as corresponding variables
        amount = float(ingr_details[0])
        meas = ingr_details[1]
        name = " ".join(ingr_details[2:])

        # check if the name of the given ingredient corresponds to any in the list
        if ingredient == name:
            # return the amount and measure if true
            return (amount, meas)


def add_to_shopping_list(
    ingredient_details: tuple[float, str, str],
    shopping_list: list[tuple[float, str, str] | None],
) -> None:
    """
    Add an ingredient from an ingredient details tuple[float, str, str] to the shopping list
    which could be empty or could contain tuples of ingredient details.
    If the ingredient being added already exists within the shopping list then the amount
    should be combined.
    If the ingredient does not exist then it can be added without any calculations.
        Example:
    >>> shopping_list = [(300.0, 'g', 'peanuts'), (0.5, 'tsp', 'salt'),
    (2.0, 'tsp', 'oil')]
    >>> add_to_shopping_list((1000.0, 'g', 'tofu'), shopping_list)
    >>> shopping_list
    [(300.0, 'g', 'peanuts'), (0.5, 'tsp', 'salt'), (2.0, 'tsp', 'oil'),
    (1000.0, 'g', 'tofu')]
    """

    # store the amount and name of the given ingredient as corresponding variables
    amount_1 = float(ingredient_details[0])
    name_1 = ingredient_details[2]

    # assign an index value to each ingredient in the shopping list
    for index, ingredient in enumerate(shopping_list):
        # store details of each ingredient in variables
        amount_2 = float(ingredient[0])
        meas = ingredient[1]
        name_2 = ingredient[2]

        # check if the name of the given ingredient corresponds to any ingredients in the list
        if name_1 == name_2:
            # if true add amounts and replace the old ingredient details at the corresponding index
            new_amount = amount_1 + amount_2
            shopping_list[index] = (new_amount, meas, name_2)
            return

    shopping_list.append(ingredient_details)


def remove_from_shopping_list(
    ingredient_name: str, amount: float, shopping_list: list
) -> None:
    """
    Remove a float amount of an ingredient, given the ingredient_name str, from the shopping_list.
    If the ingredient exists in the list then the amount given as the parameter of this func-
    tion should be subtracted from the amount that exists in the shopping_list. The ingredient
    should be removed from the shopping list altogether if the amount goes below 0.
    Example:
    >>> shopping_list = [(1500.0, 'g', 'peanuts'), (0.5, 'tsp', 'salt'),
    (2.0, 'tsp', 'oil'), (9000.0, 'g', 'tofu'), (100.0, 'g', 'sugar'),
    (50.0, 'g', 'tomato sauce'), (120.0, 'g', 'rice'),
    (920.0, 'g', 'ice cream')]
    >>> remove_from_shopping_list('ice cream', 500.0, shopping_list)
    >>> shopping_list
    [(1500.0, 'g', 'peanuts'), (0.5, 'tsp', 'salt'), (2.0, 'tsp', 'oil'),
    (9000.0, 'g', 'tofu'), (100.0, 'g', 'sugar'), (50.0, 'g', 'tomato
    sauce'), (120.0, 'g', 'rice'), (420.0, 'g', 'ice cream')]
    """

    # assign an index value to each ingredient in the shopping list
    for index, ingredient in enumerate(shopping_list):
        # assign corresponding variables to ingredient details
        original_amount = float(ingredient[0])
        meas = ingredient[1]
        name = ingredient[2]

        # check if the name of any ingredient corresponds to the given name
        if name == ingredient_name:
            # if true, remove the given amount from the original amount at the index
            new_amount = original_amount - amount
            if new_amount <= 0:
                del shopping_list[index]
            else:
                shopping_list[index] = (new_amount, meas, name)


def generate_shopping_list(
    recipes: list[tuple[str, str]]
) -> list[tuple[float, str, str]]:
    """
    Return a list of ingredient tuples (float amount, measure str, ingredient_name str),
    given a list of recipes in list[tuple[str, str]] form.
    Example:
    >>> shopping_list = generate_shopping_list([PEANUT_BUTTER,
    MUNG_BEAN_OMELETTE])
    >>> shopping_list
    [(300.0, 'g', 'peanuts'), (1.0, 'tsp', 'salt'), (3.0, 'tsp', 'oil'),
    (1.0, 'cup', 'mung bean'), (0.75, 'tsp', 'pink salt'), (0.25, 'tsp',
    'garlic powder'), (0.25, 'tsp', 'onion powder'), (0.125, 'tsp',
    'pepper'), (0.25, 'tsp', 'turmeric'), (1.0, 'cup', 'soy milk')]
    """
    shopping_list = []

    # create a loop which finds the ingredients of each given recipe, then adds them to a list
    # duplicate ingredients have their values added together using the add_to_shopping_list function
    for recipe in recipes:
        recipe = recipe_ingredients(recipe)
        for ingredient in recipe:
            add_to_shopping_list(ingredient, shopping_list)
    return shopping_list


def display_ingredients(shopping_list: list[tuple[float, str, str]]) -> None:
    """
    Prints the given shopping list row by row
    with the ingredient details of each tuple[float, str, str] in the list
    separated by "|" and a predetermined amount of spaces.
    Example:
    >>> display_ingredients([(1.0, 'large', 'banana'), (0.5, 'cup', 'ice'),])
    | 1.0 | large | banana |
    | 0.5 | cup | ice |
    """
    spaces = " "

    # initialise max values
    max_amount = 0
    max_measure = 0
    max_name = 0

    # generate max length values for each variable for each ingredient in the shopping list
    for ingredient in shopping_list:
        amount, meas, name = ingredient
        amount_len = len(str(amount))
        meas_len = len(meas)
        name_len = len(name)

        max_amount = max(amount_len, max_amount)

        max_measure = max(meas_len, max_measure)

        max_name = max(name_len, max_name)

    # create a for loop iterating over the length of amount, measure and name of each ingredient
    for ingredient in shopping_list:
        amount, meas, name = ingredient
        amount_len = len(str(amount))
        meas_len = len(meas)
        name_len = len(name)

        # format the ingredient details for each ingredient to display
        # use mathematical formulas to determine the amount of spaces
        print(
            "|"
            + (max_amount + 1 - amount_len) * spaces
            + str(amount)
            + spaces
            + "|"
            + spaces
            + (((max_measure - meas_len) // 2 + (max_measure - meas_len) % 2)) * spaces
            + meas
            + ((max_measure + 1 - meas_len) // 2 + (max_measure + 1 - meas_len) % 2)
            * spaces
            + spaces
            + "|"
            + spaces
            + name
            + (max_name - name_len + 1) * spaces
            + spaces
            + "|"
        )


def sanitise_command(command: str) -> str:
    """
    Return a command string to all lower-case and no leading or trailing white spaces removing
    any numbers from the given command string.
    Example:
    >>> sanitise_command('add chocolate brownies')
    'add chocolate brownies'
    >>> sanitise_command('add c4hocolate Brownies')
    'add chocolate brownies'
    """
    # make all characters in the command string lower case
    command = command.lower()

    # remove all leading or trailing white spaces, numbers or alpha characters from command string
    command = command.strip()
    new_command = ""
    for chara in command:
        if chara.isalpha() or chara.isspace():
            new_command += chara
    new_command = " ".join(new_command.split())

    return new_command


def main():
    """
    At the beginning of the interaction, the user is prompted with the message
    Please enter a command:
    (note the trailing space) to choose a command. Once a command is entered the user should be
    prompted again. The valid commands are outlined below:
    H or h: Help
    mkrec: creates a recipe, add to cook book.
    add {recipe}: adds a recipe to the collection.
    rm {recipe}: removes a recipe from the collection.
    rm -i {ingredient_name} {amount}: removes ingredient from shopping list.
    ls: list all recipes in shopping cart.
    ls -a: list all available recipes in cook book.
    ls -s: display shopping list.
    g or G: generates a shopping list.
    Q or q: Quit.
    Throughout the interaction, the user may add to or remove from the cookbook. They can also
    add to or remove from the list of recipes as well.
    """
    # cook book
    recipe_collection = [
        CHOCOLATE_PEANUT_BUTTER_SHAKE,
        BROWNIE,
        SEITAN,
        CINNAMON_ROLLS,
        PEANUT_BUTTER,
        MUNG_BEAN_OMELETTE,
    ]

    # Write the rest of your code here

    # initialise an empty list for the meal plan
    meal_plan = []

    # create an interaction loop that repeats until q or Q is chosen
    while True:
        # prompt the user for a command
        user_input = input("Please enter a command: ")

        # create a sanitised version of the command
        sanitised_input = sanitise_command(user_input)

        # create a list version of the input
        input_parts = user_input.split()

        # print the help text
        if user_input == "H" or user_input == "h":
            print(HELP_TEXT)

        # end the interaction loop
        elif user_input == "Q" or user_input == "q":
            break

        # prompt the user to create a recipe, then add to the cook book using add_recipe function
        elif user_input == "mkrec":
            new_recipe = create_recipe()
            add_recipe(new_recipe, recipe_collection)

        # check if user typed add at start of command
        elif sanitised_input.split()[0] == "add":
            # use find_recipe to check if recipe details exist in cook book
            recipe_details = find_recipe(sanitised_input[4:], recipe_collection)

            # print a message if it doesn't exist in cook book
            if recipe_details is None:
                print("\nRecipe does not exist in the cook book. ")
                print("Use the mkrec command to create a new recipe.\n")

            # add recipe details to the meal plan using add_recipe if it exists in the cook book
            else:
                add_recipe(recipe_details, meal_plan)

        # generate and display a shopping list containing the ingredients from the meal plan
        elif user_input == "g" or user_input == "G":
            shopping_list = generate_shopping_list(meal_plan)
            display_ingredients(shopping_list)

        # check if a user typed rm -i in the command
        elif input_parts[0] == "rm" and input_parts[1] == "-i":
            # store the given amount and name as variables
            amount = float(input_parts[-1])
            name = " ".join(input_parts[2:-1])

            # remove given amount and name of ingredient from the shopping list
            remove_from_shopping_list(name, amount, shopping_list)

        # remove the given recipe details from the meal plan if the user typed rm in the command
        elif sanitised_input.split()[0] == "rm":
            recipe_name = sanitised_input[3:]
            remove_recipe(recipe_name, meal_plan)

        # print the meal plan or a message if no recipe details have been added to the meal plan
        elif user_input == "ls":
            if len(meal_plan) == 0:
                print("No recipe in meal plan yet.")
            else:
                print(meal_plan)

        # print the available recipes in the cook book in sanitised form
        elif user_input == "ls -a":
            for recipe in recipe_collection:
                print(sanitise_command(get_recipe_name(recipe)))

        # display a shopping list containing the ingredients from the meal plan
        elif user_input == "ls -s":
            display_ingredients(shopping_list)


if __name__ == "__main__":
    main()
