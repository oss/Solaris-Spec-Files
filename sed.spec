Name: sed
Version: 4.1.4
Copyright: GPL
Group: System Environment/Base
Summary: The GNU stream editor
Release: 3
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
PATH="/opt/SUNWspro/bin:${PATH}" \
CC="gcc" CXX="g++" CPPFLAGS="-I/usr/local/include" \
LD="/usr/ccs/bin/ld" \
LDFLAGS="-L/usr/local/lib -R/usr/local/lib" \
export PATH CC CXX CPPFLAGS LD LDFLAGS
./configure --prefix=/usr/local --disable-nls
gmake
gmake check

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/local
gmake install prefix=%{buildroot}/usr/local
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
/usr/local/share/doc/sed.html

%changelog
* Tue Nov 13 2007 Naveen Gavini <ngavini@nbcs.rutgers.edu> - 4.1.4-3
- Disabled NLS
* Fri Jun 02 2006 Jonathan Kaczynski <jmkacz@nbcs.rutgers.edu> - 4.1.4-2
- Updated to 4.1.4
