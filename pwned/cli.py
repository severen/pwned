# pwned - CLI for checking if your online accounts are compromised.
# Copyright (c) 2016 Severen Redwood <severen@shrike.me>
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

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
