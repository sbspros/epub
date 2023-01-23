from common.BaseClass import BaseClass
from sql_tables.SqlTable import SqlTable,SQLCreateError,SqlSelectError,SqlInsertError
from datetime import datetime 
import traceback

__author__ = "Richard Chamberlain"
__copyright__ = "Copyright 2022"
__license__ = "MIT"
__version__ = "1.0"
__maintainer__ = "Richard Chamberlain"
__email__ = "richard@sbspros.ca"
__status__ = "Dev"

class SqlCategories(SqlTable):
    table_exists=False

    def create_table(self,bc,conn):
        try:
            sql_create_table = " CREATE TABLE IF NOT EXISTS {table_name} (\
                id integer PRIMARY KEY,\
                category text,\
                creatation_date int NOT NULL,\
                modification_date NOT NULL\
                    ); ".format(table_name=self._table_name)
            conn.execute(sql_create_table)
            conn.commit()
        except:
            bc.log.error("\t"+":"+traceback.format_exc())
            raise SQLCreateError

    def update():
        pass

    def delete():
        pass

    def insert(self,bc,conn):
        try:
            store_date=int(datetime.now().timestamp())
            sql_insert = "\
                insert into {table_name} (\
                category,\
                creatation_date,modification_date) values(\
                '{category}',\
                {creatation_date},{modification_date});".format(\
                table_name=self._table_name,\
                category=self.category,\
                creatation_date=store_date,\
                modification_date=store_date)
            bc.log.error(sql_insert)
            conn.execute(sql_insert)
            conn.commit()
            return self.get_id(conn)
        except:

            bc.log.error("\t"+":"+traceback.format_exc())
            raise SqlInsertError        
        pass

    def select(self,bc,conn):

        try:
            sql_select = " ; ".format(table_name=self._table_name,\
                        name=self._name)
            conn.execute(sql_select)
            cursor = conn.execute(sql_select)
            return cursor.fetchall()
        except:
            bc.log.error("\t"+":"+traceback.format_exc())
            raise SqlSelectError        

    def search_name(self,bc,conn,show_name):
        select_return=[]
        sql_select = "select * from {table_name}\
            where \
             ; ".format(table_name=self._table_name,\
            )
        try:
            conn.execute(sql_select)
            cursor = conn.execute(sql_select)
            select_return= cursor.fetchall()
        except:
            bc.log.error(sql_select)
            bc.log.error("\t"+":"+traceback.format_exc())
        return select_return

    def in_database(self,bc,conn,):
        sql_select = "select id from {table_name}\
            where category='{category}';".format(\
                table_name=self._table_name,\
                category=self.category\
            )
        bc.log.error(sql_select)
        conn.execute(sql_select)
        cursor = conn.execute(sql_select)
        select_return= cursor.fetchall()
        try:
            return select_return[0][0]
        except:
            return None
