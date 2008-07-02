Summary: Slang language
Name: slang
Version: 2.1.3
Release: 1
Group: Development/Languages
Copyright: GPL
Source: slang-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-root
Conflicts: vpkg-SFWslang

%description
S-Lang is an interpreted language that was designed from the start to
be easily embedded into a program to provide it with a powerful
extension language.  Examples of programs that use S-Lang as an
extension language include the jed text editor, the slrn newsreader,
and sldxe (unreleased), a numerical computation program.  For this
reason, S-Lang does not exist as a separate application. 

    [ from the manual ]

%package devel
Summary: Slang headers and static libraries
Group: Development/Libraries
Requires: slang = %{version}

%description devel
Slang-devel contains the headers and static libraries for slang; you
need this package if you are building software with slang.

%prep
%setup -q

%build
PATH="/opt/SUNWspro/bin:${PATH}" \
CC="cc" CXX="CC" CPPFLAGS="-I/usr/local/include" \
LD="/usr/ccs/bin/ld" \
LDFLAGS="-L/usr/local/lib -R/usr/local/lib"
export PATH CC CXX CPPFLAGS LD LDFLAGS

./configure --prefix=/usr/local
gmake
gmake static

%install
rm -rf %{buildroot}
mkdir -p %{buildroot} 

gmake install-all DESTDIR=%{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,bin,bin)
%doc /usr/local/share/doc
/usr/local/bin/slsh
/usr/local/etc/slsh.rc
/usr/local/lib/libslang.so*
/usr/local/lib/slang
/usr/local/share/slsh
/usr/local/share/man/man1/slsh.1

%files devel
%defattr(-,bin,bin)
/usr/local/lib/libslang.a
/usr/local/include/*.h

%changelog
* Wed Jul 2 2008 Brian Schubert <schubert@nbcs.rutgers.edu> - 2.1.3-1
- Modified to use suncc, updated to version 2.1.3, added changelog
