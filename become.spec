Name: become
Version: 2.0
Release: 3
Summary: Become group support utility
Copyright: Rutgers
Group: System Environment/Base
Source: become.tar.gz
Patch: become-mkfile.patch
BuildRoot: /var/tmp/%{name}-root

%description
Become allows a user to become another temporarily.  It is similar to
su but more complete.  Become has most of the same effects as login.
Thus it should let you read and send email as the new user.  It makes
entries in utmp and wtmp.  (from the manpage)

Become is installed setuid root.

%prep
%setup -q -n become
%patch
make clean

%build
make CC=gcc

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local/bin
mkdir -p $RPM_BUILD_ROOT/usr/local/man/man1
cp become $RPM_BUILD_ROOT/usr/local/bin
cp become.1 $RPM_BUILD_ROOT/usr/local/man/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%attr(4711, root, root) /usr/local/bin/become
/usr/local/man/man1/become.1




