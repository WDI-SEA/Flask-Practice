### ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Python Programming: Flask

This assignment was adapted from this [homework](https://git.generalassemb.ly/python-programming/python-programming/tree/revisions_v2.1/unit-6-flask/instructor-resources/hw-5day-4flask) from [GA's Python Part-Time](https://generalassemb.ly/education/python-programming) course.

<!---
This assignment was originally developed by Kevin

Questions? Comments?
1. Log an issue to this repo to alert me of a problem.
2. Suggest an edit yourself by forking this repo, making edits, and submitting a pull request with your changes back to our master branch.
3. Hit me up on Slack at @kevin.coyle.

Note: Adaptation made in fall 2019 by Brandi Butler.
--->

# Flask: Practice Problems

In this homework, you're going to write code for a few problems.

You will practice these programming concepts we've covered in class:

* Rendering templates
* Passing variables to templates
* Creating an API (sending JSON)
* Making `GET` routes

------------

## Deliverables

For this assignment you will be creating ONE Flask app. Each problem listed below will direct you to create a route or feature within that app.

*Reminder: On your laptop, you can run your server from your command line with the following command:*

```
flask run
```

> **Hint**: After finish writing code for each problem, launch your server, go into your browser, and be sure that your Flask app is outputting the intended data.


## Requirements:

* By the end of this, you should have ONE Flask app that meets the following criteria:

| METHOD | PATH | FUNCTIONALITY |
| ------ | ------------- | ---------------------------------------------------------- |
| GET | `/` | Render a home page that sends the string "Hello World" |
| GET | `/greeting` | Pass a name variable to a template that renders a personalized greeting |
| GET | `/pie` | Return a JSON object that contains a key-value pair |

------------

## Problem 1: Hello World

### Skill You're Practicing: Creating a Flask app from scratch

Set up a Flask app skeleton. This will include making a python server file - this will be named something like `app.py`.

`app.py` should include the following:

* Import Flask
* Declare your app variable
* Make your home page route (Hint: Use `@app.route()`)
* Return the string "Hello World"

At this point, run your app with `flask run` and see what happens!

> HINT: You may want to set some environment variables such as FLASK_APP and FLASK_ENV.

If you ran into an error when running your app, try setting these variables via the command line:

```
export FLASK_ENV=development
export FLASK_APP=app.py
```

## Problem 2: Render Like Rembrandt

### Skill You're Practicing: Using templates to render Python

Create a new route in your Flask app that renders an HTML template that can be accessed at the url `/greeting`. In the template, display a greeting and a `name` variable (don't forget to pass the template the argument!). Look up the `render_template` function to get started. You will need to create a `templates` folder and an `index.html` file inside that `templates` folder in order for the code to work.

#### Starter Code

```
render_template('index.html', name='Akilah')
```

#### Example Output (In-Browser)

```
"Hi there Akilah. It's great to see you today!"
```

**Hint 1:**

Remember: In templates, to render a variable's value, use the double brackets `{{}}`.

**Hint 2:**

Don't forget to import the module `render_template` from Flask.

**Checkpoint:**

Your directory should now look like:

```
project
│   
│app.py
│   
│templates
│   └─── index.html
│   
│static
│   └───style.css
```

------

## Problem 3: All I See is Static

### Skill You're Practicing: Serving Static Files

Create a `static` folder in the top-level of your project directory. This is where files like CSS, images, audio, and front-end JavaScript live. Inside your `static` folder, create a file called `style.css`.

In your `style.css` file, add some styling to change the color of your text to green (or any color other than the default!). Last, add a link tag in your index.html template to `/static/style.css`. Unlike some other languages, "static" is part of the url path.

```html
<link type="text/css" rel="stylesheet" href="/static/style.css">
```

Go check your browser to see if your changes took effect.

> Note: You may have to do a hard reload (Mac Shortcut: Command + Shift + R)

**Hint: If it didn't work...**

If you did a hard reload and restarted the server and you still don't see your CSS changes, open the "Network" tab in your developer tools. Do a page refresh. In the list that comes up, do you see `style.css`? If it is in red and the status is anything other than 200 something, you may have written the wrong path in your link tag or perhaps forgotten to add the link tag!

**Checkpoint:**

Your directory should now look like:

```
project
│   
│app.py
│   
│templates
│   └─── index.html
│   
│static
│   └───style.css
```

## Problem 4: A Detective, A PI

### Skill You're Practicing: Creating an API

Write a new route in your Flask app that can be accessed via a `GET` request to `/pie` and returns a JSON object of one of the items in a list. Make your JSON object with the `jsonify` function. Create your own `ingredients` list with at least 3 items, which should be strings.


#### Starter Code

```
return jsonify({'pie ingredient': ingredients[0]})
```

#### Example Output

```
{'pie ingredient': 'apples'}
```

**Bonus:**

Make which ingredient you return each time selected at random.

**Hint:**

Remember to import `jsonify`!

----

## Bonus: The POST Man Deliverth

### Skill You're Practicing: POST routes

Easy breezy? Flask is nice! If you finished this assignment in less than an hour, please attempt the following bonus routes:

| METHOD | PATH | FUNCTIONALITY |
| ------ | ------------- | ---------------------------------------------------------- |
| GET | `/recipe` | Render a template that shows the name of a pie, all ingredients, and a new ingredient form |
| POST | `/recipe` | The form from the GET page sends a new ingredient. Add this to your ingredients list then redirect back to `/recipe` |

> Hint: Keep `ingredients` as a global variable that you declare outside of any particular route.


#### Starter Code

```
ingredients.append(ingredient)
return redirect('/recipe')
```

**Hint 1:**

Remember to import the `redirect` module.


**Hint 2:**

You can access the method (the HTTP verb) via `request.method`.

**Hint 3:**

You can access the form data passed to your route according to the "name" property you put on your HTML input tag. For example, if you named your input "ingredient", you can access the value like so:

```python
new_ingredient = request.form["ingredient"]
```

### That's It!

Have a RESTful evening!
