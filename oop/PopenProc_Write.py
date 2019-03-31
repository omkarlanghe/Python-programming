import subprocess

print('\nwrite')
proc = subprocess.Popen(['cat','-'], stdin=subprocess.PIPE)
proc.communicate(b'\tJay jay ram krishna hari to stdin\n')



