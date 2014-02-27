(define (problem wumpustest)

	(:domain wumpusworld)

	(:objects
		right up left down - direction
		sq-1-1 sq-2-1 - position
	)

	(:init
		(facing right)
	)

	(:goal
		(facing left)
	)
)
