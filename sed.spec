Name: sed
Version: 4.1.4
Copyright: GPL
Group: System Environment/Base
Summary: The GNU stream editor
Release: 2
Source: ftp://ftp.gnu.org/gnu/sed/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-root

%description
GNU sed is a POSIX compliant `sed'.  Sed, like ed, permits scripted edits.
However, unlike ed, sed makes a single pass over its input and can accept
input from a pipeline.  Install GNU sed if you need something Solaris
sed lacks (like line addresses with ~).

%prep
%setup -q

%build
CC="gcc"
CFLAGS="-g"
CXX="g++"
CXXFLAGS="-g"
export CC CFLAGS CXX CXXFLAGS
./configure --prefix=/usr/local
make
make check

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/local
make install prefix=%{buildroot}/usr/local
rm %{buildroot}/usr/local/info/dir

%clean
rm -rf %{buildroot}

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
%doc ABOUT-NLS AUTHORS BUGS COPYING COPYING.DOC INSTALL NEWS README
%doc README-alpha README.boot THANKS doc/groupify.sed
/usr/local/info/sed.info
/usr/local/man/man1/sed.1
/usr/local/bin/sed
/usr/local/share/locale/*/LC_MESSAGES/sed.mo

%changelog
* Fri Jun 02 2006 Jonathan Kaczynski <jmkacz@nbcs.rutgers.edu> - 4.1.4-2
- Updated to 4.1.4