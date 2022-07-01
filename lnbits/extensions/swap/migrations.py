async def m001_initial(db):
    await db.execute(
        """
        CREATE TABLE swap.submarineswap (
            id TEXT PRIMARY KEY,
            wallet TEXT NOT NULL,
            amount INT NOT NULL,
            status TEXT NOT NULL,
            boltz_id TEXT NOT NULL,
            refund_privkey TEXT NOT NULL,
            expected_amount INT NOT NULL,
            timeout_block_height INT NOT NULL,
            address TEXT NOT NULL,
            claim_address TEXT NOT NULL,
            payment_hash TEXT NOT NULL,
            redeem_script TEXT NOT NULL,
            time TIMESTAMP NOT NULL DEFAULT """
        + db.timestamp_now
        + """
        );
    """
    )
    await db.execute(
        """
        CREATE TABLE swap.reverse_submarineswap (
            id TEXT PRIMARY KEY,
            wallet TEXT NOT NULL,
            claim_address TEXT NOT NULL,
            refund_address TEXT NOT NULL,
            amount INT NOT NULL,
            instant_settlement INT NOT NULL,
            status TEXT NOT NULL,
            boltz_id TEXT NOT NULL,
            timeout_block_height INT NOT NULL,
            redeem_script TEXT NOT NULL,
            preimage TEXT NOT NULL,
            claim_privkey TEXT NOT NULL,
            lockup_address TEXT NOT NULL,
            onchain_amount INT NOT NULL,
            time TIMESTAMP NOT NULL DEFAULT """
        + db.timestamp_now
        + """
        );
    """
    )