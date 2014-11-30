#!/usr/bin/env python3
#   -*- coding: utf-8 -*-
#
#   HideMyPython! - A parser for the free proxy list on HideMyAss!
#
#   This file provides a programming interface to HideMyPython's functionality.
#
#   Copyright (C) 2014 Lev Givon <lev (at) columbia (dot) edu>
# 
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
# 
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
# 
#   You should have received a copy of the GNU General Public License
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.

import arguments
import parser

from pkg_resources import resource_filename
countries_all_default = resource_filename(__name__, 'countries_all')

def get_proxies(number_of_proxies=None, countries_all=None, 
                ports=None, protocols=['http', 'https', 'socks'],
                anonymity=0, keep_alive=False, speed=0,
                connection_time=1, verbose=False):
    arg_parser = arguments.create_argument_parser()
    arg_list = []
    if number_of_proxies is not None:
        if not (isinstance(number_of_proxies, int) and number_of_proxies >= 0):
            raise ValueError('number of proxies must be an integer >= 0')
        arg_list.extend(['-n', str(number_of_proxies)])
    if countries_all is None:
        arg_list.extend(['-ct', countries_all_default])
    else:
        arg_list.extend(['-ct', countries_all])
    if ports is not None:
        try:
            iter(ports)
        except:
            raise ValueError('ports must be an iterable')        
        arg_list.extend(['-p']+list(map(str, ports)))
    try:
        iter(protocols)
    except:
        raise ValueError('protocols must be an iterable')
    if not set(protocols).intersection(set(['http', 'https', 'socks'])):
        raise ValueError('invalid protocol')
    arg_list.extend(['-pr']+list(protocols))
    if anonymity >= 1:
        arg_list.append('-'+'a'*anonymity)
    if keep_alive:
        arg_list.append('-ka')
    if speed >= 1:
        arg_list.append('-'+'s'*speed)
    if verbose:
        arg_list.append('-v')
    args = arg_parser.parse_args(arg_list)
    arguments.process_arguments(args, arg_parser)
    return [proxy for proxy in parser.generate_proxy(args)]
