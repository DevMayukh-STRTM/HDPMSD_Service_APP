(C) 2020 Quantics, Inc. All Rights Reserved.

Java Module for HDPMSD(Windows) and Python Module

getting started:

code:

import org.pmsd;
class serv{
    public static void main(String args[])
    {
        pmsd a = new pmsd("process_name");
        //Writing a file:

        String file_contents = "Hello!\nThis is the content of the file we want";
        String dir = a.getcwd('myfile.text');
        String out = a.process("{\"write\": (\""+dir+"\"\""+file_contents+"\", 0)}");

        //this will create a new file
    }
}

all methods of pmsd:

.getcwd('additional_dir'): This method returns the current working directory and it
                           also concatanates the argument string with the CWD

.process('__function__'): This takes a simple json string which sends a function call
                          to the rest API.

.sessionBuilderParseMCode('json'): This takes a Mcode and return appropriate html code

.checkConnectionToApp(): Takes no argument, returns if connection is properly established or not
.switchServicePort(): Switches the process port

another interesting method is the processBuilder() method. This executes a shell command and
returns the output. Note: PMSD API must be running in background otherwise subprocess will not work

Connection To Database:

for this , we need to import using org.DBpmsd;

now start the Database Server Application and Connect the Process of the Database.

now using database query functions, efficiently connect to database and retrieve data on any 
language

PMSD makes your lives easier by simplifying tasks that are way too complicated on Java, or other languages.

Integrate Database with Fast IO operations and JSON processing, that is what I need for My ERP software,
Parallel ERP. This MSD runs automatically whenever windows boots up.

Discussing more possible hosts:

:Each app has seperate host name, with functions running multi-core on different Levels of core