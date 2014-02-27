(define (problem wumpustest)

	(:domain wumpusworld)

	(:objects
		north west south east - direction
		s1 s2 s3 s4 s5 s6 s7 s8 s9 s10 s11 s12 - square
		agent - worldobj ;self
		p1 p1 - worldobj ;pits
		w1 - worldobj ;wumpus
	)

	(:init
		;set up game board
		(sqr-west-of  s1 s2)
		(sqr-south-of s1 s5)

		(sqr-west-of  s2 s3)
		(sqr-south-of s2 s6)
		(sqr-east-of  s2 s1)

		(sqr-west-of  s3 s4)
		(sqr-south-of s3 s7)
		(sqr-east-of  s3 s2)

		(sqr-south-of s4 s8)
		(sqr-east-of  s4 s3)

		(sqr-north-of s5 s1)
		(sqr-west-of  s5 s6)
		(sqr-south-of s5 s9)

		(sqr-north-of s6 s2)
		(sqr-west-of  s6 s7)
		(sqr-south-of s6 s10)
		(sqr-east-of  s6 s5)

		(sqr-north-of s7 s3)
		(sqr-west-of  s7 s8)
		(sqr-south-of s7 s11)
		(sqr-east-of  s7 s6)

		(sqr-north-of s8 s4)
		(sqr-south-of s8 s12)
		(sqr-east-of  s8 s7)

		(sqr-north-of s9 s5)
		(sqr-west-of  s9 s10)

		(sqr-north-of s10 s6)
		(sqr-west-of  s10 s11)
		(sqr-east-of  s10 s9)

		(sqr-north-of s6 s7)
		(sqr-west-of  s6 s12)
		(sqr-east-of  s6 s10)

		(sqr-north-of s6 s8)
		(sqr-east-of  s6 s11)




		;set up character
		(facing west)
		(in agent s1)

		;safe zones (adjecent to agent square (+self))
		(safe s1)
		(safe s5)
		(safe s2)

		;set up world objects
		(in breeze s5)
	)

	(:goal (and
		(facing north)
		(in agent s5)
	))
)

