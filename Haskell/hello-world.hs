doubleMe x = x + x
doubleUs x y = doubleMe x + doubleMe y   
doubleSmallNum x = if x < 100
 then x*2
 else x
