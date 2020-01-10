# firstboot.sh

FIRSTBOOT_EXEC=/usr/sbin/firstboot
FIRSTBOOT_CONF=/etc/sysconfig/firstboot

# source the config file
[ -f $FIRSTBOOT_CONF ] && . $FIRSTBOOT_CONF

# check if we should run firstboot
if [ -f $FIRSTBOOT_EXEC ] && [ "${RUN_FIRSTBOOT,,}" = "yes" ]; then
    # check if we're not on 3270 terminal and root
    if [ $(/sbin/consoletype) = "pty" ] && [ $EUID -eq 0 ]; then
        args=""
        if grep -i "reconfig" /proc/cmdline >/dev/null || [ -f /etc/reconfigSys ]; then
            args="--reconfig"
        fi

        . /etc/locale.conf
        . /etc/vconsole.conf
        # run firstboot only if $DISPLAY is set
        [ -n "$DISPLAY" ] && $FIRSTBOOT_EXEC $args
    fi
fi
