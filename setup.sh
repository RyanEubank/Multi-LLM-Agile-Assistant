#! /bin/bash

VIRTUAL_ENV=".project_env"

echo [*] Setting up Server project...

cd server

echo -e "[*] Checking for Virtual Environment.\n"

if [ ! -f "${VIRTUAL_ENV}/Scripts/activate" ]; then
    echo "[*] Virtual Environment not found, setting up project environment..."
    pip install virtualenv
    python -m venv ${VIRTUAL_ENV}

    if [ ! -f "${VIRTUAL_ENV}/Scripts/activate" ]; then
        echo [-] An issue with environment setup occurred.
        echo [-] Unable to setup Virtual Environment.
        exit 1
    fi

    echo [+] Virtual Environment: ${VIRTUAL_ENV} setup complete.
else
    echo -e "[+] Virtual Environment: ${VIRTUAL_ENV} found.\n"
fi

echo [*] Setting ${VIRTUAL_ENV} as active environment.
source ${VIRTUAL_ENV}/Scripts/activate

if [ $? -ne 0 ]; then
    echo [-] An issue activating environment has occurred.
    echo [-] Unable to finish setup.
    exit 1
fi

echo [*] Installing packages...

# This brings in these 2 modules and all their dependencies
pip install django & pip install langchain[llms]

if [ $? -ne 0 ]; then
    echo [-] An issue installing packages has occurred.
    echo [-] Unable to finish setup.
    exit 1
fi

echo [+] Packages Installed successfully.
echo -e "[+] Server files installed.\n"

echo [+] Finished server project setup...

cd ../client

echo [*] Setting up client app...

# Put setup for front end and React setup here...
echo [+] Packages Installed successfully.
echo [+] Client files installed.