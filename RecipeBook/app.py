from flask import Flask, redirect, url_for, request, render_template
import os
import pandas as pd
from werkzeug.utils import secure_filename
from forms import RecipeForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'nvmnkfwslzmnx.kj456/W?ERIU&WE(F*&/hksef;g98734:SP(&D'
app.config['SUBMITTED_DATA'] = os.path.join('static', 'data', '')
app.config['SUBMITTED_IMG'] = os.path.join('static', 'img', '')

@app.route('/')
def myRecipeCollection():  # put application's code here
    return render_template('index.html')
@app.route('/addRecipe', methods=['POST', 'GET'])
def addRecipe():
    """
        Function to show example instance
        :return:
    """
    form = RecipeForm()
    if form.validate_on_submit():
        name = form.recipeName
        description = form.recipeDescription
        breakfast = form.breakfastCategory
        lunch = form.lunchCategory
        supper = form.supperCategory
        snack = form.snackCategory
        drink = form.drinkCategory
        dessert = form.dessertCategory
        ingredients = form.recipeIngredients
        directions = form.recipeDirections
        pic = name.lower().replace(" ", "_")+"." + secure_filename(form.recipePicture.data.filename).split('.')[-1]
        form.recipePicture.data.save(os.path.join(app.config['SUBMITTED_IMG'] + pic))
        df = pd.DataFrame([{'name': name, 'description': description, 'breakfast': breakfast, 'lunch': lunch,
                            'supper': supper, 'snack': snack, 'drink': drink, 'dessert': dessert,
                            'ingredients': ingredients, 'directions': directions}])
        df.to_csv(os.path.join(app.config['SUBMITTED_DATA'] + name.lower().replace(" ", "_")+".csv"))
        print(df)
        return redirect(url_for('myRecipeCollection'))
    else:
        return render_template('addRecipe.html', form=form)
@app.route('/viewRecipe')
def viewRecipe():
    return render_template('view.html')
@app.route('/searchRecipes')
def searchRecipes():
    return render_template('search.html')
@app.route('/browseRecipes')
def browseRecipes():
    return render_template('browse.html')


if __name__ == '__main__':
    app.run(debug=True, port=8080)
