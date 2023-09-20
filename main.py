import time

from src.core.backend import store_ram_data
from src.db.database import connection

if __name__ == "__main__":
    with connection as conn:
        conn.create_table()

        # Run the Backend to store RAM data every minute
        # This is just an example, you may need to run this in a separate process or scheduler
        while True:
            total_ram, free_ram, used_ram = store_ram_data()
            connection.execute_and_commit(
                raw="INSERT INTO ram_usage (total, free, used) VALUES (?, ?, ?)",
                parameters=(total_ram, free_ram, used_ram)
            )
            time.sleep(60)
