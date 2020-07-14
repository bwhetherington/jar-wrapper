from subprocess import Popen, PIPE, STDOUT
import sys
import signal

JAR_FILE = sys.argv[1]


def start(process):
    args = sys.argv[2:]
    global process
    process = Popen(
        ['java', '--jar', JAR_FILE] + args, stdout=STDOUT, stderr=STDOUT, stdin=PIPE)


def handle_signal(signal, frame):
    print('SIGINT received; stopping server')
    output = process.communicate(input='stop'.encode())[0]
    print(output)
    process.wait()
    sys.exit(0)
