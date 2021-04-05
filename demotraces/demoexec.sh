export HABLIB_LOGLEVEL=INFO #INFO,ERROR
export HABLIB_FORMAT="[%(asctime)s] p%(process)s {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s"
export HABLIB_FORMAT="%(levelname)s - %(message)s" # <-- Para local, con menos verbose
export HABLIB_LOGFILE="/tmp/hablibclient.log"

trap ctrl_c INT
function ctrl_c() {
  echo "Manual exited PID: "$$
  exit 0
}
while [ true ]; do
    python3 -m habmapslib.cli --conffile config.yaml
done