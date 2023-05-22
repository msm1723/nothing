from flask import Blueprint, jsonify
import asyncio
import asyncpg

import os

bp_async = Blueprint('async', __name__)

# DATABASE_URL = 'postgresql://barack_obama:qwe123QWE@127.0.0.1:5432/the_base'

all = []

async def get_all_from_table(table):
    conn = await asyncpg.connect(os.environ.get("DATABASE_URL"))
    # conn = await asyncpg.connect(DATABASE_URL)
    record = await conn.fetch(f'''
            SELECT * from {table};
        ''')
    all.extend(record)
    await conn.close()

@bp_async.route('/async')
def get_data():
    async def get_async():
        # create tasks for each table coroutine
        tasks = [asyncio.create_task(get_all_from_table(table)) for table in ('data_1', 'data_2', 'data_3')]
        # wait each coroutine finishes
        for task in tasks:
            await task
    asyncio.run(get_async())
    return dict(sorted(all))
