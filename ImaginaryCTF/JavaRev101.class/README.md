# JavaRev101.class
**Category:** Reversing
**Difficulty:** Easy

## Description
Are you ready to take your first course in Java reverse engineering?

## Solution
Decompile the class file (using e.g. Bytecode Viewer) and figure out that it xors the flag with a 2-byte key "\x42\x24", base64-encodes the result & compares it to a static string. base64-decode the static string and xor it with "\x42\x24" to get the flag. [https://gchq.github.io/CyberChef/#recipe=From_Base64('A-Za-z0-9%2B/%3D',true,false)XOR(%7B'option':'Hex','string':'4224'%7D,'Standard',false)&input=SzBjMlFqa1ZjUmQxZXlGV2NVQXJVREY3TlJRd1VDcDdja0lkUjNKUk1GZHhWejg9&oeol=VT](https://gchq.github.io/CyberChef/#recipe=From_Base64('A-Za-z0-9%2B/%3D',true,false)XOR(%7B'option':'Hex','string':'4224'%7D,'Standard',false)&input=SzBjMlFqa1ZjUmQxZXlGV2NVQXJVREY3TlJRd1VDcDdja0lkUjNKUk1GZHhWejg9&oeol=VT)