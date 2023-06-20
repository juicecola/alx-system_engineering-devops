Project 0x14: MySQL
This project focuses on setting up a Primary-Replica infrastructure using MySQL, creating backups, and performing database administration tasks. The goal is to gain a deeper understanding of database administration, web stack debugging, and MySQL installation.

Concepts
To successfully complete this project, you should be familiar with the following concepts:

Database administration
Web stack debugging
Installing MySQL 5.7
Resources
To accomplish the tasks in this project, you may find the following resources helpful:

What is a primary-replica cluster
MySQL primary replica setup
Build a robust database backup strategy
Learning Objectives
By the end of this project, you should be able to explain the following topics without relying on external sources:

General
The main role of a database
What a database replica is
The purpose of a database replica
Why database backups need to be stored in different physical locations
The operations required to ensure the effectiveness of a database backup strategy
Requirements
Allowed editors: vi, vim, emacs
All files must end with a new line
A README.md file at the root of the project is mandatory
All Bash script files must be executable
Bash scripts must pass Shellcheck without any errors
The first line of all Bash scripts should be exactly #!/usr/bin/env bash
The second line of all Bash scripts should be a comment explaining the script's purpose
UFW must allow connections on port 3306 (default MySQL port)
Tasks
0. Install MySQL
Install MySQL 5.7.x on web-01 and web-02 servers.
The command mysql --version should display the installed version.
The SSH configuration must be correctly set up for both servers.
1. Let us in!
Create a MySQL user named holberton_user on both web-01 and web-02 servers.
The user must have the host name set to localhost and the password projectcorrection280hbtn.
Grant holberton_user the necessary permissions to check the primary/replica status of the databases.
The SSH configuration must be correctly set up for both servers.
2. If only you could see what I've seen with your eyes
Create a database named tyrell_corp.
Create a table named nexus6 within the tyrell_corp database and add at least one entry to it.
Grant holberton_user SELECT permissions on the nexus6 table.
The SSH configuration must be correctly set up for both servers.
3. Quite an experience to live in fear, isn't it?
On the primary MySQL server (web-01), create a new user for the replica server.
The new user should be named replica_user with the host name set to %.
The password for replica_user can be any password.
Grant replica_user the appropriate permissions to replicate the primary MySQL server.
holberton_user must have SELECT privileges on the mysql.user table to check if replica_user was created with the correct permissions.
The SSH configuration must be correctly set up for both servers.
