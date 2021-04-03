#
stdout as *;
internal_file;
`C:/Users/Me/Desktop/folder/file.arc` as pushed_import;
#


(my_struct; output=True; @{}){  //@predefined rules of the structure 
	2+2;            //output: 4
	@2+2 = 1; //rewrite rules for computing them expressions: 2+2 equals 1 from now in the current structure

	func(args, arg=none)(explanation:"annotations that can be anything: this func returns int; used to do something..etc.", tip : "can be also omitted") Func{
		i = 5;
		c = 12;
		return i+c
	}
	
} 

{

	returned = my_struct.Func();
	show($"{my_struct.Func[explanation]}", " : ", returned); 					//stdout.show()

	/*
	simple usage
	*/


	func() SomeFunc{
		global @2+2 = 1; //making an expression 2+2 equal 1 in the global scope
	}





	//some quick math

	formula Pifagora{
		c^2 = a^2 + b^2;			/* a formula works like interface: it can be either shown in console as string or be inherited by function where arguments will be predeclarised by names of variables that are used in the formula */
		--> c^2; // "-->" means that the object after will be accessible via calling "~" character in functions that inharite from the formula 
	}

	//formula inheritance 
	func : Pifagora() Calculate{ //a, b and c are arguments of this function now
		return ~	;
	}

	// you can use  '    ' to exclude code syntax collisions
	// non-inheritable formula --> cannot be processed; 

	!formula Something{
		aoisjdi '-->' 12312
	}


dict a ={"asfs" = 2;}

}





























