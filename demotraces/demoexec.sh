export HABLIB_LOGLEVEL=INFO #INFO,ERROR
export HABLIB_FORMAT="[%(asctime)s] p%(process)s {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s"
export HABLIB_FORMAT="%(levelname)s - %(message)s" # <-- Para local, con menos verbose
export HABLIB_LOGFILE="/tmp/hablibclient.log"

PID=99999
trap ctrl_c INT
function ctrl_c() {
  set -x
  kill -9 $PID
  exit 1
  set +x
}

while [ true ]; do
    python3 -m habmapslib.cli --conffile config.yaml
    PID=$($!)
done