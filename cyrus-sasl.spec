Summary: SASL implementation 
Name: cyrus-sasl
Version: 1.5.24
Release: 1
Group: Applications/Internet
License: BSD
Source: %{name}-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root

%description
This is the Cyrus SASL API implentation. It can be used on the client
or server side to provide authentication. See RFC 2222 for more
information.

  (from README)

%prep
%setup -q

%build
LD="/usr/ccs/bin/ld -L/usr/local/lib -R/usr/local/lib" \
LDFLAGS="-L/usr/local/lib -R/usr/local/lib" \
CPPFLAGS="-I/usr/local/include -I/usr/include/gssapi" \
./configure
gmake

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}
gmake install DESTDIR=%{buildroot}

%post
ln -s /usr/local/lib/sasl /usr/lib/sasl

%preun
rm -f /usr/lib/sasl

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc doc
%doc INSTALL AUTHORS COPYING NEWS README TODO
/usr/local/include/*
/usr/local/lib/*.so*
/usr/local/lib/sasl
/usr/local/lib/*a
/usr/local/sbin/*
/usr/local/man/*/*

