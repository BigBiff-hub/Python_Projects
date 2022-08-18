# finds email and phone numbers from a clipboard
import  pyperclip, re

phoneRegex  = re.compile(r'''(
                        ( \d{3}|\(\d{3}\))? #area code
                        (\s|-|\.)?
                        (\d{3}) 
                        (\s|-|\.)
                        (\d{4}) 
                        (\s*(ext|x|ext.)\s*(\d{2,5}))?)''', re.VERBOSE) #extention

emailRegex = re.compile(r'''
                        ([a-zA-Z0-9._%+-]+
                        @
                        [a-zA-Z0-9._%+-]+
                        (\.[a-zA-Z]{2,4})
                        )''', re.VERBOSE)