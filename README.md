**Steps to Run this project**

1) Python must be installed (use until Python 3.11. On Python 3.12 there's a bug already reported on their git page) and added to Enviroment variables on Path
2) Install the requirements by: pip install -r requirements.txt
3) Chromedriver installed
4) Open the terminal on the folder of the project and run:
   behave Frontend/features/login.feature -D browser=chrome 

parameters like:

-D browser=chrome 
-D headless=False 
-D mobile=False

Below is the image of the settings to do to use Behave runner instead by the terminal.
A second option to run the feature file
![img.png](img.png)
