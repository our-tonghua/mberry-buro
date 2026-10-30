import json, sys, pathlib
site = pathlib.Path((sys.argv[1] if len(sys.argv)>1 else "."))
c = json.loads((site/"content.json").read_text())
inline = json.dumps(c, ensure_ascii=False).replace("</", "<\\/")
html = (site/"src.html").read_text().replace("/*CONTENT*/", inline)
(site/"index.html").write_text(html)
print("built", len(html), "bytes")
