# Y2 robot arm simulator

## 432021 robot arm simulation project for the course CS-A1121 Ohjelmointi Y2
	-The program simulates a 2-dimensional robot arm with an arbitrary number of joints.
	- It allows for joint angle manipulation, moving objects and importing premade command programs.


## File and directory structure

	- Project source files can be found in /src. All code has been written by the author, allthough gui.py and the linked list implementation in arm.py and joint.py have been derived from earlier excercise rounds in the course (namely Robot and LinkedList excercises).
	- Supplementary documents may be found in /doc. This includes project plan, technical specifications and final documentation.

## Installation instructions

	- The program has been writen for python 3.7.4. Use earlier versions at your own peril.
	- The program makes use of PyQt5.

## User guide

	- The program is run by executing main.py in /src folder using python
	- As command line arguments, provide any amount of positive nonzero numbers (float), which determine the lengths between joints. A new joint is added for each number provided. At least one length must be provided.
	- If one would like to create an arm with joint lengths 50, 70 and 27.37 for example, one would first navigate to the /src folder, and then run the command "python main.py 50 70 27.37" without the quotation marks.

	- The program can also run imported command files. For import instructions, please read doc/Documentation.pdf
	- The repository contains 3 example programs in /example_command_files
		- armCommandsForTest.csv: which is used for unit testing
		- armCommandsDemo.csv: which demonstrates moving boxes around. For arm configuration, please see comments in the file.
		- armCommandsError.csv: an intentionally broken command file that demonstrates software behaviour when attempting to import an erroneous file.