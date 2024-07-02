import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345",
    database="project1_db"
)

mycursor=mydb.cursor()
def main():
    print("     *****MAHARAJA MULTIPLEX CINEMAS*****    ")
    print("TODAY MOVIES LIST")
    print(" SCREEN 1: MAHARAJA \n SCREEN 2: KALKI \n SCREEN 3: GARUDAN ")
    print("TICKET PRICE IS RS.200 PER HEAD")
main()

movies=["MAHARAJA","KALKI","GARUDAN"]
        
insert="insert into movie_booking(MOVIE_NAME,QUANTITY,CUSTOMER_NAME,MAIL_ID) VALUES (%s,%s,%s,%s)"
def insert_datas():
    try:
        movie_name=input("ENTER YOUR MOVIENAME: ")
        if movie_name in movies:
            print("YES! THIS MOVIE IS TODAY AVAILABLE")
        else:
            print("PLEASE ENTER AVAILABLE MOVIES LIST")
        quantity=int(input("ENTER HOWMANY TICKET'S YOU WANT: "))
        customer_name=input("ENTER YOUR NAME: ")
        mail_id=input("ENTER YOUR MAILID: ")
    except:
        print("PLEASE USE CAPITAL LETTERS ONLY")
    val=(movie_name,quantity,customer_name,mail_id)
    mycursor.execute(insert,val)
    mydb.commit()
    print("YOUR TICKET IS CONFORM")
    return quantity,mail_id

def payment_details():
    ticket_cost=200
    quantity=int(input("ENTER HOWMANY TICKET YOU WANT: "))
    AMOUNT=ticket_cost*quantity
    GST_RATE=18
    GST_PRICE=AMOUNT*18/100
    TOTAL_PRICE=AMOUNT+GST_PRICE
    print(f"GST APPLIED PRICE FOR: {GST_PRICE} AT GST RATE {GST_RATE}%")
    print(f"TOTAL COST OF THE TICKET INCLUDE GST = {TOTAL_PRICE}")

    return TOTAL_PRICE

def bill():
    import datetime
    f=open("bill.txt","a")
    x=datetime.datetime.now()
    TOTAL_PRICE=payment_details()
    f.write(f"\n TOTAL COST OF THE TICKET INCLUDE GST = {TOTAL_PRICE} \n {x}")
    return x

def mail_sending():
    import smtplib
    try:
        mail_id=input("PLEACE ENTER YOUR CURRENT MAILID: ")
        receiver_mail=(f"{mail_id}")
        for i in receiver_mail:
            s=smtplib.SMTP('smtp.gmail.com',587)
            s.starttls()
            s.login("subadurai2001@gmail.com","swfm lcil vsjy dryf")
        TOTAL_PRICE=payment_details()
        x=bill()
        message=f"TOTAL COST OF THE TICKET INCLUDE GST = {TOTAL_PRICE} \n {x}"
        s.sendmail("subadurai2001@gmail.com",i,message)
        s.quit()
        print("MAIL SEND SUCCESSFULLY")
    except:
        print("MAIL NOT SEND")
insert_datas()
bill()
mail_sending()