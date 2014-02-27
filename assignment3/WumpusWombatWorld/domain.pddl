(define (domain wumpusworld)
	(:requirements :strips)
	(:types	obj - object
		direction square - obj
	)

	(:predicates
		(dead)
		(facing ?dir)
		(position ?square)
		;vilket som är vilken granne beror på facing
		;(neighbor ?sq1 ?sq2)
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

	(:action turnright
		:precondition (not (dead))
		:effect (and  
			(when (facing right) 	(and (facing down)    (not (facing right))) )
			(when (facing up) 	(and (facing right)  (not (facing up)))    )
			(when (facing left)	(and (facing up)  (not (facing left)))  )
			(when (facing down)	(and (facing left) (not (facing down)))  )
		)
	)

;	(:action move
;		:precondition(not (dead))
;		:effect (and
;
;		)
;	)
)

