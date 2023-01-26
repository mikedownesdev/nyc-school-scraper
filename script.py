from pyquery import PyQuery as pq
import csv

# Helper function for converting integers to 0-prefixed strings
# Examples:  4 -> 004  ||  17 -> 017  ||  131 -> 131
def format_number_to_string(number):
    number_as_string = str(n)
    if len(number_as_string) == 1:
        return "00" + number_as_string
    elif len(number_as_string) == 2:
        return "0" + number_as_string
    else:
        return number_as_string


##################
#  Start Script  #
##################

fileName = str(input("The results will be store in the ./data folder. Please provide a file name (no extension): "))
filePath = f"./data/{fileName}.csv"

boroughCodesAndLimits = [
    ("X", 400),  # Bronx
    # ("M", 601) # Manhattan
    # ("K", 401) # Brooklyn
    # ("R", 401) # Staten Island
    # ("Q", 401) # Queens
]

allRows = [
    [
        "Queried URL",
        "School Name",
        "Grade Levels",
        "Enrollment",
        "Geographic District",
        "Borough",
        "School Leader Name & Title",
        "School Leader Email",
        "Address",
        "Maps Link",
        "Phone",
        "School Website Link",
        "Superintendant Name",
        "Superintendant Email",
    ]
]


# Begin looping
for tuple in boroughCodesAndLimits:

    code = tuple[0]
    limit = tuple[1]
    myRange = range(limit)

    for n in myRange:
        buildingCode = format_number_to_string(n)
        url = f"https://www.schools.nyc.gov/schools/{code}{buildingCode}"
        print(url)

        csvRow = []
        try:
            d = pq(url=url)

            schoolName = d("div.module.school-detail h1.title").text()
            gradeLevels = d("div.rte-content li:eq(2) span").text()
            enrollment = d("div.rte-content li:eq(3) span").text()
            geographicDistrict = d("div.rte-content li:eq(4) span").text()
            borough = d("div.rte-content li:eq(5) span").text()

            schoolLeaderHtml = d("div#accordion-panel-02 dl dd:eq(0) a")
            schoolLeaderName = schoolLeaderHtml.text()
            schoolLeaderEmail = schoolLeaderHtml.attr("href")

            addressHtml = d("div.module.school-detail ul:eq(0) li:eq(0) a")
            address = addressHtml.text()
            addressLink = addressHtml.attr("href")

            phoneNumber = d(
                "div.module.school-detail ul:eq(0) li:eq(1) span:eq(1)"
            ).text()
            schoolWebsite = d("div.module.school-detail ul:eq(0) li:eq(3) a").attr(
                "href"
            )

            superIntendantHtml = d("div#accordion-panel-03 dl dd:eq(0) a")
            superIntendantName = superIntendantHtml.text()
            superIntendantEmail = superIntendantHtml.attr("href")

            csvRow.insert(0, url)
            csvRow.insert(1, schoolName)
            csvRow.insert(2, gradeLevels)
            csvRow.insert(3, enrollment)
            csvRow.insert(4, geographicDistrict)
            csvRow.insert(5, borough)
            csvRow.insert(6, schoolLeaderName)
            csvRow.insert(7, schoolLeaderEmail)
            csvRow.insert(8, address)
            csvRow.insert(9, addressLink)
            csvRow.insert(10, phoneNumber)
            csvRow.insert(11, schoolWebsite)
            csvRow.insert(12, superIntendantName)
            csvRow.insert(13, superIntendantEmail)

        except:
            continue

        allRows.append(csvRow)


# Persist results
with open(filePath, "w", newline="") as csvfile:
    wr = csv.writer(csvfile)
    wr.writerows(allRows)
