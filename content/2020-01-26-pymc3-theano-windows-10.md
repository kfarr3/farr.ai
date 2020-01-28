Title: Configuring pymc3 with Theano on Windows 10
Date: 2020-01-26
Category: Blog
Tags: DataScience; Development;
Slug: pymc3-theano-windows-10
Status: published

![pymc3 traceplot output, used as cover]({static}/media/2020/pymc3/1 pymc3_cover.png){ width=400px }

I've recently been experimenting more with pymc3's library for probabilistic programming, specifically Bayesian networks.  It was insanely slow and I was getting around 20/samples a second from a very benign `y=b1X1 + b2X1 + alpha` model.

![Slow Model Output From pymc3]({static}/media/2020/pymc3/2 slow_goings.png){width="100%"}

![Futurama Fry with text "No Bueno...."]({static}/media/2020/pymc3/no_bueno.jpg){style="margin: 10px" align="right" width="150"} Thinking this was just my slow machine, I kept going, until I put together a slightly more complicated model that I calculated would take hours to finish. No bueno. Running a sampler with 4000 samples at 20 samples/second is only 3.3 minutes, but my actual model is around 200k samples, which is around 2.7 hours.  I may be patient, but I'm not that patient.  So, like any good scientist, I investigate the warnings that I ignored when charging ahead with something new.

![No g++ Warning from Theano]({static}/media/2020/pymc3/3 no_gpp_warning.png){width="100%"}

# Install ming-gw-64

So, yes, the warning says it right there

> g++ not available, if using conda: `conda install m2w64-toolchain`

and

> g++ not detected ! Theano will be unable to execute optimized C-implementions

Got it.  I need to get a good known g++ compiler installed so it can build the libraries for my machine.  MinGW is short for *Minimalist GNU for Windows*, which is simply a *nix (Linux, Unix, etc) like environment for Windows.  Lots of details here that are not required to understand what's required though.  Now, you can get it from [mingw.org](mingw.org), but they don't provide 64-bit versions of their libraries.  One more search shows that the project FORKED years ago.  The above recommendation `m2w64-toolchain` specifies that Theano is wanting the 64-bit version of MinGW.

If you're running in conda you might as well just skip the rest and install it from conda.  That's the easy way, but I gave up on conda years ago due to lots of issues staying updated.  It's an amazing package manager, but as a somewhat more savy superuser (and super breaker) I often was trying to figure out how to get by conda instead of working with it.  For me, I run raw [`poetry`](https://python-poetry.org/).

So, conda out, needing 64-bit MinGW, go here: <http://mingw-w64.org/doku.php/download>

# Install Warning!

![Roby the Robot"]({static}/media/2020/pymc3/danger.jpg){style="margin: 10px" align="right" width="150"}
If, like me, you charge ahead with default options because there are way too many damn options in this world (also, shout out here for intelligently designed [Nudges](https://www.amazon.com/Nudge-Improving-Decisions-Health-Happiness/dp/014311526X), of which this was not one).  If you ended up like me with the following error and no speed improvements:

![Wrong g++ Warning from Theano]({static}/media/2020/pymc3/4 wrong_gpp.png){width="100%"}

>Exception: Compilation failed (return status=1): cc1plus.exe: sorry, unimplemented: 64-bit mode not compiled in.

WHAT?

Well, you unintentionally installed the `i686` version and not the `x86_64` version.

![MinGW x86_64 v i686 setting]({static}/media/2020/pymc3/5 setting_correct_gpp.png){width="50%"}

Change that, reinstall, re-update your path (which I didn't mention above, but yeah, you need to update your path to include the location of the MinGW bin directory, which for me was in: `C:\Program Files\mingw-w64\x86_64-8.1.0-posix-seh-rt_v6-rev0\mingw64\bin`.)  Additionally, between each path update you need to relaunch PowerShell.  There is a command you can run to reload it, but it's faster for me to just relaunch.

Once relaunched, if things are setup correctly you should finally have an extremely boring Theano message.

![Correct Theano message: Using NumPy C-API based implementation for BLAS functions]({static}/media/2020/pymc3/6 correct_theano.png){width="100%"}

>WARNING (theano.tensor.blas): Using NumPy C-API based implementation for BLAS functions

Gotta love a WARNING that's really an INFO.

Now to re-test my simple NUTS sampler and, viola, 2k samples per second.

![NUTS Sampler retest with 2k samples/second]({static}/media/2020/pymc3/7 correct_theano_build.png){width="100%"}

FIN.
