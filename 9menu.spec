Summary: Menu program for X
Name: 9menu
Version: 1.4
Release: 3
Copyright: Freely distributable
Group: User Interface/X
Source: 9menu_1.4.tar.gz
BuildRoot: /var/tmp/%{name}-root

%description
9menu is a simple program that lets you create a menu in X where items
are bound to commands.

%prep
%setup -q -n 9menu-1.4.orig

# Why .orig?  I stole the Debian sources as I couldn't find them
# anywhere else on the Internet.

%build
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local/bin
mkdir -p $RPM_BUILD_ROOT/usr/local/man/man1
install -m 0755 9menu $RPM_BUILD_ROOT/usr/local/bin/9menu
install -m 0644 9menu.1 $RPM_BUILD_ROOT/usr/local/man/man1/9menu.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README
/usr/local/bin/9menu
/usr/local/man/man1/9menu.1
