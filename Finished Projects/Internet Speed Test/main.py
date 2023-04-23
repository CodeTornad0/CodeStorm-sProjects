import speedtest

st = speedtest.Speedtest()
server_names = []
print("loading...")
print(f"Upload Speed: {round(st.upload(), 3)}")
print("loading...")
print(f"Download Speed: {round(st.download(), 3)}")
print("loading...")
st.get_servers(server_names)
print(f"Ping: {round(st.results.ping, 3)} MS")
