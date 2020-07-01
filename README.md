# 0x00. AirBnB clone - The console
<p align="center">
  <img src="https://github.com/bdbaraban/AirBnB_clone/blob/master/assets/hbnb_logo.png" alt="HolbertonBnB logo">
</p>

<h1 align="center">HolbertonBnB</h1>
<p align="center">An AirBnB clone.</p>

## Command Sytax and Usage:

Command | Syntax | Output
------- | ------ | ------
help | `help [option]` | Lists all available commands, or displays what option does
quit | `quit` | Exit command interpreter
EOF | `EOF` | Exit command interpreter
create | `create [class_name]` | Creates an instance of class_name
update | `update [class_name] [object_id] [update_key] [update_value]` | Updates the key:value of class_name.object_id instance
show | `show [class_name] [object_id]` | Displays all attributes of class_name.object_id
all | `all [class_name]` | Displays every instance of class_name, if used without option displays every instance saved to the file
destroy | `destroy [class_name] [object_id]` | Deletes all attributes of class_name.object_id
count | `count [class_name]` | Counts all the instances with class name specified

### Using the Console

The HolbertonBnB console can be run both interactively and non-interactively. 
To run the console in non-interactive mode, pipe any command(s) into an execution 
of the file `console.py` at the command line.

```
$ echo "help" | ./console.py
(hbnb) 
Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  quit  show  update

(hbnb) 
$
```

## Testing :straight_ruler:

Unittests for the HolbertonBnB project are defined in the [tests](./tests) 
folder. To run the entire test suite simultaneously, execute the following command:

```
$ python3 unittest -m discover tests
```

Alternatively, you can specify a single test file to run at a time:

```
$ python3 unittest -m tests/test_console.py
```

## Authors :black_nib:
* **Oscar Andres Montes** <[Andmontc](https://github.com/Andmontc)>
* **Yesid A. López V.** <[Yesid4Code](https://github.com/Yesid4Code)>
