import sys
import os
import subprocess
import re

#def main():

#driectory of dataset for evaluation
dir = "/var/www/html/Timak/facenet/datasets/nas_dataset/evaluate"
test_folder = dir+"/Test"
content_test_folder = test_folder+"/*"
DEBUG = False
treshold = 0.5
image = sys.argv[1]

if(DEBUG):
	print("i will evaluate image:", image)
	print(dir)
	print(test_folder)
	print(content_test_folder)

os.system("rm -rf "+ content_test_folder)
#os.system("[[ -f "+sys.argv[1]+" >> /dev/null ]] || echo -1 ") #TODO overit ci subor existuje
os.system("cp -v "+image+" "+test_folder+" >> /dev/null")
#stara implementacia ale funguje a vypisuje vsetko
#os.system("python3 src/classifier.py CLASSIFY "+dir+" /var/www/html/Timak/facenet/models/20180402-114759/20180402-114759.pb /var/www/html/Timak/facenet/models/20180402-114759/my_classifier.pkl --batch_size 25")

command = "python3 /var/www/html/Timak/facenet/src/classifier.py CLASSIFY "+dir+" /var/www/html/Timak/facenet/models/20180402-114759/20180402-114759.pb /var/www/html/Timak/facenet/models/20180402-114759/my_classifier.pkl --batch_size 25"
output = subprocess.check_output(command, shell=True).decode('utf-8')
if (DEBUG):
	print(output)
data = re.search(' 0 (.+?)\n',output).group(0)
if (DEBUG):
	print(data)
meno, presnost = data.split(':')
meno = meno[4:]
presnost = presnost[1:]
if(DEBUG):
	print(meno)
	print(presnost)

if(float(presnost) > treshold):
	print(meno)
#		return(meno)
else:
	print("FUJ TO CO JE ZA KSICHT?")
