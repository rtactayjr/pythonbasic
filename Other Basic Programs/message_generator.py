"""
This is message builder is for Follow up, Reminder, escalation message, awareness
"""

msg_type = input("Choose a type of message: Follow-up, Reminder, Escalation, Awareness: ").lower()
team_name = input("Enter name of the Team or name of the tech assigned: ").title()
ticket_number = input("Enter the ticket number: ")
analyst_name = input("Enter your fullname: ").title()
print()


def message_compose(msg):
    if msg == "follow-up":
        print(f"Hi {team_name}, \n"
              f"\n"
              f"Good day! \n"
              f"We would like to follow up this ticket: {ticket_number}, assigned to your queue.\n"
              f"\n"
              f"Please check. \n"
              f"\n"
              f"Regards, \n"
              f"{analyst_name}\n"
              f"Service Desk Analyst")

    elif msg == "reminder":
        print(f"Hi {team_name} \n"
              f"\n"
              f"Good day!\n"
              f"We would like to remind you regarding on this ticket:{ticket_number}. \n"
              f"\n"
              f"Regards, \n"
              f"{analyst_name}\n"
              f"Service Desk Analyst")

    elif msg == "escalation":
        print(f"Hi {team_name} \n"
              f"\n"
              f"Good day!\n"
              f"We have assigned this ticket: {ticket_number}, to your queue, kindly check if this is under your scope of support if not please let us know \n"
              f"\n"
              f"Regards, \n"
              f"{analyst_name}\n"
              f"Service Desk Analyst")

    elif msg == "awareness":
        print(f"Hi {team_name} \n"
              f"\n"
              f"Good day!\n"
              f"This email is for your awareness - ticket:{ticket_number}.\n"
              f"\n"
              f"Regards, \n"
              f"{analyst_name}\n"
              f"Service Desk Analyst")
    else:
        print("Program closed")


message_compose(msg_type)
