# Interpolation Methods Comparison

A numerical analysis project comparing Lagrange and Cubic Spline interpolation methods for approximating the square root function.

## Files

- `lagrange_interpolation.py` - Implementation of 8th degree Lagrange polynomial interpolation
- `cubicSpline.py` - Implementation of cubic spline interpolation with natural boundary conditions
- `page50_list3.tex` - LaTeX report document
- `verify_results/` - Directory containing output images

## Requirements

- Python 3.11
- NumPy
- Matplotlib
- SciPy

## Usage

1. Run the Lagrange interpolation:
```
python lagrange_interpolation.py
```

2. Run the Cubic Spline interpolation:
```
python cubicSpline.py
```

3. Generate the report:
```
pdflatex page50_list3.tex
```

## Results

- Lagrange interpolation: Passes through all data points but suffers from Runge's phenomenon (oscillations)
- Cubic spline interpolation: Provides smoother curve that closely matches the square root function

In the interval [0,64], cubic spline interpolation is significantly more accurate. In [0,1], both methods perform similarly since there are only two data points in this interval. 