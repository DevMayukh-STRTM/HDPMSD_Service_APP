from HDPMSD import hdpmsd
from http.server import HTTPServer, BaseHTTPRequestHandler


#this is the main handler software

class get_server(BaseHTTPRequestHandler):
    
    def do_GET(self):
        if self.path == "/__ESTABLISH__CONNECTION__":
            data_to_send = "CONNECTED"
            self.send_response(200)
        else:
            try:
                codex = self.path[1:]
                codex = codex.replace('%20', ' ')
                codex = codex.replace('%7B', '{').replace('%7D', '}').replace('%22', '"')
                data_to_send = codex
                lax = eval(codex)
                func = list(lax.keys())[0]
                if len(list(lax.keys())) == 1:
                    if func == 'write':
                        if len(lax['write']) == 3:
                            self.n = hdpmsd.HDPMSD()
                            self.n.writeFile(lax['write'][0], lax['write'][1], lax['write'][2])
                            data_to_send = f'File Created: {lax["write"][0]}'
                            self.send_response(200)
                        else:
                            data_to_send = "Error 404"
                            self.send_response(404)
                    elif func == 'read':
                        if len(lax['read']) == 2:
                            self.n = hdpmsd.HDPMSD()
                            data_to_send = self.n.readFile(lax['read'][0], lax['read'][1])
                            self.send_response(200)
                        else:
                            data_to_send = "Error 404"
                            self.send_response(404)
                    else:
                        data_to_send = "Error 404"
                        self.send_response(404)
                else:
                    data_to_send = "Error 404"
                    self.send_response(404)
            
            except:
                data_to_send = "SERVER_ERR"
                self.send_response(404)


        self.end_headers()
        self.wfile.write(bytes(data_to_send, 'utf-8'))

https = HTTPServer(('', 65000), get_server)
https.serve_forever()