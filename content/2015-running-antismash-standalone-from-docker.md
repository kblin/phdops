Title: Running antiSMASH standalone from Docker
Date: 2015-07-21 07:45
Category: Science
Tags: python, antiSMASH, docker, packaging
Slug: 2015-running-antismash-standalone-from-docker
Author: Kai Blin
Summary: A short guide for running antiSMASH from Docker

Introduction
------------

After a longer discussion about the pros and cons of Docker at this year's BOSC,
and a bit of complaining about the complexities of actually running docker [in a
recent blog post]({filename}/2015-on-overengineering.md), I have decided to try
this out for [antiSMASH](http://antismash.secondarymetabolites.org/).


Setup & Install
---------------

As this is a guide for running antiSMASH in [Docker](https://docker.com), make
sure to [install Docker](http://docs.docker.com/mac/started/) first. Because
Docker needs a Linux kernel to run, this works fastest on a Linux host with a
recent kernel, because then you can avoid the overhead of a virtual machine.
antiSMASH needs at least 8 GB of RAM, so make sure to provide that amount if you
go with a virtual machine.

To "install" antiSMASH, grab the wrapper shell script off our [Bitbucket
repository](https://bitbucket.org/antismash/docker/) and put it into your path
as an executable, like so:
```bash
mkdir ~/bin  # only needed if you don't have a bin directory in your $HOME
curl https://bitbucket.org/antismash/docker/raw/HEAD/standalone/run_antismash > ~/bin/run_antismash
chmod a+x ~/bin/run_antismash
```
If you had to create your ~/bin directory, you might want to log off and on
again to get ~/bin added to your path.

To check if everything works as expected, try running `run_antismash . .
--version`, you should see the antiSMASH version being printed, e.g. `antiSMASH
3.0.3`. On the first run of the script, this might take a while as docker will
need to download the container, and that's a couple of GB in size.
If you get an error like `run_antismash: command not found`, you need to
make sure the `run_antismash` script is in your path and executable. I'll
explain why you need to add the `. .` before the `--version` next.


Running antiSMASH
-----------------

The `run_antismash` wrapper script takes a number of parameters that will be
passed to antiSMASH after some further processing. Basically, you need to pass
the input file and the output directory, so both can be added to the container.
This is required, or the antiSMASH program running inside of the container
wouldn't be able to see the input file or write the output file anywhere you can
retrieve it. Additionally, any further parameters will be passed to antiSMASH
unchanged. So to recap, running antiSMASH works like this:
```bash
run_antismash /my/input/file.gbk /my/antismash/results --parameters --for --antismash
```

### Example: Get the antiSMASH version
The actual antiSMASH script doesn't need any input or output files to just print
the version, but the wrapper script will get sad if you don't provide those. So,
the way to get the antiSMASH version is:
```bash
run_antismash . . --version
```

### Example: List available command line options
Using the same trick as previously, we can get antisMASH to print available
command line options.
```bash
run_antismash . . --help
```

### Example: Run antiSMASH on _Streptomyces coelicolor_ with KnownClusterBlast
And finally let's run some real antiSMASH job. My input file is on the `/data`
drive, I want the result to go to my `~/as_results` directory. As parameters,
I'll just go with `--knownclusterblast` for now.
```bash
run_antismash /data/genomes/current/Bacteria/Streptomyces_coelicolor_A3_2/NC_003888.gbk ~/as_results --knownclusterblast
```

The output will be in `~/as_results/NC_003888`.

Wrapping up
-----------

All in all, I think this is a pretty nice way to get your feet wet with
antiSMASH, but I have a couple of things that I find a bit annoying about this
solution:

- Some funky dance in the in-container wrapper script is required to make the
  output be owned by the user calling the script.
- At the moment, the wrapper script doesn't allow to pass multiple input files.
- You always need to pass input and output directories to the wrapper script.
