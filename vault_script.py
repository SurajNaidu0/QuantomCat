from bitcoinlib.core.script import CScript, OP_CHECKLOCKTIMEVERIFY, OP_DROP, OP_HASH160, OP_EQUALVERIFY, OP_CHECKSIG

def create_vault_script(pubkey_hash, locktime):
    # OP_CHECKLOCKTIMEVERIFY requires the locktime to be specified in the script
    script = CScript([locktime, OP_CHECKLOCKTIMEVERIFY, OP_DROP, OP_HASH160, pubkey_hash, OP_EQUALVERIFY, OP_CHECKSIG])
    return script

# Example Usage:
# Replace pubkey_hash with the hash of the public key you want to use
pubkey_hash = b'0123456789abcdef0123456789abcdef01234567'

# Set a future locktime (e.g., 1 day from now)
locktime = int(time.time()) + (24 * 60 * 60)

vault_script = create_vault_script(pubkey_hash, locktime)
print("Vault Script:", vault_script)
