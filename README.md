# Bresenham-s-Line-Drawing

## Implementation Details

### Algorithm Adjustment for \(m > 1\)

In the traditional Bresenham's algorithm, the loop typically iterates over x-values for \(0 < m < 1\). To handle the case where \(m > 1\), I modified the algorithm to iterate over y-values instead. This adjustment ensures the algorithm works correctly for lines with slopes greater than 1.

The specific adjustment is made in the loop initialization and incrementing section of the `draw_line` function in `draw_line.py`. By detecting the case automatically, the function determines whether to iterate over x-values or y-values based on the slope.

