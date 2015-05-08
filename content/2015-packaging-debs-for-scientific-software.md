Title: Packaging .debs for Scientific Software
Date: 2015-05-08 09:09
Category: Dev
Tags: python, packaging, debian
Slug: 2015-packaging-debs-for-scientific-software
Author: Kai Blin
Summary: Manual on packaging .debs for scientific software

These are my notes for creating .deb packages, mostly for my future self for the
next time I need to do this. I'm putting them up here in case anybody else finds
this useful. Note that I'm trying to strike a balance between doing "proper"
debian packages that might eventually picked up by the [Debian
Med](https://www.debian.org/devel/debian-med/) community or Debian in general,
and getting stuff done quickly so I can do back to sciencing.

Some helpful ressources
-----------------------

There's some nice docs on Debian package building, but it's spread all over the
place, and some of it is outdated. Also, I've found that none of the articles
got me all the way to creating properly signed packages. Still, if you're
completely new to Debian packaging, you might want to have a look at [Building a
Debian Package](https://wiki.debian.org/BuildingAPackage) which explains how to
modify an existing package, and also at the [Intro to Debian
Packaging](https://wiki.debian.org/IntroDebianPackaging), which covers the
basics of creating a package from scratch. I will try to not repeat things in
this post that are covered in these two documents, but instead deal with the
things that I had to figure out the hard way over the last couple of days.

Supporting multiple distributions
---------------------------------

One of my main difficulties was that I wanted to easily support packaging for
both the current Debian stable release "jessie" (8.0) and the current Ubuntu
long term support (LTS) release "trusty" (14.04). When I have some time, I might
also want to build for the non-LTS Ubuntu release of the week, whatever that
happens to be at a given moment. What I didn't want was to set up a virtual
machine for every distro, because building on VMs is slow, and I'd have to
figure out how to get my packaging signing key onto the VMs. I've decided to go
with `pbuilder`, a build tool that utilises a `chroot`-based distribution
installs. Doesn't help with multiple architectures, but honestly, if you want to
run antiSMASH on your smartphone, you can build our ARM packages yourself. I'm
fine with just supporting x86\_64 at this point.

Publishing a Debian repository for apt
--------------------------------------

The main reason for creating Debian packages in the first place is to be able to
automaticall install them (and get updates) via apt. So in addition to figuring
out how to build debs, I also wanted to figure out creating a repository. The
Debian docs list a gazillion options, I ended up going with
[aptly](http://aptly.info), which has great docs, is easy to install and seems
to do all I need.

Updating existing packages
--------------------------

I'll pick `ncbi-blast+` for this example, because that was upgraded to 2.2.30 a
while ago, but both Debian and Ubuntu currently ship older versions.
**FIXME**: write more here.

Creating compiled packages from scratch
---------------------------------------
**FIXME**: write more here.

Creating python library packages from scratch
---------------------------------------------

I'm basing this section on the Debian [Python Library Style
Guide](https://wiki.debian.org/Python/LibraryStyleGuide), with my notes added,
as the library style guide is just some guide, not a step-by-step instruction
thing.


