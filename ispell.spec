Name: ispell
Version: 3.1.20
Copyright: GPL?
Group: Applications/Editors
Summary: Interactive spell-checker
Release: 2
Source: ispell-3.1.20.tar.gz
Patch: ispell-3.1-sol8p.patch
BuildRoot: /var/tmp/%{name}-root

%description

Ispell is an interactive spell checker.  It can check spelling in
flat-text, TeX, and troff files, and it has hooks in emacs.

%prep
%setup -q -n ispell-3.1
%patch -p1
make local.h
echo "#define CC \"gcc\"" >> local.h
echo "#define USG" >> local.h

%build
make all

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local/bin
mkdir -p $RPM_BUILD_ROOT/usr/local/man/man1
mkdir $RPM_BUILD_ROOT/usr/local/info
mkdir $RPM_BUILD_ROOT/usr/local/lib
cp config.sh config.sh.bak
perl -p -e "s(/usr)($RPM_BUILD_ROOT/usr)" < config.sh.bak > config.sh
make install

%clean
rm -rf $RPM_BUILD_ROOT

%post
if [ -x /usr/local/bin/install-info ] ; then
	/usr/local/bin/install-info --info-dir=/usr/local/info \
--entry="* Ispell: (ispell).                Interactive spell-checker" \
		 /usr/local/info/ispell
fi

%preun
if [ -x /usr/local/bin/install-info ] ; then
	/usr/local/bin/install-info --delete --info-dir=/usr/local/info \
		 /usr/local/info/ispell
fi

%files
%defattr(-,bin,bin)
/usr/local/bin/ispell
/usr/local/bin/buildhash
/usr/local/bin/icombine
/usr/local/bin/ijoin
/usr/local/bin/munchlist
/usr/local/bin/findaffix
/usr/local/bin/tryaffix
/usr/local/bin/sq
/usr/local/bin/unsq
/usr/local/man/man1/ispell.1
/usr/local/man/man1/sq.1
/usr/local/man/man1/buildhash.1
/usr/local/man/man1/munchlist.1
/usr/local/man/man1/findaffix.1
/usr/local/man/man1/tryaffix.1
/usr/local/man/man1/unsq.1
/usr/local/man/man4/ispell.4
/usr/local/man/man4/english.4
/usr/local/info/ispell
/usr/local/lib/english.aff
/usr/local/lib/americanmed+.hash
/usr/local/lib/american.hash
/usr/local/lib/english.hash
