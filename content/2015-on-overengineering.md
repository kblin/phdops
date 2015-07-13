Title: Thoughts on Overengineering Bioinformatics Analyses
Date: 2015-07-12 23:07
Category: Science
Tags: docker, galaxy, workflow, commonwl
Slug: 2015-on-overengineering
Author: Kai Blin
Summary: Some musings about the usefulness of workflow management systems, containers and other "hip" technologies for explorative bioinformatics

Last Friday and Saturday, I attended the [Bioinformatics Open Source Conference 2015
(BOSC2015)](http://www.open-bio.org/wiki/BOSC_2015). One topic that [came up a
lot](https://twitter.com/kaiblin/status/619899137404891136) was using [Docker](http://docker.io) to containerize all the
things.

A lot of software packages making use of Docker were brought up, more than I can remember right now. Apart from a couple
of standalone uses, it seemed like the platform of choice of a number of workflow managements. I feel like at least a
dozen of those were shown, leaving myself and others a bit confused on where to take all of this:

<blockquote class="twitter-tweet" lang="en"><p lang="en" dir="ltr">One nice thing about the existence of all these
pipeline systems is it has cured me of wanting to develop my own. <a
href="https://twitter.com/hashtag/bosc2015?src=hash">#bosc2015</a></p>&mdash; Michael Hoffman (@michaelhoffman) <a
href="https://twitter.com/michaelhoffman/status/619860543948652544">July 11, 2015</a></blockquote>

Amidst they general Docker and workflow management systems hype, there were some dissenting voices in the audience:

<blockquote class="twitter-tweet" lang="en"><p lang="en" dir="ltr">So this is why I don&#39;t feel I need to spend time
worrying about Docker, workflows, etc - data + scripts are good enough for now <a
href="https://twitter.com/hashtag/BOSC2015?src=hash">#BOSC2015</a></p>&mdash; Holly Bik (@hollybik) <a
href="https://twitter.com/hollybik/status/619824543595630592">July 11, 2015</a></blockquote>

I pretty much agree with Holly, and want to use this blog post to quickly explain my reasoning. I don't want to slam
Docker in general, I believe it has some space in trying out tools and possibly in deploying things on a cluster. I
would just argue that there is a huge middle ground between the "let's quickly try 5 assemblers off
[nucleotid.es](http://nucleotid.es)" and "and now run this on my 100-node-cluster" where VMs or
container-technology-_du-jour_ don't really add anything. Heck, even for assemblers I can pretty much "apt-get install"
the ones that have a sane OpenSource license, thanks to the fabulous Debian Med team's packaging work.

A local install makes life a lot easier, because then you can just run the command as given in the tool's manual,
without having to come up with a [44-line wrapper script](http://nucleotid.es/using-images/). Sure, you only have to
write the wrapper once per tool use, but if installing the tool is as easy as `apt-get install tool` or `brew install
tool`, why bother? I'm probably halfway through my analysis in the time it takes me to write a "run this in Docker while
mapping all the input and output files, then clean up Docker after running" script.

That's maybe my biggest criticism of Docker. Docker is great for serving standalone services that only need to interact
with the outside world using one port they listen on for HTTP traffic. Using docker to run a self-contained web server?
Really nice and easy: `docker run my/webservice -p 5000:5000 run_webservice.py`. Hardly more boilerplate to remember
than just running `run_webservice.py`, right? Oh, and then of course once you're done you need to remember `docker rm
<long id string>`, and I hope you noted down the ID before.

But let's go for something more complex now. Let's say I want to run an assembler. I need reads that the assembler can
read, and I need to write my output somewhere outside the container, so I get to keep it. So the command turns into
something like
```
docker run \
    --volume /path/to/output/dir/outside:/path/to/output/dir/in/container:rw \
    --volume /path/to/input/dir/outside:/path/to/input/dir/in/container:ro \
    --detach=false --rm \
    my/container /usr/bin/assembler --reads /path/to/input/dir/in/container/reads.fq.gz \
    --out /path/to/output/dir/in/container --other --options --here
```
compared to
```
assembler --reads /path/to/input/dir/outside/reads.fq.gz --out /path/to/output/dir/outside \
    --other --options --here
```

The docker version is not terrible, but it does add a lot of boilerplate that makes the command harder to read in the
history. And that brings me to another argument frequently brought up by the container crowd: _reproducibility_. The
idea is that with containers, you can always reproduce the analysis at some later timepoint. The implication is that
_only_ containers allow this with a reasonable effort. I see a couple of issues there:

- You still need to capture the command line when running the container
- You need to make sure you capture the version of the container you used
- If your analysis includes any sort of randomness, even now you don't get 100% reproducibility

That doesn't look too different from the steps needed to capture versions and command lines when just running your tools
without containers. As many bioinformatics tools can easily be statically linked, it's not too hard to keep binaries
working even if you update the basic system. Maybe containers might age a bit better in the long run, but I'm not
convinced yet. Containers are not cross-architecture, so if in the future we go to 128 bit architectures instead of 64
bit, or from x86 to ARM, our containers will not work anymore, just like a non-containerised tool.

The situation is even worse when we get into workflow management systems (WMS). As mentioned previously, at the moment
it feels like there's about a dozen WMS, all having a different focus, different priorities and different ways to define
your pipeline. The "common workflow language" was started at BOSC 2014 to solve this, but at the moment, there is a
distinct feeling of

[![standard proliferation](http://imgs.xkcd.com/comics/standards.png)](http://xkcd.com/927)

If you need to repeatedly run the same analyses, like in a core facility setting, you clearly want a pipeline. For
explorative analysis? I'm less convinced this is very useful.

Last but not least, I'm wondering who the audience is for this reproducibility, and how much of this is a very
theoretical scenario. It's a bit like code reuse. I very rarely see people ripping a random function straight out of a
piece of code to reuse it elsewhere. Is the goal to make sure referees can rerun your analysis to see if your claims are
supported by your data? In that case packaging everything up nicely _after_ having done the analysis might be great, you
could even bundle the data with that. Or is your goal to allow other people to build on your work? In that case, a
container might be too restrictive, and people will probably want to install your tool directly anyway.

To sum up, I can see the use for Docker for quickly testing something, and for shipping something with a low maintenance
bar. I don't see any particular "killer app" for using Docker in day to day research. I see no real gain at all for
investing time into a workflow management system, unless you're doing diagnostic analysis that is the same every time.
In a research context, it's probably a waste of time. Maybe once one of the WMS has emerged as a market leader, it's
worth another look.

<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>
