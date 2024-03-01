# Evaluating the 2D Vector and Raster Graphics Processing Proficiency of CMU CS Academy's IDE

*Published on: Fri Mar  1 09:16:46 AM MST 2024*

## Introduction

This article sets out to evaluate the computational capabilities of CMU Computer Science (CS) Academy's Integrated Development Environment (IDE) in processing 2D Vector and Raster Graphics.

## Methodology

The evaluation framework centers on the continuous creation and rendering of 2D objects while closely observing the total count of objects effectively processed by the CMU CS Academy's IDE. The selection of test objects comprised vector shapes, along with raster text, that I found to fetch fonts from fonts.google.com based on network requests and debugging observations.

## Evaluation Method

Performance testing was carried out using a system equipped with a 12th generation Intel Core i7 processor, 16GB RAM, and an Nvidia T1000 with 4GB of GDDR6, running on Windows 10. The testing spans were deployed on Firefox and Google Chrome.

- Firefox demonstrated performance of an average count of 5,423 shapes before crash over ten runs, with each stress test lasting near five minutes before the page became unresponsive, prompting either the page to crash, the browser to crash, or the Windows desktop to crash.
- The variability of the data on Chromium-based browsers shows that this test may not be optimal for Chromium-based browsers. For a performance log recorded via Firefox's built-in profiler, click [here](http://go.poweredge.xyz/perf).

## Some Assumptions on CMU CS Academy's Graphics Rendering

CMU CS Academy leverages Brython, which is an implementation of Python 3 for the web, to execute code in a Python 3 environment and uses Ace Editor as the code editor. While Brython supports outputting to a display, specific JavaScript (JS) frameworks are required. However, due to CMU's use of Ace, it seems that none of these frameworks would be compatible. To solve this problem, they wrote a graphics library that renders directly to the webpage, but this library does not yet seem to be equipped to manage multiple shapes simultaneously. To handle the creation of shapes or text labels, an instance of their JS graphics library is spawned on-demand, creating massive inefficiency in memory and CPU usage.

Code available [here](https://cmu.adas.software/cmu.pdf).


# So what's up with transcode on the AUR?

*Published on: Wed Feb 14 10:06:38 AM MST 2024*

As the title may suggest, [transcode](https://aur.archlinux.org/packages/transcode) has something weird going on with its packagebase.

The website previously displayed for the upstream URL seems to not be in the ownership of the maintainer, or if it is, it has been repurposed as an unrelated blog about apple cider vinegar. The package previously used a GitHub clone ([https://github.com/wyyrepo/transcode](https://github.com/wyyrepo/transcode)) that isn't from the original author, but the tree is identical to what's hosted on the AUR, except that the GitHub version has a README.md instead of a README.

So basically, I'm just confused about what happened there and wanted an excuse to talk about transcoded stuff (kidding). Oh, and it's not some random irrelevant package; `kde-services` depends on it.
