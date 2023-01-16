# Decay series:

import math
import numpy as np

# Last four decays in the Uranium-235 series.

"Lead-211 -> Bismuth-211 -> Thallium-207 -> Lead-207"

"Pb-211"
# Lead-211:
# denote as 3
# T_1/2: 36 min
# decay_constant = (ln(2)) / 36

"Bi-211"
# Bismuth-211:
# denote as 2
# T_1/2: 2.1 min
# decay_constant = (ln(2)) / 2.1

"Tl-207"
# Thallium-207:
# denote as 1
# T_1/2: 4.8 min
# decay_constant = (ln(2)) / 4.8

"Pb-207"
# Lead-207:
# denote as 0
# stable

# take original iodine-131 class;
# define decay class;

"Naming"
# we should name each nuclei as shown in the periodic table.
## 1. "Pb-211"
## 2. "Bi-211"
## 3. "Tl-207"
## 4. "Pb-207"

"Methods 1"
# this class has methods for ALL radioactive atoms;
# but these methods only iterate one timestep;
# array is in str format;
# return as numpy array.

"Method 2"
# call required methods to iterate one timestep for entire decay chain;
# this step can be made as complicated as we desire;
# return as numpy array.

"Method 2.5"
# basically a method to print simulation while running.

"Method 3"
# call method 2 until half-life has been reached for the final nuclei in chain;
# this method should count for ALL nuclei half-lives;
# return multiple values:
## 1. final numpy array;
## 2. simulated values of half-lives.