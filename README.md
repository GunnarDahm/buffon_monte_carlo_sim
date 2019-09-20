<h1> Monte Carlo Simulation of Buffon's Needle </h1>
<h2> Status: Completed </h2>

<h2> Purpose </h2>
<p> The purpsose of this project is to create a Monte Carlo simulation of the geometric probability problem, Buffon's
Needle. This simulation ultimately arrives at an estimation of the mathematical constant Pi. 
</p>

<h2> Methods Used </h2>

<ul>
<li>Monte Carlo Simulation</li>
<li>Data Visualization</li>
</ul>

<h2> Technologies </h2>
<ul>
<li>Python (v.3.7)</li>
</ul>

<h2> Required Libraries </h2>
<ul>
<li>Pandas</li>
<li>NumPy</li>
<li>MatPlotLib</li>
</ul>

<h2> Project Description </h2>

<p>
This project seeks to recreate the procedures of the classic geometric probability problem of Buffon's Needle. 
For context, the mathematician Georges-Louis Leclerc, the Count of Buffon, sought to approximate the value of Pi. At 
this time the constant of Pi was known, however its value beyond approximately 3 was not yet determined. 
</p>

<p>
The Count thus devised a method of approximating the value of Pi using multi-variable calculus and probality, that could
approximate the value of pi by conducting a randomized basic physical procedure many time (i.e. a Monte-Carlo 
simulation). His procedure was simple. He attained a board of arbitrary dimensions (L x W). On this board, he drew 
parallel lines across the length of the board, similar to yard-lines on a football field, each n inches apart in 
distance. He then threw a needle, also of length n inches, randomly on to the board. Using the aforement calculus and 
probability, he knew that the probability the needle would cross any of the drawn yard-lines was 2/Pi. Therefore, all 
he had to do was physically throw this needle many times on to this board to back out the value of pi. For more reading 
on the math behind this realization, see <a href="https://en.wikipedia.org/wiki/Buffon%27s_needle_problem">
Buffon's Needle</a>.
</p>

<p>
This script thus simulates the thousands of random throws of a needle on to the board to derive the value of pi. This 
script utilizes pseudo-randomness to achieve needles positioning, plot all the needles on to board, and estimate the 
value of pi. The estimated value is compared to the actual value of pi and an error is calculated for reference. 
Additionally, a csv file is exported with all the needles thrown.
</p>

<h2> To Use: </h2>

<p>
To perform the simulation, simply run the script in the buffon_monte_carlo_sim directory and a plot of the 
board will automatically be generated. The parameters of sample size and significant figures may adjusted higher or 
lower as desired. Note that the higher the both parameters are set, the more accurate the estimation, however this will 
also increase the run-time. A csv file of all the needles postions will be automatically exported to the same directory. 
</p>

<h2> Author:</h2>
<p> Gunnar Dahm </p>