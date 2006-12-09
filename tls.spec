Summary: 	TLS (aka SSL) Channel - can be layered on any bi-directional Tcl_Channel.
Name:	 	tls	
Version:	1.5.0
Release:	1
Copyright:	BSD
Group:		Libraries
URL:		http://tls.sf.net
Source0:	%{name}%{version}-src.tar.gz
BuildRoot:	/var/tmp/%{name}-root
Prefix:		/usr/local	
Requires:	tcl >= 8.4 tcl-headers >= 8.4 openssl >= 0.9.8

%description

%prep
%setup -q -n tls1.5

%build
PATH="/opt/SUNWspro/bin:${PATH}" \
CC="cc" CXX="CC" CPPFLAGS="-I/usr/local/include" \
LD="/usr/ccs/bin/ld" \
LDFLAGS="-L/usr/local/lib -R/usr/local/lib" \
export PATH CC CXX CPPFLAGS LD LDFLAGS
./configure --prefix=/usr/local --with-ssl-dir=/usr/local/ssl --with-tcl=/usr/local/lib --enable-threads --enable-shared
make

%install
rm -rf %{buildroot}
make install all DESTDIR=%{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root)
%{prefix}/lib/*

