import os 

FILE = "/store/mc/RunIISummer20UL17MiniAODv2/GluGluHToGG_int_M125_13TeV-sherpa/MINIAODSIM/106X_mc2017_realistic_v9-v2/2520000/488497ED-7AF9-5A47-A000-36AD3E997BAD.root"
REDIRECTOR = "root://cms-xrd-global.cern.ch/"
COMMAND = "root -l %s%s"%(REDIRECTOR, FILE)
print("$",COMMAND)
os.system(COMMAND)

