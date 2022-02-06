# Fourier_drawing
A Python script that draw any svg file using the associated fourier series and epicycloids.

## Usage

From the terminal use `python -m main filename.svg coeffnumber [boolean_show]` where:

* *`filename.svg`* is the svg file to draw

* *`coeffnumber`* is the number of fourier coefficients to compute

* *`boolean_show`* to show/hide the circles and points

### Dependencies

To get the program to work, you need `numpy`, `matplotlib`, `cmath` and `svgpathtools`.

The needed versions can be found and installed from [requirements.txt](/requirements.txt)


## Example

From the file : <br> <br>
<img src="https://user-images.githubusercontent.com/38764918/152699414-9064f5a4-b9c2-41e1-8335-d3b72681c252.svg" width=40%>

<br>
We can get the following result :

| Number of coefficients  | Result |
| ------------- | :-: |
| 10  | <img src="https://user-images.githubusercontent.com/38764918/152698948-d08d0721-6ead-4a4c-93a9-27036347e2df.gif" width=50%> |
| 50  | <img src="https://user-images.githubusercontent.com/38764918/152699222-e0b2ff75-abd3-4c7e-86c9-cb2fdca75ce9.gif" width=50%> |
| 100 | <img src="https://user-images.githubusercontent.com/38764918/152699356-f5d1a9e7-138b-4241-8b76-1d4d1bbbf2cb.gif" width=50%> |

## What I plan on adding

* Possibility to use jpeg or png images.
* Improving animation speed by removing circles with a small radius which do not add much details

