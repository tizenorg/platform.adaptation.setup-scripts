Name:     setup-ivi
Version:  1.0
Release:  1
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

%description
This package provides various early system setup programs

%description -n setup-gummiboot
This package provides a command-line tool for changing the gummiboot bootloader
configuration files.

%description -n setup-extlinux
This package provides a command-line tool for changing the extlinux bootloader
configuration file.

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

install -m755 setup-ivi-boot %{buildroot}/%{_sbindir}
install -m755 setup-ivi-bootloader-conf %{buildroot}/%{_sbindir}
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
%{_sbindir}/setup-ivi-bootloader-conf
%{_prefix}/share/setup-ivi/setup-ivi-sh-functions
%{_prefix}/share/setup-ivi/installerfw-sh-functions

%files -n setup-gummiboot
%defattr(-,root,root)
%{_sbindir}/setup-gummiboot-conf

%files -n setup-extlinux
%defattr(-,root,root)
%{_sbindir}/setup-extlinux-conf
