################################################################### Linux Operating System ###################################################################

######### Linux File System ##########

## Notes ##
# 1- The Linux File System Follows A Tree-Like-Structure
# 2- /               => Is The Very Top (Root) Of The File Tree (Every Folder Is Under It)
# 3- /bin            => Stores Common Linux User Command Binaries like date, cal, cat Commands are in here
# 4- /home           => where the home dicrectories for regular users are stored  (/home/mohamed)
# 5- /root           => the home folder the root user or the super user
# 6- /sbin           => contains adminstrative commands (binaries) for the root user
# 7- /usr            => contains files that belongs to the user
# 8- .              => refers to the current directory
# 9- ..             => refers to the parent folder
# 10- Absolute paths => start at the base (/) dreictory
# 11- Relative paths => start from the current directroy
# 12- In linux file extenstions don't matter, the system looks to the contents of the file rather than his name, system looks to the header of the file rather than it's extension
# 13-


## Navigating the file system ##
# mohamed@VB:~$
#   mohamed => the name of the user
#   VB      => The virtual box
#   ~       => in the bash shell that telda (~) represents the home folder for the current user

# Commands
# 1- pwd   => print working directory

# 2- ls       => list the folders of the directory you are currently in == ls /home/mohamed == ls ~ == ls
# 3- ls -F    => will classify the folders and files ( folders will represents in blue color , files will represents in white color )
# 4- ls -l    => list the files in long format
# 5- ls -h    => list the files in human readable format  == ls --human-readable
# 6- ls -a    => list all the files including hidden ones
# 7- ls -f    => list all entries in directory order
# 8- ls -i    => print the index of each file and folder

# 9- cd       => By Default Will Take You To The Home Folder  == cd ~ == cd /home/mohamed
# 10- cd .    => refers to the crrent directroy
# 11- cd ..   => will take you to the parent folder of the folder you are currently in
# 12- file    => will till you the type of the file

## WildCards ##
# (*)         => Means Everything regardless of length
# Note that wildcards is case sensitive
# Examples
# 1- ls D*    => Will list any directroy starts with capital D letter
# 2- ls *     => will list every directroy and files
# 3- ls *.txt => will list every file ends with .txt

# (?)         => Means only one thing => it refers to only one character
# (??) refers to two character
# Examples
# 1- ls ?.txt  => means list everyfile ends with .txt but has only one character before the ? wildcard
# 2- ls ??.txt => means list everyfile ends with .txt but has only two characters before .txt

# ([])         => Similar to the ? wild card but it refers to only specific one character, matches just one place but allows you to specify options
# Examples
# 1- ls file[1-9].txt  => will list every file ends with .txt but only the ones who have number from 1 to 9 (file1.txt, file2.txt, file3.txt, file4.txt, file5.txt, file6.txt, file7.txt, file8.txt, file9.txt)
# 2- ls file[12].txt   => will list every file ends with .txt but only the ones who have number 1 or 2 (file1,.txt file2.txt)
# 3- ls file[A-Z].txt  => will list every file ends with .txt but only the ones who have letter from A to Z
# 4- ls file[1-9][A-Z][a-z].txt  => will list every file have this pattern (file11.txt, file1A.txt, file3c.txt)

## Creating Files And Directories ##
# note:- If you want to create a file or a folder with space between two words you should put the name between double quotes or single quotes "Mohamed Salama"
# 1- touch    => Creates Empty file
# 2- mkdir    => creates empty folder
# 3- mkdir -p => creates the entire folder path   example (mkdir /FolderNotExist/folder)

## Brace Expansion {} ##
# Example
# mkdir {jan,feb,mar,apr,jun,jul}{2010..2023}   => will create a bunch of folders with this pattern (jan2010,jan2011...jan2023, feb2010,feb2011...feb2023,....jul2010,jul2011..jul2023)
# touch {jan,feb,mar,apr,jun,jul}{2010..2023}/file{1..100}.txt  => this means in every folder of this create a 100 file from 1 to 100
# touch file{1,2,3} == touch file{1..3}         => will create these files (file1,file2,file3)


## Deleting Files And Folders ##
# rm  => delete files
# rmdir => delete empty directories
# rm -r => delete the folder and everything inside of it
# rm -i => will ask you before deleting (More Save)

## Copying Files And Directroies ##
# Syntax
# cp [the file you want to copy] ... [the destination]

# cp -r => means copy the folder and everything inside it

## Moving And Rename Files And Folders ##
# rename the file/folder if it's exists
# mv [old_name] [new_name]

## Editing Files With Nano ##
# Notes:-
# 1- you can create files with nano command
# 2- ^  => this symbol means CTRL on the keyboard
# 3- M- => stands for modify and it's alt key on the keyboard
# 4- Nano configuraton file located in /etc/nanorc
# 5- ./ means the folder you are currently in

## Finding Files/Folders ##
## The Locate Command ##
# the locate command searches a database for files and returns a list of results
# to avoid errors use --existing and --follow options
# best thing to do is just update the database (done automatically daily)
# Note:- when you locate some files with the locate command it's first looking for them in the database in this path /var/lib/plocate
# syntax
#   locate options [files you want to find]

# locate -i          => means locate without case sensitive
# locate --limit 3   => locate only 3 files
# locate -S          => To show you the database for the locate command
# locate -e or --existing => this means check if the files are existing in the database or not before printing them
# locate --follow    => to tell you if the symbolic links arrived in the right place
# sudo updatedb      => to update the database to give you more accurate results

## Find Command ##
# it does not need a database so it's always up to date and you do not need to update database, and it is more powerful than the locate command
# it is a bit slower than the locate command, locate is faster because it depends on a database
# the default behaviour of find command is it searches for every file/folder in the current directory and everything below it including hidden ones
# wc -l => will define the number of lines of the output

# Examples
# find /home/mohamed    => will list every single file and folder in mohamed and everything below it
# find -maxdepth input  => specify the depth of the searching  (find . -maxdepth 3)
# find -type            => specify the type f stands for file, d stands for directory  (find . -type f)
# find -name            => to search by name (find . -iname "file.txt",  i option here means case insensitive)
# find -size            => to search by the size (find / -size +100k -100k), (find / -size -10k -o size +5M)
# find -exec            => you can use the -exec option to execute another command on each of the results and remember to end the command with \;  (sudo find / -type f -size +100k -size -300k -exec cp {} ~/Desktop/copyFile \;)
# find -ok              => works the same as -exec but it is more save because it's ask you before doing anything

## Viewing Files ##
# cat   => it's stands for concatenate and it reads the content of the file
# Example
# cat file[1-5].txt > hello.txt == cat file{1..5}.txt > hello.txt    => will show the content of the five files and redirect it to hello.txt file

# tac   => read the content of the file in reverse (it's the backwards of cat command)
# rev   => read the content of the file in reverse but it's reverse each line horizontally
# less  => read the content of the file but it's more easier (let you scroll through large content)
# head  => it's useful command when you need to see just a piece of the content (by deafult will show you the first 10 lines)
# head -n input => will show you the number of lines you specify
# tail  => it works excatly like the head command but it's starts from the tail of the file

## Soring Data ##
# sort       => sort the data alphapitaclly from (a-z) (0-9)
# sort -r    => sort the data from (z-a)
# sort -n    => sort the numbres numercally (depends on the vlaue of the number)
# sort -u    => will remove dupliates
# sort -k    => this option can sort tabular data, sort by column (ls -l /etc | sort -k 5nhr)
# Example
# ls -lh /etc | head -n 20 | sort -k 6M  => will sort by column 6 and M here means sort by month

## Search File Content ##
# grep command will search what ever input you give it for lines that contain a particular piece text that you tell it to search for
# Syntax
# grep "what you are looking for" (the file)
# Examples
# grep -c "e" file.txt => will return the numbers of lines that contains the letter e
# grep -v "e" file.txt => will reverse the search (will search for the lines that doesn't have the letter e)
# grep -i "E" file.txt => -i means case insensitive
# ls =F /etc | grep -v / | sort -r > files.txt  => will list every file in the etc folder with classfication then search only for the files does not contain the / symbol and then sort files reversely from z-a and then but the files in the files.txt file

# File Archieving And Compression
# Archiving files is basically two step process:- 1- create a tarball  2- compress tarball
# we use tar command to create the tarball
# tarballs are containers to store files in for compression
# tar -cvf ourarchive.tar files => -c let the tar command know that we want to create a new archieve, -v tell the tar command to give us feedback (optional), -f let the tar command accept files
# Examples
# tar -cvf ourarchive.tar file[1-3].txt  => creat an archive for the file 1, file2, file3, ourarchive.tar is the archive name
# tar -tf ourarchive.tar => to see what is in the archive without extracting the data inside it, -t means test label and it basically lets you check what's inside tha tar file
# tar -xvf archive.tar   => to extract the files inside the archive, -x means execute the files

## Compression ##
# Compression happens using compression algorithms and there are two main compression alghorithms in use in the linux world (gzip, bzip2)
# gzip alghorithm is faster but has less compression power
# bzip2 has more compression power but does require more time
# Examples
# gzip archive.tar => compress archives with the gzip alghorithm
# gunzip archive.tar.gz => un compress the archive

# bzip2 archive.tar => to compress the archive with the bzip alghorithm
# bunzip2 archive.tar.bz2 => to uncompress the archive

# zip compression
# zip archive_name file1 file2... => to compress the files to zip
# unzip archive_name              => to unzip the archive

# examples
# tar -cvzf archive.tar.gz file1,file2...   => to compress the files in one step with gzip algorithm
# tar -cvjf archive.tar.bz2 file1,file2...  => to compress the files in one step with bzip2 alghorithm

# Note /dev/null => will delete any folder or file you redirect to it


########### Bash Scripts ###########
# best behaviour to create scripts is ( to run your scripts from anywhere in your system )
# 1- create a folder called bin in your home directory (all in lower case)
# 2- move all you scripts inside it
# 3- add execute permission to your scripts ( chmod +x script.sh )
# 4- add the /bin folder we created to the $PATH of the system which contians all the files that contains all the commands
# 4- edit the .bashrc file in your home directory (nano .bashrc)
# 5- in the end of the file write this command (PATH="$PATH:$HOME/bin")


## To create bash scripts ##
# 1- you need to create file ending with .sh
# 2- open the file and put this shabam as the first line #!/bin/bash  => this line tells the shell this is a bash file

## To create python scripts ##
# 1- you need to create file ending with .py (extensions doesn't matter in linux)
# 2- open the file and put this shabam as the first line #!/usr/bin/python3  => this line tells the shell this is a python file

# Note:- /dev/null   =>  is a place in the system called the bit bucket which basically deletes whatever is sent to it.
# Shortcut:- CTRL + k   => delete the line you are currently standing in

## Commands ##
# bash filename.sh   => to run the script
# cat script.sh      => to see the content of the script


##### Schedule Commands And Scripts Using cron #####
# cron is a command line program that is used to schedule tasks
# Each user has a cron tab which is basically is just a text file and each cron tab list which commands or scripts will be run automatically by that user and also list when they will be scheduled to be run
# every user has a crontab, this can be edited using crontab -e
# each crontab is broken up into rows, each row has 6 columns, first 5 columns is for scheduling information and the sixth column details which command or a script should be run at the schedule time
# The columns are m(0 to 59),h(0 to 23),dom(1,29),mon(1 to 12 or JAN,FEB),dow(0 to 6 or sat,mon)   command or script

# Commands
# crontab -e     => to edit the crontab of the user (choose 1 for nano because it is the easiest way)
# select-editor  => to change the editor later
# Note:- there is another way to change the editor => in your home directory edit the hidden file which is .selected_editor and put the path for the new editor
# * stands fon "Any"
# */15 means run every 15 (minutes,day)
# to schedule the scripts you need to write in the command section the following ( bash the path to your script )  => bash ~/bin/script.sh
