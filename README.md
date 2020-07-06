gb-distributions is a Python module for machine learning, its prime functionality of modules is to measure Gaussian and Binomial distribution's mean, standard deviation, and PDF(Probability Density Function).
The module also supports data and PDF visualization, source code is available at the bottom of the page.

Gaussian distribution:
In probability theory, a normal (or Gaussian or Gauss or Laplace–Gauss) distribution is a type of continuous probability distribution for a real-valued random variable. The general form of its probability density function is

<img src="http://www.sciweavers.org/tex2img.php?eq=f%28x%29%3D%7B%5Cfrac%20%7B1%7D%7B%5Csigma%20%7B%5Csqrt%20%7B2%5Cpi%20%7D%7D%7D%7De%5E%7B-%7B%5Cfrac%20%7B1%7D%7B2%7D%7D%5Cleft%28%7B%5Cfrac%20%7Bx-%5Cmu%20%7D%7B%5Csigma%20%7D%7D%5Cright%29%5E%7B2%7D%7D%7D%0A&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=0" align="center" border="0" alt="f(x)={\frac {1}{\sigma {\sqrt {2\pi }}}}e^{-{\frac {1}{2}}\left({\frac {x-\mu }{\sigma }}\right)^{2}}}" width="185" height="44" />


Binomial distribution with parameters n and p is the discrete probability distribution of the number of successes in a sequence of n independent experiments, each asking a yes–no question, and each with its own boolean-valued outcome: success/yes/true/one (with probability p) or failure/no/false/zero (with probability q = 1 − p).

<img src="http://www.sciweavers.org/tex2img.php?eq=%7B%5Cdisplaystyle%20f%28k%2Cn%2Cp%29%3D%5CPr%28k%3Bn%2Cp%29%3D%5CPr%28X%3Dk%29%3D%7B%5Cbinom%20%7Bn%7D%7Bk%7D%7Dp%5E%7Bk%7D%281-p%29%5E%7Bn-k%7D%7D&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=0" align="center" border="0" alt="{\displaystyle f(k,n,p)=\Pr(k;n,p)=\Pr(X=k)={\binom {n}{k}}p^{k}(1-p)^{n-k}}" width="436" height="47" />

