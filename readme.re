(C)2020 Kismotech, Inc. All Rights Reserved.

Hydrogen Database Parallel Micro Service Daemon or HDPMSD
is a small micro-Service that is the backbone of many
Softwares built on Java and need Essential IO operands and
JSON parsing. It provides additional Services like:

license checking
content management
plugins

functions of HDPMSD:

using java:

    import org.pmsd;
    class service {
        public static void main(String[] args){
            pmsd a = new pmsd("Parallel_CONTRARY_HOST");
            String json = "{\"name\": \"Mayukh\"}";
            String file_location = "C:\users\Mayukh\Desktop\Java";
            String desktop = "__WIN64__";

            int req = a.sendConnRequest("{\"write\": ("+json","+file_location")}");
        }
    }

How requests are send and recieved?
    Requests are transfered as HTTP, and send back as http.
    to access a function, we have to send a request to the app
    and a  json file, {"function_name": (//args)}

let's use the built-in console to access some functions

>>> connectApp("Parallel_CONTRARY_HOST")
>>> sendConnRequest({"read_from_file": ("file_name.txt")})

functions in HDPMSD:

{"writeFile": (__location__, __data__, __binary/text__)}
{"readFile": (__location__, __binary/text__)}
{"deleteFile": (__location__)}
{"filesize": (__location__)}


{"readJsonNode": (__json_data__, __NODE__)}
{"writeToJson": (__json_data__, __data__, __NODE__)}
{"deleteJsonNode": (__json_data__, __NODE__)}
{"getJsonSize": (__json_data__)}


{"readList": (__list_data__, __index__)}
{"writeList": (__list_data__, __data__)}
{"deleteListItem": (__list_data__, __index__)}
{"listsize": (__list_data__)}

