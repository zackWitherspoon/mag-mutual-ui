# mag-mutual-ui

## Description:
This is the UI for the mag-mutual-tech-screening project. It's written in python since I haven't written in python in a while and wanted to try something new. It uses a module called streamlit.

## Setup:
I've tried to write specific instructions for running this project in Windows and and in Mac. 


###### Windows:
1. Install the latests python version
2. `py -m  pip install streamlit` (might be able to use `py -m pip install -r -requirements.txt` as well)
3. `py -m streamlit run .\main.py`


###### Mac:
1. Install the latests python version
2. `python3 -m pip install stramlit` (might be able to use `python3 -m pip install -r -requirements.txt` as well)
3. `python3 -m streamlit run .\main.py`

- Once streamlit has the application running you'll be asked to enter an email address. You can just hit `Enter` to skip this and it should open the UI.
- Next run the backend, see the README.md in the `mag-mutual-tech-screening` project to see how to run that project.
- Once both projects are running you are free to click the buttons in the UI to see your output. 

A clear button is mounted at the top of the page to clear out the tables if you don't want to see it anymore. Other than that feel free to poke around.
