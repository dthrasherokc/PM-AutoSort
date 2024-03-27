# File Auto-Sorting Script

This Python script helps me organize my files & folders in Windows by automatically sorting files from a designated source folder into destination folders based on file types. I couldn't keep folders organized to save my life. So now I outsource it. Enjoy! 

# Features
 Automatic sorting of files and directories.
 Drag and drop support, paste friendly.
 Customizable source and destination folders through a JSON configuration file.
 Creates logs to debug any issues, but you're welcome to comment it out once you're comfortable for privacy reasons. 

# Prereqs
- Python 3.x

# Install
To set up the autosorting script on your local system, follow these steps:
1. Clone this repository to your local machine using:

  git clone https://github.com/dthrasherokc/PM-AutoSort.git
  cd PM-AutoSort 

  
# Config
Configure the script to directories of your choice:   
1. Open `config.json` with your favorite text editor. 
2. Set the `source_folder` to the directory you want to monitor.   #I have my source_folder on my desktop 
3. Define `destination_folders` and associate file extensions with corresponding folders. #I have these in my windows profile directory

# Usage
Execute the script from the command line or terminal:

Copy code
python autosort.py
The script will start monitoring the source_folder and sort new files into the appropriate destination_folders.

Feel free to fork the repository and submit pull requests to contribute to the project.
