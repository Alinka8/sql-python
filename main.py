import mysql.connector
from mysql.connector import Error

# Database configuration
db_name = "FitnessCenterDB"
user = "root"
password = "2001Alina"
host = "localhost"

# Function to connect to the MySQL database
def connect_db():
    try:
        conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=db_name
        )
        if conn.is_connected():
            return conn
    except Error as e:
        print(f"Error: {e}")
        return None

# Function to add a new member to the Members table
def add_member(id, name, age):
    try:
        conn = connect_db()
        if conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO Members (id, name, age) VALUES (%s, %s, %s)", (id, name, age))
            conn.commit()
            print(f"Member {name} added successfully.")
    except Error as e:
        print(f"Error adding member: {e}")
    finally:
        if conn:
            conn.close()

# Function to add a new workout session to the WorkoutSessions table
def add_workout_session(session_id, member_id, session_date, session_time, activity):
    try:
        conn = connect_db()
        if conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO WorkoutSessions (session_id, member_id, session_date, session_time, activity) VALUES (%s, %s, %s, %s, %s)", 
                           (session_id, member_id, session_date, session_time, activity))
            conn.commit()
            print(f"Workout session for member ID {member_id} added successfully.")
    except Error as e:
        print(f"Error adding workout session: {e}")
    finally:
        if conn:
            conn.close()

# Function to update the age of a member
def update_member_age(member_id, new_age):
    try:
        conn = connect_db()
        if conn:
            cursor = conn.cursor()
            cursor.execute("UPDATE Members SET age = %s WHERE id = %s", (new_age, member_id))
            if cursor.rowcount == 0:
                print(f"Member ID {member_id} does not exist.")
            else:
                conn.commit()
                print(f"Member ID {member_id}'s age updated to {new_age}.")
    except Error as e:
        print(f"Error updating member age: {e}")
    finally:
        if conn:
            conn.close()

# Function to delete a workout session based on session ID
def delete_workout_session(session_id):
    try:
        conn = connect_db()
        if conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM WorkoutSessions WHERE session_id = %s", (session_id,))
            if cursor.rowcount == 0:
                print(f"Session ID {session_id} does not exist.")
            else:
                conn.commit()
                print(f"Workout session ID {session_id} deleted successfully.")
    except Error as e:
        print(f"Error deleting workout session: {e}")
    finally:
        if conn:
            conn.close()

# Example usage
if __name__ == "__main__":
    # Add a new member
    add_member(9, 'Shown Mendes', 22)
    
    # Add a new workout session
    add_workout_session(105, 9, '2024-06-22', 'morning', 'Pilates')
    
    # Update member age
    update_member_age(9, 23)
    
    # Delete a workout session
    delete_workout_session(105)


