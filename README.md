## Getting Started with MANIM

**Prerequisites:**

* Windows operating system
* Administrative privileges

## Installation

**1. Install Chocolatey Package Manager:**

   - Open Windows PowerShell as an Administrator.
   - Run the following commands:

     ```powershell
      Set-ExecutionPolicy Bypass -Scope Process
     ```

     ```powershell
     Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('[https://community.chocolatey.org/install.ps1](https://community.chocolatey.org/install.ps1)'))
     ```

   - Verify installation: `choco -?`

**2. Install Python 3.7-3.10:**

   - Download from the official Python website (https://www.python.org/downloads/)
   - Run the installer and **ensure to add Python to PATH**.

**3. Install ffmpeg:**

   - Open an administrative PowerShell terminal and run:

     ```powershell
     choco install ffmpeg
     ```

**4. Install ManimCE:**

   - Open an administrative PowerShell terminal and run:

     ```powershell
     choco install manimce
     ```

**4. Install TinyTex:**

   - Open an administrative PowerShell terminal and run:

     ```powershell
     choco install tinytex
     ```

**5. Install LaTeX Packages:**

   - Open a command prompt or terminal and run:

     ```
     refreshenv
     tlmgr install amsmath babel-english cbfonts-fd cm-super ctex doublestroke dvisvgm everysel
     tlmgr install fontspec frcursive fundus-calligra gnu-freefont jknapltx latex-bin
     tlmgr install mathastext microtype ms physics preview ragged2e relsize rsfs
     tlmgr install setspace standalone tipa wasy wasysym xcolor xetex xkeyval
     ```

## Testing ManimCE

1. Save this file as `basic.py`.

2. Open a command prompt (cmd) in the directory where you saved `basic.py`.

3. Run the following command in the command prompt:

   ```cmmd
   manim basic.py SquareToCircle -pqm
