from comtypes.client import CreateObject
from model.group import Group
import os
import random
import string
import getopt
import sys


#try:
#    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of groups", "file"])
#except getopt.GetoptError as err:
#    getopt.usage()
#    sys.exit(2)

#for o, a in opts:
#    if o == "-n":
#        n = int(a)
#    elif o == "-f":
#        f = a

n = 5
f = "groups.xlsx"

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

project_dir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
xl = CreateObject("Excel.Application")
xl.Visible = 0
wb = xl.Workbooks.Add()
xl.Range["A1"].Value[()] = "Names"
for i in range(n):
    xl.Range["A%s" % (i+2)].Value[()] ="%s" % (Group(name=random_string("name", 10)))
if os.path.isfile(os.path.join(project_dir, f)) is True:
    os.remove(os.path.join(project_dir, f))
wb.SaveAs(os.path.join(project_dir, f))
xl.Quit()










testdata = [
    Group(name=random_string("name", 10))
    for i in range(n)
]


#with open(file, "w") as out:
#    jsonpickle.set_encoder_options("json", indent=2)
#    out.write(jsonpickle.encode(testdata))