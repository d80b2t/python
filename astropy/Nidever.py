"""
astropy@scipy.org
AstroPy Digest, Vol 120, Issue 9

Today's Topics:

  1. astropy and photutils slow (David Nidever)
  2. Re: astropy and photutils slow (Stephen Bailey)
  3. Re: astropy and photutils slow (David Nidever)
  4. Re: astropy and photutils slow (Nathan Goldbaum)


----------------------------------------------------------------------

Message: 1
Date: Tue, 13 Sep 2016 12:05:36 -0700
From: David Nidever <davidnidever@gmail.com>
To: astropy@scipy.org
Subject: [AstroPy] astropy and photutils slow
Message-ID:
	<CAL6ZbBv8D4T=47Js2SHPT5gg64Ecjjqmftfdyxgst40TKJtvwQ@mail.gmail.com>
Content-Type: text/plain; charset="utf-8"

Hi all,

I'm pretty new to astropy and to python in general.  I've been trying out
some of the astropy and photutils photometry tools, but I'm finding that
they
are running pretty slow.  I wanted to double-check that I'm not doing
something
wrong.

Below is an example of running the astropy sigma clipped statistics routine
on a fake 2Kx4K image (since I'm working on DECam data).  This takes
almost 20s to run even though similar statistics using numpy take ~0.1s
or so.

import numpy as np
from astropy.stats import sigma_clipped_stats
im = np.random.rand(4096,2048)*10.0+100.0
timeit mean, median, std = sigma_clipped_stats(im, sigma=3.0, iters=5)
1 loop, best of 3: 18.9 s per loop

It seems like it might be the use of the numpy masked array module that is
slowing things down.  Just using the masked array median versus the
normal numpy median takes ~30x longer.

timeit np.median(im)
10 loops, best of 3: 109 ms per loop

timeit np.ma.median(im)
1 loop, best of 3: 2.71 s per loop

I'm finding similar speed issues with the photutils routines (e.g.
background2D)
that I believe also use masked arrays.

Is there something I can do to speed things up?

Thanks!
David

-- 
Dr. David Lee Nidever
Survey Data Scientist, NOAO
950 N. Cherry Ave.
Tucson, AZ 85719
(520) 318-8368
-------------- next part --------------
An HTML attachment was scrubbed...
URL: <https://mail.scipy.org/pipermail/astropy/attachments/20160913/dd33e5d7/attachment-0001.html>

------------------------------

Message: 2
Date: Tue, 13 Sep 2016 13:17:18 -0700
From: Stephen Bailey <stephenbailey@lbl.gov>
To: Astronomical Python mailing list <astropy@scipy.org>
Subject: Re: [AstroPy] astropy and photutils slow
Message-ID:
	<CAMCHcTpgGk0XMKcm2f_n_6Qxw2F2mBt+SR9XtQkn22u1KJQD0Q@mail.gmail.com>
Content-Type: text/plain; charset="utf-8"

What version of numpy and astropy do you have?  (numpy.__version__ and
astropy.__version__).

As another data point, using numpy/1.11.1 and astropy/1.2.1 I get much
faster results than you:

On Tue, Sep 13, 2016 at 12:05 PM, David Nidever <davidnidever@gmail.com>
wrote:

Hi all,

I'm pretty new to astropy and to python in general.  I've been trying out
some of the astropy and photutils photometry tools, but I'm finding that
they
are running pretty slow.  I wanted to double-check that I'm not doing
something
wrong.

Below is an example of running the astropy sigma clipped statistics routine
on a fake 2Kx4K image (since I'm working on DECam data).  This takes
almost 20s to run even though similar statistics using numpy take ~0.1s
or so.

import numpy as np
from astropy.stats import sigma_clipped_stats
im = np.random.rand(4096,2048)*10.0+100.0
timeit mean, median, std = sigma_clipped_stats(im, sigma=3.0, iters=5)
1 loop, best of 3: 18.9 s per loop


1.84s per loop for me.  Still slow, but not 18.9s.


It seems like it might be the use of the numpy masked array module that is
slowing things down.  Just using the masked array median versus the
normal numpy median takes ~30x longer.

timeit np.median(im)
10 loops, best of 3: 109 ms per loop


103 ms for me; i.e. this isn't just that I have a super fast machine and
you have a super slow one.


timeit np.ma.median(im)
1 loop, best of 3: 2.71 s per loop


104 ms for me.  i.e. with numpy 1.11.1 I don't see a radical difference
between masked array or not.

Stephen



I'm finding similar speed issues with the photutils routines (e.g.
background2D)
that I believe also use masked arrays.

Is there something I can do to speed things up?

Thanks!
David

--
Dr. David Lee Nidever
Survey Data Scientist, NOAO
950 N. Cherry Ave.
Tucson, AZ 85719
(520) 318-8368

_______________________________________________
AstroPy mailing list
AstroPy@scipy.org
https://mail.scipy.org/mailman/listinfo/astropy


-------------- next part --------------
An HTML attachment was scrubbed...
URL: <https://mail.scipy.org/pipermail/astropy/attachments/20160913/f65a6a52/attachment-0001.html>

------------------------------

Message: 3
Date: Tue, 13 Sep 2016 14:47:40 -0700
From: David Nidever <davidnidever@gmail.com>
To: Astronomical Python mailing list <astropy@scipy.org>
Subject: Re: [AstroPy] astropy and photutils slow
Message-ID:
	<CAL6ZbBsugWkGjV0MAXA14+g42cPQ_KmFhbaKew1h-k=JiG0jxA@mail.gmail.com>
Content-Type: text/plain; charset="utf-8"

Hi Stephen,

This is what I had:

In [7]: np.__version__
Out[7]: '1.8.0rc1'

In [10]: astropy.__version__
Out[10]: u'1.2.1'

and I'm using python 2.7.

I upgraded to the newest version and I'm finding a similar
performance to what you showed.

Thanks!
David


On Tue, Sep 13, 2016 at 1:17 PM, Stephen Bailey <stephenbailey@lbl.gov>
wrote:

What version of numpy and astropy do you have?  (numpy.__version__ and
astropy.__version__).

As another data point, using numpy/1.11.1 and astropy/1.2.1 I get much
faster results than you:

On Tue, Sep 13, 2016 at 12:05 PM, David Nidever <davidnidever@gmail.com>
wrote:

Hi all,

I'm pretty new to astropy and to python in general.  I've been trying out
some of the astropy and photutils photometry tools, but I'm finding that
they
are running pretty slow.  I wanted to double-check that I'm not doing
something
wrong.

Below is an example of running the astropy sigma clipped statistics
routine
on a fake 2Kx4K image (since I'm working on DECam data).  This takes
almost 20s to run even though similar statistics using numpy take ~0.1s
or so.

import numpy as np
from astropy.stats import sigma_clipped_stats
im = np.random.rand(4096,2048)*10.0+100.0
timeit mean, median, std = sigma_clipped_stats(im, sigma=3.0, iters=5)
1 loop, best of 3: 18.9 s per loop


1.84s per loop for me.  Still slow, but not 18.9s.


It seems like it might be the use of the numpy masked array module that is
slowing things down.  Just using the masked array median versus the
normal numpy median takes ~30x longer.

timeit np.median(im)
10 loops, best of 3: 109 ms per loop


103 ms for me; i.e. this isn't just that I have a super fast machine and
you have a super slow one.


timeit np.ma.median(im)
1 loop, best of 3: 2.71 s per loop


104 ms for me.  i.e. with numpy 1.11.1 I don't see a radical difference
between masked array or not.

Stephen



I'm finding similar speed issues with the photutils routines (e.g.
background2D)
that I believe also use masked arrays.

Is there something I can do to speed things up?

Thanks!
David

--
Dr. David Lee Nidever
Survey Data Scientist, NOAO
950 N. Cherry Ave.
Tucson, AZ 85719
(520) 318-8368


AstroPy mailing list
AstroPy@scipy.org
https://mail.scipy.org/mailman/listinfo/astropy



_______________________________________________
AstroPy mailing list
AstroPy@scipy.org
https://mail.scipy.org/mailman/listinfo/astropy




-- 
Dr. David Lee Nidever
Survey Data Scientist, NOAO
950 N. Cherry Ave.
Tucson, AZ 85719
(520) 318-8368
-------------- next part --------------
An HTML attachment was scrubbed...
URL: <https://mail.scipy.org/pipermail/astropy/attachments/20160913/df00bb35/attachment-0001.html>

------------------------------

Message: 4
Date: Tue, 13 Sep 2016 17:14:26 -0500
From: Nathan Goldbaum <nathan12343@gmail.com>
To: Astronomical Python mailing list <astropy@scipy.org>
Subject: Re: [AstroPy] astropy and photutils slow
Message-ID:
	<CAJXewO=pa3_XRntenzSd6gT_PzLoYAxC5Pngg9OBixtfqzgxMA@mail.gmail.com>
Content-Type: text/plain; charset="utf-8"

Hi David,

On Tue, Sep 13, 2016 at 4:47 PM, David Nidever <davidnidever@gmail.com>
wrote:

Hi Stephen,

This is what I had:

In [7]: np.__version__
Out[7]: '1.8.0rc1'


This version indicates to me that you're using the Apple system python
(e.g. /usr/bin/python on OSX). I want to strongly encourage you to avoid
using the system python, since it's possible to actually break the
operating system by using it.

In addition, the apple system python in particular has a number of
questionable aspects (including a pre-release version of Numpy 1.8.0 out of
the box is one example) and this leads to a number of weird issues that can
be avoided by simply not using it.

Instead, try to install python from a package manager like homebrew or
macports or use a self-contained python environment from e.g. Anaconda.

-Nathan


In [10]: astropy.__version__
Out[10]: u'1.2.1'

and I'm using python 2.7.

I upgraded to the newest version and I'm finding a similar
performance to what you showed.

Thanks!
David


On Tue, Sep 13, 2016 at 1:17 PM, Stephen Bailey <stephenbailey@lbl.gov>
wrote:

What version of numpy and astropy do you have?  (numpy.__version__ and
astropy.__version__).

As another data point, using numpy/1.11.1 and astropy/1.2.1 I get much
faster results than you:

On Tue, Sep 13, 2016 at 12:05 PM, David Nidever <davidnidever@gmail.com>
wrote:

Hi all,

I'm pretty new to astropy and to python in general.  I've been trying out
some of the astropy and photutils photometry tools, but I'm finding that
they
are running pretty slow.  I wanted to double-check that I'm not doing
something
wrong.

Below is an example of running the astropy sigma clipped statistics
routine
on a fake 2Kx4K image (since I'm working on DECam data).  This takes
almost 20s to run even though similar statistics using numpy take ~0.1s
or so.

import numpy as np
from astropy.stats import sigma_clipped_stats
im = np.random.rand(4096,2048)*10.0+100.0
timeit mean, median, std = sigma_clipped_stats(im, sigma=3.0, iters=5)
1 loop, best of 3: 18.9 s per loop


1.84s per loop for me.  Still slow, but not 18.9s.


It seems like it might be the use of the numpy masked array module that
is
slowing things down.  Just using the masked array median versus the
normal numpy median takes ~30x longer.

timeit np.median(im)
10 loops, best of 3: 109 ms per loop


103 ms for me; i.e. this isn't just that I have a super fast machine and
you have a super slow one.


timeit np.ma.median(im)
1 loop, best of 3: 2.71 s per loop


104 ms for me.  i.e. with numpy 1.11.1 I don't see a radical difference
between masked array or not.

Stephen



I'm finding similar speed issues with the photutils routines (e.g.
background2D)
that I believe also use masked arrays.

Is there something I can do to speed things up?

Thanks!
David

End of AstroPy Digest, Vol 120, Issue 9
***************************************
"""
