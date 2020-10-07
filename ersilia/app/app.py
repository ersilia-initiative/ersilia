import os
import subprocess
from .. import ErsiliaBase


class StreamlitApp(ErsiliaBase):

    def __init__(self, config_json=None):
        ErsiliaBase.__init__(self, config_json=config_json)

    def run(self, model_id):
        filename = os.path.join(self._dest_dir, model_id, "app.py")
        if os.path.exists(filename):
            subprocess.Popen("streamlit run %s" % filename, shell=True).wait()
            return 1
        else:
            return 0


class DashApp(ErsiliaBase):

    def __init__(self, config_json=None):
        ErsiliaBase.__init__(self, config_json=config_json)

    def run(self):
        pass # TODO
