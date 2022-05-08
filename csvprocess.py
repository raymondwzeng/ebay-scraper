import csv
import traceback

def processIntoCSV(dict, headerList, fileNameAndPath):
    try:
        with open(fileNameAndPath, 'w', newline='', encoding='utf-8') as newFile: #Write the new file and open it
            csv_writer = csv.DictWriter(newFile, fieldnames=headerList) #Initialize CSV Dictionary Writer, headerList as fieldnames
            csv_writer.writeheader() #Write the field names at the top
            for line in dict:
                csv_writer.writerow(line)
            print("Successfully wrote CSV File!")
    except KeyboardInterrupt:
        print("Keybord interrupted processing, exiting.")
        exit()
    except:
        print("Error while processing CSV: ")
        traceback.print_exc()

#Calculates the averages of certain parameters given a csv.
def calculateAverage(fileNameAndPath, parameters):
    try:
        with open(fileNameAndPath, 'r') as readFile:
            csv_reader = csv.DictReader(readFile)

            for line in csv_reader:
                
    except KeyboardInterrupt:
        print("Keybord interrupted processing, exiting.")
        exit()
    except:
        print("Error while processing CSV: ")
        traceback.print_exc()