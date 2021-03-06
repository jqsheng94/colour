# -*- coding: utf-8 -*-
"""
Showcases characterisation plotting examples.
"""

from pprint import pprint

import colour
from colour.plotting import (colour_plotting_defaults, colour_checker_plot,
                             multi_spd_plot)
from colour.utilities import message_box

message_box('Characterisation Plots')

colour_plotting_defaults()

message_box('Plotting colour rendition charts.')
pprint(sorted(colour.COLOURCHECKERS.keys()))
colour_checker_plot('ColorChecker 1976')
colour_checker_plot('BabelColor Average', text_parameters={'visible': False})
colour_checker_plot('ColorChecker 1976', text_parameters={'visible': False})
colour_checker_plot('ColorChecker 2005', text_parameters={'visible': False})

print('\n')

message_box(('Plotting "BabelColor Average" colour rendition charts spectral '
             'power distributions.'))
multi_spd_plot(
    colour.COLOURCHECKERS_SPDS['BabelColor Average'].values(),
    use_spds_colours=True,
    title=('BabelColor Average - '
           'Relative Spectral Power Distributions'))
