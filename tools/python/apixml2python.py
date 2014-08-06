#!/usr/bin/python

# Copyright (C) 2014 Belledonne Communications SARL
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.

import argparse
import os
import pystache
import sys
import xml.etree.ElementTree as ET

sys.path.append(os.path.realpath(__file__))
from apixml2python.linphone import LinphoneModule


blacklisted_classes = [
	'LinphoneTunnel',
	'LinphoneTunnelConfig'
]
blacklisted_events = [
	'LinphoneCoreInfoReceivedCb',
	'LinphoneCoreNotifyReceivedCb',
	'LinphoneCoreFileTransferProgressIndicationCb',
	'LinphoneCoreFileTransferRecvCb',
	'LinphoneCoreFileTransferSendCb'
]
blacklisted_functions = [
	'linphone_call_get_user_pointer',
	'linphone_call_set_user_pointer',
	'linphone_call_log_get_local_stats',
	'linphone_call_log_get_remote_stats',
	'linphone_call_log_get_start_date',
	'linphone_call_log_get_user_pointer',
	'linphone_call_log_set_user_pointer',
	'linphone_call_params_get_received_video_size',
	'linphone_call_params_get_privacy',
	'linphone_call_params_get_sent_video_size',
	'linphone_call_params_get_used_audio_codec',
	'linphone_call_params_get_used_video_codec',
	'linphone_call_params_set_privacy',
	'linphone_call_stats_get_late_packets_cumulative_number',
	'linphone_call_stats_get_receiver_interarrival_jitter',
	'linphone_call_stats_get_sender_interarrival_jitter',
	'linphone_chat_message_get_chat_room',
	'linphone_chat_message_get_file_transfer_information',
	'linphone_chat_message_get_time',
	'linphone_chat_message_start_file_download',
	'linphone_chat_message_state_to_string',
	'linphone_chat_room_create_file_transfer_message',
	'linphone_chat_room_create_message_2',
	'linphone_chat_room_send_message2',
	'linphone_core_can_we_add_call',
	'linphone_core_enable_payload_type',
	'linphone_core_find_payload_type',
	'linphone_core_get_audio_codecs',
	'linphone_core_get_auth_info_list',
	'linphone_core_get_call_logs',
	'linphone_core_get_calls',
	'linphone_core_get_chat_rooms',
	'linphone_core_get_default_proxy',
	'linphone_core_get_payload_type_bitrate',
	'linphone_core_get_preferred_video_size',
	'linphone_core_get_friend_list',
	'linphone_core_get_proxy_config_list',
	'linphone_core_get_sip_transports',
	'linphone_core_get_sip_transports_used',
	'linphone_core_get_supported_video_sizes',
	'linphone_core_get_video_codecs',
	'linphone_core_get_video_policy',
	'linphone_core_payload_type_enabled',
	'linphone_core_payload_type_is_vbr',
	'linphone_core_publish',
	'linphone_core_set_log_file',	# There is no use to wrap this function
	'linphone_core_set_log_handler',	# Hand-written but put directly in the linphone module
	'linphone_core_set_log_level',	# There is no use to wrap this function
	'linphone_core_set_payload_type_bitrate',
	'linphone_core_set_preferred_video_size',
	'linphone_core_set_video_policy',
	'linphone_core_play_dtmf',
	'linphone_core_send_dtmf',
	'linphone_core_set_audio_codecs',
	'linphone_core_set_preview_video_size',
	'linphone_core_set_sip_transports',
	'linphone_core_subscribe',
	'linphone_event_notify',
	'linphone_event_send_publish',
	'linphone_event_send_subscribe',
	'linphone_event_update_publish',
	'linphone_event_update_subscribe',
	'linphone_presence_model_get_timestamp',
	'linphone_presence_model_set_timestamp',
	'linphone_proxy_config_get_privacy',
	'linphone_proxy_config_normalize_number',
	'linphone_proxy_config_set_file_transfer_server',
	'linphone_proxy_config_set_privacy',
	'linphone_tunnel_get_http_proxy',
	'lp_config_for_each_entry',
	'lp_config_for_each_section',
	'lp_config_get_range',
	'lp_config_load_dict_to_section',
	'lp_config_section_to_dict'
]
hand_written_functions = [
	'linphone_core_new',
	'linphone_core_new_with_config'
]

def generate(apixmlfile, outputfile):
	tree = ET.parse(apixmlfile)
	renderer = pystache.Renderer()
	m = LinphoneModule(tree, blacklisted_classes, blacklisted_events, blacklisted_functions, hand_written_functions)
	os.chdir('apixml2python')
	tmpfilename = outputfile.name + '.tmp'
	f = open(tmpfilename, 'w')
	f.write(renderer.render(m))
	f.close()
	f = open(tmpfilename, 'rU')
	for line in f:
		outputfile.write(line)
	f.close()
	os.unlink(tmpfilename)


def main(argv = None):
	if argv is None:
		argv = sys.argv
	argparser = argparse.ArgumentParser(description="Generate a Python wrapper of the Linphone API.")
	argparser.add_argument('-o', '--outputfile', metavar='outputfile', type=argparse.FileType('w'), help="Output C file containing the code of the Python wrapper.")
	argparser.add_argument('apixmlfile', help="XML file of the Linphone API generated by genapixml.py.")
	args = argparser.parse_args()
	if args.outputfile == None:
		args.outputfile = open('linphone.c', 'w')
	generate(args.apixmlfile, args.outputfile)

if __name__ == "__main__":
	sys.exit(main())
