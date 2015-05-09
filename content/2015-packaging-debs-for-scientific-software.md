Title: Packaging .debs for Scientific Software
Date: 2015-05-09 09:09
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

Initial setup
-------------

I'm doing all my builds in a directory called `/data/packaging/deb`. If you want
to go for something different, replace the paths accordingly. Now, I set up some
additional directories:
```shell
$ mkdir -p /data/packaging/deb/{jessie,trusty,pool}
```
Here, my jessie and trusty build files will go into the respective directories,
and the generated files will be put into pool.

Then I also configure pbuiler using `pbuilder-dist`.
```shell
$ pbuilder-dist jessie
# grab a coffee while the basic chroot is created
$ pbuilder-dist trusty
# grab another coffee
```

Updating existing packages
--------------------------

I'll pick `ncbi-blast+` for this example, because that was upgraded to 2.2.30 a
while ago, but both Debian and Ubuntu currently ship older versions.
As it turns out, there already is a version 2.2.30 package in Debian
experimental, so let's go to the [debian package
page](https://packages.debian.org/source/experimental/ncbi-blast+) and grab the
[upstream
tarball](http://http.debian.net/debian/pool/main/n/ncbi-blast+/ncbi-blast+_2.2.30.orig.tar.gz)
and [Debian's
changeset](http://http.debian.net/debian/pool/main/n/ncbi-blast+/ncbi-blast+_2.2.30-2.debian.tar.xz).

```shell
$ cd /data/packaging/deb
$ wget http://http.debian.net/debian/pool/main/n/ncbi-blast+/ncbi-blast+_2.2.30.orig.tar.gz
$ wget http://http.debian.net/debian/pool/main/n/ncbi-blast+/ncbi-blast+_2.2.30-2.debian.tar.xz
$ cd jessie
$ tar xf ../ncbi-blast+_2.2.30.orig.tar.gz
# create a symlink, the reason will be explained below
$ ln -s ../ncbi-blast+_2.2.30.orig.tar.gz ncbi-blast+_2.2.30~jessie.orig.tar.gz
$ cd ncbi-blast-2.2.30+-src
$ tar xf ../../ncbi-blast+_2.2.30-2.debian.tar.xz
```
Now we need to tweak a bit, because we want to build this for both jessie and
trusty, and we want to keep the debs in the same pool later on. So we'll go in
and cheat a bit and create .dsc files in two versions. One for jessie and one
for trusty. *Note*: This probably doesn't matter for NCBI blast+, but I'm doing
that with all packages for consistency's sake.

So, let's open the `debian/changelog` file and change the first line to
```
ncbi-blast+ (2.2.30~jessie-2) experimental; urgency=medium
```
Now, we can build the source package
```shell
$ debuild -S -us -uc
```

This is why we also created the symlink, so the debuild can find the tarball for
our modified version `2.2.30~jessie`. In the parent directory, this will end you
up with a file called `ncbi-blast+_2.2.30~jessie-2.dsc`.

We can now do the proper build using pbuilder:
```shell
$ cd /data/packaging/deb/jessie
$ pbuilder-dist jessie build ncbi-blast+_2.2.30~jessie-2.dsc --buildresult ../pool
```
Once this is done, rinse and repeat for trusty.



Creating python library packages from scratch, the easy way
-----------------------------------------------------------

The easy way to create deb from Python libraries is to simply use Jordan
Sissel's brilliant [fpm tool](https://github.com/jordansissel/fpm). This isn't
really cross-distribution-capable, but for pure python packages for python 2.7,
this currently works fine for jessie and trusty. fpm makes creating a debian
package as easy as
```shell
$ fpm -s python -t deb --iteration 1 straight.plugin==1.4.0-post-1
```
Note that I've picked a complicated example here, building `straight.plugin` in
exactly version `1.4.0-post-1`, as all other versions currently are broken for
me. In any case, this leaves you with a Debian package for your library in a few
seconds. Can't really beat that. As a bonus, creating RPMs with fpm is just as
easy, just replace the `-t deb` with `-t rpm`. You really can't go wrong with
fpm for stuff that you can easily package. Just don't mention this to Debian
packaging people, they get a bit agressive about people not doing things
"properly".

Creating "proper" python library packages from scratch
--------------------------------------------------------

Sometimes, unfortunately, you run into a more complicated library that fpm won't
handle, and then you have to do this the proper way.
I'm basing this section on the Debian [Python Library Style
Guide](https://wiki.debian.org/Python/LibraryStyleGuide), with my notes added,
as the library style guide is just some guide, not a step-by-step instruction
thing.

Let's use [pysvg](http://codeboje.de/pysvg/) as an example. Grab it from [PYPI](
https://pypi.python.org/pypi/pysvg/0.2.2). PYPI likes to give you zipfiles, for
packaging we need a tarball, but that also gives us the opportunity to rename
`pysvg` to `python-pysvg`, which conforms to the Debian way of naming things.
```shell
$ unzip pysvg-0.2.2.zip
$ mv pysvg-0.2.2/ python-pysvg-0.2.2
# Use XZ compression, modern Debian prefers that.
$ tar cJf python-pysvg_0.2.2.orig.tar.xz python-pysvg-0.2.2
$ mv python-pysvg-0.2.2 jessie
```
Now we need to create the `debian/` directory and all the related packaging
infrastructure. Fortunately, there's a package called `python-stdeb` that takes
care of a lot of that already. Once installed, it integrates with setuptools, so
we can use it from `setup.py`.
```shell
$ cd jessie/python-pysvg-0.2.2
$ python setup.py --command-packages=stdeb.command debianize
```
This has created a debian directory, but we need to adjust things a bit. First,
again fix `debian/changelog`. Use `dch` to edit it, and just delete the
autogenerated content the stdeb tool added and add your own changelog info.

We also need to create a `debian/copyright` file with licensing information. For
pysvg, the file looks as follows:
```
Files: *
Copyright: 2008-2012 Kerim Mansour
License: BSD

Files: debian/*
Copyright: 2015 Kai Blin
License: BSD

License: BSD
All rights reserved.

Redistribution and use in source and binary forms, with or without modification,
are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this
   list of conditions and the following disclaimer.
2. Redistributions in binary form must reproduce the above copyright notice,
   this list of conditions and the following disclaimer in the documentation
   and/or other materials provided with the distribution.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR
ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
(INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON
ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

The views and conclusions contained in the software and documentation are those
of the authors and should not be interpreted as representing official policies,
either expressed or implied, of the FreeBSD Project.
```

Now that this is out of the way, we can quicly create the `~jessie` tarball and
do the source package generation, followed by the proper pbuilder build.

```shell
$ ln -s ../../python-pysvg_0.2.2.orig.tar.xz ../pysvg_0.2.2~jessie.orig.tar.xz
$ debuild -S -us -uc
$ cd ..
$ pbuilder-dist jessie build pysvg_0.2.2~jessie-1.dsc --buildresult ../pool
```

Rinse and repeat for trusty.

To be continued
---------------
And as this blog post has grown huge already, I'll follow up with another one
about building debs from scratch for compiled packages soon.
