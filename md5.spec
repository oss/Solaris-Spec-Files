Summary: MD5 checksum calculator
Name: md5
Version: 1.0
Release: 1
Group: System Environment/Base
License: Public domain
Source: MD5.tar.Z
BuildRoot: /var/tmp/%{name}-root

%description
md5 takes as input a message of arbitrary length and produces as
output a 128-bit "fingerprint" or "message digest" of the input.  It
is conjectured that it is computationally infeasible to produce two
messages having the same message digest, or to produce any message
having a given prespeciied target message digest.  The MD5 algorithm
is intended for digital signature applications, where a large file
must be "compressed" in a secure manner before being encrypted with a
private (secret) key under a public-key cryptosystem such as RSA.

%prep
%setup -T -c -n md5
%setup -D -T -q -a 0 -n md5

%build
make

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/local/bin %{buildroot}/usr/local/man/man1
install -m 0755 md5   %{buildroot}/usr/local/bin/md5
install -m 0644 md5.1 %{buildroot}/usr/local/man/man1/md5.1

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, bin)
%doc *txt *ps
/usr/local/bin/md5
/usr/local/man/man1/md5.1
