# HomeTabs
  HomeTabs project helps you to organize bookmarks for web browsers (like a standart browser's home page, but cooler and more comfortable). Design of HomeTabs was inspiried by Mozilla Firefox startpage, i think this is the best way to organise bookmarks, but history of browsing saved on homepage - is bad idea.  
  
  HomeTabs don't collect and don't transfer any of your personal data!  
  
  *In plans: improve HomeTabs and add a lot of new interesting functions.*  
  
<p align="center">
<a href="/releases"><img src="https://img.shields.io/github/v/release/grildroid/HomeTabs?style=flat-square" alt="Github release Badge"/></a>
<a href="/license"><img src="https://img.shields.io/github/license/grildroid/HomeTabs?style=flat-square" alt="Github license Badge"/></a>
<a href="https://sourceforge.net/projects/hometabs/files/latest/download"><img alt="Download HomeTabs" src="https://img.shields.io/sourceforge/dt/hometabs.svg" ></a>
</p>
  
<p align="center">
  <a href="https://sourceforge.net/projects/hometabs/files/latest/download"><img alt="Download homeTabs" src="https://a.fsdn.com/con/app/sf-download-button" width=276 height=48 srcset="https://a.fsdn.com/con/app/sf-download-button?button_size=2x 2x"></a>
</p>
  
  ![HomeTabs example](https://user-images.githubusercontent.com/55492813/118639548-b1e40480-b7e0-11eb-8815-7f474b26a52d.png)
  
  **❤️ Come visit our Telegram channel with news about HomeTabs updates, some blog stuff and other @grildroid projects! ❤️**  
  
<p align="center">
<a href="https://t.me/grildroidcave"><img src="https://img.shields.io/badge/-Telegram%20channel-blue?style=for-the-badge&logo=Telegram" alt="Telegram Badge"/></a>
<a href="https://trello.com/b/mLLcO0iz/hometabs"><img src="https://img.shields.io/badge/-Trello-blue?&style=for-the-badge&logo=Trello" alt="Trello Badge"/></a> 
</p>

  ____
  
  Code should be a crossplatform (not tested on unix yet). So you can try to run main.py on Windows and Linux systems.
  
  * Systems: Windows 10  
  * Browsers: Google Chrome, Opera, Mozilla Firefox  
  
  
# Features
* Organize your bookmarks by positioning it
* Change an icon's for your bookmarks
* Privacy-aware (no unconfirmed user data collection)

![HomeTabs gif](https://user-images.githubusercontent.com/55492813/118640835-19e71a80-b7e2-11eb-9f4b-730701a526fe.gif)

# Getting Started (wow so simple)
\[Windows]
1. Run HomeTabs.exe
2. Open your browser and type in your address bar: 127.0.0.2 (you can check and change address in config.ini in HomeTabs main folder)
3. Enjoy ❤️

# Tips
*  On Windows you can replace ip address in address bar to domain name by editing hosts file.  
  *Example: 127.0.1.2  mycoolstartpage.net*  
  
*  On Windows you can add HomeTabs.exe or main.py files to autorun folder and load the HomeTabs startpage automatically with your system.

*  On Windows you can configure your HomeTabs app to make an app-server for your local network. Set the ip parameter in config.ini to local ip of your PC. Then try to connect from other devices to your HomeTabs. Remember about port, you should type it in adress bar if port not equal 80.  
  *Example ip value in config.ini: ip = 192.168.1.2*  
  *Example of url: http://192.168.1.2:8000*  
  **REMEMBER! Don't set port in config.ini that opened on your router! Your HomeTabs page may become visible to other users in Internet!**
  
* On Windows you can try to set the port value in config.ini to 80. Then you may try to open your HomeTabs page without typing a port value in URL.  
 *Example of url:  192.168.1.2*  
  
# Technologies
* Writed on Python3 language. Using modules: Flask, Sqlite3, flask-socketio.
* Uses Socket.IO (JS).
* Uses Font Awesome Free icons.
  
# License
  HomeTabs Copyright © 2021 grildroid  
  [Licensed under GNU General Public License v3 (GPL-3)](/LICENSE)  
