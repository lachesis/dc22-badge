term.tx(CLS)
ee.start(%000)

{"start"}
term.tx(115)
term.tx(116)
term.tx(97)
term.tx(114)
term.tx(116)
term.tx(CR)

n := 0
repeat while (n < 10000)
  term.dec(n)
  term.tx(45)
  term.dec(ee.rd_byte(n))
  term.tx(CR)
  n++

{"end"}
term.tx(101)
term.tx(110)
term.tx(100)
term.tx(CR)        
