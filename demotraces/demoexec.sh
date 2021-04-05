export HABLIB_LOGLEVEL=INFO #INFO,ERROR
export HABLIB_FORMAT="[%(asctime)s] p%(process)s {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s"
export HABLIB_FORMAT="p%(process)s -> %(levelname)s - %(message)s"
export HABLIB_LOGFILE="/tmp/hablibclient.log"
while [ true ]; do
    python3 -m habmapslib.cli --conffile config.yaml
done