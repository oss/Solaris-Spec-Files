Summary: GUI front end for ircii
Name: tkirc2
Version: 2.46
Release: 1
Group: Applications/Internet
License: GPL
Source: tkirc%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-root
Requires: tcl-tk ircii

%description
tkirc2 is the return of ircII's nice frontend. The last release was
two and a half years ago and when I don't release this next version as
soon as possible, I will be grandpa before. =:^) That's the reason for
a missing detailed manual. -- Family is more important!

ircII is a text-based client for the Internet Relay Chat and with Tcl/Tk
it was possible to create this graphical user interface for it. -- ircII,
Tcl/Tk and tkirc should run under nearly all Unix-like operating systems.

%prep
%setup -q -n tkirc2

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/local/bin
install -m 0755 tkirc2 %{buildroot}/usr/local/bin

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, bin)
%doc COPYING CHANGES README
%doc .tkirc2/*
/usr/local/bin/tkirc2
