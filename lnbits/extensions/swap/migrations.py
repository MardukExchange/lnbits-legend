# async def m001_initial(db):
#     """
#     Initial livestream tables.
#     """
#     await db.execute(
#         f"""
#         CREATE TABLE swap.livestreams (
#             id {db.serial_primary_key},
#             wallet TEXT NOT NULL,
#             fee_pct INTEGER NOT NULL DEFAULT 10,
#             current_track INTEGER
#         );
#         """
#     )

#     await db.execute(
#         f"""
#         CREATE TABLE swap.producers (
#             livestream INTEGER NOT NULL REFERENCES {db.references_schema}livestreams (id),
#             id {db.serial_primary_key},
#             "user" TEXT NOT NULL,
#             wallet TEXT NOT NULL,
#             name TEXT NOT NULL
#         );
#         """
#     )

#     await db.execute(
#         f"""
#         CREATE TABLE swap.tracks (
#             livestream INTEGER NOT NULL REFERENCES {db.references_schema}livestreams (id),
#             id {db.serial_primary_key},
#             download_url TEXT,
#             price_msat INTEGER NOT NULL DEFAULT 0,
#             name TEXT,
#             producer INTEGER REFERENCES {db.references_schema}producers (id) NOT NULL
#         );
#         """
#     )





async def m001_initial(db):
    # await db.execute(
    #     """
    #     CREATE TABLE swap.wtf (
    #         id TEXT PRIMARY KEY,
    #         wallet TEXT NOT NULL,
    #         secret TEXT NOT NULL,
    #         url TEXT NOT NULL,
    #         memo TEXT NOT NULL,
    #         amount INTEGER NOT NULL,
    #         time TIMESTAMP NOT NULL DEFAULT """
    #     + db.timestamp_now
    #     + """
    #     );
    # """
    # )
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
            bip21 TEXT NOT NULL,
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