Name: rxvt
Version: 2.6.3
Release: 3
Summary: Fast, lightweight, terminal emulator
Group: User Interface/X
License: GPL
Source0: %{name}-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root

%description
     rxvt, version 2.6.3, is a  colour  vt102  terminal  emulator
     intended  as  an  xterm(1)  replacement for users who do not
     require  features  such  as  Tektronix  4014  emulation  and
     toolkit-style  configurability.  As a result, rxvt uses much
     less swap space -- a  significant  advantage  on  a  machine
     serving many X sessions.  (from the man page)

%prep
%setup -q

%build
./configure 
make

%install
rm -fr %{buildroot}
make install DESTDIR=%{buildroot}

%clean
rm -fr %{buildroot}

%files
%defattr(-,root,root)
/usr/local/bin/
/usr/local/man/man1/


