Name: sed
Version: 3.02
Copyright: GPL
Group: System Environment/Base
Summary: The GNU stream editor
Release: 2
Source: sed-3.02.tar.gz
BuildRoot: /var/tmp/%{name}-root

%description
GNU sed is a POSIX compliant `sed'.  Sed, like ed, permits scripted edits.
However, unlike ed, sed makes a single pass over its input and can accept
input from a pipeline.  Install GNU sed if you need something Solaris
sed lacks (like line addresses with ~).


%prep
%setup -q

%build
./configure --prefix=/usr/local
make
make check

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local
make install prefix=$RPM_BUILD_ROOT/usr/local

%clean
rm -rf $RPM_BUILD_ROOT

%post
if [ -x /usr/local/bin/install-info ] ; then
	/usr/local/bin/install-info --info-dir=/usr/local/info \
		 /usr/local/info/sed.info
fi

%preun
if [ -x /usr/local/bin/install-info ] ; then
	/usr/local/bin/install-info --delete --info-dir=/usr/local/info \
		 /usr/local/info/sed.info
fi

%files
%defattr(-,root,root)
%doc COPYING
/usr/local/info/sed.info
/usr/local/man/man1/sed.1
/usr/local/bin/sed
