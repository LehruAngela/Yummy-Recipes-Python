# Yummy-Recipes
 The innovative yummy recipes app is an application that allows users  to create, save and share recipes, meeting the needs of keeping track of awesome food recipes.

The app will enable users to:
<li>Create accounts
<li>Log in
<li>Create, view, update and delete recipe categories
<li>Create, view, update or delete recipes in existing categories


To test the application and get it running, do the following:

Install virtualenv and virtualenvwrapper (Make sure to have pip installed already)
 ```
 $ pip install virtualenv
 $ pip install virtualenvwrapper
 $ export WORKON_HOME=~/Envs
 $ source /usr/local/bin/virtualenvwrapper.sh
```

 Create the virtual environment and activate it
 
 ```
 $ mkvirtualenv my_project
 $ workon my_project
 ```

Install the requirements file for all the dependencies of the application

```
pip install -r requirements.txt
```

Run the application

```
python run.py
```
Open this linl on your browser to view the application

```
http://localhost:5000
```
