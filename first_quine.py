# create defs -- defs must hold as strings all the "things" you use to print things and quote things
# print defs
# sss = print of defs\nsss =
# print sss + quote + sss + quote
# sss = sss + something # add something to defs
# print sss


nl = "\n"
snl = "nl"
eq = " = "
seq = "eq"
q = "\""
sq = "q"
bs = "\\"
sbs = "bs"
ss = "s"
sn = "n"
pr = "print("
spr = "pr"
cp = ")"
scp = "cp"
sdefs = "defs"
superq = "\"\"\""
ssuperq = "superq"
something = """sss + something
print(sss)
"""
ssomething = "something"

print(snl + eq + q + bs + sn + q + nl + ss + snl + eq + q + snl + q + nl + seq + eq + q + eq + q + nl + ss + seq + eq + q + seq + q + nl + sq + eq + q + bs + q + q + nl + ss + sq + eq + q + sq + q + nl + sbs + eq + q + bs + bs + q + nl + ss + bs + eq + q + sbs + q + nl + ss + ss + eq + q + ss + q + nl + ss + sn + eq + q + sn + q + nl + spr + eq + q + pr + q + nl + ss + spr + eq + q + spr + q + nl + scp + eq + q + cp + q + nl + ss + scp + eq + q + scp + q + nl + ss + sdefs + eq + q + sdefs + q + nl + ssuperq + eq + q + bs + q + bs + q + bs + q + q + nl + ss + ssuperq + eq + q + ssuperq + q + nl + ssomething + eq + superq + something + superq + nl + ss + ssomething + eq + q + ssomething + q + nl)

defs = "snl + eq + q + bs + sn + q + nl + ss + snl + eq + q + snl + q + nl + seq + eq + q + eq + q + nl + ss + seq + eq + q + seq + q + nl + sq + eq + q + bs + q + q + nl + ss + sq + eq + q + sq + q + nl + sbs + eq + q + bs + bs + q + nl + ss + bs + eq + q + sbs + q + nl + ss + ss + eq + q + ss + q + nl + ss + sn + eq + q + sn + q + nl + spr + eq + q + pr + q + nl + ss + spr + eq + q + spr + q + nl + scp + eq + q + cp + q + nl + ss + scp + eq + q + scp + q + nl + ss + sdefs + eq + q + sdefs + q + nl + ssuperq + eq + q + bs + q + bs + q + bs + q + q + nl + ss + ssuperq + eq + q + ssuperq + q + nl + ssomething + eq + ssuperq + something + superq + nl + ss + ssomething + eq + q + ssomething + q + nl"


print(pr + defs + cp + nl)
print(sdefs + eq + q + defs + q + nl)
sss = """
print(pr + defs + cp + nl)
print(sdefs + eq + q + defs + q + nl)
sss = """


print(sss + superq + sss + superq + nl)
sss = """
print(sss + superq + sss + superq + nl)
sss = """


print(sss + superq + sss + superq + nl)
sss = sss + something
print(sss)
