; Vi kan inte gå in i en ruta där vi inte vet vad det är.
; (ty då skulle vi kunna dö - och plannern hade kunnat springa 
; igenom planen genom att testa var den dör och då inte ta den
; vägen (dvs vi tar bort hela poängen med spelet))
;
; Därför måste vi ha någon slags 'known/safe' variabel
;
;

(define (domain wumpusworld)
	(:requirements :strips)
	(:types
		worldobj   ;assumed we got agent
		direction  ;assumed we got north, west, wouth, east
		square
		;agent wumpus pit gold stench breeze - worldobj
	)

	(:predicates
		(sqr-north-of ?sqr ?nsqr - square)
		(sqr-west-of  ?sqr ?wsqr - square)
		(sqr-south-of ?sqr ?ssqr - square)
		(sqr-east-of  ?sqr ?esqr - square)
		(safe ?sqr - square)
		(visited ?sqr - square)
		(maybe-in ?obj - worldobj ?sqr - square)
		(facing ?dir - direction)
		(in ?obj -worldobj ?sqr - square)
	)

	(:action forward
		:parameters (
			?insqr - square
			?tosqr - square
		)
		:precondition (and
			(in agent ?insqr)
			(safe ?tosqr)
			(or
				(and (facing north) (sqr-north-of ?tosqr ?insqr))
				(and (facing west)  (sqr-west-of  ?tosqr ?insqr))
				(and (facing south) (sqr-south-of ?tosqr ?insqr))
				(and (facing east)  (sqr-east-of  ?tosqr ?insqr))
			)
		)
		:effect (and
			;move
			(in agent ?tosqr)
			(visited ?tosqr)
			;if no stench/breeze surrounding squares are safe

			(when
				(not (in ?tosqr breeze))
					(forall(?sqr - square) (
						(when (sqr-north-of ?tosqr ?sqr) (safe ?sqr) )
						(when (sqr-west-of ?tosqr ?sqr) (safe ?sqr) )
						(when (sqr-south-of ?tosqr ?sqr) (safe ?sqr) )
						(when (sqr-east-of ?tosqr ?sqr) (safe ?sqr) )
					)
				)
			)
;			(when 
;				(not (in ?tosqr stench))
;			)
			(not (in agent ?insqr))
		)
	)

	(:action turnleft
		:effect (and
			(when (facing north) (and (facing west)  (not (facing north))))
			(when (facing west)  (and (facing south) (not (facing west) )))
			(when (facing south) (and (facing east)  (not (facing south))))
			(when (facing east)  (and (facing north) (not (facing east) )))
		)
	)

	(:action turnright
		:effect (and
			(when (facing north) (and (facing east)  (not (facing north))))
			(when (facing west)  (and (facing north) (not (facing west) )))
			(when (facing south) (and (facing west)  (not (facing south))))
			(when (facing east)  (and (facing south) (not (facing east) )))
		)
	)

)

