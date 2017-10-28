
# creating the script to generate these examples 
Generate them all with https://vega.github.io/vega/usage/#cli 

    npm run-script toSVG

(./toSVG also works, if path includes /npm_modules/.bin)

# Making it a branch
Looks like I'm doing enough weird stuff--in this TODO file if nothing else--that I should check it in as a branch. Time to learn that!

# Danyels notes and todo list
Editor is at https://vega.github.io/editor/#/
To play in the editor, needs web-based data

https://raw.githubusercontent.com/domoritz/vis-examples/master/data/complaints.csv?token=ADBtUtuT8aNT9AXT55IiX4eo2EDYckYGks5Z_SG7wA%3D%3D

https://raw.githubusercontent.com/domoritz/vis-examples/master/data/Health_Complaints.csv?token=ADBtUpZdorZBs-5pHqBXIQmj_sDICIgrks5Z_RQwwA%3D%3D 

https://raw.githubusercontent.com/domoritz/vis-examples/master/data/miserables.json?token=ADBtUmcYwZVPGvhvwPE5ber5xfdR_n7sks5Z_RRUwA%3D%3D

https://raw.githubusercontent.com/domoritz/vis-examples/master/data/cars.csv?token=ADBtUoR25B5XGRC3PDD0tl3QAHhNa9r2ks5Z_RoEwA%3D%3D 

https://raw.githubusercontent.com/domoritz/vis-examples/master/data/income.csv?token=ADBtUurfQEdNSlr8WjeGcuFIl6eSrnf8ks5Z_UsfwA%3D%3D

  "__todo": "Check figure captions: they are currently (SUM) and look awkward", 


---
---



CHANGE DEFAULT COLORS & TYPEFACES THROUGHOUT
IMPROVE SPACING BETWEEN LEFT MARGIN	

Most figures: fix captions

Fix aspect ratio on:
* Density / categorical
* multiple bar chart
* Pie

--
 
FIXED

Fig 25: doesn't render 
singleview_7: not rendering
Fig 7: Don’t need KDE and Normal estimate both
Fig 7: axis labels
singleview_13: only one pie needed

singleview_3: order columns by value? (for all bar charts)
   11 Done
   12: Not happening. Sorry, Miriah. Also don't know how to make titles long enough.

 singleview_9_density: render horizontal
  Done

 singleview_19: upgrade from density to actual heatmap? would be nice to have a time dimension on one
    Done on time dimension

Fig 1a-c should use consistent language
  DONE

* Figure 1 (Small multiples)
  Make it a 3x3 (modify data?)
  Why isn't yellow visible? play w/ color scale

--

Here's what I actually use (in the order they occur):
 singleview_1a_scatter.svg
 singleview_1b_clustered-bar.svg
 singleview_1d_clustered-bar-2.svg
 singleview_1c_stacked.svg
 singleview_3_hist-cat.svg
 singleview_4_hist-quant.svg
 singleview_7_noninteractive_smoothed.vl.json.svg
 singleview_8_box-plot.svg
 singleview_9_density-cat.svg
 singleview_10_density-cont.svg
 singleview_11_bar-chart.svg
 singleview_12_clustered-bar-chart.svg
 singleview_13_pie.svg
 singleview_19_heatmap.svg
 singleview_14_scatterplot.svg
 singleview_15_line.svg
 singleview_17_area-stacked.svg
 singleview_20_force.svg
 singleview_21_circular.svg
 singleview_25_adjacency_noninteractive.vg.svg
 singleview_22_treeview.svg
 singleview_23_treemap.svg
 singleview_24_sunburst.svg
 singleview_26_map.svg
 singleview_27_zip.svg
 singleview_30_wordcloud.svg

--
POSTPONED

Figure 9-10: can I control the color scheme?  -- TO WHAT?
Figure 10: can I control the number of bins? -- TO WHAT?

 singleview_4: histogram: illustrate point of multiple bin widths?
 singleview_19: 
     Yes on time dimension; no on actual value. Good enough for now.
     Fig 19: Don’t map to “number of records.” Pick a variable instead.

Figure 8: add another dimension to get colored so we can show that you can compare. (e.g. 4 cyl vs 6 cyl)

Figure 22: mess with color scale. Make that usable.


NOT IN PAPER:
Figure 2a: can fix aspect ratio or wrap? Again, not in love with BIN()
	Consider making them LOWER, and stacking VERTICALLY instead of horizontally 

Fig 18: the trellis is too damn high. Map to color instead.

Fig 28: perhaps something w/ more diversity to dimensions? The averages really smooth things out a LOT

Fig 29: there are some missing values. Or some amazing coincidences. What does that say aobut the data? Look at the “wagon” line.
