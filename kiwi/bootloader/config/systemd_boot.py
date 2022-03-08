# Copyright (c) 2022 Marcus Schäfer
#
# This file is part of kiwi.
#
# kiwi is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# kiwi is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with kiwi.  If not, see <http://www.gnu.org/licenses/>
#
# project
from kiwi.bootloader.config.bootloader_spec_base import BootLoaderSpecBase


class BootLoaderSystemdBoot(BootLoaderSpecBase):
    def setup_loader(self, target: str) -> None:
        # TODO: implementation missing
        pass

    def set_loader_entry(self, target: str) -> None:
        # TODO: implementation missing
        pass

    def create_loader_image(self, target: str) -> None:
        # TODO: implementation missing
        pass
