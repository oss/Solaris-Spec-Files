Summary: Columbia Kermit
Name: cku
Version: 7.0.197
Release: 2
Group: System Environment/Base
Source: cku197.tar.gz
Copyright: Restricted distribution
BuildRoot: /var/tmp/%{name}-root

%description 
C-Kermit is a combined serial and network communication software
package offering a consistent, medium-independent, cross-platform
approach to connection establishment, terminal sessions, file
transfer, character-set translation, numeric and alphanumeric paging,
and automation of communication tasks. C-Kermit includes:

  o   Along with Kermit 95 and MS-DOS Kermit, the fastest and most
     advanced implementation of the Kermit file transfer protocol
     available anywhere.

  o   A powerful, portable, easy-to-use script programming language to
     automate all your routine communications tasks.

  o  Consistent operation over serial connections (direct or dialed)
     and network connections (TCP/IP and in some cases also LAT or
     X.25) -- on a huge selection of hardware and software platforms.

  o  Character-set translation in both file transfer and online
     sessions, for Western- and Eastern-European languages, Cyrillic,
     Greek, Hebrew, and Japanese, now including Unicode.

  o  Ability to send numeric and alphanumeric pages.

%prep
%setup -n cku -c -T
%setup -n cku -D -T -a 0

%build
make solaris7g

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local/bin
mkdir -p $RPM_BUILD_ROOT/usr/local/man/manl

install -m 0755 wermit $RPM_BUILD_ROOT/usr/local/bin/kermit
install -m 0644 ckuker.nr $RPM_BUILD_ROOT/usr/local/man/manl/kermit.l

%clean
rm -rf $RPM_BUILD_ROOT

%post
cat <<EOF

WARNING: If C-Kermit is to be used for dialing out, you will
probably need to change its owner and group and permissions to
match the cu program.  See the ckuins.txt file for details.

EOF

%files
%defattr(-,bin,bin)
%doc *.txt *.ini ckermit.k*d cke*.ksc
/usr/local/bin/kermit
/usr/local/man/manl/kermit.l
