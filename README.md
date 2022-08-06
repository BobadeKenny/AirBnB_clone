# AirBnB clone
The goal of this project is to deploy a simple copy of the [AirBnB website](https://airbnb.com).
## Description
### The Console
This is the the entry point of the command interpreter to manage AirBnB objects. It is the first step towards the full web application and achieves the following functins:
* Puts in place a parent class (called BaseModel) to take care of the initialization, serialization and deserialization of your future instances
* Create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file
* Create all classes used for AirBnB (User, State, City, Place…) that inherit from BaseModel
* Create the first abstracted storage engine of the project: File storage.
* Create all unittests to validate all our classes and storage engine
## Installation
* Clone this repository
```bash
git clone https://github.com/BobadeKenny/AirBnB_clone.git
```
* Run the command interpreter
```bash
python console.py
```
## Usage
The console currently supports the following commands:
* EOF - Exit the program
* quit - Exit the program
* create - Creates a new instance of a class.
```bash
$ create BaseModel
```
* show - Prints the string representation of an instance based on the class name and id.
```bash
$ show BaseModel 1234-1234-1234
```
* destroy - Deletes an instance based on the class name and id.
```bash
$ destroy BaseModel 1234-1234-1234
```
* all - Prints all string representation of all instances based or not on the class name.
```bash
$ all BaseModel or $ all
```
* update - Updates an instance based on the class name and id by adding or updating attribute.
```bash
$ update BaseModel 1234-1234-1234 email "aibnb@mail.com"
```