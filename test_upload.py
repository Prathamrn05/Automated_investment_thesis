import requests

file_path = "sample.pptx"  # <-- Change this to your file's name
url = "http://127.0.0.1:5000/upload"  # Flask server upload route

with open(file_path, "rb") as f:
    files = {"file": f}
    response = requests.post(url, files=files)

    if response.status_code == 200:
        with open("result.pdf", "wb") as out:
            out.write(response.content)
        print("✅ PDF saved as result.pdf")
    else:
        print("❌ Error:", response.status_code)
        print(response.text)
