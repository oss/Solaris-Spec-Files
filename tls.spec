Summary: 	TLS (aka SSL) Channel - can be layered on any bi-directional Tcl_Channel.
Name:	 	tls	
Version:	1.4.1
Release:	1
Copyright:	BSD
Group:		Libraries
URL:		http://goatse.cx
Vendor:		chello.nl
Source0:	%{name}%{version}-src.tar.gz
BuildRoot:	/var/tmp/%{name}-root
Prefix:		/usr/local	
Requires:	tcl >= 8.0 openssl

%description

%prep
%setup -q -n tls1.4 

%build
PATH="/usr/bin:/usr/local/bin:/usr/sbin:/sbin:/usr/sfw/lib:/usr/sfw/include:/usr/ccs/bin:/usr/sfw/bin"
export
autoconf
./configure --prefix=%{buildroot}/%{prefix} --with-ssl-dir=/usr/local/ssl --with-tcl=/usr/sfw/lib 
make

%install
rm -rf %{buildroot}
make install

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root)
%{prefix}/lib/*

