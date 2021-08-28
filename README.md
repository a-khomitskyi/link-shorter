# Link-Shorter v1.0

## Table of contents
* [Description](#description)
* [Technologies](#technologies)
* [Work](#work)
* [Results](#results)
* [Installation](#installation)

## Description

This application helps to shorten a long link into a more readable form. The application uses Sqlite3 database to store and present information.

## Technologies

Project is developed with:
* Python version: 3.9.1
* Flask library version: 2.0.1
* Hashids library version: 1.3.1

## Work

When we go to the main page of the application we'll see this interface.


![img](https://user-images.githubusercontent.com/33322034/131228017-b2c0549e-8a4d-4f86-ba70-a2a87c59131e.png)
For successful execution, the user must enter a valid link which he wants to shorten the program.
![img_2](https://user-images.githubusercontent.com/33322034/131228024-f3d73fd1-18ae-4d17-b3b2-8e3a3d3f8e34.png)
User will be faced with this window when he'll write an incorrect link.
![img_6](https://user-images.githubusercontent.com/33322034/131228035-737b327d-197d-441c-b680-86424f973833.png)
When he'll send an empty line.
![img_4](https://user-images.githubusercontent.com/33322034/131228037-1bac0a86-8864-4e71-90de-b262e53d6fbb.png)
This is the statistics of this application. Here we can see all the short links and other additional fields, such as the number of clicks on this link and the date of their creation.
![img_7](https://user-images.githubusercontent.com/33322034/131228038-a69030a8-ec4a-4564-a9f7-5d7a930a4c96.png)
When we try to follow a non-existent short link, we will be greeted by this window.
![img_8](https://user-images.githubusercontent.com/33322034/131228042-45cb65e2-53e9-4419-a1f7-1d688fe5512b.png)

## Results
App deployed on Heroku:<br>
https://fierce-plains-78114.herokuapp.com/

## Installation

To run this project, install it locally using pip:
```
$ sudo pacman -S python git 
$ mkdir link-shorter && cd link-shorter
$ git clone https://github.com/a-khomitskyi/link-shorter.git
$ pip install -r requirements.txt
$ python app.py 
```
