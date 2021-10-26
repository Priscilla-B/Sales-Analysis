# **Instructions and Set up Notes**

## **Setting up Local Coding Enviroment**
### **Python**
#### What is Python?
- [Python Beginners Guide - Coursera](https://www.coursera.org/articles/what-is-python-used-for-a-beginners-guide-to-using-python)
- [Why python is so popular - Youtube](https://www.youtube.com/watch?v=Y8Tko2YC5hA)

#### How do I use python?
- Download python here: [python.org](https://www.python.org/downloads/) 
- Setting up python: [Python 3 setup and installation guide - realpython](https://realpython.com/installing-python/)

### **Git**
#### What is Git?
- [What is Git? Git explained in 2 Minutes(Mosh on YouTube)](https://www.youtube.com/watch?v=2ReR1YJrNOM)
- [Learn Git in 15 Minutes(Colt Steele on YouTube)](https://www.youtube.com/watch?v=USjZcfj8yxE)

#### How do I use Git?
- Download git here: [git-scm](https://git-scm.com/downloads)
- Create a github account here: [github](https://github.com/) ([which one too is that?](https://www.howtogeek.com/180167/htg-explains-what-is-github-and-what-do-geeks-use-it-for/))
- setting up git

### **VS Code**
#### What is VS Code?
- [What is Visual Studio Code (Educba)](https://www.educba.com/what-is-visual-studio-code/)

#### How do I use VS Code?
- Download vscode here: [visualstudio](https://code.visualstudio.com/download)
- [Getting Started with VS Code](https://www.youtube.com/watch?v=S320N3sxinE)

### **Jupyter Notebook**
- [Getting started with Jupyter Notebooks in VS Code](https://code.visualstudio.com/learn/educators/notebooks)
- [Jupyter Notebooks in VS Code](https://code.visualstudio.com/docs/datascience/jupyter-notebooks)

### **How do I connect all these tools?**
- [Working with GitHub in VScode](https://code.visualstudio.com/docs/editor/github)(*You can end at the getting started section*)
- [Your first time with git and github](https://kbroman.org/github_tutorial/pages/first_time.html)
- [Getting Started with Python in VS Code(Read)](https://code.visualstudio.com/docs/python/python-tutorial)
- [Getting Started with Python in VS Code(Watch)](https://www.youtube.com/watch?v=E9U-EBG8jVk)


## **Setting up Local and Remote Repository**
- Create a folder on your local machine to keep your project
- Open vscode. Under the file section on the top navigation, click on open folder and navigate to where you created your folder. Click on *select folder* open to open it.
- Open git bash in VS Code ([how???](https://stackoverflow.com/questions/42606837/how-do-i-use-bash-on-windows-from-the-visual-studio-code-integrated-terminal))
- Open your github account
- Create a new repository here: [new](https://github.com/new) and name it
- Maintain all default settings. Scroll down and click on *Create repository*
- swicth back to the bash terminal in VS Code
- follow the instructions in the newly created repository by copying and pasting the first set of commands one after the other after the $ sign in your bash terminal. Press enter after pasting each set of command
- refresh your github repository after all the commands have been executed. You should see your readme file


## **Setting up Project environment**

### **Creating and setting up virtual environment**
- what is a virtual environment? [virtual environments for absolute beginners](https://towardsdatascience.com/virtual-environments-for-absolute-beginners-what-is-it-and-how-to-create-one-examples-a48da8982d4b?gi=cf29cc3b5855)
- navigate to your bash terminal in vscode and follow the instructions in the link above to create a new virtual environment(follow only part 2.2). Type the codes shown in bash
- in your bash terminal, type *python -m venv sales-env* to create a new virtual environment called sales-env
- in bash, type *echo "sales-env" > .gitignore*. This will create a gitignore([huh???](https://www.pluralsight.com/guides/how-to-use-gitignore-file)) file and add sales-env to the contents of the gitignore file. This will tell git not to include sales-env in the files/folders it's tracking. 
- in the right navigation of your terminal in vscode, select powershell from the list of options
- activate your virtual environment by typing *sales-env/Scripts/activate* in your powershell terminal
- when you execute this command on your windows computer, you are likely to receive this error ".../activate cannot be loaded because the execution of scripts is disabled on this system". This error appears because windows has blocked unsual scripts from running on your computer to protect your computer from malware and other attacks.
- to resolve this and enable the venv activation script to run, type *Set-ExecutionPolicy RemoteSigned -Scope CurrentUser* in your powershell terminal. ([source](https://stackoverflow.com/questions/4647429/powershell-on-windows-7-set-executionpolicy-for-regular-users))
- now try activating the venv again by typing *sales-env/Scripts/activate* in your powershell terminal 


### **Setting up folder structure and project files**
- in your bash terminal, type *mkdir data-exploration* to create a new folder called data exploration. This is the folder that will keep our data and all the files we will create to view, clean and analyze the data. You can alternatively create this folder directly on your local machine
- type *touch data-exploration/exploration.ipynb*. This will create a new jupyter notebook in the data-exploration folder where we will write codes to view, clean and analyze the data
- open the folder on your local machine and add the excel file that contains our raw data to this folder
- navigate back to bash in vscode and type *touch sales-dash-app.py*. This will create a new file named sales-dash-app.py which will contain the codes for creating the online analytics dashboard.
- in bash type *mkdir assets*. This will create a folder called assets which will contain files such as images, css styles([what???](https://blog.devmountain.com/what-is-css-and-why-use-it/)), etc., we will be using for our project
- create a separate folder for your images in the assets folder by typing *mkdir assets/images* in your bash terminal
- create the file which will contain your css codes in the assets folder by typing "touch assets/styles.css" in bash 
- under the explorer section in the left navigation in vscode, you should see your sales analysis folder. Under it, you should see these:
    - your assets folder, which also contains your images folder and your css file
    - your data-exploration folder which contains your excel data and jupyter notebook
    - your sales-env folder which contains all files and scripts needed to manage your environment
    - your .gitignore file
    - your readme file
    - your sales-dash-app file


## Updating your github repository with all these changes you have made
- in bash, type *git status*
- git will tell you all the untracked files which need to be added and committed
- to commit all these changes and push them to github follow these instructions:
    - use *git add file-name* to add a file to the staging area
    - use *git commit -m "commit message"* to commit a staged file
    - use *git push* to push commited files from local repository to remote repository
    - detailed explanation [here](https://www.earthdatascience.org/workshops/intro-version-control-git/basic-git-commands/)
- type *git status* again to see if all changes have been commited and pushed



***** If you have been able to follow up to this stage, you should now be fully set up to start coding !!! *****

## Before you Code - Installing packages
- make sure your venv has been activated by typing *sales-env/Scripts/activate* in your powershell terminal
- in your terminal type *pip install pandas*. This will install both numpy and pandas which we will use for data munging and mathematical and statistical operations on data.
- *pip install ipykernel*, which is an engine for running jupyter notebooks
- *pip install openpyxl* to read excel files