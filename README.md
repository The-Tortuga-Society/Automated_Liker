# Automated_Liker
Automated Telegram/Substack Liking




Notes:

There is a code snippet that you can use to automatically like a whole archive at once (the "Love Shack").
To use this, load the archive page for a given user, e.g. https://cb.substack.com/archive

Scroll to the bottom of that page so that all the links in the archive are fully loaded!

Hit F12 in either Firefox or Chrome to pull up the console. You may have to enable copy-and-pasting of code, though the browser will generally prompt you as to how to do this (typically by typing ALLOW PASTING or some similar message.

Then you can cut-and-paste the text from the autoLikeArchives.js file into the console command section. 
The function block function autoLikeArchives() is the code that tells your browser what to do, 
and then the last line of the file 
autoLikeArchives();
tells your the console to execute that code, which will then begin parsing through the page and automatically liking any page that you have not already liked.

Enjoy!