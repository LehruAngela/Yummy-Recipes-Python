## Yummy-Recipes
[![Build Status](https://travis-ci.org/LehruAngela/Yummy-Recipes.png)](https://travis-ci.org/LehruAngela/Yummy-Recipes)

[![Code Climate](https://codeclimate.com/github/LehruAngela/Yummy-Recipes.png)](https://codeclimate.com/github/LehruAngela/Yummy-Recipes)

[![Coverage Status](https://coveralls.io/repos/LehruAngela/Yummy-Recipes/badge.png?branch=master)](https://coveralls.io/repos/LehruAngela/Yummy-Recipes/branch=master)


 The innovative yummy recipes app is an application that allows users  to create, save and share recipes, meeting the needs of keeping track of awesome food recipes.
	

###### The app will enable users to:
 1. Create accounts
 2. Log in
 3. Create, view, update and delete recipe categories
 4. Create, view, update or delete recipes in existing categories
	
		
###### To test the application and get it running, do the following:

1. Install virtualenv and virtualenvwrapper (Make sure to have pip installed already)
 ```
 $ pip install virtualenv
 $ pip install virtualenvwrapper
 $ export WORKON_HOME=~/Envs
 $ source /usr/local/bin/virtualenvwrapper.sh
```

 2. Create the virtual environment and activate it
 
 ```
 $ mkvirtualenv my_project
 $ workon my_project
 ```

3. Install the requirements file for all the dependencies of the application

```
$ pip install -r requirements.txt
```

4. Run the application

```
$ python run.py
```
5. Open this link on your browser to view the application

```
http://localhost:5000
```
