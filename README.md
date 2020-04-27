# mk_usdcat_all

![][banner]

# WHAT

This is a small, stand-alone, utility tool written in Python for Windows that allows you to batch convert between Pixar USD binary and ASCII formats. Under the hood it employs Houdini hython and the USD Houdini plugin, so Houdini 18 is required, and also at least an Indie license — in order to write out .usda file format.

A compiled .EXE is also provided for ease of use.

# WHY

[Pixar USD][Pixar USD] is super exciting and powerful. And [Houdini Solaris][Houdini Solaris] is, too! While learning USD, there are several very good, official, examples either by Pixar or by SideFX, but unfortunately they are all provided in USD binary — not human-readable — format (named the crate format). So in the process of learning, I found myself wanting to be able to decipher more how each part in those USD files contributes to the final scene composition. Of course one can always take advantage of the displayed USD scene graph, or the LOP code in Solaris, but I believe the ability to read the .usda (as text file) would be extremely helpful and eye-opening. 

Luckily Pixar already provides "[usdcat][usdcat]" — an utility in their [USD toolset][USD Toolset] — which allows for convenient conversion among .usda, .usdb, and .usdc formats. Just some small catches:

1. We would want to convert multiple files. The [kitchen example][Kitchen Example] has 230 USD files. It's great that usdcat accepts multi-file input, but the idea of manually passing hundreds of file paths as command arguments sounds not so fun.

[banner]: ./img/mk_usdcat_all_banner.png
[Pixar USD]: https://graphics.pixar.com/usd/docs/index.html
[Houdini Solaris]: https://www.sidefx.com/products/houdini/solaris/
[usdcat]: https://graphics.pixar.com/usd/docs/USD-Toolset.html#USDToolset-usdcat
[USD Toolset]: https://graphics.pixar.com/usd/docs/USD-Toolset.html
[Kitchen Example]: http://graphics.pixar.com/usd/downloads.html