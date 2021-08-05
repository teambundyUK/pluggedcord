import time
import urllib.request
import zipfile
import os
import subprocess
import progressbar

print("\nPluggedcord Installer\n")
print("\n         # #                   # #        \n       # #     # # # # # # #     # #      \n     # # # # # # # # # # # # # # # # #    \n     # # # # # # # # # # # # # # # # #    \n     # # # # # # # # # # # # # # # # #    \n   # # # # # # # # # # # # # # # # # # #  \n   # # # # # # # # # # # # # # # # # # #  \n   # # # # #     # # # # #     # # # # #  \n   # # # #         # # #         # # # #  \n # # # # #         # # #         # # # # #\n # # # # # #     # # # # #     # # # # # #\n # # # # # # # # # # # # # # # # # # # # #\n # # # # # # # # # # # # # # # # # # # # #\n # # # # #     # # # # # # #     # # # # #\n     # # # #                   # # # #    \n       # # # #               # # # #")
print("\nWARNING: Powercord is technically against discords Terms of Service, you can learn more here: https://powercord.dev/faq")
print("Welcome to the Pluggedcord installer for powercord, it is used to make the installation of powercord much easier without having to use git, this is not an official part of powercord!")
print("\nCopyright 2021 TeambundyUK\nPermission is hereby granted, free of charge, to any person obtaining a copy of this software and\nassociated documentation files (the `Software`), to deal in the Software without restriction, including\nwithout limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell\ncopies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the\nfollowing conditions:\n\nThe above copyright notice and this permission notice shall be included in all copies or substantial\nportions of the Software.\n\nTHE SOFTWARE IS PROVIDED `AS IS`, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.\n\nWE DO NOT TAKE ANY RESPONSIBILTY FOR DAMAGE CAUSED BY THIS PROGRAM OR ANY PROGRAMS DOWNLOADED BY IT, BY CONTINUIG YOU ARE AGREEING TO THIS\n")
print("\nIMPORTANT: Powercord Requires You to Have Nodejs Installed For It To Function, make sure you have this before running the installer, you can download it here: https://nodejs.org\n")
input("\n[Press Enter To Start The Installation]")
print("Starting Powercord Download...")
with progressbar.ProgressBar(max_value=5, redirect_stdout=True) as bar:
    os.mkdir("PowercordInstallerTemp")
    bar.update(0)
    url = "https://github.com/powercord-org/powercord/archive/refs/heads/v2.zip"
    urllib.request.urlretrieve(url, "PowercordInstallerTemp/Powercord.zip")
    bar.update(1)
    print("Downloaded Powercord Repository!")
    userdir = os.environ['USERPROFILE']
    bar.update(2)
    print("Users Home Directory Is ", userdir)
    print("Extracting Powercord Code...")
    with zipfile.ZipFile("PowercordInstallerTemp/Powercord.zip","r") as zip_ref:
        zip_ref.extractall(str(userdir))
    bar.update(3)
    print("Extracted Powercord Code!")
    print("Renaming Powercord Directory...")
    renamestart = str(userdir) + "\powercord-2"
    powercorddir = str(userdir) + "\powercord"
    os.rename(renamestart, powercorddir)
    bar.update(4)
    time.sleep(2)
    print("Renamed Powercord Directory!")
print("\n========Manual Stage========\n")
print(f"-Now open Command Prompt And Run `cd {powercorddir}`,\n-After you have done this run `npm i`,\n-Finally run `npm run plug`\n")
input("[Press Enter When Finished]")
print("Killing Discord Canary...(RIP)")
os.system("taskkill /f /im  DiscordCanary.exe")
themetoggler = "https://github.com/redstonekasi/theme-toggler/archive/refs/heads/master.zip"
themeinstaller = "https://github.com/ploogins/PowercordThemeDownloader/archive/refs/heads/master.zip"
plugininstaller = "https://github.com/LandenStephenss/PowercordPluginDownloader/archive/refs/heads/master.zip"
input("\nWould you like to install recommended plugins for downloading powercord themes and plugins? [Press Enter]")
with progressbar.ProgressBar(max_value=7, redirect_stdout=True) as bar:
    urllib.request.urlretrieve(themetoggler, "PowercordInstallerTemp/themetoggler.zip")
    print("Downloaded Theme Toggler!")
    bar.update(1)
    time.sleep(0.5)
    urllib.request.urlretrieve(themeinstaller, "PowercordInstallerTemp/themeinstaller.zip")
    print("Downloaded Theme Downloader!")
    bar.update(2)
    time.sleep(0.5)
    urllib.request.urlretrieve(plugininstaller, "PowercordInstallerTemp/plugininstaller.zip")
    print("Downloaded Plugin Downloader!")
    bar.update(3)
    time.sleep(0.5)
    plugindir = str(powercorddir) + "\src\Powercord\plugins"
    print("Extracting all plugins...")
    bar.update(4)
    time.sleep(0.5)
    with zipfile.ZipFile("PowercordInstallerTemp/themetoggler.zip","r") as zip_ref:
        zip_ref.extractall(str(plugindir))
    bar.update(5)
    time.sleep(0.5)
    with zipfile.ZipFile("PowercordInstallerTemp/themeinstaller.zip","r") as zip_ref:
        zip_ref.extractall(str(plugindir))
    bar.update(6)
    time.sleep(0.5)
    with zipfile.ZipFile("PowercordInstallerTemp/plugininstaller.zip","r") as zip_ref:
        zip_ref.extractall(str(plugindir))
    bar.update(7)
    time.sleep(1)
    print("All Plugins Downloaded!")
print("You Can Now Run Discord Canary With Powercord Installed!")
input("[Press Enter To Close]")