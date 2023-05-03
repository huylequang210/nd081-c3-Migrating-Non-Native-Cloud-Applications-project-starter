import logging
import azure.functions as func
import psycopg2
import os
from datetime import datetime
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

def main(msg: func.ServiceBusMessage):
    notification_id = int(msg.get_body().decode('utf-8'))
    logging.info('Python ServiceBus queue trigger processed message: %s',notification_id)

    conn = psycopg2.connect(dbname="techconfdb", user="huylequang210", password="@Bondaica123", host="project3-huylequang210.postgres.database.azure.com")
    cursor = conn.cursor()

    try:
        notification = cursor.execute("SELECT message, subject FROM notification WHERE id = {};".format(notification_id))
        cursor.execute("SELECT first_name, last_name, email FROM attendee;")
        attendees = cursor.fetchall()
        for attendee in attendees:
            Mail('{}, {}, {}'.format({'admin@techconf.com'}, {attendee[2]}, {notification}))
        date = datetime.utcnow()
        info = 'Notified {} attendees'.format(len(attendees))
        update_query = cursor.execute("UPDATE notification SET status = '{}', completed_date = '{}' WHERE id = {};".format(info, date, notification_id))        
        conn.commit()

    except (Exception, psycopg2.DatabaseError) as error:
        logging.error(error)
    finally:
        cursor.close()
        conn.close()