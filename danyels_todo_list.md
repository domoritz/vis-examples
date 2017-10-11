# creating the script to generate these examples 
Generate them all with https://vega.github.io/vega/usage/#cli 

    npm run-script toSVG

(./toSVG also works, if path includes /npm_modules/.bin)

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

Fix aspect ratio on:
* Density / categorical
* multiple bar chart
* Pie

Consider different color scheme between density cat and density cat?

Fig 18: the trellis is too damn high. Map to color instead.
Fig 19: Don’t map to “number of records.” Pick a variable instead.

Figure 22: mess with color scale. Make that usable.
Consider playing with size 
Why aren’t colors the same for sunburst and treemap?

Fig 28: perhaps something w/ more diversity to dimensions? The averages really smooth things out a LOT

Fig 29: there are some missing values. Or some amazing coincidences. What does that say aobut the data? Look at the “wagon” line.

--
 
