Name:     setup-scripts
Version:  1.1
Release:  0
License:  GPL-2.0
Summary:  Various early setup programs
Url:      http://www.tizen.org
Group:    System/Configuration
Source:   %{name}_%{version}.tar.gz
Provides: setup-ivi = %{version}-%{release}
Obsoletes: setup-ivi < %{version}-%{release}
Requires: /usr/bin/sed
Requires: /usr/bin/grep
Requires: /usr/bin/printf
Requires: /usr/bin/printenv
Requires: /usr/bin/sort
Requires: /usr/bin/tr
Requires: virtual-setup-scripts-bootloader
BuildArchitectures: noarch

%package -n %{name}-gummiboot
Summary:  Command-line tool for tweaking gummiboot configuration
Provides: virtual-%{name}-bootloader
Requires: %{name} = %{version}-%{release}
Requires: gummiboot

%package -n %{name}-extlinux
Summary:  Command-line tool for tweaking extlinux configuration
Provides: virtual-%{name}-bootloader
Requires: %{name} = %{version}-%{release}
Requires: syslinux-extlinux

%package -n %{name}-u-boot
Summary:  Command-line tool for tweaking u-boot configuration
Provides: virtual-%{name}-bootloader
Requires: %{name} = %{version}-%{release}
Requires: u-boot

%package -n %{name}-clone
Summary:  A tool for cloning a Tizen system
Provides: setup-ivi-clone = %{version}-%{release}
Obsoletes: setup-ivi-clone < %{version}-%{release}
Requires: %{name} = %{version}-%{release}
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

%description -n %{name}-gummiboot
This package provides a command-line tool for changing the gummiboot bootloader
configuration files.

%description -n %{name}-extlinux
This package provides a command-line tool for changing the extlinux bootloader
configuration file.

%description -n %{name}-u-boot
TODO

%description -n %{name}-clone
This package provides a command line tool for cloning a Tizen system to a
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
install -d %{buildroot}/%{_prefix}/share/setup-scripts
install -d %{buildroot}/%{_unitdir}

install -m755 setup-scripts-boot %{buildroot}/%{_sbindir}
install -m755 setup-scripts-fstab %{buildroot}/%{_sbindir}
install -m755 setup-scripts-bootloader-conf %{buildroot}/%{_sbindir}
install -m755 setup-scripts-clone %{buildroot}/%{_sbindir}
install -m755 setup-scripts-clone-service %{buildroot}/%{_sbindir}
install -m644 scripts-clone.service %{buildroot}/%{_unitdir}
install -m755 setup-gummiboot-conf %{buildroot}/%{_sbindir}
install -m755 setup-extlinux-conf %{buildroot}/%{_sbindir}
install -m644 setup-scripts-sh-functions %{buildroot}/%{_prefix}/share/setup-scripts
install -m644 installerfw-sh-functions %{buildroot}/%{_prefix}/share/setup-scripts

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
%{_sbindir}/setup-scripts-boot
%{_sbindir}/setup-scripts-fstab
%{_sbindir}/setup-scripts-bootloader-conf
%{_prefix}/share/setup-scripts/setup-scripts-sh-functions
%{_prefix}/share/setup-scripts/installerfw-sh-functions

%files -n %{name}-gummiboot
%defattr(-,root,root)
%{_sbindir}/setup-gummiboot-conf

%files -n %{name}-extlinux
%defattr(-,root,root)
%{_sbindir}/setup-extlinux-conf

%files -n %{name}-u-boot
%defattr(-,root,root)

%files -n setup-scripts-clone
%defattr(-,root,root)
%{_sbindir}/setup-scripts-clone
%{_sbindir}/setup-scripts-clone-service
# Note, we do not need to run 'systemctl enable scripts-clone' for this one because
# it is activated by the 'systemd.unit=scripts-clone.service' kernel parameter.
%{_unitdir}/scripts-clone.service
