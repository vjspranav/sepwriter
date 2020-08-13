import os

#Adding a list of public/private/vendor categorization
pub = ['adbd.te', 'apexd.te', 'app.te', 'app_zygote.te', 'asan_extract.te', 'ashmemd.te', 'attributes', 'audioserver.te', 'blkid.te', 'blkid_untrusted.te', 'bluetooth.te', 'bootanim.te', 'bootstat.te', 'bufferhubd.te', 'camera_service_server.te', 'cameraserver.te', 'charger.te', 'clatd.te', 'crash_dump.te', 'device.te', 'dhcp.te', 'display_service_server.te', 'dnsmasq.te', 'domain.te', 'drmserver.te', 'dumpstate.te', 'e2fs.te', 'ephemeral_app.te', 'fastbootd.te', 'file.te', 'fingerprintd.te', 'flags_health_check.te', 'fsck.te', 'fsck_untrusted.te', 'fwk_bufferhub.te', 'gatekeeperd.te', 'global_macros', 'gpuservice.te', 'hal_allocator.te', 'hal_atrace.te', 'hal_audio.te', 'hal_audiocontrol.te', 'hal_authsecret.te', 'hal_bluetooth.te', 'hal_bootctl.te', 'hal_broadcastradio.te', 'hal_camera.te', 'hal_cas.te', 'hal_codec2.te', 'hal_configstore.te', 'hal_confirmationui.te', 'hal_contexthub.te', 'hal_drm.te', 'hal_dumpstate.te', 'hal_evs.te', 'hal_face.te', 'hal_fingerprint.te', 'hal_gatekeeper.te', 'hal_gnss.te', 'hal_graphics_allocator.te', 'hal_graphics_composer.te', 'hal_health.te', 'hal_health_storage.te', 'hal_input_classifier.te', 'hal_ir.te', 'hal_keymaster.te', 'hal_light.te', 'hal_lowpan.te', 'hal_memtrack.te', 'hal_neuralnetworks.te', 'hal_neverallows.te', 'hal_nfc.te', 'hal_oemlock.te', 'hal_omx.te', 'hal_power.te', 'hal_power_stats.te', 'hal_secure_element.te', 'hal_sensors.te', 'hal_telephony.te', 'hal_tetheroffload.te', 'hal_thermal.te', 'hal_tv_cec.te', 'hal_tv_input.te', 'hal_usb.te', 'hal_usb_gadget.te', 'hal_vehicle.te', 'hal_vibrator.te', 'hal_vr.te', 'hal_weaver.te', 'hal_wifi.te', 'hal_wifi_hostapd.te', 'hal_wifi_offload.te', 'hal_wifi_supplicant.te', 'healthd.te', 'heapprofd.te', 'hwservice.te', 'hwservicemanager.te', 'idmap.te', 'incident.te', 'incident_helper.te', 'incidentd.te', 'init.te', 'inputflinger.te', 'install_recovery.te', 'installd.te', 'ioctl_defines', 'ioctl_macros', 'iorapd.te', 'isolated_app.te', 'kernel.te', 'keystore.te', 'llkd.te', 'lmkd.te', 'logd.te', 'logpersist.te', 'mdnsd.te', 'mediadrmserver.te', 'mediaextractor.te', 'mediametrics.te', 'mediaprovider.te', 'mediaserver.te', 'mediaswcodec.te', 'modprobe.te', 'mtp.te', 'net.te', 'netd.te', 'netutils_wrapper.te', 'network_stack.te', 'neverallow_macros', 'nfc.te', 'perfetto.te', 'performanced.te', 'perfprofd.te', 'platform_app.te', 'postinstall.te', 'ppp.te', 'priv_app.te', 'profman.te', 'property.te', 'property_contexts', 'racoon.te', 'radio.te', 'recovery.te', 'recovery_persist.te', 'recovery_refresh.te', 'roles', 'rs.te', 'rss_hwm_reset.te', 'runas.te', 'runas_app.te', 'scheduler_service_server.te', 'sdcardd.te', 'secure_element.te', 'sensor_service_server.te', 'service.te', 'servicemanager.te', 'sgdisk.te', 'shared_relro.te', 'shell.te', 'simpleperf_app_runner.te', 'slideshow.te', 'stats_service_server.te', 'statsd.te', 'su.te', 'surfaceflinger.te', 'system_app.te', 'system_server.te', 'system_suspend_server.te', 'te_macros', 'tee.te', 'tombstoned.te', 'toolbox.te', 'traced.te', 'traced_probes.te', 'traceur_app.te', 'tzdatacheck.te', 'ueventd.te', 'uncrypt.te', 'untrusted_app.te', 'update_engine.te', 'update_engine_common.te', 'update_verifier.te', 'usbd.te', 'vdc.te', 'vendor_init.te', 'vendor_misc_writer.te', 'vendor_shell.te', 'vendor_toolbox.te', 'virtual_touchpad.te', 'vndservice.te', 'vndservicemanager.te', 'vold.te', 'vold_prepare_subdirs.te', 'vr_hwc.te', 'watchdogd.te', 'webview_zygote.te', 'wificond.te', 'wpantund.te', 'zygote.te']
priv = ['access_vectors', 'adbd.te', 'apex_test_prepostinstall.te', 'apexd.te', 'app.te', 'app_neverallows.te', 'app_zygote.te', 'art_apex_boot_integrity.te', 'art_apex_postinstall.te', 'art_apex_preinstall.te', 'asan_extract.te', 'ashmemd.te', 'atrace.te', 'audioserver.te', 'auditctl.te', 'binder_in_vendor_violators.te', 'binderservicedomain.te', 'blank_screen.te', 'blkid.te', 'blkid_untrusted.te', 'bluetooth.te', 'bluetoothdomain.te', 'bootanim.te', 'bootstat.te', 'bpfloader.te', 'bufferhubd.te', 'bug_map', 'cameraserver.te', 'charger.te', 'clatd.te', 'compat/', 'coredomain.te', 'cppreopts.te', 'crash_dump.te', 'dex2oat.te', 'dexoptanalyzer.te', 'dhcp.te', 'dnsmasq.te', 'domain.te', 'drmserver.te', 'dumpstate.te', 'ephemeral_app.te', 'fastbootd.te', 'file.te', 'file_contexts', 'file_contexts_asan', 'file_contexts_overlayfs', 'fingerprintd.te', 'flags_health_check.te', 'fs_use', 'fsck.te', 'fsck_untrusted.te', 'fsverity_init.te', 'fwk_bufferhub.te', 'gatekeeperd.te', 'genfs_contexts', 'gpuservice.te', 'gsid.te', 'hal_allocator_default.te', 'halclientdomain.te', 'halserverdomain.te', 'healthd.te', 'heapprofd.te', 'hwservice_contexts', 'hwservicemanager.te', 'idmap.te', 'incident.te', 'incident_helper.te', 'incidentd.te', 'init.te', 'initial_sid_contexts', 'initial_sids', 'inputflinger.te', 'install_recovery.te', 'installd.te', 'iorapd.te', 'isolated_app.te', 'iw.te', 'kernel.te', 'keys.conf', 'keystore.te', 'llkd.te', 'lmkd.te', 'logd.te', 'logpersist.te', 'lpdumpd.te', 'mac_permissions.xml', 'mdnsd.te', 'mediadrmserver.te', 'mediaextractor.te', 'mediametrics.te', 'mediaprovider.te', 'mediaserver.te', 'mediaswcodec.te', 'migrate_legacy_obb_data.te', 'mls', 'mls_decl', 'mls_macros', 'modprobe.te', 'mtp.te', 'netd.te', 'netutils_wrapper.te', 'network_stack.te', 'nfc.te', 'notify_traceur.te', 'otapreopt_chroot.te', 'otapreopt_slot.te', 'perfetto.te', 'performanced.te', 'perfprofd.te', 'platform_app.te', 'policy_capabilities', 'port_contexts', 'postinstall.te', 'postinstall_dexopt.te', 'ppp.te', 'preloads_copy.te', 'preopt2cachename.te', 'priv_app.te', 'profman.te', 'property_contexts', 'racoon.te', 'radio.te', 'recovery.te', 'recovery_persist.te', 'recovery_refresh.te', 'roles_decl', 'rs.te', 'rss_hwm_reset.te', 'runas.te', 'runas_app.te', 'sdcardd.te', 'seapp_contexts', 'secure_element.te', 'security_classes', 'service.te', 'service_contexts', 'servicemanager.te', 'sgdisk.te', 'shared_relro.te', 'shell.te', 'simpleperf_app_runner.te', 'slideshow.te', 'stats.te', 'statsd.te', 'storaged.te', 'su.te', 'surfaceflinger.te', 'system_app.te', 'system_server.te', 'system_server_startup.te', 'system_suspend.te', 'technical_debt.cil', 'tombstoned.te', 'toolbox.te', 'traced.te', 'traced_probes.te', 'traceur_app.te', 'tzdatacheck.te', 'ueventd.te', 'uncrypt.te', 'untrusted_app.te', 'untrusted_app_25.te', 'untrusted_app_27.te', 'untrusted_app_all.te', 'update_engine.te', 'update_engine_common.te', 'update_verifier.te', 'usbd.te', 'users', 'vdc.te', 'vendor_init.te', 'viewcompiler.te', 'virtual_touchpad.te', 'vold.te', 'vold_prepare_subdirs.te', 'vr_hwc.te', 'wait_for_keymaster.te', 'watchdogd.te', 'webview_zygote.te', 'wificond.te', 'wpantund.te', 'zygote.te']

#Writing the Sepolicy
file = open("denials.txt", "r")
lines = file.readlines()
res = []
c=0
for a in lines: 
    perm = [x for x in a.split(" ")]
    for i in range(len(perm)):
        if(perm[i] == '{'):
            per = perm[i+1]
        if('scontext=' and 'u:object_r:' in perm[i]):
            scon = (perm[i].split('u:object_r:')[1]).split(':s0')[0]
        if('scontext=' and 'u:r:' in perm[i]):
            scon = (perm[i].split('u:r:')[1]).split(':s0')[0]
        if('tcontext=' and 'u:object_r:' in perm[i]):
            tcon = perm[i].split('u:object_r:')[1].split(':s0')[0]
        if('tcontext=' and 'u:r:' in perm[i]):
            tcon = perm[i].split('u:r:')[1].split(':s0')[0]
        if('tclass=' in perm[i]):
            tcl = perm[i].split('tclass=')[1]
    b = "allow " + scon + " " + tcon + ":" + tcl + " { " + per + " };"
    if b not in res: #Checking if denial resolution already exists or not
        res.append(b) #Adds the resolution to list
file.close()
res.sort()
count = len(res)

#Adding multiple permissions to same line
for i in range(1,len(res)):
    c=i
    while(res[c].split(' ')[2]==res[i-1].split(' ')[2] and res[c].split(' ')[1]==res[i-1].split(' ')[1]):
        res[i-1] = res[i-1][:-2] + ' ' + res[c].split(' ')[4] + ' ' + res[0][-2:]
        res[c]='0 0 0 0 0'
        c += 1
        if(c==len(res)):
            break
    i=c

res = [i for i in res if '0 0 0 0' not in i]

#Creating the Sepolicy Directories if missing
if not os.path.exists('sepolicy'):
    os.mkdir('sepolicy')
if not os.path.exists('sepolicy/private'):
    os.mkdir('sepolicy/private')
if not os.path.exists('sepolicy/public'):
    os.mkdir('sepolicy/public')

#Writes all the resolutions in the respective files
for i in res:
    fn = i.split(' ')[1]+".te" #Here Goes the location of your sepolicy folder"
    if fn in priv:
        fn = 'private/'+fn
    else:
        fn = 'public/'+fn
    file = open("sepolicy/"+fn, 'a')
    file.write(i+"\n")
    file.close

print(count, ' Denials resolved')

