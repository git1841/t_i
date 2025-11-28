

#!/bin/bash

while true; do
    python3 ses.py
    echo "Attente de 60 secondes..."
    sleep 60
    echo "recherche de double"
    python3 del.py
    echo "========"
done

