(define (problem wumpus-world-100)

  (:domain wumpusworld)

  (:objects
    agent - worldobj ;self
    north west south east - direction
    pit     - worldobj
    wumpus  - worldobj
    breeze  - worldobj
    stench  - worldobj
    glimmer - worldobj
    gold    - worldobj ;that good ol' gold
    s0 s1 s2 s3 s4 s5 s6 s7 s8 s9 s10 s11 s12 s13 s14 s15 s16 s17 s18 s19 s20 s21 s22 s23 s24 s25 s26 s27 s28 s29 s30 s31 s32 s33 s34 s35 s36 s37 s38 s39 s40 s41 s42 s43 s44 s45 s46 s47 s48 s49 s50 s51 s52 s53 s54 s55 s56 s57 s58 s59 s60 s61 s62 s63 s64 s65 s66 s67 s68 s69 s70 s71 s72 s73 s74 s75 s76 s77 s78 s79 s80 s81 s82 s83 s84 s85 s86 s87 s88 s89 s90 s91 s92 s93 s94 s95 s96 s97 s98 s99 - square
  )

  (:init

    ;square s0
    (sqr-north-of s10 s0)
    (sqr-east-of s1 s0)
    
    ;square s1
    (sqr-north-of s11 s1)
    (sqr-west-of s0 s1)
    (sqr-east-of s2 s1)
    
    ;square s2
    (sqr-north-of s12 s2)
    (sqr-west-of s1 s2)
    (sqr-east-of s3 s2)
    
    ;square s3
    (sqr-north-of s13 s3)
    (sqr-west-of s2 s3)
    (sqr-east-of s4 s3)
    
    ;square s4
    (sqr-north-of s14 s4)
    (sqr-west-of s3 s4)
    (sqr-east-of s5 s4)
    
    ;square s5
    (sqr-north-of s15 s5)
    (sqr-west-of s4 s5)
    (sqr-east-of s6 s5)
    
    ;square s6
    (sqr-north-of s16 s6)
    (sqr-west-of s5 s6)
    (sqr-east-of s7 s6)
    
    ;square s7
    (sqr-north-of s17 s7)
    (sqr-west-of s6 s7)
    (sqr-east-of s8 s7)
    
    ;square s8
    (sqr-north-of s18 s8)
    (sqr-west-of s7 s8)
    (sqr-east-of s9 s8)
    
    ;square s9
    (sqr-north-of s19 s9)
    (sqr-west-of s8 s9)
    
    ;square s10
    (sqr-north-of s20 s10)
    (sqr-south-of s0 s10)
    (sqr-east-of s11 s10)
    
    ;square s11
    (sqr-north-of s21 s11)
    (sqr-west-of s10 s11)
    (sqr-south-of s1 s11)
    (sqr-east-of s12 s11)
    
    ;square s12
    (sqr-north-of s22 s12)
    (sqr-west-of s11 s12)
    (sqr-south-of s2 s12)
    (sqr-east-of s13 s12)
    
    ;square s13
    (sqr-north-of s23 s13)
    (sqr-west-of s12 s13)
    (sqr-south-of s3 s13)
    (sqr-east-of s14 s13)
    
    ;square s14
    (sqr-north-of s24 s14)
    (sqr-west-of s13 s14)
    (sqr-south-of s4 s14)
    (sqr-east-of s15 s14)
    
    ;square s15
    (sqr-north-of s25 s15)
    (sqr-west-of s14 s15)
    (sqr-south-of s5 s15)
    (sqr-east-of s16 s15)
    
    ;square s16
    (sqr-north-of s26 s16)
    (sqr-west-of s15 s16)
    (sqr-south-of s6 s16)
    (sqr-east-of s17 s16)
    
    ;square s17
    (sqr-north-of s27 s17)
    (sqr-west-of s16 s17)
    (sqr-south-of s7 s17)
    (sqr-east-of s18 s17)
    
    ;square s18
    (sqr-north-of s28 s18)
    (sqr-west-of s17 s18)
    (sqr-south-of s8 s18)
    (sqr-east-of s19 s18)
    
    ;square s19
    (sqr-north-of s29 s19)
    (sqr-west-of s18 s19)
    (sqr-south-of s9 s19)
    
    ;square s20
    (sqr-north-of s30 s20)
    (sqr-south-of s10 s20)
    (sqr-east-of s21 s20)
    
    ;square s21
    (sqr-north-of s31 s21)
    (sqr-west-of s20 s21)
    (sqr-south-of s11 s21)
    (sqr-east-of s22 s21)
    
    ;square s22
    (sqr-north-of s32 s22)
    (sqr-west-of s21 s22)
    (sqr-south-of s12 s22)
    (sqr-east-of s23 s22)
    
    ;square s23
    (sqr-north-of s33 s23)
    (sqr-west-of s22 s23)
    (sqr-south-of s13 s23)
    (sqr-east-of s24 s23)
    
    ;square s24
    (sqr-north-of s34 s24)
    (sqr-west-of s23 s24)
    (sqr-south-of s14 s24)
    (sqr-east-of s25 s24)
    
    ;square s25
    (sqr-north-of s35 s25)
    (sqr-west-of s24 s25)
    (sqr-south-of s15 s25)
    (sqr-east-of s26 s25)
    
    ;square s26
    (sqr-north-of s36 s26)
    (sqr-west-of s25 s26)
    (sqr-south-of s16 s26)
    (sqr-east-of s27 s26)
    
    ;square s27
    (sqr-north-of s37 s27)
    (sqr-west-of s26 s27)
    (sqr-south-of s17 s27)
    (sqr-east-of s28 s27)
    
    ;square s28
    (sqr-north-of s38 s28)
    (sqr-west-of s27 s28)
    (sqr-south-of s18 s28)
    (sqr-east-of s29 s28)
    
    ;square s29
    (sqr-north-of s39 s29)
    (sqr-west-of s28 s29)
    (sqr-south-of s19 s29)
    
    ;square s30
    (sqr-north-of s40 s30)
    (sqr-south-of s20 s30)
    (sqr-east-of s31 s30)
    
    ;square s31
    (sqr-north-of s41 s31)
    (sqr-west-of s30 s31)
    (sqr-south-of s21 s31)
    (sqr-east-of s32 s31)
    
    ;square s32
    (sqr-north-of s42 s32)
    (sqr-west-of s31 s32)
    (sqr-south-of s22 s32)
    (sqr-east-of s33 s32)
    
    ;square s33
    (sqr-north-of s43 s33)
    (sqr-west-of s32 s33)
    (sqr-south-of s23 s33)
    (sqr-east-of s34 s33)
    
    ;square s34
    (sqr-north-of s44 s34)
    (sqr-west-of s33 s34)
    (sqr-south-of s24 s34)
    (sqr-east-of s35 s34)
    
    ;square s35
    (sqr-north-of s45 s35)
    (sqr-west-of s34 s35)
    (sqr-south-of s25 s35)
    (sqr-east-of s36 s35)
    
    ;square s36
    (sqr-north-of s46 s36)
    (sqr-west-of s35 s36)
    (sqr-south-of s26 s36)
    (sqr-east-of s37 s36)
    
    ;square s37
    (sqr-north-of s47 s37)
    (sqr-west-of s36 s37)
    (sqr-south-of s27 s37)
    (sqr-east-of s38 s37)
    
    ;square s38
    (sqr-north-of s48 s38)
    (sqr-west-of s37 s38)
    (sqr-south-of s28 s38)
    (sqr-east-of s39 s38)
    
    ;square s39
    (sqr-north-of s49 s39)
    (sqr-west-of s38 s39)
    (sqr-south-of s29 s39)
    
    ;square s40
    (sqr-north-of s50 s40)
    (sqr-south-of s30 s40)
    (sqr-east-of s41 s40)
    
    ;square s41
    (sqr-north-of s51 s41)
    (sqr-west-of s40 s41)
    (sqr-south-of s31 s41)
    (sqr-east-of s42 s41)
    
    ;square s42
    (sqr-north-of s52 s42)
    (sqr-west-of s41 s42)
    (sqr-south-of s32 s42)
    (sqr-east-of s43 s42)
    
    ;square s43
    (sqr-north-of s53 s43)
    (sqr-west-of s42 s43)
    (sqr-south-of s33 s43)
    (sqr-east-of s44 s43)
    
    ;square s44
    (sqr-north-of s54 s44)
    (sqr-west-of s43 s44)
    (sqr-south-of s34 s44)
    (sqr-east-of s45 s44)
    
    ;square s45
    (sqr-north-of s55 s45)
    (sqr-west-of s44 s45)
    (sqr-south-of s35 s45)
    (sqr-east-of s46 s45)
    
    ;square s46
    (sqr-north-of s56 s46)
    (sqr-west-of s45 s46)
    (sqr-south-of s36 s46)
    (sqr-east-of s47 s46)
    
    ;square s47
    (sqr-north-of s57 s47)
    (sqr-west-of s46 s47)
    (sqr-south-of s37 s47)
    (sqr-east-of s48 s47)
    
    ;square s48
    (sqr-north-of s58 s48)
    (sqr-west-of s47 s48)
    (sqr-south-of s38 s48)
    (sqr-east-of s49 s48)
    
    ;square s49
    (sqr-north-of s59 s49)
    (sqr-west-of s48 s49)
    (sqr-south-of s39 s49)
    
    ;square s50
    (sqr-north-of s60 s50)
    (sqr-south-of s40 s50)
    (sqr-east-of s51 s50)
    
    ;square s51
    (sqr-north-of s61 s51)
    (sqr-west-of s50 s51)
    (sqr-south-of s41 s51)
    (sqr-east-of s52 s51)
    
    ;square s52
    (sqr-north-of s62 s52)
    (sqr-west-of s51 s52)
    (sqr-south-of s42 s52)
    (sqr-east-of s53 s52)
    
    ;square s53
    (sqr-north-of s63 s53)
    (sqr-west-of s52 s53)
    (sqr-south-of s43 s53)
    (sqr-east-of s54 s53)
    
    ;square s54
    (sqr-north-of s64 s54)
    (sqr-west-of s53 s54)
    (sqr-south-of s44 s54)
    (sqr-east-of s55 s54)
    
    ;square s55
    (sqr-north-of s65 s55)
    (sqr-west-of s54 s55)
    (sqr-south-of s45 s55)
    (sqr-east-of s56 s55)
    
    ;square s56
    (sqr-north-of s66 s56)
    (sqr-west-of s55 s56)
    (sqr-south-of s46 s56)
    (sqr-east-of s57 s56)
    
    ;square s57
    (sqr-north-of s67 s57)
    (sqr-west-of s56 s57)
    (sqr-south-of s47 s57)
    (sqr-east-of s58 s57)
    
    ;square s58
    (sqr-north-of s68 s58)
    (sqr-west-of s57 s58)
    (sqr-south-of s48 s58)
    (sqr-east-of s59 s58)
    
    ;square s59
    (sqr-north-of s69 s59)
    (sqr-west-of s58 s59)
    (sqr-south-of s49 s59)
    
    ;square s60
    (sqr-north-of s70 s60)
    (sqr-south-of s50 s60)
    (sqr-east-of s61 s60)
    
    ;square s61
    (sqr-north-of s71 s61)
    (sqr-west-of s60 s61)
    (sqr-south-of s51 s61)
    (sqr-east-of s62 s61)
    
    ;square s62
    (sqr-north-of s72 s62)
    (sqr-west-of s61 s62)
    (sqr-south-of s52 s62)
    (sqr-east-of s63 s62)
    
    ;square s63
    (sqr-north-of s73 s63)
    (sqr-west-of s62 s63)
    (sqr-south-of s53 s63)
    (sqr-east-of s64 s63)
    
    ;square s64
    (sqr-north-of s74 s64)
    (sqr-west-of s63 s64)
    (sqr-south-of s54 s64)
    (sqr-east-of s65 s64)
    
    ;square s65
    (sqr-north-of s75 s65)
    (sqr-west-of s64 s65)
    (sqr-south-of s55 s65)
    (sqr-east-of s66 s65)
    
    ;square s66
    (sqr-north-of s76 s66)
    (sqr-west-of s65 s66)
    (sqr-south-of s56 s66)
    (sqr-east-of s67 s66)
    
    ;square s67
    (sqr-north-of s77 s67)
    (sqr-west-of s66 s67)
    (sqr-south-of s57 s67)
    (sqr-east-of s68 s67)
    
    ;square s68
    (sqr-north-of s78 s68)
    (sqr-west-of s67 s68)
    (sqr-south-of s58 s68)
    (sqr-east-of s69 s68)
    
    ;square s69
    (sqr-north-of s79 s69)
    (sqr-west-of s68 s69)
    (sqr-south-of s59 s69)
    
    ;square s70
    (sqr-north-of s80 s70)
    (sqr-south-of s60 s70)
    (sqr-east-of s71 s70)
    
    ;square s71
    (sqr-north-of s81 s71)
    (sqr-west-of s70 s71)
    (sqr-south-of s61 s71)
    (sqr-east-of s72 s71)
    
    ;square s72
    (sqr-north-of s82 s72)
    (sqr-west-of s71 s72)
    (sqr-south-of s62 s72)
    (sqr-east-of s73 s72)
    
    ;square s73
    (sqr-north-of s83 s73)
    (sqr-west-of s72 s73)
    (sqr-south-of s63 s73)
    (sqr-east-of s74 s73)
    
    ;square s74
    (sqr-north-of s84 s74)
    (sqr-west-of s73 s74)
    (sqr-south-of s64 s74)
    (sqr-east-of s75 s74)
    
    ;square s75
    (sqr-north-of s85 s75)
    (sqr-west-of s74 s75)
    (sqr-south-of s65 s75)
    (sqr-east-of s76 s75)
    
    ;square s76
    (sqr-north-of s86 s76)
    (sqr-west-of s75 s76)
    (sqr-south-of s66 s76)
    (sqr-east-of s77 s76)
    
    ;square s77
    (sqr-north-of s87 s77)
    (sqr-west-of s76 s77)
    (sqr-south-of s67 s77)
    (sqr-east-of s78 s77)
    
    ;square s78
    (sqr-north-of s88 s78)
    (sqr-west-of s77 s78)
    (sqr-south-of s68 s78)
    (sqr-east-of s79 s78)
    
    ;square s79
    (sqr-north-of s89 s79)
    (sqr-west-of s78 s79)
    (sqr-south-of s69 s79)
    
    ;square s80
    (sqr-north-of s90 s80)
    (sqr-south-of s70 s80)
    (sqr-east-of s81 s80)
    
    ;square s81
    (sqr-north-of s91 s81)
    (sqr-west-of s80 s81)
    (sqr-south-of s71 s81)
    (sqr-east-of s82 s81)
    
    ;square s82
    (sqr-north-of s92 s82)
    (sqr-west-of s81 s82)
    (sqr-south-of s72 s82)
    (sqr-east-of s83 s82)
    
    ;square s83
    (sqr-north-of s93 s83)
    (sqr-west-of s82 s83)
    (sqr-south-of s73 s83)
    (sqr-east-of s84 s83)
    
    ;square s84
    (sqr-north-of s94 s84)
    (sqr-west-of s83 s84)
    (sqr-south-of s74 s84)
    (sqr-east-of s85 s84)
    
    ;square s85
    (sqr-north-of s95 s85)
    (sqr-west-of s84 s85)
    (sqr-south-of s75 s85)
    (sqr-east-of s86 s85)
    
    ;square s86
    (sqr-north-of s96 s86)
    (sqr-west-of s85 s86)
    (sqr-south-of s76 s86)
    (sqr-east-of s87 s86)
    
    ;square s87
    (sqr-north-of s97 s87)
    (sqr-west-of s86 s87)
    (sqr-south-of s77 s87)
    (sqr-east-of s88 s87)
    
    ;square s88
    (sqr-north-of s98 s88)
    (sqr-west-of s87 s88)
    (sqr-south-of s78 s88)
    (sqr-east-of s89 s88)
    
    ;square s89
    (sqr-north-of s99 s89)
    (sqr-west-of s88 s89)
    (sqr-south-of s79 s89)
    
    ;square s90
    (sqr-south-of s80 s90)
    (sqr-east-of s91 s90)
    
    ;square s91
    (sqr-west-of s90 s91)
    (sqr-south-of s81 s91)
    (sqr-east-of s92 s91)
    
    ;square s92
    (sqr-west-of s91 s92)
    (sqr-south-of s82 s92)
    (sqr-east-of s93 s92)
    
    ;square s93
    (sqr-west-of s92 s93)
    (sqr-south-of s83 s93)
    (sqr-east-of s94 s93)
    
    ;square s94
    (sqr-west-of s93 s94)
    (sqr-south-of s84 s94)
    (sqr-east-of s95 s94)
    
    ;square s95
    (sqr-west-of s94 s95)
    (sqr-south-of s85 s95)
    (sqr-east-of s96 s95)
    
    ;square s96
    (sqr-west-of s95 s96)
    (sqr-south-of s86 s96)
    (sqr-east-of s97 s96)
    
    ;square s97
    (sqr-west-of s96 s97)
    (sqr-south-of s87 s97)
    (sqr-east-of s98 s97)
    
    ;square s98
    (sqr-west-of s97 s98)
    (sqr-south-of s88 s98)
    (sqr-east-of s99 s98)
    
    ;square s99
    (sqr-west-of s98 s99)
    (sqr-south-of s89 s99)
    
    ;inits due to agent spawning
    (facing east)
    (visited s0)
    (safe s0)
    (safe s1)
    (safe s10)
    (not-in pit s0)
    (not-in wumpus s0)
    (not-in pit s1)
    (not-in wumpus s1)
    (not-in pit s10)
    (not-in wumpus s10)

    ;world objects inside squares
    (in agent s0)
    (in gold s7)
    (in stench s26)
    (in stench s35)
    (in wumpus s36)
    (in stench s37)
    (in stench s46)
    (in stench s46)
    (in stench s55)
    (in wumpus s56)
    (in stench s57)
    (in stench s66)
    (in breeze s74)
    (in stench s79)
    (in breeze s83)
    (in pit s84)
    (in breeze s85)
    (in stench s88)
    (in wumpus s89)
    (in breeze s94)
    (in stench s99)
  )

  (:goal (and
    (has-gold)
    (in agent s0)
  ))
)
