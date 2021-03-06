#!/usr/bin/env python3
# 	-*- coding: utf-8 -*-
#
# 	HideMyPython! - A parser for the free proxy list on HideMyAss!
#
#	This file contains the main function of the HideMyPython! script.
#	It parses the arguments, creates a database, and save the proxies.
#
# 	Copyright (C) 2013 Yannick Méheut <useless (at) utouch (dot) fr>
# 
# 	This program is free software: you can redistribute it and/or modify
# 	it under the terms of the GNU General Public License as published by
# 	the Free Software Foundation, either version 3 of the License, or
# 	(at your option) any later version.
# 
# 	This program is distributed in the hope that it will be useful,
# 	but WITHOUT ANY WARRANTY; without even the implied warranty of
# 	MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# 	GNU General Public License for more details.
# 
# 	You should have received a copy of the GNU General Public License
# 	along with this program.  If not, see <http://www.gnu.org/licenses/>.

from __future__ import print_function

import sys
import hmp.arguments as arguments
import hmp.parser as parser
import hmp.database as database

def main():
        # We create an argument parser
	arg_parser = arguments.create_argument_parser()

	# We parse the arguments
	args = arg_parser.parse_args(sys.argv[1:])
	arguments.process_arguments(args, arg_parser)

	# If the verbose mode is on, we display the arguments
	if args.verbose:
		arguments.print_arguments(args)

        if args.output_format == 'sqlite3':
                # We open the database file where the proxies will be stored
                connection, cursor = database.initialize_database(args.database_file)

                try:
                        # We generate the proxies
                        for proxy in parser.generate_proxy(args):
                                # And we store them in the database
                                database.insert_in_database(cursor, proxy)
                except KeyboardInterrupt:
                        if args.verbose:
                                print('')
                                print('[warn] received interruption signal')

                # We save the changes made to the database, and close the file
                connection.commit()
                connection.close()
        else:
                f, writer = database.initialize_csv(args.database_file)
                try:
                        for proxy in parser.generate_proxy(args):
                                database.write_to_csv(writer, proxy)
                except KeyboardInterrupt:
                        if args.verbose:
                                print('')
                                print('[warn] received interruption signal')
                f.close()
	return 0

if __name__ == '__main__':
	main()

