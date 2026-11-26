import ssl, socket, threading, hashlib, shutil, subprocess, sys, time, os, signal
D = sys.argv[1]
os.chdir(D)
def ctx():
    c = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    c.load_cert_chain("live.crt", "live.key")   # read once, like nginx at config load
    return c
state = {"ctx": ctx(), "loaded_at": time.time()}
def reload():
    try:
        state["ctx"] = ctx(); return "reload ok"
    except Exception as e:
        return f"reload FAILED ({type(e).__name__}); old context kept"
srv = socket.socket(); srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
srv.bind(("127.0.0.1", 8443)); srv.listen()
def serve():
    while True:
        s, _ = srv.accept()
        try:
            t = state["ctx"].wrap_socket(s, server_side=True); t.close()
        except Exception: s.close()
threading.Thread(target=serve, daemon=True).start()
def fp_pem(path):
    der = ssl.PEM_cert_to_DER_cert(open(path).read()); return hashlib.sha256(der).hexdigest()[:16]
def fp_served():
    c = ssl.create_default_context(); c.check_hostname=False; c.verify_mode=ssl.CERT_NONE
    with socket.create_connection(("127.0.0.1", 8443)) as s, c.wrap_socket(s, server_hostname="localhost") as t:
        return hashlib.sha256(t.getpeercert(binary_form=True)).hexdigest()[:16]
def report(step):
    disk, served = fp_pem("live.crt"), fp_served()
    print(f"{step:<38} disk={disk} served={served} match={disk==served}")
print("old cert fp:", fp_pem("old.crt"), " new cert fp:", fp_pem("new.crt"))
report("1 start (old cert loaded)")
shutil.copy("new.crt","live.crt"); shutil.copy("new.key","live.key")
report("2 renewal wrote new files, no reload")
print("  ->", reload()); report("3 after reload")
# failure case: renewal writes a cert/key mismatch, reload fails
shutil.copy("old.crt","live.crt")  # key still 'new' -> mismatch
print("  ->", reload()); report("4 bad files + failed reload")
