Summary:	A remote display system.
Name:		vnc
Version:	4.1.2
Release:	1
URL:		http://www.realvnc.com/
Source:		vnc-%{version}_unixsrc.tar.gz
License:	GPL
Group:		User Interface/Desktops
Packager:	David Lee Halik <dhalik@nbcs.rutgers.edu>
BuildRoot:	%{_tmppath}/%{name}-%{version}-root
#BuildPrereq:	tcp_wrappers
BuildRequires:	zlib-devel libjpeg-devel

%description
Virtual Network Computing (VNC) is a remote display system which
allows you to view a computing 'desktop' environment not only on the
machine where it is running, but from anywhere on the Internet and
from a wide variety of machine architectures. This package contains a 
client which will allow you to connect to other desktops running a VNC 
server.

%prep

%setup -q -n %{name}-%{version}_unixsrc

%build
cd unix

PATH="/opt/SUNWspro/bin:${PATH}" \
CC="cc" CXX="CC" CPPFLAGS="-I/usr/local/include" \
LD="/usr/ccs/bin/ld" \
LDFLAGS="-L/usr/local/lib -R/usr/local/lib" \
export PATH CC CXX CPPFLAGS LD LDFLAGS

./configure --with-installed-zlib --prefix=/usr/local
make

%install
cd unix
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_mandir}/man1
./vncinstall %{buildroot}%{_bindir} %{buildroot}%{_mandir}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
/usr/local/bin/vncviewer
/usr/local/man/man1/vncviewer.1
/usr/local/bin/vncconfig
/usr/local/bin/vncpasswd
/usr/local/bin/vncserver
/usr/local/bin/x0vncserver
/usr/local/man/man1/vncconfig.1
/usr/local/man/man1/vncpasswd.1
/usr/local/man/man1/vncserver.1
/usr/local/man/man1/x0vncserver.1

%changelog
* Thu Sep 20 2006 David Lee Halik <dhalik@nbcs.rutgers.edu>
- Initial Solaris Sparc64 Build Version 4.1.2

