import subprocess
import time

def AcceptFiles(input_file, output_file, error_file):
    fd_input = open(input_file, "r");
    print(fd_input)

    fd_out = open(output_file, "w")
    print(fd_out)

    fd_err = open(error_file, "w")
    print(fd_err)
    
    proc = subprocess.Popen(['wc'], stdin = fd_input, stdout = fd_out, stderr = fd_err)
    
    fd_input.close()
    fd_out.close()
    fd_err.close()

def StartProcessStatus(timeout, count = 0):
    while(count != 10):
        output = subprocess.check_output(["ps", "-A"])

        print(output)
        count += 1
        time.sleep(timeout)

def main():
    #input_file = input("Enter input file name:\n");
    #output_file = input("Enter output file name:\n");
    #error_file = input("Enter error file name:\n");
    timeout = eval(input("Enter timeout :\n"))
    count = eval(input("Enter count :\n"))
    #AcceptFiles(input_file, output_file, error_file);
    StartProcessStatus(timeout, 0);

if __name__ == '__main__':
    main()
