#!/bin/bash

/bin/su -l -c "echo /usr/bin/python3 /opt/arm/arm/runui.py -d sr0 &" -s /bin/bash arm
/bin/su -l -c "echo /usr/bin/python3 /opt/arm/arm/runui.py -d sr1 &" -s /bin/bash arm
/bin/su -l -c "echo /usr/bin/python3 /opt/arm/arm/runui.py -d sr2 &" -s /bin/bash arm
