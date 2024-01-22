from bitcoinlib.core.script import CScript, OP_CAT

def op_cat_script(data1, data2):
    script = CScript([data1, data2, OP_CAT])
    return script

# Example Usage:
data1 = b"Hello, "
data2 = b"world!"

bitcoin_script = op_cat_script(data1, data2)
print("Bitcoin Script:", bitcoin_script)
