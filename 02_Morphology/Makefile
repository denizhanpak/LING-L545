all:

	hfst-lexc tr.lexc -o tr.lexc.hfst
	hfst-twolc tr.twol -o tr.twol.hfst
	hfst-compose-intersect -1 tr.lexc.hfst -2 tr.twol.hfst -o tr.gen.hfst
	cat tr.lexc | python3 lexc2dot.py | dot -Tpng -otr.lexc.png
	hfst-fst2txt tr.lexc.hfst | python3 att2dot.py  | dot -Tpng -otr.fsm.png
	hfst-lexc avar.lexc -o avar.lexc.hfst
	cat avar.lexc | python3 lexc2dot.py | dot -Tpng -o avar.lexc.png
