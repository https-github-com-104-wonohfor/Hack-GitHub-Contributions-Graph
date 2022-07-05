# Introduce
For anyone wants to have your contribution graph with lots of commit like a pro.
# Instruction
### 1. Required 
- Install Python: </a>
  <a href="https://www.python.org/downloads/">
    <img src="https://img.shields.io/badge/Python-3.10-blue" height="20" alt="Python"> 
  </a> (No need for the lastest version)

- GitHub account (of course, you can't push if you don't have 🙂)

- Make sure you linked GitHub with your code editors. Better if you have known how to push code to GitHub before. 

- Install Visual Studio Code:   <a href="https://code.visualstudio.com/download">
    <img src="https://img.shields.io/badge/Visual%20Studio%20Code-64bit-blue"> 
  </a> 
- Install Extensions in Visual Studio Code (VSC): (Click on "Extensions" in VSC or "Crtl+Shift+X" and install the folowing extensions)
  + GitHub Pull Request
  + Git Extension Pack
  + Gitignore
  + Pylance
  + Python
- Install Git: <a href="https://git-scm.com/downloads">
    <img src="https://img.shields.io/badge/Git-64bit-orange" height="20"> 
  </a>
  - Git "Log in", run this code in Terminal of VSC:
  ```
  git config --global user.name "your_username"
  git config --global user.email "your_email_address@example.com"
  ``` 
  - Then run:
  ```
  git init
  ``` 
  
 ### 2. Create new repository
 - Create your new repository (Public or Private is both ok) with a file "README.md". For example: Your new repository is named "github-graph"
 - Click on logo GitHub in VSC -> Log in your GitHub account -> Click on "Explorer" in VSC -> Click on "Clone Repository" -> Click link which linked to your new repository (For me is: github.com/account_name/github-graph.com)
 - Save your repository in any place in your computer/lap/PC.
 - Create in that file:
    + data.txt
    + Code.py
 - Copy the code below in "Code.py"
 ```
import os
import random



def make_commit(days: int):
    if days <1:
        return os.system('git push')
    else:
        dates = f'{days-random.randint(150,200)} days ago'
        with open('data.txt', 'a') as file:
            file.write(f'{dates}\n')
        os.system('git add data.txt')
        os.system('git commit --date="'+dates+'" -m"first commit"')
        return days * make_commit(days-1)

make_commit(40)
```
- Open Terminal(in VSC) and run code:
```
git config --global --add safe.directory 'your repo position'
```
  + For example, for me is:
  ```
  git config --global --add safe.directory 'H:/GitHub of 104/github-bot'
  ```

- Run terminal with code:
```
py Code.py
```
Done!!!

Note: You can do this many times to have more contribuitons in GitHub Graph.
- If you want to loop this code many times, you should add this code line:
```
os.system('py code.py')
``` 

# Advanced
- You can add contributions to your Graph on any days if you want. To do that, you need to change the code in "Code.py"
- For example, if you want to add contributions on "5th January 2022" (Today is 28th June 2022). Search gooogle:
- ![image](https://user-images.githubusercontent.com/104601534/176080258-203d8741-849a-417d-9537-edd5db6b7c33.png)
- Change the code at this line in file "Code.py"

-![image](https://user-images.githubusercontent.com/104601534/176080738-bff15cd0-6b20-4348-a761-3c060b45ed0b.png)

to 
```
dates = f'{days-175} days ago'
```
- Note: Days in code must be "-175" not "-174". For example, if you want to add contribuitons on the day which is 100 days ago, the code will be 
```
dates = f'{days-101} days ago'
```
- You can adjust cotributions on a day by changing the code at line "make_commit(40)" (the number "40" can be changed into any numbers you want)

# Delete the Contributions 
- All you need to do is delete that repository. 
