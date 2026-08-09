Agent_name = input ("Enter Agent Name :" )
Gadjet = input ("Enter Gadjet :" )
Agent_Number = 17
Speed_rating = 6.7
Mission_Completed = 19
Height = 1.62
Is_Active = True
print("Agent_Name : ",Agent_name," Type : ", type(Agent_name))
print("Gadjet : ",Gadjet," Type : ", type(Gadjet))
print("Agent_Number : ",Agent_Number," Type : ", type(Agent_Number))
print("Speed_rating : ",Speed_rating," Type : ", type(Speed_rating))
print("Mission_Completed : ",Mission_Completed," Type : ", type(Mission_Completed))
print("Height : ",Height," Type : ", type(Height))
print("Is_Active : ",Is_Active," Type : ", type(Is_Active))

Agent_Number_text = str(Agent_Number)
Speed_rating_text = str(Speed_rating)
Mission_Completed_text = str(Mission_Completed)
Status_text = str(Is_Active) 

print("Agent Number text : ",Agent_Number_text," Type : ", type(Agent_Number_text))
print("Speed rating text : ",Speed_rating_text," Type : ", type(Speed_rating_text))
print("Mission completed text : ",Mission_Completed_text," Type : ", type(Mission_Completed_text))
print("Status text : ",Status_text," Type : ", type(Status_text))

first_three = Agent_name[0:3]
Last_Letter = Agent_name[-1]
code_name = first_three + Last_Letter
print("first three : ", first_three)
print("Last Letter : ", Last_Letter)
print("code name : ", code_name)
