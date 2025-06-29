import subprocess
try:
  with open("index.html","r") as f:
    pass
  with open("about.html","r") as f:
    pass
  with open("./tutorial/index.html","r") as f:
    pass
  with open("./reference/index.html","r") as f:
    pass
  with open("./library/index.html","r") as f:
    pass
  with open("./howto/index.html","r") as f:
    pass
  with open("./faq/index.html","r") as f:
    pass
  with open("./_static/sidebar.js","r") as f:
    pass
  subprocess.run(f"am start -a android.intent.action.VIEW -d http://127.0.0.1:9000/", shell=True, capture_output=True)
  subprocess.run("python -m http.server 9000",shell=True, capture_output=True, text=True)

except FileNotFoundError:
  print("Some dependencies files are Missing")
  
