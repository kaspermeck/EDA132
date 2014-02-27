(define (domain wumpusworld)
	(:requirements :strips)
	(:types	
		direction
	)

	(:predicates
		(dead)
		(facing ?x)
	)


	(:action turnleft
		:precondition (not (dead))
		:effect (and  
			(when (facing right) 	(and (facing up)    (not (facing right))) )
			(when (facing up) 	(and (facing left)  (not (facing up)))    )
			(when (facing left)	(and (facing down)  (not (facing left)))  )
			(when (facing down)	(and (facing right) (not (facing down)))  )
		)
	)
)
