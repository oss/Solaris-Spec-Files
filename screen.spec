Name: screen
Version: 3.9.10
Copyright: GPL
Group: Applications/System
Summary: GNU screen
Release: 1
Source: screen-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root

%description
Screen is a full-screen window manager that multiplexes a physical
terminal between several processes, typically interactive shells.
Each virtual terminal provides the functions of the DEC VT100 terminal
and, in addition, several control functions from the ISO 6429 (ECMA
48, ANSI X3.64) and ISO 2022 standards (e.g. insert/delete line and
support for multiple character sets).  There is a scrollback history
buffer for each virtual terminal and a copy-and-paste mechanism that
allows the user to move text regions between windows.

%prep
%setup -q

%build
./configure --prefix=/usr/local
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local/etc
make install prefix=$RPM_BUILD_ROOT/usr/local
cp etc/etcscreenrc $RPM_BUILD_ROOT/usr/local/etc/screenrc.rpm
cp terminfo/screencap $RPM_BUILD_ROOT/usr/local/etc/screencap.rpm

%clean
rm -rf $RPM_BUILD_ROOT

%post
if [ -x /usr/local/bin/install-info ] ; then
	/usr/local/bin/install-info --info-dir=/usr/local/info \
		 /usr/local/info/screen.info \
	--entry="* Screen: (screen).                    Terminal multiplexer."
fi
echo "You need to edit /usr/local/etc/screenrc.rpm (and remove the .rpm)"
echo "and add /etc/screencap.rpm to your termcap."

%preun
if [ -x /usr/local/bin/install-info ] ; then
	/usr/local/bin/install-info --delete --info-dir=/usr/local/info \
		 /usr/local/info/screen.info
fi

%files
%defattr(-,bin,bin)
/usr/local/bin/*
/usr/local/man/man1/*
/usr/local/info/*info*
/usr/local/etc/*
