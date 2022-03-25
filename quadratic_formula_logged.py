import logging
import math

LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"
logging.basicConfig(filename=r"quadratic.log",
                    level=logging.DEBUG,
                    format=LOG_FORMAT,
                    filemode='w')
logger = logging.getLogger()

def quadratic_formula(a, b, c):
    """Returns the solution to the equation: ax**2 + bx + c = 0."""
    logger.info("quadratic_formula({0}, {1}, {2})".format(a, b, c))

    # compute the discriminant:
    logger.debug("# Compute the discriminant.")
    disc = b**2 - 4*a*c

    # compute the two roots:
    logger.debug("# compute the two roots.")
    if disc > 0:
        root1 = (-b + math.sqrt(disc)) / (2*a)
        root2 = (-b - math.sqrt(disc)) / (2*a)
    elif disc == 0:
        root1, root2 = -b / (2*a), -b / (2*a)
    else:
        root1, root2 = None, None
    # return the result
    logger.debug("# return the result.")
    return(root1, root2)

roots = quadratic_formula(1, 2, 1)
print(roots)