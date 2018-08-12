module mandel_wrap
  ! to wrap calc_num_iter for use in C

  use iso_c_binding, only: c_double, c_int
  use mandel, only:  calc_num_iter

  implicit none

contains

  ! need to make a subroutine as only scalars can be returned
  subroutine c_calc_num_iter(nre, re, nim, im, itermax, escape, out) bind(c)
    real(c_double), intent(in):: re(nre), im(nim)
    real(c_double), intent(in), value:: escape
    integer(c_int), intent(in), value:: itermax, nre, nim
    ! note that in C the indices will be reversed!:
    integer(c_int), intent(out):: out(nim, nre)
    ! thus the transpose here:
    out = transpose(calc_num_iter(re, im, itermax, escape))
  end subroutine c_calc_num_iter

end module mandel_wrap
