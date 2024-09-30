.model small
.stack 100h
.386
.data
	arr1 db 10,13,'Enter input: $'
	arr2 db 10,13,'The asci code of$'
	arr3 db ' is:$'
	arr4  db 10,13,'The number of 1 bits are: $'

.code

main proc

	mov ax,@data		
	mov ds,ax
	

	lea dx, arr1
	mov ah, 9
	int 21h
	
	
	mov ah,01h
	int 21h
	mov bl, al
	
	lea dx,arr2
	mov ah,09h
	int 21h
	
	mov dl,bl
	mov ah,02h
	int 21h
	
	lea dx,arr3
	mov ah,09h
	int 21h
	
	mov ch,'0'
	mov cl,8
	
	back:
		shl bL,1
		jc one
		mov dl, '0'
		mov ah, 02h
		int 21h
		dec cl
		jnz back
		jmp exitt
	one:
		mov dl, '1'
		mov ah, 02h
		int 21h
		inc  ch
		dec cl
		jnz back
	
	
exitt:
	lea dx, arr4
	mov ah,09H
	int 21h
	mov dl, ch
	mov ah,02h
	int 21h
	
	mov ah,4ch
	int 21h
		
main endp
end main

