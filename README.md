# CSCE 670 Final Project - SteamRec

## About
SteamRec is a new recommendation system, featuring

- Generate highly personalized recommendations based on implicit feedback and explicit feedback signals

- Make recommendations based on game genres to help you narrow down your choices among over 200k Steam games.

- With intuitive user interface

## Approach

- New User: We randomly recommended games with "overwhelmingly positive" tag. In order to broaden the selection, we also randomly selected games from the entire dataset.

- Old User: 
    
    1. General Recommendation: Following the methodology outlined in the research paper  [*"Item Recommendation on Monotonic Behavior Chains"* by Mengting Wan, et al.](https://cseweb.ucsd.edu/~jmcauley/pdfs/recsys18b.pdf), we calculated users' preferences by combining their implicit and explicit feedback. Our model incorporated four types of feedback: purchase history, playtime, playtime exceeding 10 hours, and review.

    2. Genre Recommendation: We utilized the same four types of feedback to determine a user's genre preference. The more explicit feedback a user provided for a game, the higher the score we assigned to the corresponding genre. Based on this analysis, we made game recommendations tailored to a user's genre preference.

##  SteamRec User Interface

- New User
![](/image/new_user.png)

- Old User
![](/image/old_user.png)  

\
For further information about SteamRec, please refer to our website. [SteamRec](https://sites.google.com/tamu.edu/steamrec/home) .