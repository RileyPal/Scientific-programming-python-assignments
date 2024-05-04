program calculate_pythagorean_triples

    implicit none

    integer :: a, b
    real :: c

    real, parameter :: epsilon = 1d-3
    integer, parameter :: maximum_c = 50


    do a = 1, maximum_c
        do b = a, maximum_c
            c = sqrt( real(a**2 + b**2) )
            if ( c < real(maximum_c) ) then
                if ( c - floor(c) < epsilon ) then
                    write(*,'(3i4)') a, b, int(c)
                endif
            endif
        enddo
    enddo

end program calculate_pythagorean_triples
