import os
import subprocess

# This assumes the user has already added changes to the Index and committed them.
# All that is left should be to push the current changes in their private working directory,
# and then mirror the commit to a public repo

print("Pushing changes to private git respository.")
os.system('git push')

print("Sucessfully pushed to private git repository.")

print("Finding most recent changes...")
print()

command = ['git log']
text = os.popen("git log").read()

print(text)

print("Parsing recent commits...")


#os.chdir('..\\TestRepo\\')


#tmp = os.popen("git log").read()
#print(tmp)






#os.system('cd c:\\Users\\Benjamin\\Documents\\Development')
#os.system('git status')