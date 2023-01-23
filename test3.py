from common.BaseClass import BaseClass
from connectors.SqlConnector import SqlConnector
from controllers.EpubSearch import EpubSearch
from controllers.CreateTables import CreateTables

if __name__ == '__main__':
    bc=BaseClass()
    sql_conn=SqlConnector(bc,bc._config._schema_name)._conn
    CreateTables(bc,sql_conn)
    epub_search=EpubSearch(bc,sql_conn)
    epub_search.walk_dir()

