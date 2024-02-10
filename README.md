# Bresenham-s-Line-Drawing

## Implementation Details

### Algorithm Adjustment for \(m > 1\)

In the traditional Bresenham's algorithm, the loop iterates over x-values for \(0 < m < 1\). However, when dealing with slopes \(m > 1\), adjustments are necessary to ensure accurate line drawing.

#### Iterating Over Y-values

To accommodate the case where \(m > 1\), the algorithm has been modified to iterate over y-values instead of x-values. This adjustment is crucial to handle lines with slopes greater than 1.

#### Loop Adjustment in Code

The specific modification is implemented within the `draw_line` function in `draw_line.py`. By dynamically detecting the slope of the line, the function determines whether to iterate over x-values or y-values. This approach ensures the algorithm's effectiveness for a broad range of slope values.

## Graphical Outputs

### Case 1
![Case 1 Output](Graphical%20Outputs/Case_1.jpg)

### Case 2
![Case 2 Output](Graphical%20Outputs/Case_2.jpg)

