SECTIONS
{
	. = 0X0;
	abc : {
		*(abc)
	}
	. = 100;
	def : {
		*(def)
	}
}             
