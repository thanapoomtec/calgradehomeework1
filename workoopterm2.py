def calgrade():#สร้างฟังชั่นเพื่อง่ายต่อการรัน
   totalscore = 0 #ตัวแปรเก็บคะแนนทั้งหมด
   pepletotal = 0 #ตัวแปรเก็บจำนวนคน
   average  = 0  #ตัวแปรเก็บค่าเฉบี่ย 
   count = 0 #ตัวแปรเก็บจำนวนคะแนนทั้งหมดที่กรอก
   grades = [] #list เก็บเกรด
   grade_count = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'F': 0} #list directory เก็บจำนวนคนในแต่ละเกรด
   listscore = []
   while True: # ทำการวนซ้ำเรื่อยจนกว่าจะstop
         
         score = input("Enter Score:") # รับค่าคะแนนน

         if score.lower() == "stop": #เช็คเงื่อนไขถ้าพิม stopอจะหยุดทำงานทันที 
            break
         score = float(score) #กำหนดค่าตัวแปรscoreให้เป็น float เพื่อคำนวณเกรด
         
         listscore.append(score) #เก็บคะแนนที่กรอกไวในlist
         
         if 1 <= score <= 100:  #เช็คเงื่อไขต้องกรอกเลข 1-100 
               totalscore += score
               count += 1
         else:#ถ้าไม่ตรงเงื่อนไข
            print("Please Enter Score 1-100") 
            
   average = totalscore / count #คำนวณค่าเฉลี่ย
   
   for x in listscore: #ทำการลูปตามจำนวนคะแนนใน list
      
      if x >= 80: #เช้คเงื่อนไขตามคะแนนที่กรอกมาทั้งหมด
         grade = "A"
      elif x >= 70:
         grade = "B"
      elif x >= 60:
         grade = "C"
      elif x >= 50:
         grade = "D"
      elif x <= 0:
         grade = "F"
      
      grades.append(grade) #เก็บค่าเกรดเป็น str ไว้ใน list
      
      grade_count[grade] += 1 #เก็บจำนวนคนในแต่ละเกรด
   
   print("\n")
   for grade, count in grade_count.items(): #loop showเอ้าพุตผลลัพจำนวนคนในแต่ละเกรด
      print(f"Grade:{grade} Total {count}")
   
   print(f"Average Score:{average}") #output ค่าเฉลี่ยน
   
   for c in listscore:#loop showเอ้าพุตผลลัพคำแนนทั้งหมดที่กรอกมา
      pepletotal += 1
      print(f"{pepletotal}. {c}")
     
calgrade()#เรียกใช้ฟังชั่น