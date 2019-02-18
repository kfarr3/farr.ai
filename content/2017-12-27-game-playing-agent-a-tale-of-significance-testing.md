Title: Game Playing Agent - A Tale of Significance Testing
Date: 2017-12-27
Category: Blog
Tags: AI, DataScience; Development; Math; Statistics;
Slug: game-playing-agent-a-tale-of-significance-testing
Status: published

![Robot with game pad]({static}/media/2017/robot_playing.png){ width=400px }

While I'm still writing up my review on Udacity's class on Inferential Statistics, I'm knee deep into their Artificial Intelligence Nano Degree program.  Our second project is to create a custom game playing agent for the simple Isolation game.  Isolation is played on a grid board (think chess/checkers) but of any n*m size.  For this game, our pieces were limited to moving in a chess-knight pattern.  Once a square has been occupied it can not be occupied again by either player, thus the goal is to isolate your opponent.  The loser is the first person who cannot make a legal move.

The game was implemented using minimax with alpha/beta pruning, a topic for another post.  Afterwards we were to also construct multiple 'scoring' algorithms that are used to determine which of the legal available moves are best.  Then there was a built-in tournament that allowed us to run multiple agents against each other to determine which scoring algorithm is best.  The idea here is the move that nets you more moves and your opponent fewer moves is probably better.

I crafted three such custom scoring algorithms and ran the tournament, results follow.

![Tournament Record Score]({static}/media/2017/tournament.png){.aligncenter .wp-image-257 .size-full width="637" height="272"}

# Results

WOW!  I'm amazing!  I took a 68.6% win rate up to 77.1%.  Color me impressed and dressed in my best.  If you're flashing back to my introduction, you're probably thinking there's more here though.  We're required to analyze and report the results.  Having just finished an inferential statistics class, that means t/z tests and critical regions!  YAY!  Actually, this was a really great opportunity to practice a bit of what I had learned outside of that perfectly structured learning environment.  So I popped open the Inferential Statistics course and refreshed on a few bits, calculated some t-tests and lo and behold.

![T-Test Results]({static}/media/2017/t-tests.png){.size-full .wp-image-260 .aligncenter width="651" height="124"}

# Testing

With a t-critical value of 2.179 (alpha 0.05, 2-tailed test and 12 degrees freedom) , we're not even close to being significant.  In fact, I constructed as perfect of a game as I could to get a t-test of -2.24, which WOULD be significant, and it required winning 85.7% of the games played.  Something none of these has come close to.  Interesting right?  This means that the custom scoring is more random sampling and happenstance than important.

# Files

* For those interested in the report [tournament analysis here.]({static}/media/2017/tournament-analysis.pdf)
* For those interested in the [raw tests here](https://docs.google.com/spreadsheets/d/1w-K3YhT9caZcVmskKKmg8G07X1Jdey9bv9hsrOAogEI/edit?usp=sharing)