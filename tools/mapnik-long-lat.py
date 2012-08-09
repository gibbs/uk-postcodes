# Convert eastings and northings to latitude and longitude
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 2 as
# published by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# dangibbs.co.uk <contact@danielgibbs.net>
#

import sys
import MySQLdb

""" 
To install mapnik via aptitude use something like apt-get install 
python-mapnik. Might need to apt-cache search on some distros.

Alternatively http://mapnik.org/
"""
from mapnik import Projection, Coord
from decimal import Decimal

DB_HOST = "localhost"
DB_USER = "root"
DB_PASSWORD = "password"
DB_DATABASE = "database"

britishProj = Projection('+init=epsg:27700') # British National Grid

con = MySQLdb.Connect(host = DB_HOST, user = DB_USER, passwd = DB_PASSWORD, db = DB_DATABASE)

cursor = con.cursor()
cursor.execute("SELECT postcode, eastings, northings FROM %s", (DB_DATABASE))
results = cursor.fetchall()

for result in results:
	 val = Coord(float(result[1]), float(result[2]))
	 val = britishProj.inverse(c)
	 #cursor.execute("UPDATE uk_postcode_dev SET latitude='%f', longitude='%f' WHERE postcode='%s'" % (val.y, val.x, result[0]))
	 print result[0]
	 print val.y, val.x
