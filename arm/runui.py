import sys
sys.path.append("/opt/arm")

from arm.ui import app  # noqa E402
from arm.config.config import cfg  # noqa E402
import arm.ui.routes  # noqa E402

if __name__ == '__main__':
    drive_index = int(cfg['DRIVE_ID'][-1])
    app.run(host=cfg['WEBSERVER_IP'], port=cfg['WEBSERVER_PORT'] + drive_index, debug=True)
    # app.run(debug=True)
