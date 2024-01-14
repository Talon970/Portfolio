#! /bin/bash

# Warten auf Internetverbindung
while ! ping -c 1 -W 1 8.8.8.8; do
    sleep 1
done

firefox https://www.hackthebox.com/ https://chat.openai.com/c/9a2b1371-1a22-4a7f-849b-8caa39ffb855 https://pomofocus.io/ https://www.youtube.com/watch?v=eWLDAAMsD-c https://github.com/Talon970/python-html-css-javascript_basics https://leetcode.com/
