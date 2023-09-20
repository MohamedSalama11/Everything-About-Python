# Git is the most popular version control system in the world, version control system records the changes made to our code over time in a special database called repository
# version control system can fall into two categories :-
#   1- Centralized :- in a centralized system all team members connect to a central server to get the latest copy of the code and to share the changes with others.
#   2- Distributed :- in a distributed system every team member has a copy of project with his history on their machine so they can save snapshots of the project locally in their machine
#   git is a distributed system.
# Merging is all about bringing changes from one branch to another and there's two types of merges in git 1- fast-forward merges 2- 3-way merges. 

# Notes:- 
# 1- .gitconfig is the configuration file of git
# 2- to write the message of commiting in VSC just type git commit and will open the VSC to write the message you want.



#################################################### Git Commands ####################################################
# git --version or git -v                               => To know the version of git on your local machine.
# git command_name --help                                    => To get alot of informations on this command.
# git command_name -h                                        => To get a fast refresher on this command.
# git init                                              => To Create An Empty Repositery From Existing Project.
# git clone                                             => To Clone (Copy) The Project From Remote Repo (GitHub) To Local Repo (PC).
# git status                                            => Show You What Happens In Your Working Directory.
# git status -s                                         => similar to git status but show you less information.
# git add *                                             => To Add All The Files From Working Directory To The Staging Area.
# git add *.extension                                   => To Add All The Files With The Same Extension.
# git add .                                             => To Add The Entire Directory Recursively.
# git rm file.txt                                       => This Will Remove The File From The Working Directory And The Staging Area.
# git rm --cached -r file                               => To Remove The File From The Index Or The Staging Area.
# git mv file.txt                                       => This will aplly the changes to both the working directory and the staging area, we use it instead of mv unix command
# git ls-files                                          => To List The Files In The Staging Area.
# git restoer file.txt                                  => Will Undo The Changes In This File, It Will Take The Copy Of This File From The Staging Area To The Working Directory.
# git restore --staged filename filename...             => To Restore The Files From The Staging Area To The Working Directory
# git commit -m "Here The Message You Want To Write"    => To Add The Files From Staging Area To The Local Repo, m option stands for message.
# git commit -am "Here The Message You Want To Write"   => To Commit The Changes Without Adding Them To The Staging Area ( Never use this option unless you know 100% what you are doing ).
# git remote -v                                         => Show You The Remote Repo.
# git push origin main                                  => To Push The Changes From Local Repo To The Remote Repo.
# git pull origin                                       => To Pull The Changes From The Remote Repo To The Local Repo.
# git config -l                                         => To List All The Configuration Of Git.
# git help config                                       => To Open The Configuration Manual.
# git config --global user.email "The Github Email"     => To Show The Terminal My Email.
# git config --global user.name "Github Name"           => To Show The Terminal My Name.
# git config --global user.email                        => To Print The Email Name In The Config.
# git config --global user.name                         => To Print The Email Of The User In The Config Settings.
# git config -l --show-origin                           => To Show You Where The Configuration Comes From.
# git config --global --unset Config Name               => To Delete A Specified Configuration.
# git config --global --edit                            => To Change The Configuration With The Editor (VS).
# git config --global core.editor                       => To make the VSC the default editor for git.
# git config --global core.autocrlf true                => To handle line ending in windows, cr shortcut for carriage return, lf shortcut for line feeding.
# git config --global core.autocrlf input               => To handle line ending in mac or linux.
# git config --global diff.tool vscode                  => To make the VSC the default editor for diff
# ssh-keygen -t rsa -b 4090 -C "Here Your Gmail"        => To Create SSH Key.
# ssh -T git@github.com                                 => To Test The SSH Key.
# git push -u origin master                             => To Push The Changes From The Local Repo To The Remote Repo.
# git config --global alias.st status                   => To Create An Alias To The git status Command.
# git config --global alias.st                          => To Sh ow You The Command Alias.
# git branch Branch Name                                => To Create New Branch.
# git branch                                            => Show You All The Branches In The Local Repo.
# git checkout Branch_Name                              => To Go To The Branch You Want (Old Way).
# git switch Branch_Name                                => To Go To The Branch You Want ( New Way )
# git branch -d Branch_Name                             => To Delete Specified Branch.
# git branch -D Branch_Name                             => To Force Delete The Branch Even If There's Changes In The Branch.
# git checkout -b Branch_Name                           => To Create A New Branch And Go To It ( Old Way ).
# git swithc -C Branch_Name                             => To Create A New Branch And Go To It ( New Way ).
# git branch -m Old_Branch_Name New_Branch_Name         => To Rename An Existing Branch.
# git merge Branch_Name                                 => To Merge The Branch With The Main Branch.
# git branch --merged                                   => To see the merged branchs with the master.
# git branch --no-merged                                => to see the non merged branches with the master
# git stash                                             => To Put The Files In A Stash Until You Done With It (بتركنهم على جمب لعند ما تخلص التعديلات وبعدين ترجعم من الستاش وترفعهم)
# git stash pop                                         => To Restore The Files From The Stash ( Stash Box Also Deleted ).
# git stash apply                                       => To restore The Files From The Stash But The Stash Box Not Deleted.
# git stash list                                        => To Show You All Stashes.
# git stash save "The Message You Want"                 => To Put A File In Stash Box With Message.
# git stash pop/apply stash@{Id Number}                 => To Restore Any Specified File From The Stash.
# git stash drop                                        => To Remove Stash Box With Files Inside It.
# git stash show                                        => To Show You What Happened In The Stash.
# git stash clear                                       => Remove All The Stashes.
# git clean -n                                          => To Show You The Files You Would Removed.
# git clean -f                                          => To Remove All The Untracked Files.
# git log                                               => Show You All The Commits Or The History Of The Repo, sorted from the latest to the earliest, space to show more history, q to quit.
# git log --oneline                                     => This Show You A Short Summary Of The Commit.
# git log --reverse                                     => To Show You The Commits In Reverse Order
# git log --stat                                        => To See All The Files That Have Been Changed In Each Commit.
# git log --patch                                       => To See The Actual Changes In Each Commit.
# git log -3                                            => To Filter The History, -3 Means Show Me The Last Three Commits.
# git log --author="the_author_name"                    => To Filter The History With The Author Name.
# git log --after="2023-08-1"                           => To Filter The History With The Date, this means show me all the commits after this date.
# git log --before="2023-08-1"                          => To Filter The History With The Date, this means show me all the commits before this date.
# git log --grep="the_word"                             => This Means Show Me All The Commits That Contains the_word.
# git log filename                                      => This Means Show Me All The Commits On This File.
# git log master..branch_name                           => This means show me all the commits that are in branch_name and not in master 
# git reset --hard hashCommit                           => To Remove The Last Commit And Put The Pointer To The Specific Commit Hash You Enter
# git push origin main --force                          => To Force The Updates
# .gitignore                                            => To Ignore Files And Directories In The Working Project We Need First To Create .gitignore file
# Note: Put The Files And Directories You Want To Ignore In The .gitignore File
# Note: *.log => Means That It Will Ignore Any File Ending With The Extension .log
# Note: !FileName  => Means That Not Ignoring This Specified File
# git add -f filename                                   => Adding A File Even If It Was In The .gitignore file
# git tag                                               => To Show You All The Tags
# git tag tagName (v1.0)                                => To Name A Tag
# git push origin tagname(v1.0)                         => To Push The Tag To The Github
# git tag -a tagName -m "The Message You Want"          => To Create Unnotated Tag
# git tag -l "Tags You Want"                            => To List All The Tags
# git tag -d tagName                                    => To Remove A Tag Localy
# git push origin --delete tagName                      => To Remvoe A Tag Remotely
# git diff                                              => To see unstaged things.
# git diff --staged                                     => To see what we have in the staging area that's going to the next commit. 
# git diff branch_name                                  => To show you the changes between this branch and the master
# git show                                              => To see the changes of the last commit.
# git show ID                                           => To See The Changes We Commited.
# git show HEAD~steps                                   => To See The Changes We Commited, example git show HEAD~1 => this means one step after the head.\
# git ls-tree ID                                        => To show all the files in a commit in a tree form.
# git shortlog                                          => To Show The Contributors In This Repository.
# git blame file_name                                   => To show all the lines added to the flie_name and their authors.
# git blame -e file_name                                => To see the email of the author.
