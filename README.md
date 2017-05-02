#  Movie Trailer Website

**About this program**  
This program generates an HTML file with posters and youtube trailer links to 9 different movies.  
media.py - class Movie is defined and initialized  
entertainment_center.py - contains 9 instances of the class Movie in a list. This list is used as an argument to call the fresh_tomatoes.py file  
fresh_tomatoes.py - generates an HTML page that displays posters of the movies in the list and a youtube trailer link to each movie.

**Pre-Requisites for running the program**  
This program is written in Python 2.7 and would run on this or a higher version.


**Steps to run the program**
- From the Github repository, download the below files on your machine
	- entertainment_center.py
	- media.py
	- fresh_tomatoes.py
- If Python IDLE installed, open the entertainment_center.py file and choos Run -> Run Module
- If Python IDLE not installed
	- open command prompt
	- run the command -> `python entertainment_center.py`

	
**Possible errors while running the program**  
System might not recognize the python command when you run the command in command prompt.  
Set environmental variables:  
System variables -> Advanced -> Environmental Variables  
Under user variables, if missing add a new variable called path and assign the below value  
C:\Python27;C:\Python27\Lib\site-packages;C:\Python27\Scripts  
PS: Please verify the paths from your actual folder where python is installed.  

Note: If you are unable to set the environmental variable, place the downloaded files for this program in the folder where python is installed on your machine.
