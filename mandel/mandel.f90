module mandel
  implicit none

  integer, parameter :: dp=kind(0.d0) ! double precision

contains

  pure function mandel_frac(z, c) result(out)
    ! The Mandelbrot function z -> z^2 + c
    complex(dp), intent(in):: z, c
    complex(dp):: out
    out = z**2 + c
  end function mandel_frac

  pure function calc_num_iter(re, im, itermax, escape) result(out)
    ! Iterates on mandel_frac
    real(dp), intent(in):: re(:), im(:), escape
    integer, intent(in):: itermax
    integer:: out(size(re), size(im))
    integer:: ii, jj, kk, itt
    complex(dp):: zz, cc

    do ii=1,size(re)
       do jj=1,size(im)
          zz = 0
          cc = cmplx(re(ii), im(jj), dp)
          itt = 0
          do kk=1,itermax
             zz = mandel_frac(zz, cc)
             itt = kk
             if (abs(zz)>escape) then
                exit
             end if
          end do
          out(ii,jj) = itt
       end do
    end do

  end function calc_num_iter

end module mandel
