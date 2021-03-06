# ====== Legal notices
#
# Copyright (C) 2013 - 2018 GEATEC engineering
#
# This program is free software.
# You can use, redistribute and/or modify it, but only under the terms stated in the QQuickLicence.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY, without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the QQuickLicence for details.
#
# The QQuickLicense can be accessed at: http://www.qquick.org/license.html
#
# __________________________________________________________________________
#
#
#  THIS PROGRAM IS FUNDAMENTALLY UNSUITABLE FOR CONTROLLING REAL SYSTEMS !!
#
# __________________________________________________________________________
#
# It is meant for training purposes only.
#
# Removing this header ends your licence.
#

import math

from SimPyLC import *

g = 10

earthMoonDist = 500

earthDiam = 50
earthMass = 8e7

moonDiam = 15
moonMass = 1e6

# Gravity made proportional to r^-0.5 instead of r^-2 to get a more "telling" simulation

gamma = g * (earthDiam / 2) * (earthDiam / 2) / earthMass

def getGravVec (mass0, mass1, diam, relPos):
    relPos = tEva (relPos)
    dist = tNor (relPos)
    factor = -1 if dist > diam / 2 else 0.1
    return tsMul (tUni (relPos), factor * gamma * mass0 * mass1 / (dist * dist))
    



