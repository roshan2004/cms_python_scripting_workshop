import os 
import glob
import argparse
# Creating a parser
parser = argparse.ArgumentParser("This script parses amber mdout files to extract the total energy") # String description of what program does

parser.add_argument("filepath", help = "The filepath to the file to be analyzed") #Adding arguments, what to expect?

args = parser.parse_args()#Get arguments out of parser, list of what user inputs, pull out arguments, and store them

filename = args.filepath
f = open(filename, 'r')
data = f.readlines()
f.close()

print(f'Analyzing {filename}')

#03_Prod.mdout
#03_Prod_Etot.txt

# polyAT_vac.mdout
# polyAT_vac_Etot.txt

output_filename = os.path.basename(filename)
output_filename = output_filename.split('.')[0]
output_filename = f'{output_filename}_Etot.txt'

print(f'Writing output to {output_filename}')

f_write = open(output_filename, 'w+')
for line in data:
    if 'Etot' in line:
        f_write.write(f'{line.split()[2]}\n')
f_write.close()
print(f'Done analyzing {filename}')