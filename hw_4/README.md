# AY250 HW#4: parallelization

I implemented the Monte Carlo dart-throwing simulation to simulate pi serially
(blue), and sped it up for large numbers with concurrent processes (orange).

Sampling the dart coordinates is much faster with numpy's arrays (green). Dask's
arrays further improve performance for large numbers.

I repeated the simulations x10 for each 10^n darts. Errors show standard deviations.


Total simulation time:

![simulation time](https://github.com/zbalewski/python-ay250-homework/blob/main/hw_4/sim_time.png?raw=true)


Rate of dart throws:

![throw rate](https://github.com/zbalewski/python-ay250-homework/blob/main/hw_4/throw_rate.png?raw=true)


Estimates of pi:

![simulation time](https://github.com/zbalewski/python-ay250-homework/blob/main/hw_4/est_pi.png?raw=true)




Homework assignment 4 from AY250.
