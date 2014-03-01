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
		
		(safe    ?sqr - square)
		(visited ?sqr - square)
		(facing  ?dir - direction)
		(has-gold)
		(has-arrow)
		
		(in     ?obj - worldobj ?sqr - square)
		(not-in ?obj - worldobj ?sqr - square)	
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
			(not (in agent ?insqr))
			(visited ?tosqr)

			
			;if no breeze - no pits around
			(forall (?s - square) (when (and (sqr-north-of ?s ?tosqr) (not (in breeze ?tosqr))) (not-in pit ?s)))
			(forall (?s - square) (when (and (sqr-west-of  ?s ?tosqr) (not (in breeze ?tosqr))) (not-in pit ?s)))
			(forall (?s - square) (when (and (sqr-south-of ?s ?tosqr) (not (in breeze ?tosqr))) (not-in pit ?s)))
			(forall (?s - square) (when (and (sqr-east-of  ?s ?tosqr) (not (in breeze ?tosqr))) (not-in pit ?s)))
			
			;if no stench - no wumpus around
			(forall (?s - square) (when (and (sqr-north-of ?s ?tosqr) (not (in stench ?tosqr))) (not-in wumpus ?s)))
			(forall (?s - square) (when (and (sqr-west-of  ?s ?tosqr) (not (in stench ?tosqr))) (not-in wumpus ?s)))
			(forall (?s - square) (when (and (sqr-south-of ?s ?tosqr) (not (in stench ?tosqr))) (not-in wumpus ?s)))
			(forall (?s - square) (when (and (sqr-east-of  ?s ?tosqr) (not (in stench ?tosqr))) (not-in wumpus ?s)))

			;set square safe if there is no wumpuses or pits in it
			(forall (?s - square) (when (and (not-in wumpus ?s) (not-in pit ?s)) (safe ?s)))
			
			;if glimmer - set glimmer in the square
			(when (in gold ?tosqr) (in glimmer ?tosqr))
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

	(:action grab
		:parameters (?sqr - square)
		:precondition (in agent ?sqr)
		:effect (when (in glimmer ?sqr) (has-gold))
	)

)

