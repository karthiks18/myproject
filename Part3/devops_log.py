##PROGRAM TO MONITOR LOGS AND FETCH ONLY THE ERROR IN LOG FILE. ALSO DISPLAY OUTPUT WITH TOTAL ERROR AND MESSAGES FOR THE SAME SESSION BEFORE THE ERROR.
import os
import string
#COUNT NUMBER OF LINES IN THE FILE
totalnumberoflines = len(open("K:\\github project\\users.txt", "r").readlines(  ))
print ('total number of lines in the log file is=',totalnumberoflines)
fileread = open("K:\\github project\\users.txt", "r")
#Defining the function
def search_string_in_file(fileread, string_to_search):
    line_number = 0
    string_to_search= "ERROR"
    list_of_results = []
# Open the file in read only mode
    with open("K:\\github project\\users.txt", 'r') as read_obj:
# Read all lines in the file one by one
        for line in read_obj:
# For each line, check if line contains the string
            line_number += 1
            if string_to_search in line:
# If yes, then add the line number & line as a tuple in the list
                list_of_results.append((line_number, line.rstrip()))
# Return list of tuples containing line numbers and lines where string is found
    return list_of_results
#Calling the function
matched_lines = search_string_in_file(fileread, 'ERROR')
string_to_search= "ERROR"
print('Total Error in logs : ', len(matched_lines))
for elem in matched_lines:
    N=3
    LineNumber = 0
    test_str = elem[1]
    sessionID = test_str.split () [N-1]
    print('# WARNING: Error ID', sessionID)
    matching_lines = [line for line in open("K:\\github project\\users.txt",'r').readlines() if sessionID in line]
    print (*matching_lines, sep='\n')
