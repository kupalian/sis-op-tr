.section .data
data_items:

data_items:
.long 3,67,34,222,45,7,54,34,44,5,22,11,1,9

.section .text

.globl _start
_start:
movl $0, %edi
movl data_items(,%edi,4),%eax
movl %eax, %ebx

start_loop:

incl %edi
movl data_items(,%edi,4),%eax
cmpl $0, %eax
je loop_exit
cmpl %ebx, %eax
jge start_loop

movl %eax, %ebx
jmp start_loop

loop_exit:

movl $1, %eax
int $0x80


