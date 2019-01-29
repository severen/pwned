# This file is a part of Pwned (https://github.com/severen/pwned).
# Copyright (C) 2016-2019  Severen Redwood <severen@shrike.me>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import click
import requests

from pwned import __version__

@click.command()
@click.argument('email')
@click.option('-j', '--json', is_flag=True)
@click.version_option(__version__)
def pwned(email, json):
    params = {'truncateResponse': 'true'}
    r = requests.get('https://haveibeenpwned.com/api/v2/breachedaccount/%s'
                     % email, params=params)

    if r.status_code is 404:
        print('Congratulations, you haven\'t been pwned!')
    elif r.status_code is 200:
        if json is True:
            print(r.text)
            return

        print('Unfortunately one or more of your online accounts have been ' +
              'compromised.\n')

        print('Compromised accounts:')
        for account in r.json():
            print('• %s' % account['Name'])

if __name__ == '__main__':
    pwned()
