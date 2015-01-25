#!/usr/bin/env python
import subprocess

class Py3status:
    cache_timeout = 0

    def _get_cmus_info(self):
        cmus_remote_pipe = subprocess.Popen(["cmus-remote", "-Q"], stdout = subprocess.PIPE, stderr = subprocess.PIPE)
        cmus_info_text = cmus_remote_pipe.communicate()[0].decode()

        if cmus_info_text == "":
            return {}

        cmus_info = {
            "tags": {}
        };
    
        for line in cmus_info_text.splitlines():
            entry = line.split(None, 2)
            
            if entry[0] == "tag" and len(entry) > 2:
                cmus_info["tags"][entry[1]] = entry[2]
            elif len(entry) > 1:
                cmus_info[entry[0]] = entry[1]
    
        return cmus_info

    def cmus(self, i3s_output_list, i3s_config):
        response = {}
        cmus_info = self._get_cmus_info();

        if "status" in cmus_info:
            if "artist" in cmus_info["tags"]:
                now_playing_artist = cmus_info["tags"]["artist"]
            else:
                now_playing_artist = "Unknown"

            if "title" in cmus_info["tags"]:
                now_playing_title = cmus_info["tags"]["title"]
            else:
                now_playing_title = "Unknown"

            response["full_text"] = "♫ : " + now_playing_artist + " - " + now_playing_title
        else:
            response["full_text"] = ""

        return response

if __name__ == "__main__":
    """
    Test this module by calling it directly.
    """
    from time import sleep
    x = Py3status()
    while True:
        print(x.cmus([], {}))
        sleep(1)
