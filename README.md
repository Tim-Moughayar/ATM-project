# ATM Project
**CIS 206 - Session 14**

## Directions
This branch includes a running atm that is connected to the Customer Console and Transaction modules.

- To run the ATM, run the "_main.py_" file.
- To run the tests for the atm file, run the "_atm.py_" file itself. We will probably put these tests in a separate file though.
- To view the draw.io diagram, go to https://app.diagrams.net/. Save to GitHub and open existing diagram. Then connect your GitHub acount with draw.io and then you should be able open, edit and save the file to the repo. 

## Changes

- I changed the file names to make it easier to import/connect them.
- Adjusted the Customer Console module so the **display()** method accepts the text as a parameter and displays that text; similar to how it works in the ATM's example source code. I believe having the **display()** method will make it easier for Bryan to incorporate the GUI, so he doesn't have to worry about **print()** functions scattered in other modules.
- The **read_menu_choices()** method in the Customer Console module now takes "menu options" as a parameter and displays those options. It also gets and returns the user's choice.
- The Transaction module currently has only one method which starts a transaction.
- I removed the "*bank_address*" variable from the atm class because it's an IP address to the bank, and we wouldn't be using that.
- The other variables like "*id*", "*place*", "*bank_name*" in the ATM class are only useful if we print out a receipt, so we may end up getting rid of those.
- I've added the proposed ERD for the SQL database needed to make the ATM work. Will upload new version if changes are adopted by the group.

## Suggestions

- When creating tests for a module, put the tests in a separate file, like what Frank did. 
- Make sure to start the test file name with "test" so we can run all test files together if need be. 
