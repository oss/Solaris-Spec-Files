Summary: PLT Dr. Scheme
Name: drscheme
Version: 360
License: LGPL
Group: Development/Languages
Release: 3
Source: plt-%{version}-src-unix.tgz
URL: http://www.plt-scheme.org/
Packager: Eric Rivas <kc2hmv@nbcs.rutgers.edu>
BuildRoot: /var/tmp/%{name}-root
BuildRequires: xft2-devel
BuildRequires: cairo-devel
Requires: xft2
Requires: cairo


%description
DrScheme is an interactive, integrated, graphical programming environment
for the Scheme, MzScheme, and MrEd programming languages.

%prep
%setup -q -n plt-360

%build
PATH="/opt/SUNWspro/bin:${PATH}" \
CC="cc" CXX="CC" \
LD="/usr/ccs/bin/ld" \
LDFLAGS="-L/usr/local/lib -R/usr/local/lib" \
LDFLAGS="${LDFLAGS} -L/usr/local/ssl/lib -R/usr/local/ssl/lib" \
CPPFLAGS="-I/usr/local/include -I/usr/local/ssl/include" \
PLT_EXTENSION_LIB_PATHS="/usr/local/ssl"
export LDFLAGS CPPFLAGS PLT_EXTENSION_LIB_PATHS LD PATH CC CXX

cd src
./configure --prefix=/usr/local/plt --disable-gl --disable-nls

gmake

%install
mkdir -p ${RPM_BUILD_ROOT}/usr/local
PATH="/opt/SUNWspro/bin:${PATH}" \
CC="cc" CXX="CC" \
LD="/usr/ccs/bin/ld" \
LDFLAGS="-L/usr/local/lib -R/usr/local/lib" \
LDFLAGS="${LDFLAGS} -L/usr/local/ssl/lib -R/usr/local/ssl/lib" \
CPPFLAGS="-I/usr/local/include -I/usr/local/ssl/include" \
PLT_EXTENSION_LIB_PATHS="/usr/local/ssl"
export LDFLAGS CPPFLAGS PLT_EXTENSION_LIB_PATHS LD PATH CC CXX

# The SSL libs are a real pain, they can't find the OpenSSL libraries unless
# this is set.  I don't like the way it looks either.
LD_LIBRARY_PATH="/usr/local/ssl/lib"
export LD_LIBRARY_PATH

cd src
gmake install DESTDIR=$RPM_BUILD_ROOT

%post
# I have no idea why we have to do this, but we must...
# This set paths in files and stuff.  I don't know.
#cat << EOF
#Running setup-plt script, please wait...
#EOF
#PLT_EXTENSION_LIB_PATHS="/usr/local/ssl"
#export PLT_EXTENSION_LIB_PATHS
#cd /usr/local/plt/
#./install
#chown -R root:bin *

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, bin)
/usr/local/plt

%changelog
* Tue Nov 13 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 360-3
- Disable NLS
* Thu May 11 2006 Eric Rivas <kc2hmv@nbcs.rutgers.edu> - 301-1
- Inital version 301.

