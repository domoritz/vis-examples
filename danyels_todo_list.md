# creating the script to generate these examples 
Generate them all with https://vega.github.io/vega/usage/#cli 

    bin/vg2svg -h spec/bar.vg.json bar.svg

So the shell script looks like

    foreach file f in *.vg.json
	    Bin/vg2svg -h $f $f.svg

    foreach file f in *.vl.json
	    vl2svg vlSpec

(except do correct filename globbing)
https://kb.iu.edu/d/abec suggests using the command basename

    basename -s .vl.json filename.vl.json 

returns "filename"

Within the Vega project directories, you can use 

    ./bin/vg2png 
    ./bin/vg2svg
    ./node_modules/bin/vg2png

    danyelf@DANYELF-SURBOOK:~/home/git/vis-examples$ ./node_modules/.bin/vl2svg
    ./node_modules/.bin/vl2svg: line 8: vg2svg: command not found

Need to add vg2svg and vl2svg to the path
Technique at https://firstdoit.com/no-need-for-globals-using-npm-dependencies-in-npm-scripts-3dfb478908?gi=7cb8957e11a1

and
https://stackoverflow.com/questions/9679932/how-to-use-package-installed-locally-in-node-modules

Ah.  I'd say use `npm-run` except that doesn't work.

Ok, we're going to do this as a script. https://docs.npmjs.com/cli/run-script reassures me that the path will be right

    npm run-script toSVG


# Making it a branch
Looks like I'm doing enough weird stuff--in this TODO file if nothing else--that I should check it in as a branch. Time to learn that!

# Danyels notes and todo list
Editor is at https://vega.github.io/editor/#/

  "__todo": "Check figure captions: they are currently (SUM) and look awkward", 

Fig 1a-c should use consistent language
Fix aspect ratio for 1a?
Can get rid of “k”?

Figure 2a: can fix aspect ratio or wrap? Again, not in love with BIN()
	Consider making them LOWER, and stacking VERTICALLY instead of horizontally


Fig 7: Don’t need KDE and Normal estimate both
Fig 7: axis labels

CHANGE DEFAULT COLORS & TYPEFACES THROUGHOUT
IMPROVE SPACING BETWEEN LEFT MARGIN	

Figure 8: add another dimension to get colored so we can show that you can compare. (e.g. 4 cyl vs 6 cyl)
Figure 10: can I control the number of bins?
Figure 9-10: can I control the color scheme?
Most figures: fix captions

Fig 18: the trellis is too damn high. Map to color instead.
Fig 19: Don’t map to “number of records.” Pick a variable instead.

Figure 22: mess with color scale. Make that usable.
Consider playing with size 
Why aren’t colors the same for sunburst and treemap?

Fig 28: perhaps something w/ more diversity to dimensions? The averages really smooth things out a LOT

Fig 29: there are some missing values. Or some amazing coincidences. What does that say aobut the data? Look at the “wagon” line.

--
 
