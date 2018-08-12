subroutine pythagoras(a, b, c) bind(C)

   use iso_c_binding
   implicit none
   real (C_FLOAT), intent(in) :: a, b
   real (C_FLOAT), intent(out) :: c
 
   c = sqrt(a*a + b*b)
  
end subroutine pythagoras
