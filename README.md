# You've stumbled upon a secret lab!

![](https://media.giphy.com/media/dwGQJX1OKzCSgc0QV2/giphy.gif)

Looks like you were getting a bit bored finishing up the lab extensions, so
we've got something a bit more fun for you to work on!

# What Are We Doing?

We're going to write a slack bot!  This bot can do whatever you want (within
reason).  It can read messages sent to our slack channel, and based on those
messages can send messages back to the channel.

We're going to do this somewhat in secrecy; we want to just put the bots into
the channel and see how the rest of the folks in class react!

If you want to bounce ideas off of someone, come find Anand.

## Ground Rules

1.  Only work on this after you've finished the lab you're supposed to get done
as well as all the extensions to the lab.  The reason you're here is to work the
curriculum that exists, this is for when you're done and still want more :)

2.  Pay attention to the lectures and other material in class.  This isn't an
excuse to ignore the teachers or other labs.  If we see this, we'll revoke the
bot token.

3.  Be nice.  We're going to be building a chat bot, which means it can talk on
the slack channel.  Which means it will be visible to all of your peers,
teachers, and staff.  If we see a rude, offensive, or mean bot, we'll stop this
entirely and nobody will get to have any more fun.  Don't ruin it!

4.  For simplicity, I'm going to share a bot token with you.  Treat that token
like a password; don't share it with others or post it anywhere.  Put it in your
code, but don't plan on checking your code in anywhere with the token.  Don't
make me regret this!  This is generally a bad practice, but setting up proper
key distribution for 2.5 weeks seems like a lot.

5.  Be creative!  Bots can do lots of cool things; they can be helpful, they can
be funny, they can be cryptic.  Use your imagination!  A couple random ideas
I've come up with are:
    - A bot that can help decide what category to use for concentration.
    - A bot that can come up with rules for the game "debugger".
    - A bot that tells lame jokes.

## Getting Started

To work on this bot, you'll need to do a couple things that are slightly
different to get your environment set up.

### Install pip
Pip is a python tool that helps install libraries that other people have made.  
We're going to use pip to install a tool called virtualenv (explained below).

To install pip, you will need to run the following commands:

1.  Download a file that can install Pip:
```shell
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
```
2.  Install Pip for our user:
```shell
python get-pip.py --user
```
3.  Make it so you can find pip when you try to run it:
```shell
echo "export PATH=$HOME/Library/Python/2.7/bin:\$PATH" >> $HOME/.bash_profile
```
4.  Close this terminal and open a new one.  Then verify pip is installed:
```shell
pip
```

You should have gotten some output telling you all the ways you can run pip.

### Install virtualenv
Since we'll be doing things like installing libraries, we could mess up our CSSI
environment.  Good news is there is a nifty tool called virtualenv that creates
a sandboxed environment so that we can do all the fun bot stuff without
affecting the main CSSI environment.

1.  Install virtualenv for our user
```shell
pip install virtualenv --user
```
2.  Verify that you have virtualenv installed:
```shell
virtualenv
```
You should have gotten some output telling you all the ways you can run virtualenv.

### Set up our virtual environment

1.  From your home directory, create the virtualenv for our bot:
```shell
cd ~
virtualenv cssibot
```

2.  Enter the virtual environment:
```shell
source cssibot/bin/activate
```

If this worked correctly, your terminal command prompt should start with
'(cssibot)'.  This means you are in the cssibot virtual environment.  If you
close your terminal and want to open another to work on this bot, you'll need to
re-run step 2.

### Install the SlackClient library and Websockets in our virtual environment

This will install a library that someone else wrote that helps us talk to slack:
```shell
pip install slackclient
pip install websocket_client==0.47.0
```

### Download the bot skeleton

Alongside this file, there is a cssibot.py file that provides a skeleton for a
bot that connects to slack and can read and send messages.  Download it and put
it in your cssibot directory.

### Replace SLACK_BOT_TOKEN, YOUR_NAME, YOUR_TRIGGER, and YOUR_CATCHPHRASE

The file has a constant called SLACK_BOT_TOKEN that needs to be a valid bot
token.  Ask Anand for the token.  He will also add you to a testing channel
where the bot is connected.  You can use that testing channel to run your bot
and talk to it without polluting the main slack channel.

Also, there is a YOUR_NAME variable that you should update with your name.
Since we are using a single test channel for everyone in the classroom, having
a unique way to turn your bot on and off helps clear the noise!

You can replace YOUR_TRIGGER with whatever word(s) you like.  You can replace
YOUR_CATCHPHRASE with whatever your personal catchphrase is. Whenever your bot
is on and sees that set of words (exactly), it will respond with the catchphrase
you set up below.

### Get Creative!

There are 2 functions you can fill in:
1.  `handle_direct_mention` is a function that will get called when the bot is
direct mentioned (i.e. @Bot).  The message is the part that follows after the
mention.
2.  `handle_regular_message` is a function that will get called whenever there
is a regular message to the channel.  The message is the whole thing that was
said.

### Test your bot!
Just like any other python application, run `python cssibot.py`.  Remember, you
need to be in the virtual environment you created above, so you may need to run
`source cssibot/bin/activate`.

This will run your bot in the testing channel and you should be able to talk to
it!

To turn your bot on, you'll need to send a message like
`@cssikirbottest YOUR_NAME On`.  To turn it off, `@cssikirbottest YOUR_NAME Off`

### Get it in the main channel

Just like real production code, we don't just let it run without review.  Call
Anand over and we'll chat about your code.  If it looks good, you'll send it
over to him and he'll put it on a server.
