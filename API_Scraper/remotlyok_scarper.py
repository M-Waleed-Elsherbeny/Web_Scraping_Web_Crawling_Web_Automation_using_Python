import requests
import xlwt as xl

BASE_URL = "https://remoteok.com/api"
HEADER = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9,ar-EG;q=0.8,ar;q=0.7,hy;q=0.6"
}


def get_jobs_API():
    response = requests.get(BASE_URL, headers=HEADER)
    return response.json()

def output_json_in_xls(data):
    workbook = xl.Workbook()
    job_sheet = workbook.add_sheet("Jobs_2")
    headers = list(data[0].keys())
    # print(headers)
    for i in range(len(headers)):
        job_sheet.write(0, i, headers[i])

    for i in range(len(data)):
        jobs = data[i]
        values = list(jobs.values())
        for j in range(len(values)):
            job_sheet.write(i+1, j, values[j])
    
    workbook.save("jobs.xls")



if __name__ == "__main__":
    json = get_jobs_API()[1:]
    output_json_in_xls(json)
    