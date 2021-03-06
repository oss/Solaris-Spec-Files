%define major_version 8.4
%define minor_version 16
%define version %{major_version}.%{minor_version}

Summary: The Tcl scripting language
Name: tcl
Version: %{version}
Release: 1
Group: Development/Languages
Copyright: freely distributable
Source0: http://telia.dl.sourceforge.net/sourceforge/tcl/tcl%{version}-src.tar.gz
Source1: http://telia.dl.sourceforge.net/sourceforge/tcl/tk%{version}-src.tar.gz
BuildRoot: /var/tmp/%{name}-root

%description
Tcl is a scripting language.

%package tk
Summary: The Tk toolikit for Tcl
Group: Development/Languages
Requires: tcl

%description tk
Tk lets you develop GUI interfaces to Tcl programs.

%package headers
Summary: Tcl source
Group: Development/Languages

%description headers
This package contains the private headers for Tcl; it is useful if you
are building software (such as Expect) which requires them.

%prep
%setup -q -c -a 0
%setup -q -T -D -a 1

%build
PATH="/opt/SUNWspro/bin:${PATH}" \
CC="cc" CXX="CC" CPPFLAGS="-I/usr/local/include" \
LD="/usr/ccs/bin/ld" \
LDFLAGS="-L/usr/local/lib -R/usr/local/lib" \
export PATH CC CXX CPPFLAGS LD LDFLAGS

cd tcl%{version}/unix
./configure --enable-shared --enable-threads --prefix=/usr/local
#./configure --enable-gcc --prefix=/usr/local
gmake
cd ../../tk%{version}/unix
./configure --enable-shared --enable-threads --prefix=/usr/local
#./configure --enable-gcc --prefix=/usr/local

%install
PATH="/opt/SUNWspro/bin:${PATH}" \
CC="cc" CXX="CC" CPPFLAGS="-I/usr/local/include" \
LD="/usr/ccs/bin/ld" \
LDFLAGS="-L/usr/local/lib -R/usr/local/lib" \
export PATH CC CXX CPPFLAGS LD LDFLAGS

build_dir=`pwd`
umask 022

rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local/src/tcl-%{version}
cd tcl%{version}/unix
gmake install INSTALL_ROOT=$RPM_BUILD_ROOT
# awful kludge.  This file conflicts with a Perl manpage:
#mv $RPM_BUILD_ROOT/usr/local/man/man3/Thread.3 \
#   $RPM_BUILD_ROOT/usr/local/man/man3/TCL_Thread.3
find $RPM_BUILD_ROOT \! -type d | sed "s#$RPM_BUILD_ROOT##" | sort \
    > $build_dir/TCL_FILE_LIST

cd $build_dir/tk%{version}/unix
make install INSTALL_ROOT=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT \! -type d | sed "s#$RPM_BUILD_ROOT##" | sort \
    | comm -1 -3 $build_dir/TCL_FILE_LIST - > $build_dir/TK_FILE_LIST

cd $build_dir/tcl%{version}
find . | cpio -pdm $RPM_BUILD_ROOT/usr/local/src/tcl-%{version}

# till we start running RPM version which can handle hardlinks..
cat $build_dir/TCL_FILE_LIST $build_dir/TK_FILE_LIST
cd $RPM_BUILD_ROOT
/usr/local/bin/unhardlinkify.py ./

%clean
rm -rf $RPM_BUILD_ROOT

%files -f TCL_FILE_LIST
%defattr(-,bin,bin)
%doc tcl%{version}/license.terms

%files -f TK_FILE_LIST tk 
%defattr(-, bin, bin)

%files headers
%defattr(-, bin, bin)
/usr/local/src/tcl-%{version}

%changelog
* Wed Nov 07 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 8.4.16-1
- Bump to 8.4.16
