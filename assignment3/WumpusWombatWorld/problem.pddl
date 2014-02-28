(define (problem wumpustest)

	(:domain wumpusworld)

	(:objects
		north west south east - direction
		s1 s2 s3 s4 s5 s6 s7 s8 s9 s10 s11 s12 - square
		agent - worldobj 	;self
		p - worldobj 		;pits
		w - worldobj 		;wumpus
		b - worldobj 		;breeze
		s - worldobj		;stench
		gold - worldobj		;big money honey kaching
	)

	(:init
		;set up game board

		;square 1 all relations
		(sqr-west-of  s1 s2)
		(sqr-south-of s1 s5)

		;square 2
		(sqr-west-of  s2 s3)
		(sqr-south-of s2 s6)
		(sqr-east-of  s2 s1)

		;square 3
		(sqr-west-of  s3 s4)
		(sqr-south-of s3 s7)
		(sqr-east-of  s3 s2)

		;square 4
		(sqr-south-of s4 s8)
		(sqr-east-of  s4 s3)

		;square 5
		(sqr-north-of s5 s1)
		(sqr-west-of  s5 s6)
		(sqr-south-of s5 s9)

		;square 6
		(sqr-north-of s6 s2)
		(sqr-west-of  s6 s7)
		(sqr-south-of s6 s10)
		(sqr-east-of  s6 s5)

		;square 7
		(sqr-north-of s7 s3)
		(sqr-west-of  s7 s8)
		(sqr-south-of s7 s11)
		(sqr-east-of  s7 s6)

		;square 8
		(sqr-north-of s8 s4)
		(sqr-south-of s8 s12)
		(sqr-east-of  s8 s7)

		;square 9
		(sqr-north-of s9 s5)
		(sqr-west-of  s9 s10)

		;square 10
		(sqr-north-of s10 s6)
		(sqr-west-of  s10 s11)
		(sqr-east-of  s10 s9)

		;square 11
		(sqr-north-of s6 s7)
		(sqr-west-of  s6 s12)
		(sqr-east-of  s6 s10)

		;square 12
		(sqr-north-of s6 s8)
		(sqr-east-of  s6 s11)


		;set up character
		(facing west)
		(in agent s1)

		;visited zones
		(visited s1)

		;safe zones (adjecent to agent square (+self))
		(safe s1)
		(safe s5)
		(safe s2)

		;set up wumpus 'w' with surrounding stench 's'
		(in w s3)
		(in s s2)
		(in s s4)
		(in s s7)

		;set up pits 'p' with surrounding breeze 'b'
		(in p s9)
		(in b s10)
		(in b s5)

		;set up gold
		(in gold s10)
	)

	(:goal (and
		(facing north)
		(in agent s10)
	))
)

