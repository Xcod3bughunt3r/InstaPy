---
title: Home
hide_title: true
slug: /
---

<p align="center">
  <img src="https://i.imgur.com/sJzfZsL.jpg" width="154" />
  <h1 align="center">InstaPy</h1>
  <p align="center">Tooling that <b>automates</b> your social media interactions to "farm" Likes, Comments, and Followers on Instagram implemented in Python using the Selenium module.</p>
  <p align="center">
    <a href="https://github.com/Xcod3bughunt3r/blob/main/InstaPy/LICENSE">
      <img src="https://img.shields.io/badge/license-GPLv3-blue.svg" />
    </a>
    <a href="https://github.com/SeleniumHQ/selenium">
      <img src="https://img.shields.io/badge/built%20with-Selenium-yellow.svg" />
    </a>
    <a href="https://www.python.org/">
    	<img src="https://img.shields.io/badge/built%20with-Python3-red.svg" />
    </a>
    <a href="https://travis-ci.org/timgrossmann/InstaPy">
      <img src="https://travis-ci.org/timgrossmann/InstaPy.svg?branch=master" />
    </a>
    <a href="https://github.com/Xcod3bughunt3r/InstaPy#backer">
      <img src="https://opencollective.com/instapy/backers/badge.svg" />
    </a>
    <a href="https://github.com/Xcod3bughunt3r/InstaPy#sponsors">
      <img src="https://opencollective.com/instapy/sponsors/badge.svg" />
    </a>  
    <a href="https://discord.gg/FDETsht">
      <img src="https://img.shields.io/discord/510385886869979136.svg" />
    </a>
  </p>
</p>

[Twitter of InstaPy](https://twitter.com/Xcod3bughunt3r) | [How it works (FreeCodingCamp)](https://www.freecodecamp.org/news/my-open-source-instagram-bot-got-me-2-500-real-followers-for-5-in-server-costs-e40491358340/) | [Listen to the "Talk Python to me"-Episode](https://talkpython.fm/episodes/show/142/automating-the-web-with-selenium-and-instapy)


**Newsletter: [Sign Up for the Newsletter here!](http://eepurl.com/cZbV_v)**   
**Guide to Bot Creation: [Learn to Build your own Bots](https://www.udemy.com/course/the-complete-guide-to-bot-creation/?referralCode=7418EBB47E11E34D86C9)**     

<br />

## **Installation**
```elm
pip install instapy
```
__Important:__ depending on your system, make sure to use `pip3` and `python3` instead.

>If you would like to install a specific version of Instapy you may do so with:
>```elm
>pip install instapy==0.1.1
>```

#### Running Instapy

To run InstaPy, you'll need to run the **[quickstart](https://github.com/InstaPy/instapy-quickstart)** script you've just downloaded.

- [Here is the easiest **quickstart** script you can use](https://github.com/InstaPy/instapy-quickstart/blob/master/quickstart.py)  

- [And here you can find lots of sophisticated **quickstart** templates shared by the community!](https://github.com/InstaPy/instapy-quickstart/tree/master/quickstart_templates) 

You can put in your account details now by passing the username and password parameters to the `InstaPy()` function in your **quickstart** script, like so: 
```python
InstaPy(username="abcd", 
        password="1234")
```
Or you can [pass them using the Command Line Interface (CLI)](/additional-information#pass-arguments-by-cli).

Once you have your **quickstart** script configured you can execute the script with the following commands.

```elm
python quickstart.py
-- or
python quickstart.py --username abcd --password 1234
```

InstaPy will now open a browser window and start working.

> If want InstaPy to run in the background pass the `--headless-browser` option when running from the CLI   
Or add the `headless_browser=True` parameter to the `InstaPy(headless_browser=True)` constructor.

#### Updating InstaPy
```elm
pip install instapy -U
```

## Guides
#### Written Guides:
**[How to Ubuntu (64-Bit)](https://github.com/InstaPy/instapy-docs/blob/master/How_Tos/How_To_DO_Ubuntu_on_Digital_Ocean.md) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**

**[How to RaspberryPi](https://github.com/InstaPy/instapy-docs/blob/master/How_Tos/How_to_Raspberry.md) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**

**[RealPythons InstaPy Guide](https://realpython.com/instagram-bot-python-instapy/) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**

**[InstaPy : développez vous-même votre bot Instagram !](https://www.yubigeek.com/instapy-bot-instagram/) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**

## External Tools:

**[InstaPy Dashboard (Deprecated) ](https://github.com/converge/instapy-dashboard)**<a name="dashboard" />
> InstaPy Dashboard is an Open Source project developed by [@converge](https://github.com/converge/) to visualize Instagram accounts progress and real-time InstaPy logs on the browser.

**[InstaPy GUI](https://github.com/breuerfelix/instapy-gui)**<a name="gui" />
> InstaPy GUI is a Graphical User Interface including some useful Analytics developed by [@breuerfelix](https://github.com/breuerfelix).


## Docker
All information on how to use InstaPy with Docker can be found in the [instapy-docker](https://github.com/InstaPy/instapy-docker) repository.

## Support

### Do you need help?
If you should encounter any issue, please first [search for similar issues](https://github.com/Xcod3bughunt3r/InstaPy/issues) and only if you can't find any, create a new issue or use the for help.

### Do you want to support us?

<a href="https://opencollective.com/instapy/donate" target="_blank">
  <img hspace="11" src="https://opencollective.com/instapy/contribute/button@2x.png?color=blue" width="300" />
</a>

<br />

**Help build InstaPy!**      
Check out this short guide on [how to start contributing!](https://github.com/InstaPy/instapy-docs/blob/master/CONTRIBUTORS.md).

## Credits
### Community
An active and supportive community is what every open-source project needs to sustain. Together we reached every continent and most of the countries in the world!   
Thank you all for being part of the InstaPy community ✌️

![InstaPy reach](https://i.imgur.com/XkxHcM7r.png)

### Backers
Thank you to all our backers! 🙏 [[Become a backer](https://opencollective.com/instapy#backer)]

<a href="https://opencollective.com/instapy#backers" target="_blank"><img src="https://opencollective.com/instapy/backers.svg?width=890" /></a>

> **Disclaimer**<a name="disclaimer" />: Please Note that this is a research project. I am by no means responsible for any usage of this tool. Use on your own behalf. I'm also not responsible if your accounts get banned due to extensive use of this tool.
