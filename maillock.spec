Name: maillock
Version: 1
Release: 3
Copyright: Rutgers
Summary: Mail locking
Group: System Environment/Base
Source: maillock.tar.gz
BuildRoot: /var/tmp/%{name}-root

%description
Maillock is used in imap to lock mailboxes.  You want this package.

%prep
%setup -q -n maillock

%build
mv Makefile.sol2 Makefile
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local/lib
mkdir -p $RPM_BUILD_ROOT/usr/local/man/man8
cp maillock $RPM_BUILD_ROOT/usr/local/lib
cp maillock.8 $RPM_BUILD_ROOT/usr/local/man/man8

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,bin,bin)
%doc RUHISTORY
%attr(2755,root,mail) /usr/local/lib/maillock
%attr(644, bin, bin) /usr/local/man/man8/maillock.8
