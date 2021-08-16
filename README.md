# HomeTabs
  HomeTabs project helps you to organize bookmarks for web browsers (like a standart browser's home page, but cooler and more comfortable). Design of HomeTabs was inspiried by Mozilla Firefox startpage, i think this is the best way to organise bookmarks, but history of browsing saved on homepage - is bad idea.  
  
  HomeTabs don't collect and don't transfer any of your personal data!  
  
  In plans: *improve HomeTabs and add a lot of new interesting functions.*  
  
  * Systems: Windows 10, Linux
  * Browsers: Any (maybe except the Safari)
  * Not working on mobile browsers and OS's  
  
<p align="center">
<a href="https://github.com/grildroid/HomeTabs/releases"><img src="https://img.shields.io/github/v/release/grildroid/HomeTabs?style=flat-square" alt="Github release Badge"/></a>
<a href="/LICENSE"><img src="https://img.shields.io/github/license/grildroid/HomeTabs?style=flat-square" alt="Github license Badge"/></a>
<a href="https://sourceforge.net/projects/hometabs/files/latest/download"><img alt="Download HomeTabs" src="https://img.shields.io/sourceforge/dt/hometabs.svg" ></a>
</p>

<p align="center">
  <a href="https://sourceforge.net/projects/hometabs/files/latest/download"><img alt="Download homeTabs" src="https://a.fsdn.com/con/app/sf-download-button" width=276 height=48 srcset="https://a.fsdn.com/con/app/sf-download-button?button_size=2x 2x"></a>
</p>
  
  ![HomeTabs example](https://user-images.githubusercontent.com/55492813/118639548-b1e40480-b7e0-11eb-8815-7f474b26a52d.png)
  
<p align="center">
❤️ <b>Come visit the Discord channel with news about gToWbot updates, some blog stuff and other grildroid's projects!</b> ❤️
</p>

<p align="center">
  <a href="https://discord.gg/6ZGDgFjDVm" title="Join the discord!"><img src="https://img.shields.io/badge/Discord-7289DA?style=for-the-badge&logo=discord&logoColor=white" /></a>
  <!--<a href="https://t.me/grildroidcave"><img src="https://img.shields.io/badge/-Telegram%20channel-blue?style=for-the-badge&logo=Telegram" alt="Telegram Badge"/></a>-->  
  <a href="https://trello.com/b/mLLcO0iz/hometabs"><img src="https://img.shields.io/badge/-Trello-blue?&style=for-the-badge&logo=Trello" alt="Trello Badge"/></a>  
</p>

# License
  HomeTabs is a free opensource project!
  HomeTabs Copyright © 2021 grildroid  
  [Licensed under GNU General Public License v3 (GPL-3)](/LICENSE)  
  
# Features
* Organize your bookmarks by positioning it
* Change an icon's for your bookmarks
* Privacy-aware (no unconfirmed user data collection)

![HomeTabs gif](https://user-images.githubusercontent.com/55492813/118640835-19e71a80-b7e2-11eb-9f4b-730701a526fe.gif)

# Getting Started (wow so simple)
1. Run HomeTabs.exe
2. Open your browser and type in your address bar: http://127.0.1.1:8000 (you can check and change address in config.ini in HomeTabs main folder)
3. Enjoy ❤️

# Tips
* You can replace ip address in address bar to domain name by editing hosts file.  
  *Example: 127.0.1.1  mycoolstartpage.net*  
  
* You can set HomeTabs.exe or main.py files to autorun and load the HomeTabs startpage automatically with your system.
  
* On Windows you can try to set the port value in config.ini to 80. Then you may try to open your HomeTabs page without typing a port value in URL.  
  
# Technologies
* Writed on Python3 language. Using modules: Flask, Sqlite3, flask-socketio.
* Uses Socket.IO (JS).
* Uses Font Awesome Free icons.

