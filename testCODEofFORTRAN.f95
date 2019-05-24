program test_code
implicit none
integer :: age
character :: name*10
print *,'What is your name?'
read *, name
print *, 'Hi ',name,
print *, 'Tell me your age?'
read *, age
print *, 'I am also',age,
end program test_code