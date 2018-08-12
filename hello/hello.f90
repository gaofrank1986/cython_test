module test

contains

        subroutine hello1() bind(c)
        use iso_c_binding
        implicit none
        write(*,*) 'hello,world'


        end subroutine
end module
