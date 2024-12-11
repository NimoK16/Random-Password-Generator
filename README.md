# Random-Password-Generator
1. Our Goal

Creating a password using random characters in order to avoid predictability.                                                                    
Allowing user to specify length as well as characters to be used for password generation.

2. Importing Libraries

secrets: This library ensures random generation of characters.It provides better randomness, essential for sensitive passwords.

string: Contains predefined sets of characters:- 
        
        lowercase letters (ascii_lowercase)
        uppercase letters (ascii_uppercase)
        digits (digits)
        special characters (punctuation)

3. Character Pools

Set up characters into groups:-

Lowercase Letters: string.ascii_lowercase                                                                                                                                          
Uppercase Letters: string.ascii_uppercase                                                                                                                                               
Numbers: string.digits                                                                                                                                                              
Symbols: string.punctuation

4. Password Generation 

(a). Create character pools and conditionally add them.                                                                                                                           
(b). Combine all the selected character types into a single pool.                                                                                                             
(c). If no character type is selected or the length of password is out of range, make sure an error is raised.                                                                                                          
(d). Use a loop to generate the password by randomly selecting length characters from all_characters.                                                                             
          random.choice ensures the characters are picked randomly.

5. User Input

Input prompts the user and accepts input as a string.                                                                                                                                   
Logical checks like input(...) == 'y / n' determines if the user wants a specific character type or not.                                                                                 
The try/except block handles errors, such as when the user selects no character types.


