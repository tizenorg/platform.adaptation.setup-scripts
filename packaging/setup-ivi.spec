Name:     setup-ivi
Version:  1.1
Release:  0
License:  GPL-2.0
Summary:  Various early setup programs
Url:      http://www.tizen.org
Group:    System/Configuration
Source:   %{name}_%{version}.tar.gz
Requires: /usr/bin/sed
Requires: /usr/bin/grep
Requires: /usr/bin/printf
Requires: /usr/bin/printenv
Requires: /usr/bin/sort
Requires: /usr/bin/tr
Requires: virtual-setup-ivi-bootloader
BuildArchitectures: noarch

%package -n setup-gummiboot
Summary:  Command-line tool for tweaking gummiboot configuration
Provides: virtual-setup-ivi-bootloader
Requires: %{name}
Requires: gummiboot

%package -n setup-extlinux
Summary:  Command-line tool for tweaking extlinux configuration
Provides: virtual-setup-ivi-bootloader
Requires: %{name}
Requires: syslinux-extlinux

%package -n setup-ivi-clone
Summary:  A tool for cloning a Tizen IVI system
Requires: %{name}
Requires: /usr/bin/mount
Requires: /usr/bin/udevadm
Requires: /usr/bin/uuidgen
Requires: /usr/bin/sync
Requires: /usr/bin/tail
Requires: systemd
Requires: gptfdisk
Requires: e2fsprogs
Requires: dosfstools
Requires: rsync

%description
This package provides various early system setup programs

%description -n setup-gummiboot
This package provides a command-line tool for changing the gummiboot bootloader
configuration files.

%description -n setup-extlinux
This package provides a command-line tool for changing the extlinux bootloader
configuration file.

%description -n setup-ivi-clone
This package provides a command line tool for cloning a Tizen IVI system to a
different disk.

###
### PREP
###
%prep
%setup -q -n %{name}-%{version}

%build

###
### INSTALL
###
%install
install -d %{buildroot}/%{_sbindir}
install -d %{buildroot}/%{_prefix}/share/setup-ivi
install -d %{buildroot}/%{_unitdir}

install -m755 setup-ivi-boot %{buildroot}/%{_sbindir}
install -m755 setup-ivi-fstab %{buildroot}/%{_sbindir}
install -m755 setup-ivi-bootloader-conf %{buildroot}/%{_sbindir}
install -m755 setup-ivi-clone %{buildroot}/%{_sbindir}
install -m755 setup-ivi-clone-service %{buildroot}/%{_sbindir}
install -m644 ivi-clone.service %{buildroot}/%{_unitdir}
install -m755 setup-gummiboot-conf %{buildroot}/%{_sbindir}
install -m755 setup-extlinux-conf %{buildroot}/%{_sbindir}
install -m644 setup-ivi-sh-functions %{buildroot}/%{_prefix}/share/setup-ivi
install -m644 installerfw-sh-functions %{buildroot}/%{_prefix}/share/setup-ivi

###
### CLEAN
###
%clean
rm -rf %{buildroot}

###
### FILES
###
%files
%defattr(-,root,root)
%{_sbindir}/setup-ivi-boot
%{_sbindir}/setup-ivi-fstab
%{_sbindir}/setup-ivi-bootloader-conf
%{_prefix}/share/setup-ivi/setup-ivi-sh-functions
%{_prefix}/share/setup-ivi/installerfw-sh-functions

%files -n setup-gummiboot
%defattr(-,root,root)
%{_sbindir}/setup-gummiboot-conf

%files -n setup-extlinux
%defattr(-,root,root)
%{_sbindir}/setup-extlinux-conf

%files -n setup-ivi-clone
%defattr(-,root,root)
%{_sbindir}/setup-ivi-clone
%{_sbindir}/setup-ivi-clone-service
# Note, we do not need to run 'systemctl enable ivi-clone' for this one because
# it is activated by the 'systemd.unit=ivi-clone.service' kernel parameter.
%{_unitdir}/ivi-clone.service
