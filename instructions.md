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
- 
- 

#### How do I use Git?
- Download git here: [git-scm](https://git-scm.com/downloads)
- Create a github account here: [github](https://github.com/) ([which one too is that?](https://www.howtogeek.com/180167/htg-explains-what-is-github-and-what-do-geeks-use-it-for/))
- setting up git

### **Vscode**
#### What is Vscode?
- 

#### How do I use Vscode?
- Download vscode here: [visualstudio](https://code.visualstudio.com/download)
- 

### **Jupyter Notebook**
- what is jupyter notebook?
- installing jupyter notebook in vscode

### **How do I connect all these tools?**
- connecting github to vscode
- connecting local git installation to github
- using python in vscode
- using jupyter notebook in vscode


## **Setting up Local and Remote Repository**
- Create a folder on your local machine to keep your project
- Open vscode. Under the file section on the top navigation, click on open folder and navigate to where you created your folder. Click on *select folder* open to open it.
- Open git bash in vscode ([how???](https://stackoverflow.com/questions/42606837/how-do-i-use-bash-on-windows-from-the-visual-studio-code-integrated-terminal))
- Open your github account
- Create a new repository here: [new](https://github.com/new) and name it
- Maintain all default settings. Scroll down and click on *Create repository*
- swicth back to the bash terminal in vscode
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
- you are now set up to begin coding!!!


### **Setting up folder structure and project files**
- in your bash terminal, type *mkdir data-exploration* to create a new folder called data exploration. This is the folder that will keep our data and all the files we will create to view, clean and analyze the data. You can alternatively create this folder directly on your local machine
- open the folder on your local machine and add the excel file that contains our raw data to this folder
- navigate back to bash in vscode and type *cd data-exploration*. This will change your location in bash to the data-exploration directory(folder).
- in bash, type *touch exploration.ipynb*. This will create a new jupyter notebook where we will write codes to view, clean and analyze the data
- under the explorer section in the left navigation in vscode, you should see your sales analysis folder. Under it, you should see these:
    - your data-exploration folder which contains your excel data and jupyter notebook
    - your sales-env folder which contains all files and scripts needed to manage your environment
    - your .gitignore file
    - your readme file
