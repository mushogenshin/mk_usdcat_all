# mk_usdcat_all

![][banner]

# WHAT

This is a small, stand-alone, utility tool written in Python for Windows that allows you to batch convert between Pixar USD binary and ASCII formats. Under the hood it employs Houdini [hython] and the native USD support in [Houdini Solaris], so Houdini 18 is required, and also at least an Indie license — in order to write out *.usda* file format.

A compiled *.exe* is also provided for ease of use.

# WHY

[Pixar USD] is super exciting and powerful. And Houdini Solaris is, too! While learning USD, there are several very good, official, examples — [here][kitchen example] and [here][LOPs tutorials] — either by Pixar or by SideFX, but unfortunately they are all provided in USD binary — not human-readable — format (named the [crate format]). So in the process of learning, I found myself wanting to be able to decipher more how each part in those USD files contributes to the final [scene composition]. Of course one can always take advantage of the displayed USD scene graph either in [usdview] or in Solaris, or take advantage of the LOPs code in Solaris, but I believe the ability to read the *.usda* (as text file) would be extremely helpful and eye-opening. 

Luckily Pixar already provides "[usdcat]" — an utility in their [USD toolset] — which allows for convenient conversion among *.usda*, *.usdb*, and *.usdc* formats. Just some small catches:

1. We would want to convert multiple files. The [kitchen example] has 230 USD files. It's great that [usdcat] accepts multi-file input, but the idea of manually passing hundreds of file paths as command arguments sounds not so fun.
2. Though very likely an outlier case and an especially subpar practice, in case you also want to change the file extensions during conversion, e.g. from *.usdc* to *.usda* and vice versa, then you would then also need to tweak the references in the USD file content in order to have the USD [asset resolution] working. For example, after our binary to ASCII conversion, all lines that have `"@/any_asset.usd@"` in the resulted files must also be changed to `"@/any_asset.usda@"`

# HOW

[banner]: ./img/mk_usdcat_all_banner.png
[hython]: https://www.sidefx.com/docs/houdini/hom/commandline.html#hython
[Pixar USD]: https://graphics.pixar.com/usd/docs/index.html
[Houdini Solaris]: https://www.sidefx.com/products/houdini/solaris/
[crate format]: http://graphics.pixar.com/usd/docs/USD-Glossary.html#USDGlossary-CrateFileFormat
[scene composition]: http://graphics.pixar.com/usd/files/Siggraph2019_USD%20Composition.pdf
[usdview]: https://graphics.pixar.com/usd/docs/USD-Toolset.html#USDToolset-usdview
[usdcat]: https://graphics.pixar.com/usd/docs/USD-Toolset.html#USDToolset-usdcat
[USD Toolset]: https://graphics.pixar.com/usd/docs/USD-Toolset.html
[kitchen example]: http://graphics.pixar.com/usd/downloads.html
[LOPs tutorials]: https://www.sidefx.com/docs/houdini/solaris/tutorials.html
[asset resolution]: http://graphics.pixar.com/usd/docs/USD-Glossary.html#USDGlossary-AssetResolution