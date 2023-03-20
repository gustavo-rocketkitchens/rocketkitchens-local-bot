# carregando as funções em outros arquivos .py
import database as db

# Create a cursor to interact with the database
conn = db.con
cur = conn.cursor()


# função para inserir registros no banco de dados
def insert(dish, total, sales):
    # Create the item_analysis table if it doesn't exist
    create_query = "CREATE TABLE IF NOT EXISTS rocket_kitchens.item_analysis (id SERIAL PRIMARY KEY, dish TEXT, total INTEGER[], sales INTEGER[])"
    cur.execute(create_query)
    # Include registers in the database

    # Insert the data into the item_analysis table
    insert_query = "INSERT INTO rocket_kitchens.item_analysis (dish, total, sales) VALUES (%s, %s, %s)"
    cur.execute(insert_query, (dish, total, sales))

    # Commit the transaction to save the changes
    conn.commit()

    # Close the cursor and the connection
    cur.close()
    conn.close()


# função para excluir registros no banco de dados
def delete(id):
    # excluir registros no  banco de dados
    db.cur.execute("""
            DELETE FROM clientes WHERE id = '%s'
    """ % (id))
    db.con.commit()


# função para alterar registros no banco de dados
def update(nome, idade, profissao, id):
    # alterar registros no banco de dados
    db.cur.execute("""
            UPDATE clientes SET (nome, idade, profissao) = ('%s', '%s', '%s')  WHERE id = '%s'
    """ % (nome, idade, profissao, id))
    db.con.commit()


# função para selecionar todos os registros no banco de dados
def select():
    # selecionar registros no banco de dados
    conn.execute("""SELECT * FROM mytable;""")
    recset = conn.fetchall()
    rows = []
    for rec in recset:
        rows.append(rec)
    return rows


# função para selecionar apenas um registros no banco de dados
def select_id(id):
    db.cur.execute("""
            SELECT * FROM clientes WHERE id = '%s'
    """ % (id))
    recset = db.cur.fetchall()
    rows = []
    for rec in recset:
        rows.append(rec)
    return rows



# Perform query.
# Uses st.cache_data to only rerun when the query changes or after 10 min.
# @st.cache_data(ttl=600)
def run_query(query):
    with conn as cur:
        cur.execute(query)
        return cur.fetchall()

# rows = client.run_query("SELECT * from mytable;")

# print(run_query("SELECT * from mytable;"))

if __name__ == '__main__':

   sel = select()

   print("sel:\n", sel)