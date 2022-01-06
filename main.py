import os
import sys
import signal

signal.signal(signal.SIGINT, signal.SIG_DFL)

if __name__ == '__main__':
    import app
    sys.exit(app.main(1))