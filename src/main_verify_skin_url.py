import connect_databases
import verify
if __name__ == '__main__':
    db = connect_databases.open_database_mc_skin()
    urls = connect_databases.select_skin_url_from_skin(db)
    lst = verify.verify(urls)
    print(len(lst))
    connect_databases.close_database(db)
