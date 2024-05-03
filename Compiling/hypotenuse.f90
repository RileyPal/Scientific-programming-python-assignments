subroutine hypotenuse(a, b, c)

    integer, intent(in) :: a, b
    real, intent(out) :: c

    c = sqrt(real(a**2 + b**2))

end subroutine hypotenuse
