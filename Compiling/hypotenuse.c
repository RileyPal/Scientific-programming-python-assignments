/**
 * Calculates the length of the hypotenuse of a right triangle given the lengths of its two legs.
 *
 * @param a The length of the first leg.
 * @param b The length of the second leg.
 * @return The length of the hypotenuse.
 * @author (Riley Palermo), (2024)-(5)-(3)
 */
#include <math.h>

double hypotenuse(int a, int b)
{
    double c;

    c = sqrt(pow((double)a, 2) + pow((double)b, 2));
    return c;
}
