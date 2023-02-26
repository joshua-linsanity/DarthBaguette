import requests
from requests.cookies import cookiejar_from_dict
from bs4 import BeautifulSoup
import re
import json

# Class for a person's information to be stored and called later
class UserInfo:
	def __init__(self, ID, pfpURL, name, grade, school, schoolYear, dob, advisor, counselor):
		self.id = ID
		self.pfpURL = pfpURL
		self.name = name
		self.grade = grade
		self.school = school
		self.schoolYear = schoolYear
		self.dob = dob
		self.advisor = advisor
		self.counselor = counselor

	# Gives all information in json format
	def json(self):
		infoJson = {
			"info": {
				"id": self.id,
				"pfpURL": self.pfpURL,
				"name": self.name,
				"grade": self.grade,
				"school": self.school,
				"schoolYear": self.schoolYear,
				"dob": self.dob,
				"advisor": self.advisor,
				"counselor": self.counselor
			}
		}

		return json.loads(json.dumps(infoJson))

# Organizes information and returns it as a UserInfo class
def UserInfoOrganizer(info, url):
	studentBannerIDClass = BeautifulSoup(info.text , 'html.parser').find(class_ = "odd sturow")
	studentBannerID = studentBannerIDClass.get('id')
	children = studentBannerIDClass.findChildren("td" , recursive=False)
	pfpURL = url + children[1].findAll('img')[0]["src"][1:]

	studentInfo = []
	for index in range(len(children)):
		studentInfo.append(children[index].text)
	studentInfo[0] = pfpURL[pfpURL.rindex('/')+1:]
	studentInfo[1] = pfpURL

	return UserInfo(*studentInfo), studentBannerID

def cleanText(text):
	return text.replace("\t", "").replace("\n", "").replace("\r", "").replace("\xa0", "")

# Creates session, logs in, and calls pages. THIS IS THE MAIN FUNCTION
class QwebSession:
	# Logs in with username and password
	def __init__(self, username, password):
		# I have seen the same program be used with other schools so maybe changing the link might work with others
		self.qweb = 'https://qweb.clovisusd.k12.ca.us/'
		qweb = self.qweb
		self.session = requests.Session()
		s = self.session

		# Supposedly a popular user agent
		userAgent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
		s.headers["User-Agent"] = userAgent

		# This is imporant for logging in. The payload is what will get you that "valid: 1"
		loginPayload = {
			"districtid": "connect",
			"Pin": username,
			"Password": password,
			"GuidFromQ": ""
		}

		# This section is used to generate cookies for logging in
		StudentPortal = s.get(qweb + 'StudentPortal/')
		aspSessionID = StudentPortal.cookies["ASP.NET_SessionId"]
		Aequitas = StudentPortal.cookies["LM_Aequitas"]
		s.headers["Cookie"] = 'ASP.NET_SessionId=' + aspSessionID + '; LM_Aequitas=' + Aequitas

		# The main login post call
		loginPage = s.post(qweb + 'StudentPortal/Home/Login', data=loginPayload)
		if (json.loads(loginPage.text)["valid"] == "0"):
			raise ValueError("Failed to login. ID/Password is invalid")
		# This portion loads the main page and gets the student information of the first student. The banner is for the next section to select that student.
		PortalMainPage = s.get(qweb + 'StudentPortal/Home/PortalMainPage')
		self.UserInfo, studentBannerID = UserInfoOrganizer(PortalMainPage, qweb)

		# Yes, these are important for selecting the student. Though it says you successfully logged in you still need to run these get requests so that the correct page and user is chosen (will choose first student)
		SetStudentBanner = s.get(qweb + 'StudentPortal/StudentBanner/SetStudentBanner/' + studentBannerID)
		PortalMainPage2 = s.get(qweb + 'StudentPortal/Home/PortalMainPage')

	def assignmentsJson(self):
		s = self.session
		qweb = self.qweb
		assignmentsPage = s.get(qweb + 'StudentPortal/Home/LoadProfileData/Assignments', cookies=s.cookies)
		assignmentsPageSoup = BeautifulSoup(assignmentsPage.text , 'html.parser')
		classes = assignmentsPageSoup.find_all(class_ = 'txtin3 displaytbl')
		assignmentsList = {}
		# Prepare and create the list
		for index in range(len(classes)):
			topString = cleanText(classes[index].find("caption").text)
			period = re.search(r'\d+', topString).group()
			classNumber = "class"+str(index+1)
			assignmentsList[classNumber] = {}
			assignmentsList[classNumber]["name"] = topString.split(period, 1)[1]
			assignmentsList[classNumber]["period"] = period
			thead = classes[index].find_all("tr")
			gradeTest = thead[0].find("td").text
			assignmentsList[classNumber]["gradingPeriod"] = cleanText(gradeTest.split("Grade: ", 1)[0])
			assignmentsList[classNumber]["grade"] = cleanText(gradeTest.split("Grade: ", 1)[1].split(" \r", 1)[0])
			teacherInfo = thead[0].find_all("td")[1].find("a")
			assignmentsList[classNumber]["teacher"] = {}
			assignmentsList[classNumber]["teacher"]["name"] = teacherInfo.text
			assignmentsList[classNumber]["teacher"]["email"] = teacherInfo["href"].split("mailto:")[1]
			assignmentsList[classNumber]["assignments"] = []
			assignmentsSoup = classes[index].find("tbody").find_all("tr")
			for assignment in assignmentsSoup:
				values = assignment.find_all("td")
				if not values[0].text == "No Assignments Available":
					assignmentsList[classNumber]["assignments"].append({
							"detail": cleanText(values[0].text),
							"dateDue": cleanText(values[1].text),
							"dateAssigned": cleanText(values[2].text),
							"assignment": cleanText(values[3].text),
							"pointsPossible": cleanText(values[4].text),
							"score": cleanText(values[5].text),
							"scoredAs": cleanText(values[6].text),
							"extraCredit": cleanText(values[7].text),
							"notGraded": cleanText(values[8].text),
							"comments": cleanText(values[9].text),
						})

		return json.loads(json.dumps(assignmentsList))


if __name__=="__main__":
	username = '150062644'
	password = 'LINLI64JOS'

	if username == None:
		print("Please fill in the username and password variable if you want to use this testing feature. Otherwise import the file and use it in your own code.")
	else:
		QwebSession = QwebSession(username, password)

		json = QwebSession.assignmentsJson()
		for class_ in json:
			print(json[class_]["teacher"]["email"])
