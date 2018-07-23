# OutOfTheBlue
Just a little project using PiFM + Twilio

So the gist is this: you'll text in whatever song you want to play and this'll play it on the radio.

Will probably use youtube-dl and download whatever song people want played.

Requests will be added to a queue. You can't request something else until your first song gets out of the queue.

We probably won't have people constantly requesting songs, so previously requested songs will stay downloaded. When the request queue is empty, a queue will be loaded up with all downloaded songs.

There will be commands. !skip to vote to skip (not sure how to do vote threshold, maybe base it on number of songs in queue). !blacklist to vote to blacklist song. !clear to clear queue (admin). !stop to stop music (admin). !play to play music (admin). !shuffle to shuffle queue (admin).

Will probably have to use threads. I'm thinking a thread for playing music, a thread for downloading music, and a thread for listening for commands.
