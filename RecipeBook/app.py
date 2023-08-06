from flask import Flask, redirect, url_for, request, render_template
import os
import pandas as pd
from werkzeug.utils import secure_filename
from forms import RecipeForm
import random

app = Flask(__name__)
app.config['SECRET_KEY'] = 'nvmnkfwslzmnx.kj456/W?ERIU&WE(F*&/hksef;g98734:SP(&D'
app.config['SUBMITTED_DATA'] = os.path.join('static', 'data', '')
app.config['SUBMITTED_IMG'] = os.path.join('static', 'img', '')

# Get the current list of recipe names
path = os.getcwd() + "/static/data"
recipeNames = []
for r in os.listdir(path):
    recipeNames.append(r.replace(".csv", ""))

def searchRecipe(term):
    i =- 1
    for df in recipeList:
        i = df.str.find(term)
    if 1 >= 0:
        return render_template('viewRecipe.html', mainRecipe=recipeList[i][0])

@app.route('/', methods=['POST', 'GET'])
def myRecipeCollection():
    """
    Function to get random recipes to display on page
    :return:
    """
    random.shuffle(recipeNames)
    r1 = pd.read_csv(os.path.join(app.config['SUBMITTED_DATA'] +
                                  recipeNames[0].lower().replace(" ", "_") + '.csv'), index_col=False)
    r2 = pd.read_csv(os.path.join(app.config['SUBMITTED_DATA'] +
                                  recipeNames[1].lower().replace(" ", "_") + '.csv'), index_col=False)
    r3 = pd.read_csv(os.path.join(app.config['SUBMITTED_DATA'] +
                                  recipeNames[2].lower().replace(" ", "_") + '.csv'), index_col=False)
    r4 = pd.read_csv(os.path.join(app.config['SUBMITTED_DATA'] +
                                  recipeNames[3].lower().replace(" ", "_") + '.csv'), index_col=False)

    if request.method == 'POST':
        searchString = request.form['searchString']
        searchRecipes(searchString)

    return render_template('index.html', r1=r1.iloc[0], r2=r2.iloc[0], r3=r3.iloc[0], r4=r4.iloc[0])


@app.route('/addRecipe', methods=['POST', 'GET'])
def addRecipe():
    """
        Create and get data to make a recipe.
        :return: if form is complete, go to home page. Else reload addRecipe page
    """
    form = RecipeForm()
    if form.validate_on_submit():
        name = form.recipeName.data
        description = form.recipeDescription.data
        breakfast = form.breakfastCategory.data
        lunch = form.lunchCategory.data
        supper = form.supperCategory.data
        snack = form.snackCategory.data
        drink = form.drinkCategory.data
        dessert = form.dessertCategory.data
        ingredients = form.recipeIngredients.data
        directions = form.recipeDirections.data
        pic = name.lower().replace(" ", "_") + "." + secure_filename(form.recipePicture.data.filename).split('.')[-1]
        form.recipePicture.data.save(os.path.join(app.config['SUBMITTED_IMG'] + pic))
        df = pd.DataFrame([{'name': name, 'description': description, 'breakfast': breakfast, 'lunch': lunch,
                            'supper': supper, 'snack': snack, 'drink': drink, 'dessert': dessert,
                            'ingredients': ingredients, 'directions': directions, 'pic': pic}])
        df.to_csv(os.path.join(app.config['SUBMITTED_DATA'] + name.lower().replace(" ", "_") + ".csv"))
        recipeNames.append(df['name'])
        return redirect(url_for('myRecipeCollection'))
    else:
        return render_template('addRecipe.html', form=form)


@app.route('/viewRecipe/<recipeName>')
def viewRecipe(recipeName):
    """
    Function to parse the ingredients and description.
    :param recipeName:
    :return: recipe name, ingredients, description
    """
    mainRecipe = pd.read_csv(os.path.join(app.config['SUBMITTED_DATA'] +
                                  recipeName.lower().replace(" ", "_") + '.csv'), index_col=False)
    ingredients = mainRecipe['ingredients'].str.split("\n")
    directions = mainRecipe['directions'].str.split("\n")

    recipeList = [recipe for recipe in recipeNames]
    # recipeList.remove(mainRecipe['name'])
    random.shuffle(recipeList)
    r2 = pd.read_csv(os.path.join(app.config['SUBMITTED_DATA'] +
                                  recipeList[0].lower().replace(" ", "_") + '.csv'), index_col=False)
    r3 = pd.read_csv(os.path.join(app.config['SUBMITTED_DATA'] +
                                  recipeList[1].lower().replace(" ", "_") + '.csv'), index_col=False)
    r4 = pd.read_csv(os.path.join(app.config['SUBMITTED_DATA'] +
                                  recipeList[2].lower().replace(" ", "_") + '.csv'), index_col=False)

    return render_template('viewRecipe.html', mainRecipe=mainRecipe.iloc[0], ingredients=ingredients[0], directions=directions[0],
                           r2=r2.iloc[0], r3=r3.iloc[0], r4=r4.iloc[0])


@app.route('/searchRecipes')
def searchRecipes(term):
    return render_template('searchRecipes.html')


@app.route('/browseRecipes')
def browseRecipes():
    return render_template('browseRecipes.html')


if __name__ == '__main__':
    app.run(debug=True, port=5003)
