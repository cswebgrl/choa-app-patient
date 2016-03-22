# fgh-web
Frogs' Greatest HITs web prototype

## Setting up for development

Note: if you don't have Python installed, you can install it on Mac using Homebrew:

    brew install python
Or you can install it on Windows using the instructions at http://docs.python-guide.org/en/latest/starting/install/win/.

You may also need to install sqlite and/or sqlite3-devel depending on your operating system.

To run the app, you need to install Django and dependencies:

    git clone https://github.gatech.edu/cdchealthyweight/fgh-web.git fgh
    cd fgh
    pip install -r requirements.txt

After this, you can set up the app locally:

    (may not work) ~~python manage.py syncdb~~
    (try) python manage.py migrate

And run it using:

    python manage.py runserver
    
The application should now be accessible at http://127.0.0.1:8000/questionnaire.

Note: if for some reason you wish to run the development server on a machine other than your development box, you can do that as follows:

    python manage.py runserver 0.0.0.0:8000&
(see http://stackoverflow.com/questions/13522228/running-django-development-server-on-a-remote-machine-using-putty-how-to-run-th)

However, if you find yourself doing this on a regular basis you should really just bite the bullet and set up Apache+WSGI.
