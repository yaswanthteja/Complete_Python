
# Table of Contents

- [Installation of Python](#installation-of-python)
- [Installation of Python in Windows](#how-to-install-python-on-windows)
- [Installation of Python on macOS](#how-to-install-python-on-macos)
- [Installation of  Python on Linux](#how-to-install-python-on-linux)

# Installing IDE's & Code Editors

- [Installing Vscode](#installing-vscode)
- [Installing Jupyter Notebook](#jupyter-notebook)
- [Other IdE and code editors](#other-ide-and-code-editors)

Installation of Python

Installing or updating Python on your computer is the first step to becoming a Python programmer.

This tutorial focuses on official distributions, as they’re generally the best option for getting started with learning to program in Python.

In this tutorial you’ll learn how to:

Check which version of Python, if any, is installed on your machine

- Install or update Python on Windows, macOS, and Linux
- Use Python on mobile devices like phones or tablets
- Use Python on the Web with online interpreters
- No matter what operating system you’re on, this tutorial has you covered. Find your operating system below and dive in!

## How to Install Python on Windows.

Python doesn’t come prepackaged with Windows.we should install python in our machine.

- To Install [python](https://www.python.org/downloads/) in windows
- go to python.org or [click here](https://www.python.org/downloads/)

Which Python Version Should You Use?
In general, you should just download and install the latest version of Python.
Click “Download Python 3.x.x.”

![image](https://github.com/yaswanthteja/100Days_of_Python/assets/93423367/b6f50d28-32b4-45fe-bb39-b6656ae6d2d8)

Download the file

- click on the download setup file.

![image](https://github.com/yaswanthteja/100Days_of_Python/assets/93423367/c083db62-f2d5-46b6-91cd-ff919d3bafba)

- On the first screen, enable the “Add Python.exe PATH” option and then click “Install Now.”
- Next, you have a decision to make. Clicking the “Disable path length limit” option removes the limitation on the MAX_PATH variable. This change won’t break anything, but will allow Python to use long path names. Since many Python programmers are working in Linux and other *nix systems where path name length isn’t an issue, turning this on in advance can help smooth over any path-related issues you might have while working in Windows.
- After the installation open your command promt or powershell or windows terminal  type in the following command and press Enter

```
C:\> python --version
Python 3.11.0
```

- Once if you see like this  python installed successfully.
- If you’re interested in where the installation is located, then you can use the where.exe command in cmd.exe or PowerShell:

```
C:\> where.exe python
```

- It will give you the location of python installation like this

```
C:\Users\mertz\AppData\Local\Programs\Python\Python37-32\python.exe
```

## How to Install Python on macOS

- Python 2 comes preinstalled on older versions of macOS. This is no longer the case for current versions of macOS, starting with macOS Catalina.
- There are two installation methods on macOS:

1. The official installer
2. The Homebrew package manager

- In this section, you’ll learn how to check which version of Python, if any, is installed on your macOS device. You’ll also learn which of the two installation methods you should use.

## How to Check Your Python Version on a Mac

To check which Python version you have on your Mac, first open a command-line application, such as Terminal.

Open your terminal

With the command line open, type in the following commands:

```
# Check the system Python version
$ python --version

# Check the Python 2 version
$ python2 --version

# Check the Python 3 version
$ python3 --version
```

If you have Python on your system, then one or more of these commands should respond with a version number.

## How to Install From the Official Installer

- Installing Python from the official installer is the most reliable installation method on macOS. It includes all the system dependencies needed for developing applications with Python.

-You can install from the official installer in two steps.

`Step 1: Download the Official Installer`
Follow these steps to download the full installer:

- Open a browser window and navigate to the Python.org Downloads page for macOS.
- Under the “Python Releases for Mac OS X” heading, click the link for the Latest Python 3 Release - Python 3.x.x. As of this writing, the latest version was Python 3.8.4.
- Scroll to the bottom and click macOS 64-bit installer to start the download.
- When the installer is finished downloading, move on to the next step.

`Step 2: Run the Installer`

- Run the installer by double-clicking the downloaded file. You should see the following window:

![image](https://github.com/yaswanthteja/100Days_of_Python/assets/93423367/a603e1c3-8bc6-4ce4-8b61-3aff6d6fd1c6)

### Follow these steps to complete the installation:

- Press Continue a few times until you’re asked to agree to the software license agreement. Then click Agree.
- You’ll be shown a window that tells you the install destination and how much space it will take. You most likely don’t want to change the default location, so go ahead and click Install to start the installation.
- When the installer is finished copying files, double-click the Install Certificates command in the finder window to make sure your SSL root certificates are updated.
- Congratulations—you now have the latest version of Python 3 on your macOS computer!

# How to Install Python on Linux

- There are two installation methods on Linux:

  - Using your operating system’s package manager
  - Building Python from source code
- In this section, you’ll learn how to check which version of Python, if any, is on your Linux computer. You’ll also learn which of the two installation methods you should use.

### How to Check Your Python Version on Linux

- Many Linux distributions come packaged with Python, but it probably won’t be the latest version and may even be Python 2 instead of Python 3. You should check the version to make sure.
- To find out which version of Python you have, open a terminal window and try the following commands:

```
# Check the system Python version
$ python --version

# Check the Python 2 version
$ python2 --version

# Check the Python 3 version
$ python3 --version
```

- If you have Python on your machine, then one or more of these commands should respond with a version number.
- For example, if you already had Python 3.6.10 on your computer, then the python3 --version command would display that version number:

```
$ python3 --version
Python 3.7.2
```

- You’ll want to get the latest version of Python if your current version is in the Python 2.X series or is not the latest version of Python 3 available, which was 3.8.4 as of this writing.

 What Your Options Are

- There are two ways to install the official Python distribution on Linux:

  - Install from a package manager: This is the most common installation method on most Linux distributions. It involves running a command from the command line.
  - Build from source code: This method is more difficult than using a package manager. It involves running a series of commands from the command line as well as making sure you have the correct dependencies installed to compile the Python source code.
- Not every Linux distribution has a package manager, and not every package manager has Python in its package repository. Depending on your operating system, building Python from source code might be your only option.

### Linux Installation Recommendations

The most popular way to install Python on Linux is with your operating system’s package manager, which is a good choice for most users. However, depending on your Linux distribution, Python may not be available through a package manager. In this case, you’ll need to build Python from source code.

- There are three main reasons that you might choose to build Python from source code:
- You can’t download Python from your operating system’s package manager.
- You need to control how Python gets compiled, such as when you want to lower the memory footprint on embedded systems.
- You want to try out beta versions and release candidates of the latest and greatest version before it’s generally available.
- To complete the installation on your Linux machine, find your Linux distribution below and follow the steps provided.

## How to Install on Ubuntu

Depending on the version of the Ubuntu distribution you run, the process for setting up Python on your system will vary. You can determine your local Ubuntu version by running the following command:

```
$ lsb_release -a
No LSB modules are available.
Distributor ID: Ubuntu
Description:    Ubuntu 16.04.4 LTS
Release:        16.04
Codename:       xenial
```

### Follow the instructions below that match the version number you see under Release in the console output:

- Ubuntu 18.04, Ubuntu 20.04 and above: Python 3.8 doesn’t come by default on Ubuntu 18.04 and above, but it is available in the Universe repository. To install version 3.8, open a terminal application and type the following commands:

```
$ sudo apt-get update
$ sudo apt-get install python3.8 python3-pip
```

- Once the installation is complete, you can run Python 3.8 with the python3.8 command and pip with the pip3 command.

## How to Build Python From Source Code

Sometimes your Linux distribution doesn’t have the latest version of Python, or maybe you just want to be able to build the latest, greatest version yourself. Here are the steps you need to take to build Python from source:

### Step 1: Download the Source Code

- To start, you need to get the Python source code. Python.org makes this fairly straightforward. If you go to the [Downloads page](https://www.python.org/downloads/source/), then you’ll see the latest source for Python 3 at the top. Just make sure you don’t grab Legacy Python, Python 2!
- When you select the Python 3 version, you’ll see a “Files” section at the bottom of the page. Select Gzipped source tarball and download it to your machine. If you prefer a command-line method, you can use wget to download the file to your current directory:

```
$ wget https://www.python.org/ftp/python/3.10.11/Python-3.10.11.tgz
```

- When the tarball finishes downloading, there are a few things you’ll need to do to prepare your system for building Python.

### Step 2: Prepare Your System

- There are a few distro-specific steps involved in building Python from scratch. The goal of each step is the same on all distros, but you might need to translate to your distribution if it doesn’t use apt-get:
- First, update your package manager and upgrade your packages:

```
$ sudo apt-get update
$ sudo apt-get upgrade
```

Next, make sure you have all of the build requirements installed:

```
# For apt-based systems (like Debian, Ubuntu, and Mint)
$ sudo apt-get install -y make build-essential libssl-dev zlib1g-dev \
       libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm \
       libncurses5-dev libncursesw5-dev xz-utils tk-dev

# For yum-based systems (like CentOS)
$ sudo yum -y groupinstall "Development Tools"
$ sudo yum -y install gcc openssl-devel bzip2-devel libffi-devel
```

- It’s fine if you already have some of the requirements installed on your system. You can execute the above commands and any existing packages will not be overwritten.
- Now that your system is ready to go, it’s time to start building Python!

### Step 3: Build Python

Once you have the prerequisites and the TAR file, you can unpack the source into a directory. Note that the following command will create a new directory called Python-3.8.3 under the one you’re in:

```
$ tar xvf Python-3.10.11.tgz
$ cd Python-3.10.11
```

Now you need to run the ./configure tool to prepare the build:

```
$ ./configure --enable-optimizations --with-ensurepip=install
```

- The enable-optimizations flag will enable some optimizations within Python to make it run about 10 percent faster. Doing this may add twenty or thirty minutes to the compilation time. The with-ensurepip=install flag will install pip bundled with this installation.
- Next, you build Python using make. The -j option simply tells make to split the building into parallel steps to speed up the compilation. Even with the parallel builds, this step can take several minutes:

```
$ make -j 8
```

Finally, you’ll want to install your new version of Python. You’ll use the altinstall target here to avoid overwriting the system Python. Since you’re installing into /usr/bin, you’ll need to run as root:

```
$ sudo make altinstall
```

It might take a while to finish installation. Once it’s done, you can verify that Python is set up correctly.

### Step 4: Verify Your Installation

Test that the python3.10 --version command returns the latest version:

```
$ python3.10 --version
Python 3.10.11
```

- If you see Python 3.10.11, then you’re all set!
- If you have some extra time on your hands, you can also run the test suite to make sure everything is working properly on your system.
- To run the test suite, type the following command:

```
$ python3.10 -m test
```

- You’ll probably want to find something else to do for a while, as your computer will be running tests for some time. If all the tests pass, then you can be confident that your brand-new Python build is working as expected!

# Installing IDE's & Code Editors

## installing Vscode

To install Visual Studio Code (VS Code) on Windows, you can follow these steps:

- Visit the official VS Code website: Go to the official website of [Visual Studio Code](https://code.visualstudio.com/)
- Download the installer: On the VS Code website, click on the "Download" button to download the installer based on your operating system.

![image](https://github.com/yaswanthteja/100Days_of_Python/assets/93423367/67ba499c-7f33-4b3b-891a-f55daf98e281)

- Run the installer: Once the installer is downloaded, locate the downloaded file (typically named "VSCodeSetup.exe") and double-click on it to run the installer.

![image](https://github.com/yaswanthteja/100Days_of_Python/assets/93423367/d1c6a56c-6de8-4073-a9cf-f899f86b5b02)

- User Account Control (UAC) prompt: If a User Account Control prompt appears, click "Yes" to allow the installer to make changes to your device.
- Select Installation Options: The VS Code installer will open. You can choose the installation location and select additional options according to your preference. By default, the recommended options are pre-selected, so you can proceed by clicking "Next".

![image](https://github.com/yaswanthteja/100Days_of_Python/assets/93423367/68de930c-24e2-4a0b-bc42-b9934004fd38)

- Select Start Menu Folder: Choose the folder where you want to create shortcuts for VS Code in the Start Menu. Click "Next" to continue.
- Additional Tasks: The installer may present additional tasks such as adding context menu options. Choose the desired options and click "Next".

![image](https://github.com/yaswanthteja/100Days_of_Python/assets/93423367/6bc44913-d6f2-4f3c-87d7-605d28f63a74)

- Start VS Code: Once the installation is complete, you can choose to launch VS Code immediately by keeping the checkbox "Launch Visual Studio Code" selected. Otherwise, you can uncheck it and manually launch VS Code later.

![image](https://github.com/yaswanthteja/100Days_of_Python/assets/93423367/f3e142f1-7c1f-49fe-9010-c40c3d4ed840)

- Finish the installation: Click the "Finish" button to complete the installation process.

![image](https://github.com/yaswanthteja/100Days_of_Python/assets/93423367/2a943918-9360-40a5-9d42-bd59ae3a01b5)

- This is what VS Code home page looks like.

![image](https://github.com/yaswanthteja/100Days_of_Python/assets/93423367/5d40ba8f-84ea-4519-88fd-8fb7cfb12b4a)

- After following these steps, Visual Studio Code should be successfully installed on your Windows machine. You can launch VS Code by locating it in the Start Menu or by double-clicking on the desktop shortcut if you chose to create one during installation.

### Extenstions

To run the python in VS Code smoothly, we need to install the Python extension provided by Microsoft. It offers IntelliSense (Pylance), linting, debugging, code navigation, code formatting, refactoring, variable explorer, test explorer and more!

To install it:

- First click the four dots menu on the left side called “Extensions”.

![image](https://github.com/yaswanthteja/100Days_of_Python/assets/93423367/fac6f2c6-f3c7-4dc9-8358-ed8580b1d71c)

- Then type Python in the search bar (it requires internet connection).
- Look for the Python by Microsoft.
- Click it and look on the right side for install button.
- Click on the install button.

![image](https://github.com/yaswanthteja/100Days_of_Python/assets/93423367/e0870407-0146-4d2a-9c20-456f24f9cb33)

### Jupyter Notebook

- Install the Python and Jupyter extensions
- I recommend using Visual Studio Code that way if you want to make .py files it's easy
- Code Cells, inline plots

Open VSCode and click on the "Extensions" button on the left side of the toolbar. Use the search bar to download the "Python" and "Jupyter" extensions from the marketplace.

![python Extentions](https://github.com/yaswanthteja/100Days_of_Python/assets/93423367/78e08a44-0138-44fc-96c6-11499f209b1b)

- Next, click on the “Explorer” located on the left side menu (top one).
- Next press Ctrl + Shift + P, it will open the Command Palette. The command palette is the option menu from where any functionality of VS Code can be set or altered.
  Next, type in the search “Select Interpreter”. Once it shows the option, click on it and wait for a few seconds.

![image](https://github.com/yaswanthteja/100Days_of_Python/assets/93423367/497ea80d-154c-4307-ace6-546b0eae6df1)

- After waiting for a few seconds, it will show all the available Python interpreters. Here in the below image it is showing the Python 3.9.7 as interpreter but in your case it may show other interpreter version numbers like Python 3.your installed python version number, so choose Python .your version no,here 3.9.7  this is the  installed version of python in my system it may differ to your  and we could utilize it to run Python codes.
- But occasionally, we need to create a separate environment for running Python, especially for a group project. Here comes the part called Python environment.

![image](https://github.com/yaswanthteja/100Days_of_Python/assets/93423367/1855d66d-819d-47f3-aaa1-3cfbcb7f2246)

## jupyter

![jupyter extenstion](https://github.com/yaswanthteja/100Days_of_Python/assets/93423367/45687ad7-29a2-4c17-8626-2cc87228826b)

## installing Juputer notebook in windows

- Install Jupyter using pip: Once Python is installed, open a command prompt or terminal and run the following command to install Jupyter Notebook using pip, which is a package manager for Python:

```python
pip install jupyter
```

- Launch Jupyter Notebook: After the installation is complete, you can launch Jupyter Notebook by running the following command in the command prompt or terminal:

```
python -m jupyter notebook
```

- This will start the Jupyter Notebook server and open a web browser window with the Jupyter Notebook interface.
- Create a new notebook: In the Jupyter Notebook interface, you can navigate to a directory where you want to create a new notebook and click on the "New" button to create a new notebook. You can choose either a Python 3 notebook or any other available kernels depending on your requirements.

## Other IdE and code editors.

you can install these also

- [Pycharm](https://www.jetbrains.com/pycharm/download/)
- [sublime](https://www.sublimetext.com/)
- vim

## Conclusion

Congratulations! You now have access to the latest version of Python and tools for your system. Your Python journey is just beginning.
