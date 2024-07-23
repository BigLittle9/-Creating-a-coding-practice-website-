# 👾Creating a coding practice website👾

With this guide and the files included in the repository, you will be able to re-create a simple question and answer coding site. If you have Python experience, you likely can go ahead and set-up everything quickly, using this as a template. Any code explanations will mostly be covered in comments, but any common errors that I encountered will be documented along with possible solutions in the Troubleshooting FAQs section. To start, you will need an IDE that you can code in Python with. I recommend [Visual Studio Code](https://code.visualstudio.com/), but you can use any other option.

Some options:
- 
-
-

## Python libraries
Once you determine and set-up your python IDE, you will need to install some libraries using the command line. You begin with installing the pip installer, then set-up your virtual environment, then python Flask. 

For mac/Linux 
```
python -m pip install
```
and
```
python -m pip update
```


For Windows
```
py -m pip install
```
and
```
py -m pip update
```

Once pip is installed and up to date, you will need to set-up your virtual environment.

## Setting-up the virtual environment
Read the SET-UP document to [set-up a virtual environment](/SET-UP.md)

## Installing Python Flask.

With pip installed, and your virtual environment set-up, you can now instal the Python Flask library. Input these prompts into your command line.


For mac/Linux and Windows
```
$ pip install Flask
```

Flask is now installed, and you are ready to start organising the files provided in the repository.

## Creating the necessary files
Once you've set-up and installed the required libraries, you can go ahead and start adding files to the project directory. In this project, I have seperate HTML files for the login, register, question, and leaderboard page, which act as the front-end. You can also create your python flask application, which will act act as the back-end. Your file-tree should look something like this.

```
my_flask_app/
├── app.py
└── templates/
    ├── login.html
    ├── register.html
    ├── question.html
    └── leaderboard.html
```

Your virtual environment will be what is named 'my_flask_app'. For convenience you can create a file that contains the venv file, and name it whatever you want. Within this venv file, the hierarchy/organisation of the files will need to be consistent. It is important that you save your files under the same file that was referred to when setting up the virtual environment, in this case, my_flask_app -> venv. It is also important to note that any references to other files are by their name, so any changes would need to be updated in the code to ensure that the correct file is being called. One example of an error could be having the login page named 'loginpage.html', and using the code:

```
return render_template('login.html', error='Invalid username or password')
```
When the code refers to a HTML page, it is required that names are consistent. If no HTML file is found with the name inputted in a request, and error will occur.

It may be easier to keep the file names used in this repository for initial set-up. 


## Running the program

Once all of your files are in the correct order and named appropriately, you should run the flask application (app.py). If done correctly, you should recieve this output,

```
 ~file directory~
 * Serving Flask app 'app'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
```
What this means is that a local instance of the flask application has been created on the local (http://127.0.0.1:5000) address. By visiting this address, you will see that you are directed to a webpage of 'login.html'.
![](/assets/images/Screenshot 2024-07-23 at 19.21.31)

<img width="220" alt="Screenshot 2024-07-23 at 19 40 14" src="https://github.com/user-attachments/assets/03781b4a-bf7c-4d5a-af52-7f523dbe0d20">

```python
h

print()

```



