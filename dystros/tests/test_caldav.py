# Dystros
# Copyright (C) 2016 Jelmer Vernooij <jelmer@jelmer.uk>
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; version 2
# of the License or (at your option) any later version of
# the License.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
# MA  02110-1301, USA.

from dystros.caldav import (
    WellknownResource,
    NonDavResource,
    UserPrincipalResource,
    CalendarSetResource,
    )

import unittest


class WellknownResourceTests(unittest.TestCase):

    def test_get_body(self):
        r = WellknownResource('/some/root')
        self.assertEqual(b'/some/root', b''.join(r.get_body()))

    def test_propget(self):
        r = WellknownResource('/some/root')
        self.assertRaises(KeyError, r.propget, 'unknown-property')

    def test_members(self):
        r = WellknownResource('/some/root')
        self.assertEqual([], r.members())