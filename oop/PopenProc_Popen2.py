import subprocess

print('\npopen2:')

proc = subprocess.Popen(['cat','-'], stdin = subprocess.PIPE, stdout = subprocess.PIPE)

stdout_value = proc.communicate(b'through stdin in to stdout')[0]
print(b'\t pass through', repr(stdout_value))

