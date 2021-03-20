#v4l2-ctl -d /dev/video0 --set-ctrl=brightness
#v4l2-ctl -d /dev/video0 --set-ctrl=contrast
#v4l2-ctl -d /dev/video0 --set-ctrl=saturation
# v4l2-ctl -d /dev/video0 --set-ctrl=white_balance_temperature_auto=1
#v4l2-ctl -d /dev/video0 --set-ctrl=gain
#v4l2-ctl -d /dev/video0 --set-ctrl=power_line_frequency
#v4l2-ctl -d /dev/video0 --set-ctrl=sharpness
#v4l2-ctl -d /dev/video0 --set-ctrl=backlight_compensation
v4l2-ctl -d /dev/video0 --set-ctrl=exposure_auto=3
#v4l2-ctl -d /dev/video0 --set-ctrl=exposure_absolute
v4l2-ctl -d /dev/video0 --set-ctrl=exposure_auto_priority=0
#v4l2-ctl -d /dev/video0 --set-ctrl=pan_absolute
#v4l2-ctl -d /dev/video0 --set-ctrl=tilt_absolute
#v4l2-ctl -d /dev/video0 --set-ctrl=focus_absolute
v4l2-ctl -d /dev/video0 --set-ctrl=focus_auto=0
v4l2-ctl -d /dev/video0 --set-ctrl=zoom_absolute=100
