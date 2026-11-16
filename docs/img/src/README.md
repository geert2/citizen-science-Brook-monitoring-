# Diagram sources

The wiring pictures in this folder (`../*.svg`) are generated from these small Python scripts,
so they can be corrected and regenerated when the design changes.

    python build_a.py && python build_b.py && python build_c.py

No libraries are needed (plain Python). To make PNG copies: `pip install cairosvg`, then
`cairosvg ../01-power-battery.svg -o 01.png -s 2`.
